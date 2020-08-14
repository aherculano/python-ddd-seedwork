import abc


class ValidationRule(abc.ABC):
    message: dict = None

    @abc.abstractmethod
    def is_valid(self) -> bool:
        raise NotImplementedError
