from datetime import timedelta, datetime
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi import Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from jose import jwt
from pydantic import BaseModel
from starlette import status

from server.forms import LoginForm


class Token(BaseModel):
    access_token: str
    token_type: str


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

DB = {
    'users': {
        'siri': {
            'name': 'siri',
            'password': 'siri'
        },
        'elexa': {
            'name': 'elexa',
            'password': 'elexa'
        }
    }
}

SECRET = "a2546d38de467bd3236278691b993cfbb52d7b8d433d0fa6"
ALGORITHM = "HS256"


@router.get("/login/")
def login(request: Request):
    return templates.TemplateResponse("server/login.html", {"request": request})


@router.post("/login/")
async def login(request: Request):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful :)")
            response = templates.TemplateResponse("auth/login.html", form.__dict__)
            login_for_access_token(response=response, form_data=form, db=DB)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("auth/login.html", form.__dict__)
    return templates.TemplateResponse("auth/login.html", form.__dict__)


@router.post("/token", response_model=Token)
def login_for_access_token(
        response: Response,
        form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=1000)
    access_token = create_access_token(
        data={"sub": user['name']}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True
    )
    return {"access_token": access_token, "token_type": "bearer"}


def authenticate_user(username: str, password: str):
    user = DB['users'].get(username)
    print(user)
    if not user:
        return False
    if not password == user['password']:
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=1000
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET, algorithm=ALGORITHM
    )
    return encoded_jwt
