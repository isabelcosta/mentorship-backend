import os

from flask import Flask, jsonify, json
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
from app.security import authenticate, identity
from datetime import datetime
from config import get_env_config

application = Flask(__name__)

# setup application environment
application.config.from_object(get_env_config())

api = Api(
    app=application,
    title='Mentorship System API',
    version='1.0',
    description='API documentation for the backend of Mentorship System',
    # doc='/docs/'
)

@application.before_first_request
def create_tables():
    from app.database.db_utils import db
    db.create_all()

# Adding namespaces
def add_namespaces():
    # called here to avoid circular imports
    from app.api.resources.user import users_ns as user_namespace
    api.add_namespace(user_namespace, path='/')
    from app.api.resources.admin import admin_ns as admin_namespace
    api.add_namespace(admin_namespace, path='/')
    from app.api.resources.mentorship_relation import mentorship_relation_ns as mentorship_namespace
    api.add_namespace(mentorship_namespace, path='/')


jwt = JWT(application, authenticate, identity)


@jwt.auth_response_handler
def custom_jwt_response_handler(access_token, identity):
    payload = jwt.jwt_payload_callback(identity)

    if 'exp' in payload:
        expiry = payload['exp']
    else:
        expiry = datetime.utcnow() + application.config.get('JWT_EXPIRATION_DELTA')

    return jsonify({
        'access_token': access_token.decode('utf-8'),
        'expiry': expiry.timestamp()
    })


db = SQLAlchemy(application)


@application.before_first_request
def create_tables():
    # db.drop_all()
    db.create_all()


def export_api_to_postman():
    # previous_value = application.config['SERVER_NAME']
    # application.config['SERVER_NAME'] = 'localhost:5000/'
    with application.app_context():
        urlvars = False  # Build query strings in URLs
        swagger = True  # Export Swagger specifications
        data = api.as_postman(urlvars=urlvars, swagger=swagger)
        f = open(os.path.join('docs', 'postman_collection_v1.json'), 'w')
        f.write(json.dumps(data))
        f = open(os.path.join('docs', 'swagger_generated.json'), 'w')
        f.write(json.dumps(api.__schema__))
    # application.config['SERVER_NAME'] = previous_value


if __name__ == "__main__":
    add_namespaces()
    export_api_to_postman()
    application.run(port=5000)

