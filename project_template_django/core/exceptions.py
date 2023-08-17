import logging


def guard(
    *,
    message: str,
    exc: Exception,
    panic: bool = True,
    logger_name: str = "core.exceptions",
    log_errors: bool = True
) -> None:
    """
    Guards an exception.
    - control panic, i.e. raise the exception
    - control logging, i.e. log the exception

    ! this might include !not! panicking when there is an excpetion that should be raised.

    Use the flags with care. Preferably, in dev only - or have a very specific
    usecase (like the --no-panic flag on project setup `commands.py setup --production --no-panic`).
    """
    if log_errors:
        log = logging.getLogger(logger_name)
        log.error(message)
    if panic:
        raise exc
