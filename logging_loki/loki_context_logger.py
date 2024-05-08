from .log_context import LogContext
from .loki_logger import LokiLogger


class LokiContextLogger:
    def __init__(self, logger: LokiLogger):
        self.logger = logger

    def _log(self, level, message, code=None, log_context: LogContext | None = LogContext(), exc_info=None):
        log_context.set_message(message)
        tags = {"message_code": code}
        tags.update(log_context.get_tags())
        log_func = getattr(self.logger, level)
        if level == "exception":
            log_func(log_context.to_string(), tags, exc_info=exc_info)
        else:
            log_func(log_context.to_string(), tags)

    def debug(self, message, code=None, log_context=None):
        self._log('debug', message, code, log_context)

    def info(self, message, code=None, log_context=None):
        self._log('info', message, code, log_context)

    def warning(self, message, code=None, log_context=None):
        self._log('warning', message, code, log_context)

    def error(self, message, code=None, log_context=None):
        self._log('error', message, code, log_context)

    def critical(self, message, code=None, log_context=None):
        self._log('critical', message, code, log_context)

    def exception(self, message, exc_info=None, code=None, log_context=None):
        self._log('exception', message, code, log_context, exc_info)
