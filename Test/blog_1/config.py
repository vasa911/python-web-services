import pathlib


BASE_DIR = pathlib.WindowsPath(__file__).parent

class Config:
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(BASE_DIR / "data" / "db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ksadhfjadshHG*&Y$@'