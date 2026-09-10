---
skill: revisar
etapa: 7
nombre: Revisión del cambio
gatillada_por: [persona]
gatilla: [cosechar]
gate: gate del revisor
habilita_el_gate: Revisor, distinto del constructor
escribe_fuera: [comentarios]
consulta: [catalogo, falsos-positivos]
---

# /revisar — Revisión del cambio

## Propósito

Que una persona distinta del autor valide el cambio, con apoyo. Se ejecuta varias veces mientras dura la revisión.

## Precondiciones

Propuesta de cambio abierta. Acceso a todos los repositorios del ticket.

## Qué hace

- Lee los hilos de todos los cambios del ticket en una pasada y los separa en abiertos, que hay que responder, y resueltos, que son el insumo de /cosechar.
- Verifica cada sugerencia de otro revisor contra el código real antes de apoyarla o cuestionarla. Un patrón puede estar establecido en un componente y ausente en otro.
- Levanta hallazgos con severidad, archivo y línea, y con el identificador de la regla cuando sale del catálogo. Sin ese identificador nadie puede ir a discutir la regla.
- Consulta el registro de falsos positivos antes de levantar algo que el equipo ya rechazó.
- Mira el radio de impacto entre componentes.
- Gatilla /cosechar en cada pasada sobre los hilos resueltos desde la anterior.

## Qué NO hace

- No publica ningún hallazgo sin confirmación, caso por caso.
- No aprueba ni integra.
- No reemplaza la verificación funcional.

## Gate

**Gate del revisor.** Lo habilita: Revisor, distinto del constructor.

## Expediente

**Lee:** Propuesta de cambio y guion de verificación.

**Escribe:** Hilos respondidos, hallazgos publicados, decisiones para la etapa 12.
