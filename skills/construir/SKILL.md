---
skill: construir
etapa: 5
nombre: Desarrollo
gatillada_por: [persona]
gatilla: [autorrevisar]
gate: ninguno
habilita_el_gate: —
escribe_fuera: [repositorios]
consulta: [catalogo]
---

# /construir — Desarrollo

## Propósito

Implementar dejando el rastro que las etapas siguientes necesitan.

## Precondiciones

Expediente con diseño aceptado. Rama enlazada al ticket. Linters, análisis estático y pruebas instalados.

## Qué hace

- Consulta el catálogo antes de proponer un patrón.
- Instrumenta lo que el plan de observabilidad definió, en el mismo cambio y no después.
- Escribe las pruebas junto con el código, no como una tarea posterior que se recorta cuando aprieta la fecha.

## Qué NO hace

- No decide arquitectura: eso se resolvió en la etapa 4.
- No abre la propuesta de cambio: eso es /autorrevisar.

## Gate

Ninguno. Esta skill no detiene la cadena.

## Expediente

**Lee:** Registro de decisión y subtareas.

**Escribe:** Cambio implementado, instrumentado y con pruebas.
