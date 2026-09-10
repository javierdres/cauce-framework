#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Javier Núñez
"""Valida que las skills del framework declaren un contrato completo y coherente.

Comprueba, por cada skill: que el frontmatter traiga todos los campos, que las
secciones obligatorias existan, y que la cadena de disparo cierre — si A dice que
gatilla a B, B tiene que decir que la gatilla A.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(RAIZ, "skills")

CAMPOS = ["skill", "etapa", "nombre", "gatillada_por", "gatilla", "gate",
          "habilita_el_gate", "escribe_fuera", "consulta"]
SECCIONES = ["## Propósito", "## Precondiciones", "## Qué hace", "## Qué NO hace",
             "## Gate", "## Expediente"]
# orígenes válidos que no son otra skill
EXTERNOS = {"persona", "alerta"}

errores = []


def error(donde, msg):
    errores.append("%s: %s" % (donde, msg))


def lista(valor):
    valor = valor.strip()
    if valor.startswith("[") and valor.endswith("]"):
        valor = valor[1:-1]
    return [x.strip() for x in valor.split(",") if x.strip()]


def leer(ruta):
    texto = io.open(ruta, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", texto, re.S)
    if not m:
        return None, None
    front = {}
    for linea in m.group(1).split("\n"):
        if ":" in linea:
            k, v = linea.split(":", 1)
            front[k.strip()] = v.strip()
    return front, m.group(2)


def main():
    if not os.path.isdir(SKILLS):
        print("no existe skills/", file=sys.stderr)
        return 1

    nombres = sorted(d for d in os.listdir(SKILLS)
                     if os.path.isdir(os.path.join(SKILLS, d)))
    fronts = {}

    for n in nombres:
        ruta = os.path.join(SKILLS, n, "SKILL.md")
        donde = "skills/%s/SKILL.md" % n
        if not os.path.exists(ruta):
            error("skills/%s" % n, "falta SKILL.md")
            continue
        front, cuerpo = leer(ruta)
        if front is None:
            error(donde, "sin frontmatter")
            continue
        fronts[n] = front

        for c in CAMPOS:
            if c not in front:
                error(donde, "falta el campo '%s'" % c)
        if front.get("skill") != n:
            error(donde, "el campo skill ('%s') no calza con el directorio"
                  % front.get("skill"))
        for s in SECCIONES:
            if s not in cuerpo:
                error(donde, "falta la sección '%s'" % s)
        et = front.get("etapa", "")
        if et != "transversal" and not (et.isdigit() and 0 <= int(et) <= 12):
            error(donde, "etapa inválida: '%s' (0 a 12, o 'transversal')" % et)
        if front.get("gate") != "ninguno" and front.get("habilita_el_gate", "—") == "—":
            error(donde, "declara un gate pero no quién lo habilita")
        if front.get("gate") == "ninguno" and front.get("habilita_el_gate", "—") != "—":
            error(donde, "no declara gate pero sí quién lo habilita")
        if et == "transversal":
            if "consultada_por" not in front:
                error(donde, "una skill transversal declara consultada_por, no gatillada_por")
            if lista(front.get("gatillada_por", "")):
                error(donde, "una skill transversal no se gatilla: se consulta")

    # la cadena tiene que cerrar en los dos sentidos
    for n, front in fronts.items():
        donde = "skills/%s/SKILL.md" % n
        for destino in lista(front.get("gatilla", "")):
            if destino not in fronts:
                error(donde, "gatilla a '%s', que no existe" % destino)
            elif n not in lista(fronts[destino].get("gatillada_por", "")):
                error(donde, "gatilla a '%s', pero '%s' no lo declara en gatillada_por"
                      % (destino, destino))
        for lector in lista(front.get("consultada_por", "")):
            if lector not in fronts:
                error(donde, "dice que la consulta '%s', que no existe" % lector)
        for origen in lista(front.get("gatillada_por", "")):
            if origen in EXTERNOS:
                continue
            if origen not in fronts:
                error(donde, "dice que la gatilla '%s', que no existe" % origen)
            elif n not in lista(fronts[origen].get("gatilla", "")):
                error(donde, "dice que la gatilla '%s', pero '%s' no lo declara en gatilla"
                      % (origen, origen))

    for e in errores:
        print("✖ %s" % e)
    if errores:
        print("\n✖ %d problema(s) en %d skill(s)." % (len(errores), len(nombres)))
        return 1
    print("✔ %d skills válidas y la cadena de disparo cierra." % len(nombres))
    humanas = [n for n, f in fronts.items()
               if "persona" in lista(f.get("gatillada_por", ""))]
    print("  Invocación humana: %s" % ", ".join("/%s" % h for h in sorted(humanas)))
    gates = [(int(f["etapa"]) if f["etapa"].isdigit() else 99, n, f["gate"], f["habilita_el_gate"])
             for n, f in fronts.items() if f.get("gate") != "ninguno"]
    print("  Gates: %d" % len(gates))
    for _, n, g, h in sorted(gates):
        print("    /%-24s %-26s %s" % (n, g, h))
    return 0


if __name__ == "__main__":
    sys.exit(main())
