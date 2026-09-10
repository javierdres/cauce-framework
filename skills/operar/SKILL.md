---
skill: operar
etapa: 10
nombre: Operación y SRE
gatillada_por: [desplegar, alerta]
gatilla: [analizar-incidente]
gate: gate de operación
habilita_el_gate: Responsable de operación
escribe_fuera: [alertas, incidentes]
consulta: []
---

# /operar — Operación y SRE

## Propósito

Sostener el servicio, detectar antes que el usuario, y recuperar dentro de la ventana comprometida.

## Precondiciones

Fuentes de datos accesibles: logs de aplicación e infraestructura, métricas, trazas, auditoría, estado de dependencias externas. Identificador de correlación propagado y retención declarada.

## Qué hace

- Correlaciona las fuentes a partir de un síntoma y distingue la causa del ruido, sosteniendo cada afirmación en la fuente que la puede probar.
- Compara el comportamiento actual contra la línea base previa al último cambio y lo vincula con el ticket que lo introdujo.
- Propone qué amerita alerta y, sobre todo, qué no: si al dispararse nadie va a hacer nada distinto, es un dato de tablero.
- Prepara el guion del ensayo de recuperación y compara el resultado real contra la ventana comprometida.

## Qué NO hace

- No toca producción sin confirmación, incluido silenciar una alerta.
- No afirma una causa sin la fuente que la prueba.

## Gate

**Gate de operación.** Lo habilita: Responsable de operación.

## Expediente

**Lee:** Sistema en producción.

**Escribe:** Diagnósticos con evidencia, incidentes, resultado de ensayos de continuidad.
