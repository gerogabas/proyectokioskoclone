from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from . import models
from . import login


app = FastAPI()

# Configurar el middleware CORSMiddleware
# Permitir solicitudes desde todos los orígenes
origins = [
    "http://localhost",
    "http://localhost:3000",  # Cambia esto por la URL de tu frontend
    "https://example.com",
    "https://example.com:3000",
    "http://localhost:5173/logIn",
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Puedes ajustar esto a los orígenes permitidos específicos si lo deseas
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Aquí puedes especificar los métodos permitidos
    allow_headers=["*","Content-Type"]
)

@app.get("/")
async def nada():
    return "hola"

@app.post("/login/")
async def login(l: models.LoginRequest):
    # Validar el correo electrónico y la contraseña (hardcodeado)
    if l.email == "g@g" and l.password == "123":
        return {"message": "Login exitoso"}
    else:
        # Si la validación falla, devuelve un error HTTP 401 no autorizado
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

# ---------------------------------MATERIAS---------------------------------------------
# ---------------------------------MATERIAS---------------------------------------------

# Lista de ejemplo de materias
materias = [
    models.Materia(id=1, nombre="Matematicas", carrera="Ingenieria"),
    models.Materia(id=2, nombre="Fisica", carrera="Ingenieria"),
    models.Materia(id=3, nombre="Quimica", carrera="Ingenieria"),
    models.Materia(id=4, nombre="Matematicas", carrera="TUP"),
]

# Rutas para operaciones CRUD
@app.get("/materias")
async def obtener_materias():
    return materias

@app.post("/materias")
async def crear_materia(materia: models.Materia):
    materias.append(materia)
    return {"message": "Materia creada exitosamente"}

@app.put("/materias/{nombre}")
async def actualizar_materia(nombre: str, nueva_materia: models.Materia):
    for materia in materias:
        if materia.nombre == nombre:
            materia.nombre = nueva_materia.nombre
            materia.carrera = nueva_materia.carrera
            return {"message": f"Materia {nombre} actualizada"}
    raise HTTPException(status_code=404, detail="Materia no encontrada")

@app.delete("/materias/{nombre}")
async def borrar_materia(nombre: str):
    for i, materia in enumerate(materias):
        if materia.nombre == nombre:
            del materias[i]
            return {"message": f"Materia {nombre} eliminada"}
    raise HTTPException(status_code=404, detail="Materia no encontrada")



# ---------------------------------- Seccion Estudiantes ------------------------------------
# Base de datos simulada
estudiantes_db = [
    {
        "nombre": "Juan Pedro Jacinto Roberto jr.",
        "apellido": "Pérez Rosales",
        "legajo": "12345",
        "edad": 21,
        "carrera": "Ingeniería",
        "email": "juan.perez@example.com",
        "telefono": "123-456-7890",
        "direccion": "Calle Falsa 123",
        "materias": [
            {"nombre": "Matemáticas", "nota": 8.5},
            {"nombre": "Física", "nota": 7.0},
            {"nombre": "Química", "nota": 9.0}
        ]
    },
    {
        "nombre": "María",
        "apellido": "Gómez",
        "legajo": "67890",
        "edad": 22,
        "carrera": "Medicina",
        "email": "maria.gomez@example.com",
        "telefono": "987-654-3210",
        "direccion": "Avenida Siempreviva 742",
        "materias": [
            {"nombre": "Biología", "nota": 9.5},
            {"nombre": "Anatomía", "nota": 8.0},
            {"nombre": "Fisiología", "nota": 7.5}
        ]
    },
    {
        "nombre": "Carlos",
        "apellido": "López",
        "legajo": "54321",
        "edad": 23,
        "carrera": "Derecho",
        "email": "carlos.lopez@example.com",
        "telefono": "456-789-0123",
        "direccion": "Calle Principal 456",
        "materias": [
            {"nombre": "Derecho Constitucional", "nota": 8.0},
            {"nombre": "Derecho Penal", "nota": 7.5},
            {"nombre": "Derecho Civil", "nota": 9.0}
        ]
    },
    {
        "nombre": "Ana",
        "apellido": "Martínez",
        "legajo": "98765",
        "edad": 20,
        "carrera": "Arquitectura",
        "email": "ana.martinez@example.com",
        "telefono": "321-654-0987",
        "direccion": "Boulevard de los Sueños 789",
        "materias": [
            {"nombre": "Dibujo Arquitectónico", "nota": 9.0},
            {"nombre": "Historia de la Arquitectura", "nota": 8.5},
            {"nombre": "Diseño Urbano", "nota": 9.5}
        ]
    },
    {
        "nombre": "Luis",
        "apellido": "Fernández",
        "legajo": "11223",
        "edad": 24,
        "carrera": "Informática",
        "email": "luis.fernandez@example.com",
        "telefono": "234-567-8910",
        "direccion": "Calle de la Tecnología 101",
        "materias": [
            {"nombre": "Programación", "nota": 9.0},
            {"nombre": "Redes", "nota": 8.5},
            {"nombre": "Bases de Datos", "nota": 9.5}
        ]
    },
    {
        "nombre": "Laura",
        "apellido": "García",
        "legajo": "44556",
        "edad": 21,
        "carrera": "Psicología",
        "email": "laura.garcia@example.com",
        "telefono": "123-123-1234",
        "direccion": "Calle de la Paz 567",
        "materias": [
            {"nombre": "Psicología General", "nota": 8.0},
            {"nombre": "Psicología Clínica", "nota": 9.0},
            {"nombre": "Neuropsicología", "nota": 8.5}
        ]
    },
    {
        "nombre": "Jorge",
        "apellido": "Rodríguez",
        "legajo": "77889",
        "edad": 22,
        "carrera": "Economía",
        "email": "jorge.rodriguez@example.com",
        "telefono": "567-890-1234",
        "direccion": "Avenida de la Libertad 890",
        "materias": [
            {"nombre": "Microeconomía", "nota": 8.5},
            {"nombre": "Macroeconomía", "nota": 7.5},
            {"nombre": "Econometría", "nota": 9.0}
        ]
    },
    {
        "nombre": "Sofía",
        "apellido": "Hernández",
        "legajo": "33445",
        "edad": 23,
        "carrera": "Biología",
        "email": "sofia.hernandez@example.com",
        "telefono": "678-901-2345",
        "direccion": "Calle de la Naturaleza 234",
        "materias": [
            {"nombre": "Biología Molecular", "nota": 9.0},
            {"nombre": "Genética", "nota": 8.5},
            {"nombre": "Ecología", "nota": 9.5}
        ]
    },
    {
        "nombre": "Andrés",
        "apellido": "Ramírez",
        "legajo": "55667",
        "edad": 24,
        "carrera": "Química",
        "email": "andres.ramirez@example.com",
        "telefono": "789-012-3456",
        "direccion": "Calle de la Ciencia 345",
        "materias": [
            {"nombre": "Química Orgánica", "nota": 8.5},
            {"nombre": "Química Inorgánica", "nota": 9.0},
            {"nombre": "Bioquímica", "nota": 8.0}
        ]
    },
    {
        "nombre": "Lucía",
        "apellido": "Morales",
        "legajo": "88990",
        "edad": 21,
        "carrera": "Historia",
        "email": "lucia.morales@example.com",
        "telefono": "890-123-4567",
        "direccion": "Calle de la Historia 456",
        "materias": [
            {"nombre": "Historia Antigua", "nota": 8.0},
            {"nombre": "Historia Medieval", "nota": 9.0},
            {"nombre": "Historia Moderna", "nota": 8.5}
        ]
    }
]

@app.get("/estudiantes/")
async def get_estudiantes():
    return estudiantes_db

@app.get("/estudiantes/{legajo}", response_model=models.Estudiante)
async def get_estudiante(legajo: str):
    estudiante = next((est for est in estudiantes_db if est["legajo"] == legajo), None)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

@app.post("/estudiantes/", response_model=models.Estudiante)
async def create_estudiante(estudiante: models.Estudiante):
    estudiantes_db.append(estudiante.model_dump())
    return estudiante

@app.put("/estudiantes/{legajo}", response_model=models.Estudiante)
async def update_estudiante(legajo: str, estudiante: models.Estudiante):
    index = next((i for i, est in enumerate(estudiantes_db) if est["legajo"] == legajo), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    estudiantes_db[index] = estudiante.model_dump()
    return estudiante

@app.delete("/estudiantes/{legajo}", response_model=models.Estudiante)
async def delete_estudiante(legajo: str):
    index = next((i for i, est in enumerate(estudiantes_db) if est["legajo"] == legajo), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    estudiante = estudiantes_db.pop(index)
    return estudiante