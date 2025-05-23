import json
from src.log_customizado.logger_instance import LoggerFactory
from src.bucket_s3.bucket_manager import BucketManager

from src.log_customizado.log_config import setup_logger
setup_logger()


def lambda_handler(event, context):
    logger = LoggerFactory.create_logger(
        correlation_id=event.get("correlation_id"),
        context=context,
        invoked_by=event.get("invoked_by")
    )
    
    logger.info("Evento recebido", payload=event)
    
    bucket_manager = BucketManager(logger=logger)
    list_buckets = bucket_manager.list_buckets_s3()
    
    return {
        "statusCode": 200,
        "body": json.dumps({"status": "sucesso", "buckets": list_buckets}),
        "correlation_id": logger.correlation_id
    }

lambda_handler({'teste':123},None)
