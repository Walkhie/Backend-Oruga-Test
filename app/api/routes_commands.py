from fastapi import APIRouter, HTTPException
from app.api.models import CreateEntity
from app.core.orion_client import update_entity_state, create_entity, get_entities, delete_entity

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
    
@router.get("/entities/get")
def get_entities():
    try:
        entities = get_entities()
        if not entities:
            return {"message": "No hay entidades registradas."}
        return {"count": len(entities), "entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/entities/delete/{entity_id}")
def delete_entity_route(entity_id: str):
    # Elimina una entidad de Orion por su ID.
    try:
        result = delete_entity(entity_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))