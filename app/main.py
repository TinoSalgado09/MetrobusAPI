from fastapi import FastAPI
from strawberry.asgi import GraphQL

from app.db import SessionLocal

from .schema import schema

graphql_app = GraphQL(schema)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.mount("/graphql", graphql_app)


