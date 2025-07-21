# src/libs/settingInitialize.py

import os
from .setEnv import setEnv
from .setLogger import setLogger


def setInitialize():
    env_data = setEnv()

    logger = setLogger(env_data)

    init = {
        "local_output_path": env_data["local_output_path"],
        "log_output_path": env_data["log_output_path"],
        "log_file_name": env_data["log_file_name"],
        "project_path": os.getcwd(),
    }

    return init, logger
