import abc

from ddd_seedwork.domain.Exceptions import ValueObjectError
from ddd_seedwork.domain.ValidationRule import ValidationRule


class ValueObject(abc.ABC):

    def check_rule(self, validator: ValidationRule):
        if not validator.is_valid():
            raise ValueObjectError(validator.message)
