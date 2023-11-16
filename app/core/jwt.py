from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from starlette.status import HTTP_404_NOT_FOUND

import jwt
from app.crud.user import get_user
from app.db.mongodb import AsyncIOMotorClient, get_database
from app.models.token import TokenData
from app.models.user import User
from app.core.config import SECRET_KEY

ALGORITHM = "HS256"
access_token_jwt_subject = "access"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(db: AsyncIOMotorClient = Depends(get_database), access_token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(access_token, str(SECRET_KEY), algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    dbuser = await get_user(db, token_data.username)
    if not dbuser:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    user = User(**dbuser.dict(), access_token=access_token)
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user


def create_access_token(*, data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": access_token_jwt_subject})
    encoded_jwt = jwt.encode(to_encode, str(SECRET_KEY), algorithm=ALGORITHM)
    return encoded_jwt
