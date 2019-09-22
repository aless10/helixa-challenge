import abc


class BaseStrategy:
    name = None

    @staticmethod
    @abc.abstractmethod
    def run(input_value) -> dict:
        pass

    def __str__(self) -> str:
        return f"Strategy:{self.name}"
