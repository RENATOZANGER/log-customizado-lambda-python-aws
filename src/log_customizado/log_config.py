import logging


def setup_logger():
    root_logger = logging.getLogger()
    
    if not root_logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)
    
    root_logger.setLevel(logging.INFO)
    
    for noisy_logger in ("boto3", "botocore", "urllib3", "s3transfer"):
        logging.getLogger(noisy_logger).setLevel(logging.ERROR)
