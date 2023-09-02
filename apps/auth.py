import uvicorn
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI(
    debug=True
)


def get_users_list():
    with open('users.txt', 'r') as users_file:
        return {user.split(':')[0]: user.split(':')[1] for user in users_file.read().strip().split('\n')}


def add_user(user, passwd):
    users = get_users_list()
    if not users.get(user, False):
        with open('users.txt', 'a') as file:
            file.write(f'\n{user}:{passwd}')
        return True, 'user added'
    return False, 'User exist'


class Credential(BaseModel):
    username: str
    password: str


@app.get('/', status_code=status.HTTP_200_OK)
def who_are_you():
    return {'detail': 'This is \"Auth\" app'}


@app.post('/login', status_code=status.HTTP_200_OK)
def login(credential: Credential):
    users = get_users_list()
    if users.get(credential.username, False) and users.get(credential.username, False) == credential.password:
        return {'detail': 'Logged in successful!'}
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Invalid user or password!'
    )


@app.post('/register', status_code=status.HTTP_201_CREATED)
def register(user: str, passwd: str):
    if add_user(user, passwd)[0]:
        return {'detail': 'User added'}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail='Username exist!'
    )


if __name__ == "__main__":
    uvicorn.run("auth:app", host="0.0.0.0", port=8000, reload=True)
