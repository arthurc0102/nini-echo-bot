def get_mode(mode):
    mode_mapping = {
        'dev': 'development',
        'development': 'development',
        'test': 'test',
        'prod': 'production',
        'production': 'production',
    }

    assert type(mode) is str, 'Mode should be string'
    assert mode in mode_mapping, 'Invalid mode choice'

    return mode_mapping[mode]
