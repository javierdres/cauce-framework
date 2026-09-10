---
skill: verificar
etapa: 8
nombre: Verificación funcional
gatillada_por: [autorrevisar, persona]
gatilla: []
gate: gate de QA
habilita_el_gate: Verificador
escribe_fuera: []
consulta: []
---

# /verificar — Verificación funcional

## Propósito

Comprobar contra los criterios de la etapa 2, sobre el sistema funcionando.

## Precondiciones

Cambio desplegado en un ambiente de prueba. Guion redactado en la etapa 6.

## Qué hace

- Redacta el guion con una marca por resultado comprobable, no una por caso, de modo que un fallo señale qué falló.
- Un bloque por componente afectado, nombrando qué mirar en cada pantalla.
- La precondición escrita como una comprobación que quien prueba pueda hacer, con qué hacer si no se cumple.
- Pasos ejecutables con las herramientas que quien prueba ya tiene.
- Las falsas alarmas conocidas, dichas de antemano.
- Qué hacer con lo que no se puede probar en ese ambiente: dejarlo sin marcar y anotarlo, nunca darlo por fallido.

## Qué NO hace

- No ejecuta las pruebas.
- No da por aprobado ningún criterio.

## Gate

**Gate de qa.** Lo habilita: Verificador.

## Expediente

**Lee:** Guion de verificación.

**Escribe:** Resultado por criterio.
