from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomErrorDetail(_message.Message):
    __slots__ = ("reason", "field")
    REASON_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    reason: str
    field: str
    def __init__(self, reason: _Optional[str] = ..., field: _Optional[str] = ...) -> None: ...

class Payment(_message.Message):
    __slots__ = ("paymentNumber", "paymentAmount")
    PAYMENTNUMBER_FIELD_NUMBER: _ClassVar[int]
    PAYMENTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    paymentNumber: int
    paymentAmount: float
    def __init__(self, paymentNumber: _Optional[int] = ..., paymentAmount: _Optional[float] = ...) -> None: ...

class InvestmentResult(_message.Message):
    __slots__ = ("investorName", "totalInvestmentAmount", "paymentSchedule")
    INVESTORNAME_FIELD_NUMBER: _ClassVar[int]
    TOTALINVESTMENTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAYMENTSCHEDULE_FIELD_NUMBER: _ClassVar[int]
    investorName: str
    totalInvestmentAmount: float
    paymentSchedule: _containers.RepeatedCompositeFieldContainer[Payment]
    def __init__(self, investorName: _Optional[str] = ..., totalInvestmentAmount: _Optional[float] = ..., paymentSchedule: _Optional[_Iterable[_Union[Payment, _Mapping]]] = ...) -> None: ...

class InvestmentRequest(_message.Message):
    __slots__ = ("investorFullName", "initialDeposit", "interestRate", "investmentPeriod", "compoundFrequency")
    INVESTORFULLNAME_FIELD_NUMBER: _ClassVar[int]
    INITIALDEPOSIT_FIELD_NUMBER: _ClassVar[int]
    INTERESTRATE_FIELD_NUMBER: _ClassVar[int]
    INVESTMENTPERIOD_FIELD_NUMBER: _ClassVar[int]
    COMPOUNDFREQUENCY_FIELD_NUMBER: _ClassVar[int]
    investorFullName: str
    initialDeposit: int
    interestRate: float
    investmentPeriod: int
    compoundFrequency: str
    def __init__(self, investorFullName: _Optional[str] = ..., initialDeposit: _Optional[int] = ..., interestRate: _Optional[float] = ..., investmentPeriod: _Optional[int] = ..., compoundFrequency: _Optional[str] = ...) -> None: ...

class CustomFieldError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _containers.RepeatedCompositeFieldContainer[CustomErrorDetail]
    def __init__(self, error: _Optional[_Iterable[_Union[CustomErrorDetail, _Mapping]]] = ...) -> None: ...

class InvestmentResponse(_message.Message):
    __slots__ = ("investmentResult", "errorDetail")
    INVESTMENTRESULT_FIELD_NUMBER: _ClassVar[int]
    ERRORDETAIL_FIELD_NUMBER: _ClassVar[int]
    investmentResult: InvestmentResult
    errorDetail: CustomFieldError
    def __init__(self, investmentResult: _Optional[_Union[InvestmentResult, _Mapping]] = ..., errorDetail: _Optional[_Union[CustomFieldError, _Mapping]] = ...) -> None: ...
