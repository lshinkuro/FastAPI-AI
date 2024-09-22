from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    quantity: int

class PredictionResponse(BaseModel):
    harga: float

class DetectFaceResponse(BaseModel):
    expression: str

