import logging


def test_logging():
    logger = logging.getLogger(__name__)


#filehandler object is enetered in addhandler (ie file location)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)

    logger.debug("Debug statement will be executed")

    logger.info("Info msg is displayed")

    logger.warning("warning mode enabled")

    logger.error("Error Occurred..!!")

    logger.critical("This is CRITICAL...")
