# src/readEnv.py
import os
from dotenv import load_dotenv


def setEnv():

    # 本番環境内では矢印内をコメントアウトする。
    # ↓
    # env_path = os.path.join(os.path.dirname(
    #     os.path.dirname(os.path.abspath(__file__))), '.env')
    # load_dotenv(dotenv_path=env_path)
    # ↑

    env_data = {
        "local_output_path": os.getenv("LOCAL_OUTPUT_PATH"),
        "log_output_path": os.getenv("LOG_OUTPUT_PATH"),
        "log_file_name": os.getenv("LOG_FILE_NAME"),
    }

    return env_data
