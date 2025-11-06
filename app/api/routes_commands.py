from fastapi import APIRouter, HTTPException
from app.api.models import CreateEntity
from app.core.orion_client import update_entity_state, create_entity, get_entities, delete_entity, get_entity_status

router = APIRouter()

@router.post("/entities/create")
def create_entity_route(body: CreateEntity):
    try:
        code = create_entity(body.entity_id,body.entity_type,body.state,body.speed)
        return {"message": "Entidad creada (o ya existia)", "status_code": code}
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))
    
@router.post("/entities/upsert")
def upsert_entity_route(body: CreateEntity):
    try:
        code = update_entity_state(body.entity_id,body.entity_type,body.state,body.speed)
        return {"message":"Entidad actualizada","status_code":code}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@router.get("/entities/get")
def get_entities_route():
    try:
        entities = get_entities()

        if not entities:
            return {"message": "No hay entidades registradas."}
        
        return {"count": len(entities), "entities": entities}
    
    except Exception as e:
        print("Error en /entities/get:", e)
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/entities/get/state/{entity_id}")
def get_entity_status_route(entity_id:str):
    try:
        entity_data = get_entity_status(entity_id)
        if entity_data is None:
            return {"message": f"La entidad '{entity_id}' no existe."}
        return {"entity_data": entity_data}
    except Exception as e:
        print("Error en /entities/state:", e)
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.delete("/entities/delete/{entity_id}")
def delete_entity_route(entity_id: str):
    # Elimina una entidad de Orion por su ID.
    try:
        result = delete_entity(entity_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    