from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from dataclasses import dataclass, field
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


@dataclass
class Container:
    database_url: str
    _app: Flask = field(init=False)
    _db: SQLAlchemy = field(init=False)
    _manager: APIManager = field(init=False)

    def __post_init__(self):
        self._app = Flask(__name__)
        self._app.config['SQLALCHEMY_DATABASE_URI'] = self.database_url
        self._db = SQLAlchemy(self._app)
        self._manager = APIManager(self._app, flask_sqlalchemy_db=self._db)

    @property
    def db(self):
        return self._db

    @property
    def app(self):
        return self._app


container = Container(
    database_url=os.getenv('DATABASE_URL'),
)
