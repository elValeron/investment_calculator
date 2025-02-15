"""Модуль расчета инвестиций"""
from collections.abc import Iterable
import investment_pb2
from config import COMPOUND_FREQUENCY_TYPE


def calculate_investment(
        data: dict
) -> tuple[Iterable[investment_pb2.Payment], float]:
    """
    Функция расчета инвестиций, возвращает два кортеж со значениями:
    1. Список выплат Payment(payment_number, payment_amount)
    2. Вещественное число, - итоговый результат
    """
    payment_period = COMPOUND_FREQUENCY_TYPE[
        data['compoundFrequency']
    ]*data['investmentPeriod']
    investment_result = []
    for payment_number in range(
        1, payment_period+1
    ):
        investment_result.append(
            investment_pb2.Payment(
                paymentNumber=payment_number,
                paymentAmount=round(
                    int(data['initialDeposit'])*(
                        1+data['interestRate']/100/(
                            COMPOUND_FREQUENCY_TYPE[
                                data['compoundFrequency']
                            ]
                        )
                    )**payment_number,
                    2
                )
            )
        )
    return investment_result, investment_result.pop(-1).paymentAmount
