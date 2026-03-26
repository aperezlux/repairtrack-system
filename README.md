# RepairTrack System

Sistema de gestión de reparaciones de celulares.

## Instalación

pip install -r requirements.txt

## Ejecución

uvicorn app.main:app --reload

Abrir en navegador:
http://127.0.0.1:8000/docs

## Endpoints

- POST /orders
- GET /orders
- GET /orders/{id}
- PUT /orders/{id}/status
