from dotenv import load_dotenv, find_dotenv
import os

_ : bool = load_dotenv(".env") # read local .env file

print("Hello, world!")
print(os.environ.get('name'))
print(os.environ.get('db_keys'))

from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None






engine = create_engine(str(os.environ.get("db_keys")), echo=True)

SQLModel.metadata.create_all(engine)
