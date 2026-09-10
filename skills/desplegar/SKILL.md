---
skill: desplegar
etapa: 9
nombre: Despliegue
gatillada_por: [persona]
gatilla: [operar, validar-resultado]
gate: gate de despliegue
habilita_el_gate: Responsable de operación
escribe_fuera: [producción]
consulta: []
---

# /desplegar — Despliegue

## Propósito

Poner el cambio en producción y comprobar con datos que se comporta como decían los criterios.

## Precondiciones

Etapa 8 aprobada. Instrumentación desplegada. Procedimiento de reversión probado, no solo documentado.

## Qué hace

- Reúne y presenta los pasos manuales que el despliegue exige, en vez de dejar que aparezcan durante la ventana.
- Compara el comportamiento observado contra los criterios no funcionales de la etapa 2, usando las fuentes de datos de la etapa 10.
- Vigila la ventana posterior buscando desviaciones respecto de la línea base previa, no de un umbral inventado.
- Si detecta desviación, presenta la evidencia y propone revertir.

## Qué NO hace

- No ejecuta ninguna acción sobre producción sin confirmación.
- No decide revertir: lo propone.

## Gate

**Gate de despliegue.** Lo habilita: Responsable de operación.

## Expediente

**Lee:** Cambio aprobado por QA.

**Escribe:** Verificación posterior registrada, o reversión con la evidencia de por qué.
