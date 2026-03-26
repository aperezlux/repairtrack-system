from pydantic import BaseModel
from enum import Enum

class EstadoOrden(str, Enum):
    pendiente = "pendiente"
    en_proceso = "en_proceso"
    terminado = "terminado"

class OrderCreate(BaseModel):
    cliente: str
    equipo: str
    problema: str

class Order(OrderCreate):
    id: int
    estado: EstadoOrden
