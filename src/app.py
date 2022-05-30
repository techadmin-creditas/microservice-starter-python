"""
This is the starter app to launch the microservice application

Example:
    To launch the application, use python ./src/app.py
"""

import connexion
import logging

from controllers.health import health
from exception_handler import exceptions, exception_handlers



logging.basicConfig(level=logging.DEBUG)
PORT = 5001
HOST = "0.0.0.0"

# For more configuration https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
options = {
    "swagger_ui": True,
    "swagger_ui_config": {
        "displayOperationId": False
    }
}

exception_codes = {
    401 : "Unauthorized",
    403 : "Forbidden",
    405 : "Method Not Allowed",
    500 : "Internal Server Error"
}

if __name__ == '__main__':
    """
    Configure the application and launch the service    
    """
    app = connexion.FlaskApp(__name__,
                             specification_dir='../openapi',
                             options=options,
                             server='flask')
    app.add_api('spec.yaml')
    app.add_url_rule("/health", "health", health)
    
    # Exception handlers
    app.add_error_handler(exceptions.NotFoundException, exception_handlers.not_found_handler)
    app.add_error_handler(exceptions.BadRequestException, exception_handlers.bad_request_handler)

    for i in exception_codes.keys():
        app.add_error_handler(i, exception_handlers.internal_server_handler)




    app.run(port=PORT, host=HOST)
    logging.INFO(f"Application is running on port:{PORT}")
