from os import getenv
from flask import Flask
from flask_migrate import Migrate
from views.index import index_bp
from models.database import db

app = Flask(__name__)

CONFIG_OBJECT_PATH = "config.{}".format(getenv("CONFIG_NAME", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJECT_PATH)

db.init_app(app)

migrate = Migrate(app, db)
app.register_blueprint(index_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
