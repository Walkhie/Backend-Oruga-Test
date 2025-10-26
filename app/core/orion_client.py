import requests
from app.core.config import settings

HEADERS = {
    "Content-Type": "application/json",
    "Fiware-Service": settings.FIWARE_SERVICE,
    "Fiware-ServicePath": settings.FIWARE_SERVICEPATH
}

def ensure_entity_exist(entity_id:str) -> bool:
    "Verificar si existe la entidad en orion"
    url = f"{settings.ORION_HOST}/v2/entities/{entity_id}"
    # resultado de request
    r = requests.get(url, headers=HEADERS, timeout=5)
    return r.status_code == 200

def create_entity(entity_id: str, entity_type: str = "RobotOruga", state: str = "IDLE") -> bool:
    "Crea una nueva entidad oruga en Orion"
    url = f"{settings.ORION_HOST}/v2/entities"
    payload = {
        "id": entity_id,
        "type": entity_type,
        "state": {"type":"Text","value":state},
        #"speed":{"type":"Integer","value":0}
    }

    r = requests.post(url, json=payload, headers=HEADERS, timeout=5)
    # status_code 201 = creado, 422 = ya existe

def update_entity_state(entity_id:str,entity_type: str = "RobotOruga", state:str = "IDLE"):
    # Actualiza el estado de la entidad. Crea la entidad si no existe

    # 1. Verificar existencia
    if not ensure_entity_exist(entity_id):
        print(f"Entidad {entity_id} no existe, creando...")
        created = create_entity(entity_id)

        if not created:
            raise Exception(f"No se pudo crear la entidad {entity_id}")
        
    
    #2. Actualizar el atributo state 
    url = f"{settings.ORION_HOST}/v2/entities/{entity_id}/attrs"
    data = {"state": {"type": entity_type,"value": state}}

    r = requests.patch(url, json=data, headers=HEADERS, timeout=5)
    if r.status_code not in (204,201):
        raise Exception(f"Error al actualizar entidad {entity_id}: {r.text}")
    
    return {"entity": entity_id, "state": state}
