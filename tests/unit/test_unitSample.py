import pytest
import connexion
from api import health


def test_app():
#arrange
 flask_app = connexion.FlaskApp(__name__,specification_dir='../../openapi',options = {"swagger_ui": True,"swagger_ui_config": {"displayOperationId": False}},server='flask')
#act
 flask_app.add_api('testSpec.yaml')
 with flask_app.app.test_client() as c:
    response=health()
 flask_app.run(port=5001)
#assert
 assert response==({'msg': 'ok'}, 200)
   

 