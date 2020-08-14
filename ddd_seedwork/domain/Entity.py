import abc

from ddd_seedwork.domain.ValueObject import ValueObject


class Entity(abc.ABC):
    domain_id = None
    errors = []

    def get_errors(self):
        for key in self.__dict__:
            obj = self.__dict__.get(key)
            if type(obj) is ValueObject:
                obj: ValueObject
                print(obj.errors)

    def __eq__(self, e) -> bool:
        return e.domain_id == self.domain_id and type(self) == type(e)
