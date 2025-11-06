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

def create_entity(entity_id: str, entity_type: str = "RobotOruga", state: str = "IDLE", speed : int = 0) -> bool:
    "Crea una nueva entidad oruga en Orion"
    url = f"{settings.ORION_HOST}/v2/entities"
    payload = {
        "id": entity_id,
        "type": entity_type,
        "state": {"type":"Text","value":state},
        "speed":{"type":"Integer","value":0}
    }

    try:
        r = requests.post(url, json=payload, headers=HEADERS, timeout=5)
        print("Orion response:", r.status_code, r.text)
        return {"status_code": r.status_code, "response": r.text}
        # status_code 201 = creado, 422 = ya existe

    except requests.exceptions.RequestException as e:
        print("Error de conexión con Orion:", e)
        raise

def update_entity_state(entity_id:str,entity_type: str = "RobotOruga", state:str = "IDLE",speed:int = 0):
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

# headers sin context type
delete_headers = {
    "Fiware-Service": settings.FIWARE_SERVICE,
    "Fiware-ServicePath": settings.FIWARE_SERVICEPATH
}

def get_entities():
    # Obtiene todas las entidades del Orion Context Broker.

    url = f"{settings.ORION_HOST}/v2/entities"
    try:
        r = requests.get(url, headers=delete_headers, timeout=5)
        print("Orion GET /entities:", r.status_code)
        if r.status_code == 200:
            return r.json()
        
        # Si no hay entidades
        elif r.status_code == 404:
            return []
        
        else:
            raise Exception(f"Error {r.status_code}: {r.text}")
        
    except requests.exceptions.RequestException as e:
        raise Exception("Error de conexión con Orion:", e)

def delete_entity(entity_id: str):
    """
    Elimina una entidad de Orion Context Broker por su ID.
    """
    url = f"{settings.ORION_HOST}/v2/entities/{entity_id}"

    try:
        r = requests.delete(url, headers=delete_headers, timeout=5)
        print(f"DELETE /entities/{entity_id}", r.status_code, r.text)

        if r.status_code == 204:
            return {"deleted": True, "message": "Entidad eliminada correctamente"}
        elif r.status_code == 404:
            return {"deleted": False, "message": "Entidad no encontrada"}
        else:
            raise Exception(f"Error {r.status_code}: {r.text}")

    except requests.exceptions.RequestException as e:
        print("Error de conexión con Orion:", e)
        raise

def get_entity_state_speed(entity_id: str):
    
    # Consulta en Orion una entidad específica y devuelve solo su estado actual.
    url = f"{settings.ORION_HOST}/v2/entities/{entity_id}"
    try:

        r = requests.get(url, headers=delete_headers, timeout=5)
        print(f"Orion GET /entities/{entity_id}:", r.status_code)

        if r.status_code == 200:
            data = r.json()
            return {"state": data["state"]["value"],
                    "speed": data["speed"]["value"]}

        elif r.status_code == 404:
            return None

        else:
            raise Exception(f"Error {r.status_code}: {r.text}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error de conexión con Orion: {e}")
