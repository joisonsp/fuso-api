from fastapi import FastAPI
from datetime import datetime, timezone
import pytz

app = FastAPI()


@app.get("/horario")
async def horario(fuso_horario: str):
    try:
        tz = pytz.timezone(fuso_horario)
    except pytz.exceptions.UnknownTimeZoneError:
        return {"error": "Fuso horário inválido."}

    agora = datetime.now(timezone.utc).astimezone(tz)
    return {"horario": agora.strftime("%Y-%m-%d %H:%M:%S %Z%z")}
