from fastapi import APIRouter, HTTPException
from app.api.models import Command
from app.core.orion_client import update_entity_state

router = APIRouter()

@router.post("/commands")
async def send_command(cmd: Command):
    " Create the entity if no exist and update the state in Orion"
    try:
        result = update_entity_state(cmd.entity_id, cmd.state)
        return {
            "message": f"Entidad {cmd.entity_id} actualizada correctamente.",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el estado de la entidad: {e}")