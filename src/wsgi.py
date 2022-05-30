import connexion

options = {
    "swagger_ui": False,
    "swagger_ui_config": {
        "displayOperationId": False
    }
}

from controllers.health import health




def get_application():
    app = connexion.FlaskApp(__name__,
                             specification_dir='../openapi',
                             options=options)
    app.add_api('spec.yaml')
    app.add_url_rule("/health", "health", health)
    return app


application = get_application()