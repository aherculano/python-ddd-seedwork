import abc

from ddd_seedwork import Entity, DTO
from ddd_seedwork.domain.Exceptions import ValueObjectError
from ddd_seedwork.domain.ValueObject import ValueObject


class BaseMapper(abc.ABC):
    errors = []

    @abc.abstractmethod
    def domain_to_dto(self, dom: Entity) -> DTO:
        raise NotImplementedError()

    @abc.abstractmethod
    def dto_to_domain(self, dto: DTO) -> Entity:
        raise NotImplementedError()

    def _make_value_object(self, cls: ValueObject, *fields):
        try:
            return cls(*fields)
        except ValueObjectError as ve:
            self.errors.append({cls.__name__: ve.message})
