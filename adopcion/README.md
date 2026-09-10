# Adopción

En este orden. Cada paso funciona sin los siguientes, y ninguno exige tener el anterior
perfecto.

## 1. El catálogo de estándares, vacío

Un repositorio propio de la organización, con formato de regla, validador y catálogo
generado. Vacío a propósito: un set copiado de una guía de la industria describe a quien lo
copió, no a la organización.

- [ ] Repositorio creado con el formato de `plantillas/regla.md`
- [ ] Validador de formato corriendo
- [ ] Un lugar de baja fricción para registrar falsos positivos, fuera del proceso de
      aprobación de reglas

## 2. La revisión previa

Es la que más devuelve por lo que cuesta y no obliga a nadie más a cambiar su forma de
trabajar.

- [ ] `/autorrevisar` implementada
- [ ] Linters y análisis estático accesibles desde la skill
- [ ] Credenciales personales por persona, nunca compartidas
- [ ] Convención de ramas que enlace con el ticket

## 3. La revisión del cambio, con la cosecha adentro

Las dos juntas. Una revisión asistida que no cosecha deja el ciclo abierto.

- [ ] `/revisar` implementada, pensada para ejecutarse varias veces
- [ ] `/cosechar` gatillada por `/revisar`, nunca por una persona
- [ ] Verificado que quien construye no revisa su propio cambio

## 4. El guion de verificación funcional

Barato, y separa con claridad revisión de QA.

- [ ] `/verificar` implementada
- [ ] Plantilla de guion adoptada

## 5. El refinamiento y el diseño

Cuando el catálogo ya tiene reglas que valga la pena consultar antes de decidir una
arquitectura.

- [ ] `/refinar` y `/disenar` implementadas
- [ ] `/consultar-catalogo` disponible para ambas
- [ ] Verificado que quien propone un diseño no lo acepta

## 6. Operación y SRE

Requiere que las fuentes de datos existan y sean confiables, que suele ser el trabajo más
largo de todos.

- [ ] Identificador de correlación propagado de punta a punta
- [ ] Una sola fuente de verdad por pregunta
- [ ] Retención declarada y suficiente
- [ ] Procedimiento de reversión probado, no solo documentado
- [ ] `/operar` y `/analizar-incidente` implementadas

## 7. Gate 0, definición y requerimientos

Dependen de que producto adopte el hábito, y eso no se decreta.

- [ ] `/cauce`, `/definir` y `/especificar` implementadas
- [ ] Expediente adoptado como única fuente de contexto

## 8. La validación de resultado

La última, porque exige tener datos de negocio confiables y la disposición a registrar que
una hipótesis falló.

- [ ] `/validar-resultado` implementada
- [ ] Plazo de validación fijado en la etapa 2 de cada trabajo
