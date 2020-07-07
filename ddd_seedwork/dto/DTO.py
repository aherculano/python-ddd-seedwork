import abc


class DTO(abc.ABC):
    @abc.abstractmethod
    def to_dict(self):
        raise NotImplementedError
