import abc


class BaseStrategy:
    name = None

    @staticmethod
    @abc.abstractmethod
    def run(input_value) -> dict:
        pass
