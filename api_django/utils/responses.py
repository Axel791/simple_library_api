from rest_framework.response import Response


def error_response_context(error_type, status_code, description):
    return {
        'error': {
            "status_code": status_code,
            "type": error_type,
            "description": description
        }
    }


def SuccessResponse(data=None, status=None, **kwargs):
    if data is None:
        data = {}
    return Response({"data": data}, status, **kwargs)


def ErrorResponse(error_type, status, description=None, **kwargs):
    description = description or error_type
    return Response(
        error_response_context(
            error_type=error_type,
            status_code=status,
            description=description
        )
    )
