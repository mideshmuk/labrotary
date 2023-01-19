
from flask import Flask
from . import user
from flask_redis import FlaskRedis

app = Flask(__name__)
redis_client = FlaskRedis(app)

def create_app():  
    
    app = Flask(__name__, instance_relative_config=True)
    redis_client.init_app(app)

    app.register_blueprint(user.userBlueprint)

    return app