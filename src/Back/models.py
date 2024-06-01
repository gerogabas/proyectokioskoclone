from pydantic import BaseModel
from typing import List

class LoginRequest(BaseModel):
    email: str
    password: str


class Materia(BaseModel):
    id: int
    nombre: str
    carrera: str

class Estudiante(BaseModel):
    nombre: str
    apellido: str
    legajo: str
    edad: int
    carrera: str
    email: str
    telefono: str
    direccion: str
    materias: List[Materia]

#CLASES USADAS POR LOGIN
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

