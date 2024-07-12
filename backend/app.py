from fastapi import FastAPI
<<<<<<< HEAD
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.userrol import userrol

app=FastAPI(
    title="Gimnasio S.A. de C.V.",
    description="API para el almacenamiento de informacipn de un gimnasio"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
print ("Hola bienvenido a mi backend")
=======
from routes.users import user
from routes.persons import person

app = FastAPI()

app.include_router(user)
app.include_router(person)

print("Bienvenido a mi aplicacion")
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822
