from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from . import models

# clave secreta hardcodeada
SECRET_KEY = "la_clave"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# hasheo de pass
pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

# OAuth
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="tokenzote")

# aca hay que meter los user y los pass, que podrian ser tranquilamente las cuentas de google asociadas
fake_users_db = {
    "tuevieja@entanga.com": {
        "username": "tuvieja",
        "name": "user1",
        "hashed_password": pwd_context.hash("pass1"),
        "disabled": False
    }
}

def verificar_pass(plain_pass, hashed_pass):
    return pwd_context.verify(plain_pass, hashed_pass)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return models.UserInDB(**user_dict)
