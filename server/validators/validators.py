from numbers import Number

from config import COMPOUND_FREQUENCY_TYPE
from .exeptions import EmptyFieldError


def check_field_values(field, request_fields):
    """
    Проверка наличия полей, в случае нулевого или отрицательного значения
    поднимается исключение ValueError с параметрами:
    1. Сообщение с названием поля и кратким описанием.
    2. Названия поля
    """
    if isinstance(request_fields[field.name], Number):
        if request_fields[field.name] <= 0:
            raise ValueError(
                f'{field.name} поле должно быть положительным числом',
                field.name
                )
    if field.name == 'compound_frequency':
        check_compound_frequency_value(request_fields[field.name])


def check_range_interest_rate(interest_rate: float):
    """
    Проверка соответствия значения поля interest_rate
    вхождению в диапазон значений.
    """
    if not (0.1 < interest_rate < 40):
        raise ValueError(
            'Процентная ставка не может быть меньше 0.1% и больше 40%',
            'interest_rate'
        )


def check_request_fields_exists(field, request_fields):
    """
    Проверка наличия поля/значения поля в запросе от клиента
    """
    if field.name not in request_fields.keys():
        raise EmptyFieldError(
            f'{field.name} обязательное поле',
            field.name
        )


def check_compound_frequency_value(compound_frequency):
    if compound_frequency not in COMPOUND_FREQUENCY_TYPE.keys():
        ValueError(
            (
                'Неправильное значение поля compound_frequency'
                'Допустимые варинты значения:'
                '"dayly", "weekly", "monthly",'
                '"quarterly", "semiannually", "annually"'
            ),
            compound_frequency
        )
