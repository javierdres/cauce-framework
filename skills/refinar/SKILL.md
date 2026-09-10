---
skill: refinar
etapa: 3
nombre: Refinamiento
gatillada_por: [especificar]
gatilla: [disenar]
gate: gate técnico
habilita_el_gate: Responsable técnico
escribe_fuera: [subtareas]
consulta: [catalogo]
---

# /refinar — Refinamiento

## Propósito

Convertir los requerimientos en trabajo ejecutable, con los riesgos sobre la mesa antes de escribir código.

## Precondiciones

Etapa 2 aprobada. Acceso de lectura al código de todos los componentes que puedan estar involucrados.

## Qué hace

- Descompone en tareas con salida verificable cada una.
- Mapea qué componentes toca leyendo el código real. Un mapa hecho de memoria o de un diagrama viejo se equivoca justo en los sistemas que más han cambiado.
- Levanta riesgos de seguridad y cumplimiento apoyado en la clasificación de datos y en las reglas duras vigentes.
- Detecta cuando el requerimiento choca con una regla vigente y lo plantea como decisión de producto, no como un problema a resolver después.
- Propone el plan de pruebas, incluida la regresión sobre lo que el cambio roza.
- Propone el plan de observabilidad. Lo que no se instrumenta acá no existe en la etapa 10.

## Qué NO hace

- No implementa.
- No compromete fechas.
- No deja pasar un riesgo sin dueño asignado.

## Gate

**Gate técnico.** Lo habilita: Responsable técnico.

## Expediente

**Lee:** Criterios de aceptación y de cumplimiento.

**Escribe:** Subtareas, mapa de componentes, riesgos con dueño, plan de pruebas y de observabilidad.
