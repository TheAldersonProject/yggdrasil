"""Basic logging class for logging in JSON format."""

import logging
from enum import Enum
from functools import wraps
from typing import Any, Callable, TypeVar
from uuid import uuid4

import structlog

R = TypeVar("R")


class LogLevel(Enum):
    """Enum for logging levels.

    Used to define the log level, possible to use:
    Debug = logging.DEBUG
    Info = logging.INFO
    Warning = logging.WARNING
    Error = logging.ERROR
    Critical = logging.CRITICAL
    """

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def get_logger(log_level: LogLevel = LogLevel.DEBUG) -> "Logger":
    """Get logger with default parameters."""
    return Logger(log_level=log_level)


class Logger:
    """Basic logging class for logging in JSON format."""

    def __init__(
        self,
        log_level: LogLevel = LogLevel.DEBUG,
        logger_uuid: str | None = None,
    ) -> None:
        """
        Configures and initializes a structured logging system, setting up logging
        parameters and providing support for JSON-rendered logs. The logger defaults
        to a unique identifier unless explicitly set.

        :param log_level: The logging level to use. Defaults to LogLevel.DEBUG.
        :param logger_uuid: A unique string identifier for the logger. If none is
            provided, a new UUID will be generated.
        """
        logging.basicConfig(
            format="%(message)s",
            level=log_level.value,
        )

        structlog.configure(
            processors=[
                structlog.contextvars.merge_contextvars,
                structlog.processors.add_log_level,
                structlog.processors.StackInfoRenderer(),
                structlog.dev.set_exc_info,
                structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=True),
                structlog.dev.ConsoleRenderer(),
            ],
            wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
            context_class=dict,
            logger_factory=structlog.PrintLoggerFactory(),
            cache_logger_on_first_use=False,
        )

        self._uuid = logger_uuid or str(uuid4())
        self._log = structlog.get_logger()

    @staticmethod
    def log(func: Callable[..., R]) -> Callable[..., R]:
        """
        A static method that serves as a decorator to add custom logging behavior to a function.

        This method wraps a given function (e.g., `debug`, `info`, `warning`) and dynamically attaches
        additional behavior for logging purposes. Specifically, it appends an ` uuid ` to the keyword arguments
        to ensure traceability in logs. The decorator retrieves the corresponding logging method from the
        wrapped logger and invokes it dynamically. The wrapped function itself is not modified but is
        augmented with additional functionality.

        :param func: The function to be wrapped, typically a logging method (e.g., `debug`, `info`, etc.).
        :type func: Callable
        :return: The wrapped function with enhanced logging capabilities.
        :rtype: Callable
        """

        @wraps(func)
        def logger(self, message: str, **kwargs):
            """
            Logs a message by dynamically calling a log method from the wrapped logging object.

            The logger dynamically determines the log method (e.g., debug, info, warning) from the wrapped
            logging object based on the name of the function being wrapped. A `uuid` is added to the
            log kwargs for traceability during logging.

            :param self:
            :param message: The log message to be recorded.
            :type message: Str
            :param kwargs: Additional keyword arguments to pass to the logging method.
            :type kwargs: Dict
            :return: The result of calling the appropriate log method from the wrapped logging object.
            :rtype: Any
            """
            kwargs = kwargs or {}
            kwargs["uuid"] = self._uuid
            # kwargs["uid"] = str(uuid4())
            log_method = getattr(self._log, func.__name__)

            return log_method(message, **kwargs)

        return logger

    @log
    def info(self, message: str, **kwargs) -> Any:
        """
        Logs an informational message.

        This method is used to log messages with the informational severity level.
        It can accept a message as a string and additional keyword arguments for
        customized logging details.

        :param message: The message string to be logged as informational.
        :type message: Str
        :param kwargs: Additional context or metadata to be logged along with
            the message. Should be provided as keyword arguments.
        :type kwargs: Dict
        :return: None
        :rtype: None
        """

    @log
    def debug(self, message: str, **kwargs) -> None:
        """
        Logs a debug message with the specified content and additional keyword arguments.

        This method allows logging of a debug-level message. The message provided
        and optional additional keyword arguments are passed and formatted for
        the logging system. Debug-level messages are typically used for detailed
        internal application events that are useful during development or for
        troubleshooting.

        :param message: A string containing the debug message to be logged.
        :param kwargs: Additional keyword arguments that may provide relevant
            details or context for the logged message.
        :return: None
        """

    @log
    def warning(self, message: str, **kwargs) -> None:
        """
        Logs a warning-level message with optional keyword arguments.

        This method logs a message using a warning level. It can take additional
        keyword arguments that may provide further contextual details about the
        message being logged. The logging behavior is decorated to include additional
        processing defined by the `_log_decorator`.

        :param message: The warning message to be logged.
        :type message: Str
        :param kwargs: Additional context or information to include in the log entry.
        :type kwargs: Dict
        :return: None
        """

    @log
    def error(self, message: str, **kwargs) -> None:
        """
        Logs an error message.

        This method is used to log messages at the error level. It accepts a message
        string and additional keyword arguments that can be used for contextual
        information.

        :param message: The error message to be logged.
        :type message: Str
        :param kwargs: Additional optional keyword arguments that provide more
            context about the error.
        :return: Nothing.
        :rtype: None
        """

    @log
    def critical(self, message: str, **kwargs) -> None:
        """
        Logs a critical severity message to the logging system. This method uses a
        decorator to process the log entry before execution.

        The critical log level typically indicates severe errors that might cause the
        application to terminate or fail. Use this for urgent, unrecoverable events.

        :param message: The critical log message to be recorded.
        :type message: Str
        :param kwargs: Additional keyword arguments that might need to be used for
            logging customization or context.
        :return: This method does not return a value.
        :rtype: None
        """
