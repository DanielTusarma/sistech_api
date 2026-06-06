from fastapi import FastAPI
from routers.dependencia_router import router as dependencias_router
from routers.empleado_router import router as empleados_router
from routers.cargo_router import router as cargos_router
from routers.usuario_router import router as usuario_router
from auth.auth_router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de gestión de empleados en Sistech",
    description="Backend REST para la gestion de empleados y dependencias en Sistech",
    version="1.0.0"
)


# CORS configuration
origins = [
    "http://localhost:4200", # Angular
    "http://localhost:5173", # react - vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endpoint raiz de la app
@app.get("/")
def raiz():
    return {"mensaje": "API Sistech de gestión de empleados funcionando correctamente"}

app.include_router(dependencias_router)
app.include_router(empleados_router)
app.include_router(cargos_router)
app.include_router(usuario_router)
app.include_router(auth_router)