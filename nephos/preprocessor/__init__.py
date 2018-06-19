"""
Stores all the code concerning the preprocessor operations
"""

config = None


def set_preprocessor_config(preprocess_config):
    """
    sets config for the module

    Parameters
    ----------
    preprocess_config
        type: dict
        configuration for the preprocessor

    Returns
    -------

    """
    global config
    config = preprocess_config


def get_preprocessor_config():
    """
    Returns
    -------
    type: dict
    configuration for the preprocessing module

    """
    global config
    return config
