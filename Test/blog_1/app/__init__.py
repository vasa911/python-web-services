from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
import config

convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(column_0_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app, metadata=MetaData(naming_convention=convention))
migrate = Migrate(app, db)
api = Api(app)


from . import routes
from . import auth