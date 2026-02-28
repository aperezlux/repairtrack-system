# System Brief – RepairTrack

## 1. Visión

RepairTrack busca digitalizar la gestión de órdenes de reparación en talleres de celulares, permitiendo un control claro del estado de cada equipo y mejor organización interna.

## 2. Problema

Actualmente muchos talleres:
- Registran reparaciones en papel
- No tienen control del estado del equipo
- No pueden consultar historial de clientes fácilmente
- No cuentan con reportes básicos de ingresos

Esto genera desorden y mala experiencia para el cliente.

## 3. Stakeholders

- Dueño del taller
- Recepcionista
- Técnico
- Cliente

## 4. Scope (Incluye)

- Registrar órdenes de reparación
- Actualizar estado (Recibido, En reparación, Listo, Entregado)
- Consultar orden por número
- Ver historial de cliente
- Generar reporte mensual básico

## 5. No-Scope (Por ahora)

- Aplicación móvil
- Pagos en línea
- Facturación electrónica
- Integración con proveedores

## 6. Diagrama de Contexto

```mermaid
flowchart LR
    Cliente -->|Entrega equipo| Sistema
    Recepcionista -->|Registra orden| Sistema
    Tecnico -->|Actualiza estado| Sistema
    Sistema -->|Muestra estado| Cliente
    Dueño -->|Consulta reportes| Sistema