# Sistema de Gestión de Historiales Clínicos

## Descripción

Este proyecto es una aplicación web desarrollada con **FastAPI** (backend) y **React** (frontend) para gestionar de manera segura los historiales clínicos de pacientes. Utiliza **SQLAlchemy** como ORM y **MySQL** como base de datos. El sistema está diseñado para que los doctores puedan consultar, crear, actualizar y eliminar historiales clínicos, así como gestionar consultorios y pacientes.

## Características principales

- **Gestión de usuarios y doctores**: Registro seguro, inicio de sesión y control de acceso.
- **Historiales clínicos**: CRUD completo, con soporte para múltiples historiales por paciente y odontograma para dentistas.
- **Consultorios**: Un doctor puede gestionar varios consultorios.
- **Seguridad**: Uso de JWT para autenticación, contraseñas encriptadas y validación de datos.
- **Colaborativo**: Estructura modular y limpia para facilitar el trabajo en equipo.

## Estructura del proyecto

```
/app
    /models         # Modelos SQLAlchemy (tablas)
    /schemas        # Esquemas Pydantic (validación y serialización)
    /crud           # Lógica de acceso a datos (CRUD)
    /api            # Rutas y controladores FastAPI
    /core           # Configuración y utilidades
    /db             # Sesión y conexión a la base de datos
    /security       # Utilidades de seguridad (hash, JWT)
    main.py         # Punto de entrada FastAPI
requirements.txt    # Dependencias del proyecto
README.md           # Este archivo
```

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd <nombre-del-proyecto>
```

### 2. Crear y activar un entorno virtual

En Windows:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

En Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Edita `app/core/config.py` y coloca tu cadena de conexión MySQL:

```python
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://usuario:contraseña@localhost:3306/tu_basededatos"
```

Crea la base de datos en MySQL si no existe:

```sql
CREATE DATABASE tu_basededatos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. Inicializar las tablas

Puedes usar Alembic o crear las tablas automáticamente desde los modelos:

```python
# En main.py o un script aparte
from app.models import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)
```

### 6. Ejecutar el servidor de desarrollo

```bash
uvicorn app.main:app --reload
```

## Lógica y buenas prácticas

- **Modelos**: Cada tabla de la base de datos tiene su modelo SQLAlchemy.
- **Esquemas**: Los esquemas Pydantic validan y serializan los datos de entrada/salida.
- **CRUD**: La lógica de acceso a datos está separada para facilitar pruebas y mantenimiento.
- **Seguridad**: Las contraseñas se almacenan encriptadas y se usa JWT para autenticación.
- **Colaboración**: El código está modularizado para que varios desarrolladores puedan trabajar en paralelo.

## Contribución

1. Crea una rama para tu funcionalidad.
2. Haz tus cambios y pruebas.
3. Haz un pull request describiendo claramente tus cambios.

## Notas

- No compartas tu archivo `.env` ni credenciales sensibles.
- Sigue las convenciones de código y comentarios para facilitar la colaboración.

---

¿Listo para continuar con la implementación de los modelos y la lógica de negocio?