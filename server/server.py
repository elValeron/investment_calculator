from concurrent import futures

from google.protobuf.json_format import MessageToDict
import grpc
import investment_pb2
import investment_pb2_grpc
from psycopg2.errors import IntegrityError, OperationalError

from config import logger, SERVER_PORT
from db import investment_journal
from utils import calculate_investment
from validators.validators import (
    check_request_fields_exists,
    EmptyFieldError,
    check_field_values
)


class InvestmentService(investment_pb2_grpc.InvestmentServicer):
    def CreateInvestment(self, request, response):
        error_list = []
        request_fields = MessageToDict(request, use_integers_for_enums=True)
        for field in request.DESCRIPTOR.fields:
            try:
                check_request_fields_exists(field, request_fields)
                check_field_values(field, request_fields)
            except (ValueError, EmptyFieldError) as error:
                error_list.append(
                    investment_pb2.CustomErrorDetail(
                        reason=error.args[0],
                        field=error.args[1]
                    )
                )
        if error_list:
            return investment_pb2.InvestmentResponse(
                errorDetail=investment_pb2.CustomFieldError(
                    error=error_list
                )
            )
        try:
            all_payments, total = calculate_investment(
                request_fields
            )
            request_fields['total'] = total
            investment_journal(request_fields)
            logger.debug(
                f'Added to journal investor: {request.investorFullName}'
            )
        except IntegrityError as e:
            logger.error(
                'Data has not been added to the journal.'
                f'error: {str(e)}'
            )
        except OperationalError as e:
            logger.error(
                f'database connection error: {str(e)}'
            )
        return investment_pb2.InvestmentResponse(
            investmentResult=investment_pb2.InvestmentResult(
                investorName=request.investorFullName,
                totalInvestmentAmount=total,
                paymentSchedule=all_payments
            )
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    investment_pb2_grpc.add_InvestmentServicer_to_server(
        InvestmentService(), server
    )
    logger.info(
        f'The grpc server is running, listening to port {SERVER_PORT}'
    )

    server.add_insecure_port(f'[::]:{SERVER_PORT}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        serve()
    except KeyboardInterrupt:
        logger.info('Server has stopped')
