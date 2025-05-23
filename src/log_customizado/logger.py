import uuid
import json
import inspect
from datetime import datetime
from zoneinfo import ZoneInfo
import logging

BRASILIA_TZ = ZoneInfo("America/Sao_Paulo")
LAMBDA_NAME = "Nome_lambda"

class CustomLogger:
    def __init__(self, correlation_id=None, context=None, invoked_by=None):
        self.correlation_id = correlation_id or str(uuid.uuid4())
        self.context = context
        self.invoked_by = invoked_by
    
    @staticmethod
    def _get_brasilia_time():
        return datetime.now(BRASILIA_TZ).strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def _get_caller_info():
        for frame_info in inspect.stack():
            if frame_info.function not in ["_log", "_get_caller_info", "info", "warning", "error", "debug"]:
                module = inspect.getmodule(frame_info.frame)
                module_name = module.__name__ if module else "unknown"
                filename = frame_info.filename.split('/')[-1].split('\\')[-1]
                lineno = frame_info.lineno
                function_name = frame_info.function
                cls_name = None
                if "self" in frame_info.frame.f_locals:
                    cls_name = type(frame_info.frame.f_locals["self"]).__name__
                if cls_name:
                    return f"module={module_name}, file={filename}, class={cls_name}, function={function_name}, line={lineno}"
                else:
                    return f"module={module_name}, file={filename}, function={function_name}, line={lineno}"
        return "caller_info_not_found"
    
    def _log(self, message, level, payload=None):
        log_entry = {
            "correlationId": self.correlation_id,
            "appName": LAMBDA_NAME,
            "timeStamp": self._get_brasilia_time(),
            "level": level,
            "invoked_by": self.invoked_by,
            "code_location": self._get_caller_info(),
            "message": message,
        }
        if self.context:
            log_entry["function_name"] = getattr(self.context, "function_name", None)
            log_entry["aws_request_id"] = getattr(self.context, "aws_request_id", None)
        
        if payload is not None:
            log_entry["payload"] = payload
        
        log_json = json.dumps(log_entry, ensure_ascii=False, separators=(',', ': '), default=str)
        log_func = getattr(logging, level.lower(), logging.info)
        log_func(log_json)
    
    def info(self, message, payload=None):
        self._log(message, level="INFO", payload=payload)
    
    def warning(self, message, payload=None):
        self._log(message, level="WARNING", payload=payload)
    
    def error(self, message, payload=None):
        self._log(message, level="ERROR", payload=payload)
    
    def debug(self, message, payload=None):
        self._log(message, level="DEBUG", payload=payload)
