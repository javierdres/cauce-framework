> **Español** · [English](README.md)

# GATE

**Governed, Assisted, Traceable Engineering.** Un framework de ciclo de vida de software con
asistencia de IA: define las etapas, sus entradas y salidas, los puntos de control humano y los
actores de cada una.

Agnóstico de empresa, dominio, lenguaje y plataforma.

Asistencia que se detiene donde empieza el criterio.

## En 95 segundos

[docs/GATE.webm](docs/GATE.webm) recorre el framework completo: el problema, los cinco momentos
de invocación humana, la línea entre lo que hace la IA y lo que hacen las personas, y el lazo de
aprendizaje. Sin audio; el guion está en [docs/video-script.md](docs/video-script.md).

## Para arrancar

Dos comandos que arman lo que cualquier equipo necesita antes de la primera corrida:

```
python3 bin/bootstrap.py catalog ../nuestros-estandares
python3 bin/bootstrap.py config  ../nuestro-proyecto
```

El primero escribe un repositorio de catálogo completo, vacío de reglas a propósito. El segundo
deja el `.gate/config.yml` en un proyecto, completando lo que puede leer del repositorio.

Después `python3 bin/check_config.py ../nuestro-proyecto/.gate/config.yml` te dice cuáles de los
ocho campos siguen bloqueando el arranque.

## Por dónde empezar

**[START-HERE.es.md](START-HERE.es.md)** responde las tres preguntas que de verdad vienen primero: cómo inicio un proyecto nuevo, cómo inicio un requerimiento nuevo sobre uno existente, y
cómo resuelvo una incidencia. Cada una con qué cambia respecto de cómo lo haces hoy, y qué
cuesta.

## La referencia

[GATE.md](GATE.md) es el documento completo, en inglés. Si tienes diez minutos, lee la sección 2
(la puerta de entrada y el expediente) y la 6 (los actores, y la línea entre lo que hace la IA y
lo que hacen las personas).

## Qué contiene

```
├── START-HERE.es.md    Las tres formas de entrar, y qué cambia cada una
├── GATE.md             El framework completo
├── CONTRIBUTING.md     Cómo cambia el framework mismo
├── skills/             Las 16 skills, cada una con su contrato
├── templates/          Config de proyecto, expediente, decisión de diseño, guion de QA, postmortem, regla
├── adoption/           Cómo implantarlo, paso a paso
├── bin/
│   ├── bootstrap.py    Arma el catálogo de estándares y la config de un proyecto
│   ├── validate.py     Comprueba que los contratos estén completos y la cadena cierre
│   ├── check_config.py Reporta qué le falta al .gate/config.yml de un proyecto
│   └── build_pdf.py    Regenera el PDF desde el Markdown
└── docs/
    ├── GATE.pdf        El documento en PDF
    ├── GATE.webm       Explicativo de 95 segundos, sin audio
    └── video-script.md Guion de narración de ese video
```

## Qué no contiene, a propósito

**Las reglas de tu organización.** El catálogo de estándares es de cada organización y vive en
su propio repositorio, uno por organización por muchos proyectos que tenga. Este framework
define cómo se alimenta ese catálogo, no qué dice. La sección 7 del documento explica cómo
encajan los niveles.

**Ceremonias, cadencia ni estimación.** GATE describe el recorrido de un trabajo y quién
habilita cada paso. Scrum, Kanban o lo que uses para organizar al equipo sigue funcionando
encima.

**Las implementaciones de las skills.** Cada una declara su contrato: quién la gatilla, qué
entrega, dónde se detiene a preguntar. Conectarlo con tus herramientas te corresponde a ti.

## Las skills

Catorce de ciclo y dos transversales. Cada una declara en su frontmatter quién la gatilla, a
quién gatilla, qué gate tiene, quién lo habilita, qué escribe fuera y qué consulta.

```
python3 bin/validate.py
```

Comprueba que todos los contratos estén completos y que la cadena cierre en los dos sentidos: si
A dice que gatilla a B, B tiene que decir que la gatilla A.

## Los cinco momentos de invocación humana

`/init` cuando nace la necesidad. `/build` cuando alguien se sienta a implementar. `/review`
cuando alguien revisa, varias veces. `/verify` cuando alguien prueba. `/deploy` cuando alguien
despliega.

El framework encadena todo lo demás. Los mecanismos que dependen de que una persona recuerde
invocarlos no ocurren.

## De dónde sale

GATE no nace de una recopilación bibliográfica. Sale de dirigir equipos de desarrollo y de ver, una y
otra vez, los mismos cuatro problemas: la calidad dependiendo de quién usó el asistente ese día,
las decisiones evaporándose entre conversaciones, la seguridad entrando tarde, y nadie capaz de
responder qué vara se aplicó a un cambio.

Cada regla de este framework responde a algo que salió mal en la práctica. Los gates existen
porque hubo automatismos que ejecutaron de más. Las tres incompatibilidades de rol existen
porque un equipo chico con asistencia fuerte converge rápido, y a veces hacia el lado
equivocado. La etapa 12 existe porque es fácil encontrar un catálogo de estándares vacío al lado
de un cambio con ciento cincuenta comentarios de discusión.

Es un framework vivo, en uso y en mejora continua. Lo que hoy son contratos de skills va a
seguir cambiando a medida que se aplique.

## Autoría y licencia

Autor y titular: **Javier Núñez**.

| Qué | Licencia |
|---|---|
| Documentación: `GATE.md`, `README.md`, `skills/`, `templates/`, `adoption/`, `docs/` | [CC BY 4.0](LICENSE-DOCS) |
| Código: `bin/` | [MIT](LICENSE) |

Puedes usar GATE en tu organización, adaptarlo y redistribuirlo, incluso comercialmente. Lo único
que se pide a cambio es la atribución.

### Sobre el nombre

La licencia cubre la obra, no el nombre. Si adaptas GATE para tu organización, úsalo con
libertad. Si publicas un derivado con cambios sustanciales en las etapas, los gates o la
separación entre lo que hace la IA y lo que hacen las personas, ponle otro nombre y menciona su procedencia: así "GATE" sigue significando una sola cosa.
