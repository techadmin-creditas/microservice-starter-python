"""
This module contains the various exception handlers
"""

import logging


def not_found_handler(error):
    logging.info("exception_handler" + str(error))
    error_details = error.get_error_object()
    return {
        "error_code": error_details.get('error_code'),
        "message": error_details.get('message')
    }, 404


def bad_request_handler(error):
    logging.info("exception_handler" + str(error))
    error_details = error.get_error_object()
    return {
        "error_code": error_details.get('error_code'),
        "message": error_details.get('message')
    }, 400


def internal_server_handler(error):
    logging.info("exception_handler" + str(error))
    return {
        "error_code": 'SRVX400',
        "message": "BadRequest",
    }, 400
