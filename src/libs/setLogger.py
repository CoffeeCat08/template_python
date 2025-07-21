# src/libs/setLogger.py

import os
import logging


def setLogger(env_data):
    # ログファイルの出力ディレクトリを定義する
    log_dir = env_data["log_output_path"]

    # ログディレクトリが存在しない場合は作成する
    os.makedirs(log_dir, exist_ok=True)

    # ログファイルのフルパスを構築する
    log_file_name = env_data["log_file_name"]
    log_file_path = os.path.join(log_dir, log_file_name)

    logger = logging.getLogger()

    if not logger.handlers:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filename=log_file_path,
            filemode="a",
        )
