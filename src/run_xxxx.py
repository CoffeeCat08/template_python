# src/run_xxxx.py

import logging

from .libs.setInitialize import setInitialize


def main():
    initData, logger = setInitialize()
    logger = logging.getLogger(__name__)


if __name__ == "__main__":
    main()
