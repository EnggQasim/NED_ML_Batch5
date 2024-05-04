`poetry add fastapi uvicorn httpx httpie requests`
step 1: create `main.py` file in subfolder
```
from fastapi import FastAPI


app : FastAPI = FastAPI()


@app.get('/')
def index():
    return {"Hello": "world"}

```

Run poetry project:
`poetry run uvicorn ned_fastapi.main:app --reload`

## Moc server or Auto documentation of your application
`http://localhost:8000/docs`

# REferences
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
* https://fastapi.tiangolo.com/tutorial/first-steps/
