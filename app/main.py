from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_commands import router as cmd_router
from app.core.config import settings
import requests

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Record routes 
app.include_router(cmd_router, prefix=settings.API_PREFIX,tags=["orion"])

@app.get("/health")
def health():
    try:
        r= requests.get(f"{settings.ORION_HOST}/version", timeout=3)
        # Si la solicitud a Orion es exitosa
        if r.status_code == 200:
            return {"status":"ok","orion":"reachable","app": settings.APP_NAME}

        else:
            return{"status":"warning","orion":"unreachable","app": settings.APP_NAME}
        
    except Exception:
        return {"status": "error","orion": "not responding", "app": settings.APP_NAME}


