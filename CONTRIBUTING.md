# Contribuir a CAUCE

CAUCE está en uso y en mejora continua. Las contribuciones más valiosas son las que salen de
haberlo aplicado, no de haberlo leído.

## Qué aporta más

**Experiencias de adopción.** Qué etapa costó más implantar, cuál se saltaron y qué pasó, en
qué tamaño de equipo. Eso vale más que una corrección de redacción.

**Contratos de skill afinados.** Si al implementar una skill descubriste que le falta un
límite o que hace algo que no debería, cámbialo y explica el caso que lo motivó.

**Antipatrones nuevos.** La sección de antipatrones creció desde errores reales. Si viste uno
que no está, agrégalo con lo que costó.

## Qué no entra

Reglas de estándar concretas. El catálogo es de cada organización y vive en su propio
repositorio: este marco define cómo se alimenta, no qué dice.

Ceremonias, cadencia o estimación. CAUCE describe el recorrido de un trabajo y quién habilita
cada paso; la forma de organizar al equipo va por fuera.

Buenas prácticas genéricas sin una decisión detrás. Si no puedes rastrearla a algo que
ocurrió, todavía no es material para este marco.

## Antes de abrir un pull request

Corre el validador. Comprueba que los contratos estén completos y que la cadena de disparo
cierre en los dos sentidos.

```
python3 bin/validar.py
```

Si tocaste `CAUCE.md`, regenera el PDF.

```
python3 bin/generar_pdf.py CAUCE.md
```

## Licencia de las contribuciones

Al enviar una contribución aceptas que se publique bajo las mismas licencias del repositorio:
CC BY 4.0 para documentación y MIT para código. No hace falta firmar nada.
