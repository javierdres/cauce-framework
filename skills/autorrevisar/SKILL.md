---
skill: autorrevisar
etapa: 6
nombre: Revisión previa
gatillada_por: [construir]
gatilla: [verificar]
gate: gate del autor
habilita_el_gate: Constructor, sobre su propio trabajo
escribe_fuera: [propuesta de cambio, guion de QA]
consulta: [catalogo, falsos-positivos]
---

# /autorrevisar — Revisión previa

## Propósito

Revisar el cambio en privado para que llegue depurado a la revisión humana. Su salida va al autor y no a un sistema compartido.

## Precondiciones

Rama lista. Acceso a todos los repositorios que el cambio toca.

## Qué hace

- Identifica el ticket desde la rama y trae su definición sin editarla.
- Determina todos los repositorios que el cambio toca y verifica que ninguno quedó a medias.
- Corre linters y análisis estático. Un error de sintaxis es bloqueante.
- Verifica cada afirmación sobre convenciones contra el código real.
- Hace un pase completo de reglas duras si el cambio toca autenticación, autorización, aislamiento entre clientes o los datos que la etapa 1 clasificó como sensibles.
- Cruza los artefactos que van juntos: migraciones con su registro de cambios, instrumentación con el plan, documentación con el código.
- Compara la rama completa contra la base, no solo los últimos commits, contra los criterios de la etapa 2.
- Redacta la propuesta de cambio y el guion de verificación funcional.

## Qué NO hace

- No publica hallazgos en ningún sistema compartido.
- No integra.
- No reemplaza la revisión humana.

## Gate

**Gate del autor.** Lo habilita: Constructor, sobre su propio trabajo.

## Expediente

**Lee:** Cambio implementado.

**Escribe:** Hallazgos resueltos, propuesta de cambio enlazada, guion de verificación.
