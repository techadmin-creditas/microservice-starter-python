"""
This is the starter app to launch the microservice application

Example:
    To launch the application, use python ./src/app.py
"""

import connexion
import logging

from controllers.health import health

logging.basicConfig(level=logging.DEBUG)
PORT = 5001
HOST = "0.0.0.0"

# For more configuration https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/
options = {
    "swagger_ui": False,
    "swagger_ui_config": {
        "displayOperationId": False
    }
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

    app.run(port=PORT, host=HOST)
    logging.INFO(f"Application is running on port:{PORT}")
