from fastapi import APIRouter, HTTPException
from typing import List
from .models import Order, OrderCreate, EstadoOrden

router = APIRouter()

db = []
counter = 1

@router.post("/orders", response_model=Order)
def create_order(order: OrderCreate):
    global counter
    new_order = Order(id=counter, estado=EstadoOrden.pendiente, **order.dict())
    db.append(new_order)
    counter += 1
    return new_order

@router.get("/orders", response_model=List[Order])
def get_orders():
    return db

@router.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    for order in db:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Orden no encontrada")

@router.put("/orders/{order_id}/status", response_model=Order)
def update_status(order_id: int, estado: EstadoOrden):
    for order in db:
        if order.id == order_id:
            order.estado = estado
            return order
    raise HTTPException(status_code=404, detail="Orden no encontrada")
