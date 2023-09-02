from typing import Annotated

import uvicorn
import httpx
from decouple import config
from fastapi import FastAPI, Header, HTTPException, status

auth_app_url = config('auth_app_url')

app = FastAPI(
    debug=True
)


@app.get('/', status_code=status.HTTP_200_OK)
def who_are_you():
    return {'message': 'This is \"Blog\" app'}


@app.get('/posts', status_code=status.HTTP_200_OK)
def get_posts(username: Annotated[str, Header()] = None, password: Annotated[str, Header()] = None):
    res = httpx.post(auth_app_url + '/login', json={'username': username, 'password': password})
    if res.is_success:
        return [
            'LOREM IPSUM GENERATOR Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'LOREM IPSUM GENERATOR Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'LOREM IPSUM GENERATOR Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'LOREM IPSUM GENERATOR Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        ]
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=res.json().get('detail')
    )


if __name__ == "__main__":
    uvicorn.run("blog:app", host="0.0.0.0", port=8000, reload=True)
