# Requirements – RepairTrack

## Link del Backlog
[PEGAR AQUÍ LINK DEL TABLERO]

---

## Historias de Usuario

1. Registrar orden de reparación – Must  
2. Actualizar estado de reparación – Must  
3. Consultar estado por número de orden – Must  
4. Ver historial de cliente – Should  
5. Generar reporte mensual – Should  
6. Registrar costo de reparación – Could  
7. Agregar notas internas – Could  
8. Notificación automática por WhatsApp – Won’t (por ahora)

---

## Historias Must con criterios Given / When / Then

### 1. Registrar orden de reparación (Must)

**Historia:**  
Como recepcionista quiero registrar una orden de reparación para llevar control del equipo ingresado.

**Criterios de aceptación:**

- Given que el cliente entrega un equipo  
  When ingreso marca, modelo y descripción de la falla  
  Then el sistema crea una orden con estado “Recibido”

- Given que la orden fue creada  
  When se guarda en el sistema  
  Then se genera un número único de orden

---

### 2. Actualizar estado de reparación (Must)

**Historia:**  
Como técnico quiero actualizar el estado de la reparación para informar el progreso del trabajo.

**Criterios de aceptación:**

- Given que existe una orden registrada  
  When cambio el estado a “En reparación”  
  Then el sistema actualiza el estado correctamente

- Given que el estado es actualizado  
  When se guarda el cambio  
  Then el sistema registra la fecha de actualización

---

## MVP Rationale

El MVP incluye las historias clasificadas como Must porque permiten operar el taller digitalmente desde el primer día: registrar órdenes, actualizar estados y consultar reparaciones. Sin estas funcionalidades el sistema no tendría valor operativo. Las historias Should y Could agregan mejoras, pero no son necesarias para el funcionamiento básico inicial.