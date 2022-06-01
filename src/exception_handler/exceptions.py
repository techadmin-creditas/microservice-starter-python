"""
This module will contain the various exceptions.
"""

import logging
import werkzeug.exceptions as e


class NotFoundException(RuntimeError):
    """Not found."""


class NotFoundException(NotFoundException):
    error_object = {}

    def __init__(self, error_code, message, detail):
        response = {
            "error_code": error_code,
            "message": message,
            "detail": detail
        }
        logging.info(f"response : {response}")
        super().__init__(response)
        self.set_error_object(response)

    def set_error_object(self, response):
        self.error_object = response

    def get_error_object(self):
        return self.error_object


class BadRequestException(RuntimeError):
    """Bad Request"""


class BadRequestException(BadRequestException):
    error_object = {}

    def __init__(self, error_code, message, detail):
        response = {
            "error_code": error_code,
            "message": message,
            "detail": detail
        }
        logging.info(f"response : {response}")
        super().__init__(response)
        self.set_error_object(response)

    def set_error_object(self, response):
        self.error_object = response

    def get_error_object(self):
        return self.error_object


class InternalServerError(RuntimeError):
    """Internal server error"""


class MyInternalServerError(e.InternalServerError):
    def __init__(self, id):
        super().__init__(f"ID '{id}' something went worng.")
