---
skill: registrar-falso-positivo
etapa: transversal
nombre: Transversal
gatillada_por: []
consultada_por: [autorrevisar, revisar]
gatilla: []
gate: ninguno
habilita_el_gate: —
escribe_fuera: [registro de falsos positivos]
consulta: [falsos-positivos]
---

# /registrar-falso-positivo — Transversal

## Propósito

Dejar por escrito un hallazgo que el equipo rechazó, y el motivo, para que no se vuelva a levantar.

## Precondiciones

Acceso de escritura al registro de falsos positivos.

## Qué hace

- Registra qué levanta el análisis, por qué no aplica, y qué verificar antes de volver a levantarlo.
- Enlaza el origen del rechazo.
- No pasa por el proceso de aprobación de reglas, a propósito: si registrar un falso positivo costara una aprobación, nadie lo registraría.

## Qué NO hace

- No corrige la regla que produjo el falso positivo: eso es un cambio al catálogo, por su propio proceso.

## Gate

Ninguno. Esta skill no detiene la cadena.

## Expediente

**Lee:** Hallazgo rechazado y su motivo.

**Escribe:** Entrada en el registro de falsos positivos.
