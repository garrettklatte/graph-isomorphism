import decimal

from delivery.aws_lambda import http_response

def test_decimal_encoding():
    # Given
    message = decimal.Decimal('14.5')
    status_code = 200

    # When
    response = http_response(status_code, message)

    # Then
    assert response == {
        "statusCode": 200,
        "body": '14.5',
        "headers": {"Access-Control-Allow-Origin": "*"}}
