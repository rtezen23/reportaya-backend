# ReportaYa Backend

API REST para el registro y seguimiento de incidencias en conjuntos residenciales.

## Requisitos

- Python 3.11 o superior

## Ejecución local

Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

La aplicación usa SQLite de forma predeterminada y crea el archivo
`reportaya.db` al iniciar. Para conectarla a MySQL, copiar `.env.example` como
`.env` y cambiar la variable:

```env
DATABASE_URL=mysql+pymysql://usuario:contrasena@localhost:3306/reportaya
```

Iniciar el servidor:

```powershell
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000` y su documentación en
`http://127.0.0.1:8000/docs`.
