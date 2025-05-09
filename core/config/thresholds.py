def get_thresholds(level='beginner'):
    if level == 'beginner':
        _ANGLE_HIP_KNEE_VERT = {
            'NORMAL': (0, 32),
            'TRANS': (35, 65),
            'PASS': (70, 95)
        }

        return {
            'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,
            'HIP_THRESH': [10, 50],
            'ANKLE_THRESH': 45,
            'KNEE_THRESH': [50, 70, 95],
            'OFFSET_THRESH': 35.0,
            'INACTIVE_THRESH': 15.0,
            'CNT_FRAME_THRESH': 50
        }

    elif level == 'pro':
        _ANGLE_HIP_KNEE_VERT = {
            'NORMAL': (0, 32),
            'TRANS': (35, 65),
            'PASS': (80, 95)
        }

        return {
            'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,
            'HIP_THRESH': [15, 50],
            'ANKLE_THRESH': 30,
            'KNEE_THRESH': [50, 80, 95],
            'OFFSET_THRESH': 35.0,
            'INACTIVE_THRESH': 15.0,
            'CNT_FRAME_THRESH': 50
        }

    else:
        raise ValueError("Unknown level: must be 'beginner' or 'pro'")
