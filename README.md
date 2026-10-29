Acortador de enlaces 
Aplicación web que acorta URLs. El backend (FastAPI) genera un UUID, lo guarda en
DynamoDB y redirige al usuario a la URL original. La interfaz (HTML, CSS y JS) se
publica en S3.

Estructura
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
´´´
DynamoDB
- Nombre: `short_links`
- Clave de partición: `short_code` (String)
- Atributos: `original_url`, `created_at`

ejecución local

cd backend
python -m venv venv
venv\Scripts\activate        # Windows  (en Linux: source venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env       # y edita los valores
fastapi dev

