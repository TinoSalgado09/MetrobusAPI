from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#decople maneja variables de entorno
from decouple import config

DB_DATABASE = config('DB_DATABASE')
DB_HOST = config('DB_HOST')
DB_USERNAME = config('DB_USERNAME')
DB_PASSWORD = config('DB_PASSWORD')
DB_PORT = config('DB_PORT')

# Varibale to connet to the database
SQLALCHEMY_DATABASE_URL = 'postgresql'+'://'+DB_USERNAME+':'+DB_PASSWORD+'@'+DB_HOST+'/'+DB_DATABASE

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()