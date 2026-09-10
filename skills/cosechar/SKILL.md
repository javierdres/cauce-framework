---
skill: cosechar
etapa: 12
nombre: Aprendizaje
gatillada_por: [revisar, analizar-incidente]
gatilla: []
gate: gate por regla
habilita_el_gate: Custodio del estándar
escribe_fuera: [catálogo]
consulta: [catalogo, falsos-positivos]
---

# /cosechar — Aprendizaje

## Propósito

Que las decisiones y las causas raíz sobrevivan a la conversación o al turno donde aparecieron.

## Precondiciones

Acceso de escritura al repositorio de estándares. Catálogo y registro de falsos positivos al día.

## Qué hace

- Toma dos fuentes: hilos resueltos de una revisión y causas raíz de un incidente.
- Cosecha solo lo que cumple las dos condiciones: el hilo cerró con un desenlace explícito, y la afirmación sigue siendo cierta fuera de ese caso.
- Descarta lo que describe cómo está construido un proyecto, que va a su documentación, y lo que es práctica genérica sin decisión propia detrás, que ya cubre la base de la industria.
- Deduplica contra el catálogo antes de redactar. Si la regla ya existe, edita la existente sumando el origen y una línea al historial.
- Redacta la regla como candidata, nunca como vigente.
- Cierra siempre con tres listas: cosechadas, descartadas con el motivo, y decisiones pendientes.

## Qué NO hace

- No promueve una regla a vigente.
- No escribe ninguna regla sin confirmación, regla por regla.
- No inventa reglas sin origen enlazable.

## Gate

**Gate por regla.** Lo habilita: Custodio del estándar.

## Expediente

**Lee:** Hilos resueltos y causas raíz.

**Escribe:** Reglas candidatas y el reporte de tres listas.
