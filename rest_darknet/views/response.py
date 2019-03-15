

class Response(object):

    def __init__(self, body, status_code):
        self.body = body
        self.status_code = status_code


    def to_dict(self):
        return self.__dict__


    def __str__(self):
        return str(self.to_dict())


class SuccessResponse(Response):

    SUCCESS_STATUS_CODES = {
        "OK": 200
    }

    def __init__(self, body, status_code):
        super().__init__(body, self.SUCCESS_STATUS_CODES[status_code])



NO_IMAGE_FOUND = Response(
    {
        "error": "No image found in request"
    },
    400
)


NOT_ALLOWED_FILE = Response(
    {
        "error": "Not allowed file"
    },
    400
)

NO_SELECTED_IMAGE = Response(
    {
        "error": "No selected image"
    },
    400
)

NOT_ALLOWED_METHOD = Response(
    {
        "error": "Method not allowed"
    },
    405
)

INTERNAL_SERVER_ERROR = Response(
    {
        "error": "Internal server error"
    },
    500
)

