---
skill: validar-resultado
etapa: 11
nombre: Validación de resultado
gatillada_por: [desplegar]
gatilla: []
gate: gate de producto
habilita_el_gate: Responsable de producto
escribe_fuera: [ticket]
consulta: []
---

# /validar-resultado — Validación de resultado

## Propósito

Volver a preguntar si el problema de la etapa 1 se resolvió.

## Precondiciones

El cambio lleva en producción el plazo fijado en la etapa 2. Indicadores de negocio disponibles.

## Qué hace

- Compara el comportamiento observado en producción contra el problema enunciado en la etapa 1.
- Distingue tres desenlaces y los nombra sin suavizarlos: el problema se resolvió, se resolvió a medias y qué quedó fuera, o no se resolvió y la hipótesis estaba equivocada.
- Registra la hipótesis que falló, que es información tan valiosa como una causa raíz y se pierde con la misma facilidad.

## Qué NO hace

- No decide qué hacer con el resultado: eso es de producto.

## Gate

**Gate de producto.** Lo habilita: Responsable de producto.

## Expediente

**Lee:** Verificación posterior y criterios de la etapa 1.

**Escribe:** Resultado contrastado contra el problema original.
