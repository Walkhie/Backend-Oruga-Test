from pydantic import BaseModel, Field

class CreateEntity(BaseModel):
    entity_id: str = Field(..., example="oruga001")
    entity_type: str = Field("RobotOruga", example="RobotOruga")
    state: str = Field("IDLE", example="IDLE")
