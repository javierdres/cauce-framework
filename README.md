# CAUCE

**Ciclo Asistido Unificado de Construcción y Entrega.** Un SDLC Framework con asistencia
de IA: define las etapas del ciclo de vida del software, sus entradas y salidas, los puntos
de control humano y los actores de cada una.

Agnóstico de empresa, dominio, lenguaje y plataforma.

La asistencia de IA sin cauce es una crecida. Con cauce es un río.

## Por dónde empezar

[CAUCE.md](CAUCE.md) es el documento completo. Si tienes diez minutos, lee la sección 2
(la puerta de entrada y el expediente) y la 6 (los actores, y la línea que separa lo que
hace la IA de lo que hacen las personas).

## Qué hay acá

```
├── CAUCE.md            El framework completo
├── skills/             Las 16 skills, cada una con su contrato
├── plantillas/         Expediente, decisión de diseño, guion de QA, postmortem, regla
├── bin/
│   ├── validar.py      Comprueba que los contratos estén completos y la cadena cierre
│   └── generar_pdf.py  Regenera el PDF desde el Markdown
├── adopcion/           Cómo implantarlo, paso a paso
└── docs/CAUCE.pdf      El documento en PDF
```

## Qué NO hay acá, a propósito

**Las reglas de tu organización.** El catálogo de estándares es de cada organización y vive
en su propio repositorio. Este marco define cómo se alimenta ese catálogo, no qué dice.

**Ceremonias, cadencia ni estimación.** CAUCE describe el recorrido de un trabajo y quién
habilita cada paso. Scrum, Kanban o lo que uses para organizar al equipo sigue funcionando
encima.

## Las skills

Catorce de ciclo y dos transversales. Cada una declara en su frontmatter quién la gatilla,
a quién gatilla, qué gate tiene, quién lo habilita, qué escribe fuera y qué consulta.

```
python3 bin/validar.py
```

Comprueba que todos los contratos estén completos y que la cadena cierre en los dos
sentidos: si A dice que gatilla a B, B tiene que decir que la gatilla A.

## Los cinco momentos de invocación humana

`/encauzar` cuando nace la necesidad. `/construir` cuando alguien se sienta a implementar.
`/revisar` cuando alguien revisa, varias veces. `/verificar` cuando alguien prueba.
`/desplegar` cuando alguien despliega.

Todo lo demás lo encadena el framework. Los mecanismos que dependen de que una persona
recuerde invocarlos no ocurren.

## Cómo adoptarlo

Ver [adopcion/](adopcion/README.md). El framework rinde desde el segundo paso; no hay que
esperar a tenerlo completo.
