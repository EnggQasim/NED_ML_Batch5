from dotenv import load_dotenv, find_dotenv
import os

_ : bool = load_dotenv(".env") # read local .env file

print("Hello, world!")
print(os.environ.get('name'))
