from src.log_customizado.logger import CustomLogger


class LoggerFactory:
    @staticmethod
    def create_logger(correlation_id, context=None, invoked_by=None):
        return CustomLogger(
            correlation_id=correlation_id,
            context=context,
            invoked_by=invoked_by
        )
