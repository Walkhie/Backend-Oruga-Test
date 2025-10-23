from pydantic import BaseModel, Field

class Command(BaseModel):
    entity_id: str = Field(...,example="oruga001")
    state: str = Field(..., example = "IDLE")
