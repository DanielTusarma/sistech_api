# API Gestión de empleados Sistech

Proyecto backend desarrollado con FastAPI para gestionar los empleados y dependencias de la empresa Sistech.

La aplicación permite:

* Crear dependencias.
* Listar todas las dependencias.
* Crear empleados.
* Listar todos los empleados.
* Obtener un empleado.
* Editar un empleado.
* Desactivar un empleado usando soft delete.
* Listar todos los empleados activos.
* Listar todos los empleados inactivos.
* Listar los empleados por dependencia.

---

# Tecnologías utilizadas

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* Pydantic
* Uvicorn

---

# Arquitectura del proyecto

El proyecto está organizado siguiendo una estructura por capas y patrón Repository:

```plaintext
routes/         # Rutas y endpoints
models/         # Modelos SQLAlchemy
repositories/   # Repositorios para interactuar con la base de datos
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

## Empleados

* Crear empleado.
* Listar empleados.
* Obtener un empleado
* Editar un empleado.
* Desactivar un empleado.
* Obtener empleados activos.
* Obtener empleados inactivos.
* Obtener empleados por dependencia.


---

# Regla de negocio

Los empleados no pueden ser eliminados totalmente de la base de datos. En este caso 
solo se pueden desactivar agregando la fecha de salida de dicho empleado

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

# Documentación automática

FastAPI genera documentación automática en:

```plaintext
http://127.0.0.1:8000/docs
```

---

# Estado del proyecto

En desarrollo.

Próximas mejoras:


* Autenticación.
* Testing automatizado.
* Dockerización.
