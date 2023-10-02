

class PyRithmicException(Exception):
    pass


class EnvironmentNotConfiguredException(PyRithmicException):
    pass


class ConfigFileNotFoundException(PyRithmicException):
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
