import random

import uvicorn
from fastapi import FastAPI, status

app = FastAPI(
    debug=True
)


@app.get('/', status_code=status.HTTP_200_OK)
def who_are_you():
    return {'detail': 'This is \"Calculator\" app'}


@app.get('/calculate', status_code=status.HTTP_200_OK)
def calculate():
    value = 0
    for i in range(100):
        value += random.randint(0, 10 ** 100)
    return {'value': value}


if __name__ == "__main__":
    uvicorn.run("calculator:app", host="0.0.0.0", port=8000, reload=True)
