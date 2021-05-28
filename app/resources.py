import sys
from string import ascii_uppercase

from loguru import logger

from app import config


async def startup():
    setup_logger()
    if config.DEBUG:
        show_config()


async def shutdown():
    ...


def setup_logger():
    """
    Configure Loguru's logger
    """
    logger.remove()  # remove standard handler
    logger.add(
        sys.stderr,
        level=config.LOG_LEVEL,
        colorize=True,
        backtrace=config.DEBUG,
        enqueue=True,
    )  # reinsert it to make it run in a different thread


def show_config() -> None:
    values = {
        v: getattr(config, v)
        for v in sorted(dir(config))
        if v[0] in ascii_uppercase
    }
    logger.debug(values)
    return
