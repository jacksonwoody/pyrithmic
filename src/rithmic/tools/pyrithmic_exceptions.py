

class PyRithmicException(Exception):
    pass


class EnvironmentNotConfiguredException(PyRithmicException):
    pass


class ConfigFileNotFoundException(PyRithmicException):
    pass


class RithmicCredentialPathNotSetException(PyRithmicException):
    pass


class WebsocketClosedException(PyRithmicException):
    pass


class MissingCustomCallback(PyRithmicException):
    pass


class CallbackIdNotFoundException(PyRithmicException):
    pass


class NoValidTradingAccountException(PyRithmicException):
    pass


class NoValidTradeRouteException(PyRithmicException):
    pass


class NoTradingConfigException(PyRithmicException):
    pass


class DuplicateOrderIdException(PyRithmicException):
    pass


class UncancellableOrderException(PyRithmicException):
    pass


class UnmodifiableOrderException(PyRithmicException):
    pass


class ReferenceDataUnavailableException(PyRithmicException):
    def __init__(self, message, request_id):
        super().__init__(message)
        self.request_id = request_id


class DownloadErrorException(PyRithmicException):
    pass
