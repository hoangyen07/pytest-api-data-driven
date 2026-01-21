import json
import pytest
import logging
import sys
from pathlib import Path


@pytest.fixture(scope="session")
def posts_test_data():
    with open("data/posts_test_data.json") as f:
        return json.load(f)


def pytest_configure():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # ---------- FORMAT ----------
    log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    formatter = logging.Formatter(log_format)

    # ---------- ROOT LOGGER ----------
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # allow all logs

    # ---------- CONSOLE HANDLER ----------
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)  # 👈 console = INFO
    console_handler.setFormatter(formatter)

    # ---------- FILE HANDLER ----------
    file_handler = logging.FileHandler(log_dir / "test.log", mode="w")
    file_handler.setLevel(logging.DEBUG)  # 👈 file = DEBUG
    file_handler.setFormatter(formatter)

    # ---------- CLEAN DUPLICATE ----------
    if root_logger.handlers:
        root_logger.handlers.clear()

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # ---------- REDUCE NOISE ----------
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
