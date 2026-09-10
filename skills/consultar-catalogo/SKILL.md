---
skill: consultar-catalogo
etapa: transversal
nombre: Transversal
gatillada_por: []
consultada_por: [refinar, disenar, autorrevisar, revisar]
gatilla: []
gate: ninguno
habilita_el_gate: —
escribe_fuera: []
consulta: [catalogo]
---

# /consultar-catalogo — Transversal

## Propósito

Traer las reglas vigentes que aplican por ámbito y por proyecto, para que las demás skills no lo resuelvan cada una a su manera.

## Precondiciones

Catálogo accesible por lectura mecánica.

## Qué hace

- Filtra por estado, ámbito y proyectos.
- Devuelve las vigentes con su severidad real y las candidatas siempre como sugerencia.
- Si el catálogo no se puede leer, lo dice explícitamente y no lo omite en silencio.

## Qué NO hace

- No evalúa el código.
- No promueve ni edita reglas.

## Gate

Ninguno. Esta skill no detiene la cadena.

## Expediente

**Lee:** Ámbito y proyecto del trabajo.

**Escribe:** Reglas aplicables con su severidad.
