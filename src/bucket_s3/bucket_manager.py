import boto3
from botocore.exceptions import BotoCoreError, ClientError

class BucketManager:
    def __init__(self, logger):
        self.s3_client = boto3.client("s3")
        self.logger = logger

    def list_buckets_s3(self):
        self.logger.info("Iniciando listagem de buckets S3")
        try:
            response = self.s3_client.list_buckets()
            if not response.get("Buckets"):
                self.logger.warning("Nenhum bucket encontrado", payload="")
                return []
            bucket_names = [bucket["Name"] for bucket in response.get("Buckets", [])]
            self.logger.info("Buckets encontrados com sucesso", payload=bucket_names)
            return bucket_names
        except (BotoCoreError, ClientError) as e:
            self.logger.error("Erro ao listar buckets", payload={"erro": str(e)})
            raise
