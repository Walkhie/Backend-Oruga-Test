from pydantic import BaseModel, Field

class CreateEntity(BaseModel):
    entity_id: str = Field(..., example="oruga001")
    entity_type: str = Field("RobotOruga", example="RobotOruga")
    state: str = Field("IDLE", example="IDLE")
    speed: int = Field(0, example=0, description="velocidad del robot en ")
