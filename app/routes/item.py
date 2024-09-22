from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models import Item, PredictionResponse, DetectFaceResponse
from app.service import prediksi_harga
from app.detectFace import detect_expression

router = APIRouter()

# In-memory "database"
items_db = {}

@router.post("/items/", response_model=Item)
async def create_item(item: Item):
    if item.id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item.id] = item
    return item

@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"detail": "Item deleted"}


@router.post("/predict_harga/", response_model=PredictionResponse)
async def predict_harga(luas: int, strategis: int ):
    harga = prediksi_harga(luas, strategis)
    return {"harga": harga}


@router.post("/detect_face/")
async def detect_face(file: UploadFile = File(...)):
    # Membaca file gambar yang diunggah
    image_data = await file.read()

    expression = detect_expression(image_data)
    return {"expression": expression}