
import logging

def setup_logging(log_file):
    """
    Configures the logging for the application.
    """
    for handler in logging.getLogger().handlers[:]:
        logging.getLogger().removeHandler(handler)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
