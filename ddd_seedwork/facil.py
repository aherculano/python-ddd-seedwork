from ddd_seedwork import Entity, DTO
from ddd_seedwork.domain import DomainError
from ddd_seedwork.domain.ValidationRule import ValidationRule
from ddd_seedwork.domain.ValueObject import ValueObject
from ddd_seedwork.mapper.BaseMapper import BaseMapper


class NotNoneValidator(ValidationRule):
    message = "{} cant be none"

    def __init__(self, value: str, field: str):
        self._value = value
        self.message = self.message.format(field)

    def is_valid(self) -> bool:
        return self._value is not None


class NotEmptyValidator(ValidationRule):
    message = "{} cant be empty"

    def __init__(self, value: str, field: str):
        self._value = value
        self.message = self.message.format(field)

    def is_valid(self) -> bool:
        return len(self._value.strip()) != 0


class NotNegativeValidator(ValidationRule):
    message = "{} cant be negative"

    def __init__(self, value: str, field: str):
        self._value = value
        self.message = self.message.format(field)

    def is_valid(self) -> bool:
        return self._value >= 0


class Name(ValueObject):
    def __init__(self, name: str):
        self.check_rule(NotNoneValidator(name, "name"))
        self.check_rule(NotEmptyValidator(name, "name"))
        self.name = name


class Address(ValueObject):
    def __init__(self, street: str, house_number: int):
        self.check_rule(NotNoneValidator(street, "street"))
        self.check_rule(NotNoneValidator(house_number, "house_number"))
        self.check_rule(NotEmptyValidator(street, "street"))
        self.check_rule(NotNegativeValidator(house_number, "house_number"))
        self.street = street
        self.house_number = house_number


class Person(Entity):
    def __init__(self, name: Name, address: Address):
        self.name = name
        self.address = address


class PersonDTO(DTO):

    def __init__(self, name: str, street: str, house_number: int):
        self.name = name
        self.street = street
        self.house_number = house_number

    def to_dict(self):
        return {
            "name": self.name,
            "street": self.street,
            "house_number": self.house_number
        }


class PersonMapper(BaseMapper):

    def domain_to_dto(self, dom: Person) -> PersonDTO:
        return PersonDTO(
            dom.name.name, dom.address.street, dom.address.house_number
        )

    def dto_to_domain(self, dto: PersonDTO) -> Person:
        self.errors = []
        person_name = self._make_value_object(Name, dto.name)
        address = self._make_value_object(Address, dto.street, dto.house_number)
        if len(self.errors) > 0:
            raise DomainError(self.errors, "Error Creating a Person")
        return Person(person_name, address)


if __name__ == '__main__':
    person_dto1 = PersonDTO("Name", "Street", 1)
    person_dto2 = PersonDTO("", "", 1)
    mapper = PersonMapper()
    person1 = mapper.dto_to_domain(person_dto1)
    try:
        person2 = mapper.dto_to_domain(person_dto2)
    except DomainError as de:
        print(de.notifications)
