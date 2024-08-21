from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol
from routes.puestos_departamentos import puesto_departamento
from routes.puestos import puesto
from routes.areas_medicas import area_medica
from fastapi.middleware.cors import CORSMiddleware

# Crear la instancia de FastAPI
app = FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API para el almacenamiento de información de un hospital"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],  # URL de tu frontend Vue.js
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir las rutas de las tablas
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(puesto)
app.include_router(puesto_departamento)
app.include_router(area_medica)

print("Hola bienvenido a mi backend")
