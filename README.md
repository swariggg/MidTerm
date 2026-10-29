# Acortador de enlaces (S3 + DynamoDB + EC2)

Aplicación web que acorta URLs. El backend (FastAPI) genera un UUID, lo guarda en
DynamoDB y redirige al usuario a la URL original. La interfaz (HTML, CSS y JS) se
publica en S3.

## Estructura

```
acortador-enlaces/
├── backend/
│   ├── app/
│   │   ├── main.py        # Endpoints de la API
│   │   ├── database.py    # Acceso a DynamoDB (boto3)
│   │   ├── schemas.py     # Modelos de datos
│   │   └── config.py      # Variables de entorno
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── config.js          # URL de la API (IP de EC2)
└── deploy/
    └── acortador.service  # Servicio systemd para EC2
```

## Endpoints

| Método | Ruta                 | Descripción                                  |
|--------|----------------------|----------------------------------------------|
| POST   | `/shorten`           | Crea un enlace corto                         |
| GET    | `/{short_code}`      | Redirige (307) a la URL original, o 404      |
| GET    | `/urls/{short_code}` | Devuelve la información del enlace en JSON   |

## Tabla DynamoDB

- Nombre: `short_links`
- Clave de partición: `short_code` (String)
- Atributos: `original_url`, `created_at`

## Ejecutar en local

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows  (en Linux: source venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env       # y edita los valores
uvicorn app.main:app --reload
```

Documentación interactiva: http://localhost:8000/docs

> En local necesitas credenciales de AWS configuradas (`aws configure`). En EC2 se
> usa el rol IAM; nunca subas claves al repositorio.
