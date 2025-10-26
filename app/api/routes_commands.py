from fastapi import APIRouter, HTTPException
from app.api.models import CreateEntity
from app.core.orion_client import update_entity_state, create_entity

router = APIRouter()

@router.post("/entities/create")
def create_entity_route(body: CreateEntity):
    try:
        code = create_entity(body.entity_id,body.entity_type,body.state)
        return {"message": "Entidad creada (o ya existia)", "status_code": code}
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))
    
@router.post("/entities/upsert")
def upsert_entity_route(body: CreateEntity):
    try:
        code = update_entity_state(body.entity_id,body.entity_type,body.state)
        return {"message":"Entidad actualizada","status_code":code}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))