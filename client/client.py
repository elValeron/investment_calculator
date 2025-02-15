from __future__ import print_function

import grpc
from flask import flash, Flask, render_template, request

import investment_pb2
import investment_pb2_grpc

from config import Config, logger, SERVER_PORT
from forms import InvestmentCalculatorForm
from vars import FORM_FIELDS

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def render_form():
    form = InvestmentCalculatorForm()
    channel = grpc.insecure_channel('server:'+SERVER_PORT)
    stub = investment_pb2_grpc.InvestmentStub(channel)
    try:
        if request.method == "GET":
            logger.debug('Main template render successfully')
            return render_template('index.html', form=form)
        request_to_server = stub.CreateInvestment(
            investment_pb2.InvestmentRequest(
                investorFullName=form.investorFullName.data,
                initialDeposit=form.initialDeposit.data,
                interestRate=form.interestRate.data,
                investmentPeriod=form.investmentPeriod.data,
                compoundFrequency=form.compoundFrequency.data
            )
        )
        if request_to_server.HasField('errorDetail'):
            for error in request_to_server.errorDetail.error:
                flash(
                    (
                        error.reason.replace(
                            error.field,
                            FORM_FIELDS[error.field]
                        ),
                        error.field
                    )
                )
                logger.error(error.reason)
            return render_template('index.html', form=form)
        logger.debug(
            'Investment report for user '
            f'{request_to_server.investmentResult.investorName}'
            'has been generated'
        )
        return render_template('result.html', context=request_to_server)
    except grpc.RpcError as error:
        logger.fatal(str(error))
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
