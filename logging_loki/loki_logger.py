import logging
import logging.handlers
from multiprocessing import Queue
from .handlers import LokiHandler


class LokiLogger:
    def __init__(
        self,
        loki_url: str | None = None,
        default_loki_labels: dict | None = None,
        headers: dict | None = None,
        log_format: str | None = None,
        log_dateformat: str | None = None,
        log_level: str | int = logging.INFO
    ):
        logging.basicConfig(
            format="%(asctime)s %(process)d,%(threadName)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s" if
            log_format is None else log_format,
            datefmt="%Y-%m-%d %H:%M:%S" if log_dateformat is None else log_dateformat,
            level=log_level
        )
        self.logger = logging.getLogger(__name__)
        # only log to loki if loki_url is configured
        if loki_url:
            queue = Queue(-1)
            logging.handlers.QueueHandler(queue)
            handler_loki = LokiHandler(
                url=loki_url,
                tags=default_loki_labels,
                headers=headers,
            )
            logging.handlers.QueueListener(queue, handler_loki)
            self.logger.addHandler(handler_loki)
            self.info(
                "Loki url is configured, logs will be exported to Loki"
            )
        else:
            self.info(
                "Loki url is not configured, logs will not be exported to Loki"
            )

    def debug(self, msg: str, tags=None):
        self.logger.debug(msg, extra={
            "tags": tags if tags else {}})

    def info(self, msg: str, tags=None):
        self.logger.info(msg, extra={
            "tags": tags if tags else {}})

    def warning(self, msg: str, tags=None):
        self.logger.warning(msg, extra={
            "tags": tags if tags else {}})

    def error(self, msg: str, tags=None):
        self.logger.error(msg, extra={
            "tags": tags if tags else {}})

    def critical(self, msg: str, tags=None):
        self.logger.critical(msg, extra={
            "tags": tags if tags else {}})

    def exception(self, msg: str, tags=None, exc_info=None):
        self.logger.exception(
            msg, exc_info=exc_info, extra={
                "tags": tags if tags else {}
            }
        )
