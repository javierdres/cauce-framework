---
skill: encauzar
etapa: 0
nombre: Puerta de entrada
gatillada_por: [persona]
gatilla: [definir]
gate: ninguno
habilita_el_gate: —
escribe_fuera: [ticket]
consulta: []
---

# /encauzar — Puerta de entrada

## Propósito

Recibir una necesidad en cualquier formato y abrir el expediente que va a acompañar al trabajo por todo el ciclo.

## Precondiciones

Acceso al sistema de tickets y al historial de trabajos anteriores.

## Qué hace

- Clasifica el tipo de trabajo: proyecto nuevo, cambio sobre algo existente, o incidente. De esa clasificación depende por qué etapa entra la cadena.
- Identifica quién pide y para qué. Es lo único que no puede faltar; todo lo demás lo levanta la etapa 1 preguntando.
- Busca si ya existe un expediente o un ticket sobre lo mismo, y en ese caso lo actualiza en vez de abrir uno nuevo.
- Abre el expediente y lo deja enlazado al ticket.

## Qué NO hace

- No define el problema ni propone solución.
- No prioriza ni estima.
- No abre el ticket sin aprobación de quien pide.

## Gate

Ninguno. Esta skill no detiene la cadena.

## Expediente

**Lee:** Necesidad en cualquier formato: nota, correo, transcripción, ticket de soporte.

**Escribe:** Expediente abierto, con quién pide, para qué y de qué tipo es el trabajo.
