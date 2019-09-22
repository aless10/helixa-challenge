import abc

from helixa_app.schema.schema import RequestModel


class BaseStrategy:
    name = None

    @staticmethod
    @abc.abstractmethod
    def run(input_value: RequestModel) -> dict:
        pass
