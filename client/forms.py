from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    StringField,
    IntegerField,
    FloatField,
    SubmitField
)

from vars import COMPOUND_FREQUENCY_TYPE, FORM_FIELDS


class InvestmentCalculatorForm(FlaskForm):

    investorFullName = StringField(
        label=FORM_FIELDS['investorFullName']
    )
    initialDeposit = IntegerField(
        label=FORM_FIELDS['initialDeposit']
    )
    interestRate = FloatField(
        label=FORM_FIELDS['interestRate']
    )
    investmentPeriod = IntegerField(
        label=FORM_FIELDS['investmentPeriod']
    )
    compoundFrequency = SelectField(
        label=FORM_FIELDS['compoundFrequency'],
        choices=COMPOUND_FREQUENCY_TYPE.keys()
    )
    calculate = SubmitField(
        label=FORM_FIELDS['calculate']
    )
