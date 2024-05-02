from .log_context import LogContext
from .loki_logger import LokiLogger


class LokiContextLogger:
    def __init__(self, logger: LokiLogger):
        self.logger = logger
        self.log_context = LogContext()

    def _log(self, level, message, code=None, exc_info=None):
        self.log_context.set_message(message)
        tags = {"message_code": code}
        tags.update(self.log_context.get_tags())
        log_func = getattr(self.logger, level)
        if level == "exception":
            log_func(self.log_context.to_string(), tags, exc_info=exc_info)
        else:
            log_func(self.log_context.to_string(), tags)

    def debug(self, message, code=None):
        self._log('debug', message, code)

    def info(self, message, code=None):
        self._log('info', message, code)

    def warning(self, message, code=None):
        self._log('warning', message, code)

    def error(self, message, code=None):
        self._log('error', message, code)

    def critical(self, message, code=None):
        self._log('critical', message, code)

    def exception(self, message, exc_info=None, code=None):
        self._log('exception', message, code, exc_info)
