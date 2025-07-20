# Sistema de Gestión de Historiales Clínicos

## Descripción

Aplicación web desarrollada con **FastAPI** (backend) y **React** (frontend) para la gestión segura de historiales clínicos de pacientes. Utiliza **SQLAlchemy** como ORM y **MySQL** como base de datos. Permite a los doctores consultar, crear, actualizar y eliminar historiales clínicos, así como gestionar consultorios y pacientes, con autenticación segura y control de acceso.

---

## Estructura del Proyecto

```
/app
    /models         # Modelos SQLAlchemy (tablas de la BD)
        models.py
    /schemas        # Esquemas Pydantic (validación y serialización)
        schemas.py
    /crud           # Lógica de acceso a datos (CRUD)
        crud.py
    /api            # Rutas y controladores FastAPI
        api.py
    /core           # Configuración y utilidades
        config.py
    /db             # Sesión y conexión a la base de datos
        session.py
        init_db.py
    /security       # Utilidades de seguridad (hash, JWT)
        auth.py
    main.py         # Punto de entrada FastAPI
requirements.txt    # Dependencias del proyecto
.env                # Variables de entorno (no subir a git)
.gitignore          # Exclusiones para git
README.md           # Este archivo
```

---

## Instalación y Configuración

### 1. Clona el repositorio

```bash
git clone <URL-del-repositorio>
cd <nombre-del-proyecto>
```

### 2. Crea y activa un entorno virtual

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```
**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno

Crea un archivo `.env` en la raíz del proyecto con tus credenciales de MySQL:

```
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_contraseña
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=nombre_base_datos
```

> **Nota:** No subas `.env` a git, ya está en `.gitignore`.

### 5. Configura la base de datos

Crea la base de datos en MySQL si no existe:

```sql
CREATE DATABASE nombre_base_datos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. Inicializa las tablas

Ejecuta el script de inicialización desde la raíz del proyecto:

```bash
python -m app.db.init_db
```

Esto creará todas las tablas según los modelos definidos en `app/models/models.py`.

### 7. Ejecuta el servidor de desarrollo

```bash
uvicorn app.main:app --reload
```

Accede a la documentación interactiva en [http://localhost:8000/docs](http://localhost:8000/docs).

---

## Lógica y Buenas Prácticas

- **Modelos:** Todas las tablas están definidas en `app/models/models.py` usando SQLAlchemy.
- **Esquemas:** Los esquemas Pydantic para validación y serialización están en `app/schemas/schemas.py`.
- **CRUD:** Toda la lógica de acceso a datos está centralizada en `app/crud/crud.py`, usando los modelos y esquemas correctos.
- **Rutas:** Los endpoints de la API están en `app/api/api.py`, importando funciones CRUD y esquemas desde sus módulos correspondientes.
- **Seguridad:** Contraseñas encriptadas con bcrypt, autenticación JWT, y configuración de CORS segura.
- **Configuración:** Todas las variables sensibles y de conexión están en `.env` y se cargan automáticamente con `pydantic-settings`.
- **Colaboración:** Estructura modular y limpia, siguiendo las mejores prácticas para proyectos colaborativos y escalables.

---

## Ejemplo de Flujo de Trabajo

1. **Registro de doctor:**  
   POST `/register` con los datos del doctor.

2. **Login de doctor:**  
   POST `/login` con correo y contraseña para obtener un JWT.

3. **CRUD de pacientes e historiales clínicos:**  
   Usa los endpoints `/patients/` y `/medical_history/` para crear, consultar, actualizar y eliminar registros.

---

## Contribución

- Crea una rama para tu funcionalidad.
- Haz tus cambios y pruebas.
- Haz un pull request describiendo claramente tus cambios.
- Sigue las convenciones de código y comentarios para facilitar la colaboración.

---

## Notas

- No compartas tu archivo `.env` ni credenciales sensibles.
- Si agregas nuevas dependencias, actualiza `requirements.txt`.
- Si modificas la estructura de la base de datos, actualiza los modelos y ejecuta las migraciones o el script de inicialización.

---

¿Dudas o sugerencias? ¡Colabora y mejora el proyecto!