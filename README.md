# Desarrollo de APIs con Python — Clase 3

Este repositorio contiene el estado final del proyecto correspondiente a la **Clase 3** de la asignatura **Desarrollo de APIs con Python**.

Su propósito es servir como punto de partida para que los estudiantes puedan reproducir en casa la práctica de la **Clase 4** y comparar posteriormente su resultado con el estado final esperado.

---

## Objetivos alcanzados en la Clase 3

En este proyecto se trabajaron los siguientes conceptos:

- creación de una API con FastAPI;
- documentación automática con OpenAPI y Swagger UI;
- modelos Pydantic para entrada y salida de datos;
- validación de campos con `Field`;
- rechazo de campos adicionales con `extra="forbid"`;
- uso de type hints;
- path parameters;
- query parameters;
- organización inicial mediante `APIRouter`;
- separación entre routers y schemas;
- dependencias básicas con `Depends`;
- manejo inicial de errores mediante `HTTPException`;
- respuestas HTTP `201`, `404` y `422`.

---

## Estructura del proyecto

```text
.
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── projects.py
│   └── schemas/
│       ├── __init__.py
│       └── projects.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Requisitos

Para ejecutar este proyecto se necesita:

- Git
- Docker Desktop o Docker Engine con Docker Compose

No es necesario instalar Python ni las dependencias del proyecto directamente en el sistema operativo.

Docker se encargará de construir el entorno de ejecución.

---

## Clonar el repositorio

Ejecute:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Luego entre en la carpeta:

```bash
cd desarrollo-apis-python-clase-03
```

---

## Construir y ejecutar la aplicación

La primera vez que ejecute el proyecto, Docker deberá construir la imagen e instalar las dependencias definidas en `requirements.txt`.

Ejecute:

```bash
docker compose up --build
```

Cuando la aplicación haya iniciado correctamente, debería aparecer un mensaje similar a:

```text
Uvicorn running on http://0.0.0.0:8000
```

---

## Abrir la documentación de la API

Desde el navegador abra:

```text
http://localhost:8000/docs
```

FastAPI mostrará automáticamente la documentación interactiva de la API mediante Swagger UI.

---

## Endpoints disponibles

### Health check

```text
GET /health
```

Respuesta esperada:

```json
{
  "status": "ok"
}
```

---

### Crear un proyecto

```text
POST /projects
```

Ejemplo de request válido:

```json
{
  "name": "API Course",
  "description": "Project created during the course"
}
```

Respuesta esperada:

```text
201 Created
```

Ejemplo de respuesta:

```json
{
  "id": 1,
  "name": "API Course",
  "description": "Project created during the course",
  "status": "active"
}
```

---

## Validación de nombres

El nombre del proyecto debe tener al menos 3 caracteres.

Ejemplo inválido:

```json
{
  "name": "AI"
}
```

Resultado esperado:

```text
422 Unprocessable Entity
```

---

## Campos adicionales

El modelo de entrada no permite campos no definidos en el contrato.

Ejemplo inválido:

```json
{
  "name": "API Course",
  "description": "Example",
  "owner": "Student"
}
```

Resultado esperado:

```text
422 Unprocessable Entity
```

---

## Listar proyectos

```text
GET /projects
```

Devuelve la lista disponible de proyectos.

---

## Filtrar proyectos por estado

Ejemplo:

```text
GET /projects?status=active
```

El parámetro `status` es un query parameter opcional.

---

## Consultar un proyecto

```text
GET /projects/{project_id}
```

Ejemplo:

```text
GET /projects/1
```

Resultado esperado:

```text
200 OK
```

---

## Proyecto inexistente

Ejemplo:

```text
GET /projects/99
```

Resultado esperado:

```text
404 Not Found
```

Respuesta:

```json
{
  "detail": "Project not found"
}
```

---

## Identificador inválido

Ejemplo:

```text
GET /projects/abc
```

Como `project_id` está definido como un entero, FastAPI realiza la validación automáticamente.

Resultado esperado:

```text
422 Unprocessable Entity
```

---

## Resumen de pruebas manuales

Puede utilizar `/docs` para comprobar los siguientes casos:

```text
POST /projects
    request válido
    → 201

POST /projects
    nombre menor de 3 caracteres
    → 422

POST /projects
    campo adicional
    → 422

GET /projects
    → 200

GET /projects?status=active
    → 200

GET /projects/1
    → 200

GET /projects/99
    → 404

GET /projects/abc
    → 422
```

---

## Detener la aplicación

Si ejecutó Docker Compose en primer plano, puede detenerlo con:

```text
Ctrl+C
```

Luego ejecute:

```bash
docker compose down
```

---

## Reconstruir la imagen

Si se modifica `Dockerfile` o `requirements.txt`, puede volver a construir la imagen con:

```bash
docker compose up --build
```

Para cambios normales en archivos Python no debería ser necesario reconstruir la imagen, ya que el proyecto está montado dentro del contenedor y Uvicorn se ejecuta con recarga automática.

---

## Propósito de este repositorio

Este repositorio representa el **estado final de la Clase 3**.

No contiene todavía la estructura que será introducida en la Clase 4.

Durante la siguiente clase el proyecto evolucionará para incorporar, entre otros temas:

- separación inicial de responsabilidades;
- capa de servicios;
- configuración de la aplicación;
- introducción al desarrollo guiado por especificaciones;
- requerimientos funcionales y no funcionales;
- criterios de aceptación;
- especificaciones mediante `spec.md`;
- planificación mediante `plan.md`;
- tareas mediante `tasks.md`.

La intención es que el estudiante parta de este repositorio y reproduzca paso a paso esa evolución.

---

## Metodología de trabajo

El objetivo no es únicamente obtener una API funcionando.

Durante el curso se busca desarrollar una forma de trabajo en la que los cambios sean:

```text
comprensibles
→ pequeños
→ verificables
→ reproducibles
```

A medida que avance la asignatura se incorporarán progresivamente prácticas de especificación, pruebas automatizadas, persistencia, arquitectura y desarrollo asistido por inteligencia artificial.

---

## Autor

**Prof. José Gregorio Castillo Pacheco**

Asignatura: **Desarrollo de APIs con Python**