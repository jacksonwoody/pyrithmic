

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
