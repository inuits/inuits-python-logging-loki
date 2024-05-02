import json

from .loki_logger import LokiLogger


class JsonLokiLogger:
    def __init__(
            self, loki_logger: LokiLogger
    ):
        self._loki_logger = loki_logger

    def _log(self, level, msg: str, tags: dict | None = None, extra_json_properties: dict | None = None,
             exc_info=None):
        loki_log_func = getattr(self._loki_logger, level)
        dict_msg = {"message": msg}
        if extra_json_properties is not None:
            dict_msg.update(extra_json_properties)
        if level == 'exception':
            loki_log_func(json.dumps(dict_msg), tags, exc_info=exc_info)
        else:
            loki_log_func(json.dumps(dict_msg), tags)

    def debug(self, msg: str, tags: dict | None = None, extra_json_properties: dict | None = None):
        self._log('debug', msg, tags=tags, extra_json_properties=extra_json_properties)

    def info(self, msg: str, tags: dict | None = None, extra_json_properties: dict | None = None):
        self._log('info', msg, tags=tags, extra_json_properties=extra_json_properties)

    def warning(self, msg: str, tags: dict | None = None, extra_json_properties: dict | None = None):
        self._log('warning', msg, tags=tags, extra_json_properties=extra_json_properties)

    def error(self, msg: str, tags: dict | None = None, extra_json_properties: dict | None = None):
        self._log('error', msg, tags=tags, extra_json_properties=extra_json_properties)

    def critical(self, msg: str, tags: dict | None = None, extra_json_properties: dict | None = None):
        self._log('critical', msg, tags=tags, extra_json_properties=extra_json_properties)

    def exception(self, msg, tags: dict | None = None, extra_json_properties: dict | None = None, exc_info=None):
        self._log('exception', msg, tags=tags, extra_json_properties=extra_json_properties, exc_info=exc_info)
