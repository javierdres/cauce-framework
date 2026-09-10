---
skill: analizar-incidente
etapa: 10
nombre: Postmortem
gatillada_por: [operar]
gatilla: [cosechar]
gate: gate de cierre
habilita_el_gate: Responsable de operación
escribe_fuera: [documento]
consulta: []
---

# /analizar-incidente — Postmortem

## Propósito

Reconstruir qué pasó y por qué, para que la organización aprenda del incidente.

## Precondiciones

Incidente cerrado. Acceso a las fuentes de datos del periodo.

## Qué hace

- Reconstruye la línea de tiempo desde las fuentes y no desde la memoria de quien estuvo de turno.
- Separa la causa raíz de los factores que contribuyeron.
- Nombra qué habría detectado el problema antes, y si eso existe o hay que construirlo.
- Gatilla /cosechar con la causa raíz.

## Qué NO hace

- No asigna culpas a personas.
- No cierra el incidente: eso es humano.

## Gate

**Gate de cierre.** Lo habilita: Responsable de operación.

## Expediente

**Lee:** Incidente.

**Escribe:** Línea de tiempo, causa raíz, y material para la etapa 12.
