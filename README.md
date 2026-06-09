# API REST de Gestión empresarial - Sistech

Backend desarrollado con Python y FastAPI para la administración de empleados, usuarios, dependencias, cargos y permisos dentro de la empresa Sistech.

La aplicación implementa autenticación JWT, autorización basada en roles (RBAC), persistencia con PostgreSQL y una arquitectura modular orientada a la escalabilidad y mantenibilidad del software.

La aplicación permite:

* Gestión de empleados, usuarios, cargos y dependencias.
* Autenticación y autorización mediante JWT y RBAC.
* Soft delete de empleados con registro de fecha de salida.
* Filtrado y consulta de empleados por cargo, dependencia y estado.
* Documentación automática con Swagger UI.
* Migraciones de base de datos con Alembic.


---

# Tecnologías utilizadas

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* Pydantic
* Uvicorn
* JWT + RBAC
* Docker

---

# Arquitectura del proyecto

El proyecto está organizado siguiendo una estructura por capas y patrón Repository:


```plaintext
Carpeta         Responsabilidad
routes/         # Rutas y endpoints
models/         # Modelos SQLAlchemy
repositories/   # Acceso y persistencia de datos
schemas/        # Validaciones y serialización con Pydantic
services/       # Lógica de negocio
database.py     # Configuración de base de datos
main.py         # Punto de entrada de FastAPI
```

---

# Funcionalidades implementadas

## Dependencias

* Crear dependencia.
* Listar dependencias.
* Obtener una dependencia.

## Cargos

* Crear cargo.
* Listar cargos.

## Usuarios

* Crear usuario.
* Obtener un usuario por su Id o email.

## Empleados

* Crear, listar, obtener y editar empleado.
* Desactivar un empleado mediante soft delete.
* Consultar empleados activos e inactivos.
* Obtener empleados por dependencia o cargo.

---

# Regla de negocio

Los empleados no se eliminan físicamente de la base de datos. En su lugar, se aplica un soft delete, desactivando el registro y almacenando la fecha de salida.

Si se desactiva un empleado por ejemplo:

```json
{
  "activo": false,
  "fecha_salida": date,
}
```

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/DanielTusarma/sistech_api.git
cd sistech_api
```

---

## 2. Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Configurar variables de entorno

Crear un archivo `.env`

```env
DATABASE_URL=postgresql+psycopg2://usuario:password@localhost:5432/sistecn_db
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 5. Ejecutar migraciones

```bash
alembic upgrade head
```

---

## 6. Ejecutar servidor

```bash
uvicorn main:app --reload
```

---

# 7 Documentación automática

FastAPI genera documentación automática en:

```plaintext
http://127.0.0.1:8000/docs
```

---

# Capturas de pantalla

## Documentación Swagger
![Swagger](docs/images/Swagger.png)

## Consulta de empleados
![Empleados](docs/images/empleados1.png)
![Empleados](docs/images/empleados2.png)

# Estado del proyecto

En desarrollo activo.

Próximas mejoras:

* Testing automatizado con Pytest.
* Docker Compose para entorno completo.
