# -*- coding: utf-8 -*-
"""Integra C-05/C-06 en la copia del Word sin regenerar plantilla."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "2.2.2-Gestion-de-cambios-Kiran.docx"


def set_cell_text(cell, text: str) -> None:
    """Reemplaza el texto de la celda conservando el primer párrafo/run si existe."""
    if not cell.paragraphs:
        cell.text = text
        return
    p0 = cell.paragraphs[0]
    if p0.runs:
        p0.runs[0].text = text
        for run in p0.runs[1:]:
            run.text = ""
    else:
        p0.text = text
    # Limpiar párrafos extra de la celda
    for p in cell.paragraphs[1:]:
        p._element.getparent().remove(p._element)


def clone_row(table, source_idx: int = -1):
    tr = table.rows[source_idx]._tr
    new_tr = deepcopy(tr)
    table._tbl.append(new_tr)
    return table.rows[-1]


def fill_row(row, values: list[str]) -> None:
    for cell, value in zip(row.cells, values):
        set_cell_text(cell, value)


def insert_paragraph_after(paragraph: Paragraph, text: str) -> Paragraph:
    new_p = deepcopy(paragraph._p)
    # Quitar runs del clon
    for child in list(new_p):
        if child.tag == qn("w:r"):
            new_p.remove(child)
    paragraph._p.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
    # Copiar formato del primer run del párrafo origen si existe
    if paragraph.runs:
        run = new_para.add_run(text)
        src = paragraph.runs[0]
        run.bold = src.bold
        run.italic = src.italic
        if src.font.size:
            run.font.size = src.font.size
        if src.font.name:
            run.font.name = src.font.name
    else:
        new_para.add_run(text)
    return new_para


def find_para(doc: Document, startswith: str | None = None, contains: str | None = None):
    for p in doc.paragraphs:
        t = p.text or ""
        if startswith is not None and t.startswith(startswith):
            return p
        if contains is not None and contains in t:
            return p
    raise KeyError(f"Párrafo no encontrado: startswith={startswith!r} contains={contains!r}")


def replace_in_para(doc: Document, contains: str, old: str, new: str) -> None:
    p = find_para(doc, contains=contains)
    if old not in (p.text or ""):
        return
    full = p.text.replace(old, new)
    if p.runs:
        p.runs[0].text = full
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.text = full


def main() -> None:
    doc = Document(str(DOCX))
    tables = doc.tables
    # Índices: T0=Tabla1, T1=Tabla2, ... T10=Tabla11
    t2, t3, t4, t5, t6, t7, t8, t9, t10, t11 = (
        tables[1],
        tables[2],
        tables[3],
        tables[4],
        tables[5],
        tables[6],
        tables[7],
        tables[8],
        tables[9],
        tables[10],
    )

    # --- Introducciones ---
    replace_in_para(
        doc,
        "Este documento aplica un solo procedimiento",
        "cuatro cambios potenciales del caso",
        "seis cambios potenciales del caso",
    )
    replace_in_para(
        doc,
        "Las cuatro situaciones siguientes se consideran cambios",
        "Las cuatro situaciones siguientes",
        "Las seis situaciones siguientes",
    )

    intro_prio = find_para(doc, contains="Cuando dos cambios caben en el mismo cuadrante")
    insert_paragraph_after(
        intro_prio,
        "C-05 y C-06 no suman encima de la fotografía, el segundo punto de inventario y el servicio "
        "externo: compiten por las mismas dos tarjetas por persona. Si entra uno, sale una historia "
        "equivalente del sprint. La contingencia del 12 % sigue cerrada sin razón escrita. Un "
        "datalake completo, un modelo hospedado por el equipo o una IA para hogares y donantes no "
        "entran en esta ventana: o se cierran, o quedan como solicitud futura fuera del piloto.",
    )

    # --- Tabla 2 ---
    fill_row(
        clone_row(t2),
        [
            "C-05",
            "Ejemplo de solicitud. La dirección pide un asistente de IA de uso interno para tickets, "
            "reportes y decisiones. En este plan la formulación completa no se aprueba: solo se "
            "contempla la fase 1 (resumen de ticket, checklist de terreno y sugerencia del siguiente "
            "ticket en cola, con confirmación humana), tras un tablero usable y sin enviar datos de "
            "hogares a un modelo externo.",
            "Dirección / equipo",
            "9 de noviembre (depende del tablero) y 4 de diciembre (tickets). No la ruta crítica de inventario.",
        ],
    )
    fill_row(
        clone_row(t2),
        [
            "C-06",
            "Se pide una priorización visual en el tablero: cola o filtros que muestren qué atender "
            "primero (kit en falla, urgencia), para bajar consultas fuera del sistema al soporte "
            "local. No cambia los estados del kit ni abre una app ciudadana. Reutiliza la prioridad "
            "de C-01b si esa medida entra; no la sustituye.",
            "Contraparte / soporte local",
            "9 de noviembre y, por uso, 4 de diciembre",
        ],
    )

    p_c04 = find_para(doc, startswith="C-04 no afirma")
    p_c05 = insert_paragraph_after(
        p_c04,
        "C-05 se rotula como ejemplo de solicitud porque concreta el tipo de cambio de productividad "
        "con IA que el piloto puede recibir. No es un copiloto ya construido. Lo que amerita registro "
        "es la ampliación de superficie de producto y el costo variable de una API de modelo. La "
        "medida factible, si cabe, es solo la fase 1 de soporte.",
    )
    insert_paragraph_after(
        p_c05,
        "C-06 no es lo mismo que C-01b. C-01b agrega el dato de prioridad y la nota en el modelo del "
        "ticket. C-06 es la cola o el filtro en la interfaz para que el técnico vea el orden sin "
        "pedir por WhatsApp qué kit mirar primero. Sin C-01b (o sin un dato equivalente), la cola "
        "visual no tiene criterio; sin C-06, el dato de prioridad queda escondido en el formulario.",
    )

    p_12 = find_para(doc, contains="No se registra como cambio una consulta")
    # Ampliar §1.2
    full = p_12.text
    add = (
        " Explorar «IA generativa en producción» o un datalake corporativo sin registro no entra. "
        "Un ranking automático sin aprobación, o un lago de datos con pipelines y BI dedicado, es "
        "solicitud nueva y se trata como C-05 o como solicitud futura rechazada en esta ventana, no "
        "como ajuste de una historia ya comprometida."
    )
    if "datalake corporativo" not in full:
        if p_12.runs:
            p_12.runs[0].text = full + add
            for r in p_12.runs[1:]:
                r.text = ""
        else:
            p_12.text = full + add

    # --- §2 evaluación intro ---
    p_eval = find_para(doc, contains="Cada cambio se examina en cronograma, alcance, costo y calidad")
    full = p_eval.text
    add = (
        " Para C-05 y C-06 el examen incluye también esfuerzo del sprint, rendimiento del piloto y "
        "del equipo, recursos de infraestructura e indicadores estratégicos (E) y operativos (O)."
    )
    if "indicadores estratégicos" not in full:
        if p_eval.runs:
            p_eval.runs[0].text = full + add
            for r in p_eval.runs[1:]:
                r.text = ""

    # Renumerar 2.5 / 2.6 y agregar secciones C-05 / C-06
    p_25 = find_para(doc, startswith="2.5. Efecto conjunto")
    p_26 = find_para(doc, startswith="2.6. Riesgos y mitigación")
    if p_25.runs:
        p_25.runs[0].text = "2.7. Efecto conjunto"
        for r in p_25.runs[1:]:
            r.text = ""
    else:
        p_25.text = "2.7. Efecto conjunto"
    if p_26.runs:
        p_26.runs[0].text = "2.8. Riesgos y mitigación"
        for r in p_26.runs[1:]:
            r.text = ""
    else:
        p_26.text = "2.8. Riesgos y mitigación"

    p_24_body = find_para(doc, contains="El efecto positivo de tratarlo como cambio")
    # Insertar 2.5 y 2.6 antes de 2.7
    # Encontrar párrafo justo antes de 2.7 (el cuerpo de C-04)
    anchor = p_25
    # Insertar en orden inverso antes de 2.7
    bodies = [
        (
            "2.5. C-05. Asistente de IA de uso interno",
            "En los términos pedidos (copiloto para tickets, reportes y decisiones), el cambio toca "
            "integración, costo variable de API, privacidad y calidad de las sugerencias. Nicolás "
            "sostiene la integración. Skarlett valida la calidad de lo sugerido. Ari registra el "
            "tope de gasto. Giannina sostiene el control de cambios. Un modelo propio, un fine-tuning "
            "o un datalake para entrenar no están en el plan.",
            "El efecto positivo acotado es aliviar al técnico a 0,4 FTE: menos tiempo para entender un "
            "ticket y elegir el siguiente, si la sugerencia se usa y se corrige. El efecto negativo "
            "de la formulación completa es ampliar el alcance, abrir gasto no comprometido y "
            "priorizar mal por una alucinación. La fase 1 no cambia el estado del kit ni redacta el "
            "reporte a donantes. Indicadores amenazados: E1, E4 y E5. Operativos a monitorear: O1, "
            "O4 y O6, con submetricas de adopción y rechazo de sugerencias.",
        ),
        (
            "2.6. C-06. Priorización visual en la interfaz",
            "El cambio toca la interfaz del tablero y, si hace falta, filtros en el backend. "
            "Giannina sostiene la UI. No abre estados nuevos del kit. No es una app ciudadana.",
            "El efecto positivo es bajar el costo de soporte informal. El efecto negativo es "
            "presión de esfuerzo hacia el 9 de noviembre y más líneas cambiadas antes del 4 de "
            "diciembre, con riesgo sobre O1 y, si persiste, sobre E1. El orden de adopción es "
            "C-06 antes que la IA fase 1: la IA no adelanta a un tablero que el soporte aún no usa.",
        ),
    ]
    # Insert before p_25 by inserting after p_24_body then titles
    cursor = p_24_body
    for title, p1, p2 in bodies:
        cursor = insert_paragraph_after(cursor, title)
        cursor = insert_paragraph_after(cursor, p1)
        cursor = insert_paragraph_after(cursor, p2)

    # Ampliar efecto conjunto
    p_conj = find_para(doc, contains="Aceptar a la vez la fotografía de C-01")
    full = p_conj.text
    add = (
        " Aceptar además un datalake completo y un copiloto de IA «todo en uno» no son mejoras "
        "independientes: caen sobre el mismo techo, el mismo equipo y los mismos cortes. Un "
        "datalake o lakehouse (ingesta, catálogo, ETL, BI dedicado) queda fuera del 100 % de la "
        "EDT del piloto: se rechaza o se difiere post cierre. La línea base de datos sigue siendo "
        "la base del aplicativo más el export para el reporte del 4 de diciembre. Un depósito "
        "mínimo de logs agregados sin PII, si alguien lo pide, solo cabe condicionado y dentro "
        "del hosting variable, sin competir con C-06. C-05 fase 1 y C-06 solo entran si reemplazan "
        "historia y respetan dos tarjetas por persona. Hay que evitar acumular superficie de "
        "producto sin capacidad de integración y prueba."
    )
    if "datalake o lakehouse" not in full:
        if p_conj.runs:
            p_conj.runs[0].text = full + add
            for r in p_conj.runs[1:]:
                r.text = ""

    # --- Tabla 3 ---
    fill_row(
        clone_row(t3),
        [
            "C-05 completo (copiloto / datalake / modelo propio)",
            "Alto. Abre plataforma de datos o IA fuera de la EDT.",
            "Gasto variable y posible contingencia. Rompe E4 si supera el 10 % de desviación.",
            "Rompe o desplaza el 4 de diciembre.",
            "No",
        ],
    )
    fill_row(
        clone_row(t3),
        [
            "C-05 fase 1 (soporte)",
            "Medio. Integra API y prompts acotados; el humano confirma.",
            "Horas replanificadas más sobre API dentro del costo variable. Contingencia cerrada salvo razón escrita.",
            "Post 9 de noviembre; no en la semana del 5 al 9 de diciembre.",
            "Condicionado a C-06 o C-01b, cupo de sprint y tope de API.",
        ],
    )
    fill_row(
        clone_row(t3),
        [
            "C-06",
            "Medio. UX de cola o filtros; reutiliza la prioridad de C-01b.",
            "Casi sin infraestructura extra; esfuerzo de UI y backend del techo.",
            "Presión hacia el 9 de noviembre.",
            "Condicionado a reemplazo de historia y al límite de dos tarjetas.",
        ],
    )

    # --- Tabla 4 ---
    for vals in [
        [
            "La IA amplía el alcance sin control.",
            "Se construye un copiloto, auto-estados o un reporte a donantes sin fila nueva.",
            "Solo fase 1 asistida. Un salto de fase es solicitud nueva. El análisis de impacto lo "
            "revisa un rol senior (Ari o Nicolás), no un junior en planificación ni en control de cambios.",
        ],
        [
            "El costo de API o un datalake come el techo.",
            "Se contrata un lago completo o se abre la contingencia sin acta.",
            "El datalake completo se rechaza o se difiere. Ari pone tope de API en Excel. Si la "
            "desviación supera el 10 %, se pausa la IA antes que el corte.",
        ],
        [
            "La cola visual se confunde con los estados del kit.",
            "C-06 cambia la semántica de activo, en falla o dado de baja.",
            "C-06 solo ordena y filtra. Los estados siguen en el modelo del inventario.",
        ],
        [
            "Se acumula superficie sin integración.",
            "Entran C-05 y C-06 junto a la fotografía, el segundo punto y el servicio externo.",
            "Un cambio constructivo a la vez, además de C-04. Si entra IA o cola, sale otra historia. "
            "Mentoría docente de una hora por sprint si el cambio es ambiguo.",
        ],
    ]:
        fill_row(clone_row(t4), vals)

    # --- §3.1 soluciones ---
    p_c04_sol = find_para(doc, startswith="C-04 se aprueba como regla")
    p = insert_paragraph_after(
        p_c04_sol,
        "C-05 se aprueba solo por fases. La fase 1 (soporte) queda condicionada a que C-06 y, si "
        "aplica, C-01b estén en marcha o en el mismo plan de sprint, a que quepa en dos tarjetas "
        "por persona y a un tope de llamadas API en Excel. La fase 2 (borradores internos de cierre) "
        "solo post 4 de diciembre o con un control de cambios nuevo. La fase 3 (copiloto amplio, "
        "priorización automática, IA a hogares o donantes, modelo propio) se rechaza entre "
        "septiembre y diciembre de 2026. No se aprueba un copiloto único «todo en uno».",
    )
    insert_paragraph_after(
        p,
        "C-06 se aprueba en forma condicionada: vistas de cola o filtro en el tablero hacia el 9 de "
        "noviembre, sin aprendizaje automático, midiendo menos consultas informales. Es prerrequisito "
        "de la IA fase 1. Si no cabe en el límite de trabajo en curso, no entra.",
    )

    # --- Tabla 5 priorización ---
    fill_row(
        clone_row(t5),
        [
            "C-06, cola visual",
            "Sí, si baja la carga del soporte sin abrir una app ciudadana.",
            "Sí hacia el 9 de noviembre.",
            "Planificar dentro de ese corte.",
            "Antes que C-05. Condicionada al reemplazo de una historia.",
        ],
    )
    fill_row(
        clone_row(t5),
        [
            "C-05 fase 1",
            "Sí para el soporte, no antes que la cola.",
            "No antes del tablero usable.",
            "Planificar después del 9 de noviembre.",
            "Después de C-06. Condicionada al cupo y al tope de API.",
        ],
    )
    fill_row(
        clone_row(t5),
        [
            "C-05 fases 2–3 / datalake completo",
            "No en esta ventana.",
            "No.",
            "Sacar del camino o planificar sin fecha de construcción.",
            "Rechazado o diferido. Sin pasos en sep–dic 2026.",
        ],
    )

    # --- Tabla 6 decisión ---
    fill_row(
        clone_row(t6),
        [
            "C-05 fase 1",
            "Aprobada condicionada a C-06 o C-01b, al límite de dos tarjetas y al tope de API. Las fases 2 y 3 no.",
            "Apoya los tickets sin abrir un producto nuevo ni un reporte automático a donantes.",
            "Abierto, condicionado",
            "Sí, a la dirección, si proponen mover el 4 de diciembre o abrir la contingencia por API.",
        ],
    )
    fill_row(
        clone_row(t6),
        [
            "C-05 completo / datalake",
            "No se aprueba en esta ventana. Se cierra esa formulación.",
            "El piloto usa la base del aplicativo y el export; no un segundo producto de datos.",
            "Cerrado",
            "Sí, a la dirección, si se insiste en un lago o en un modelo propio.",
        ],
    )
    fill_row(
        clone_row(t6),
        [
            "C-06",
            "Aprobada condicionada al reemplazo de una historia y al límite de dos tarjetas.",
            "Hace usable la prioridad sin depender de consultas fuera del sistema.",
            "Abierto",
            "Sí, a la dirección, si alguien propone cambiar los estados del kit o mover el 9 de noviembre.",
        ],
    )

    # --- Tabla 7 efecto alcance ---
    fill_row(
        clone_row(t7),
        [
            "C-06, medida condicionada",
            "El tablero agrega cola o filtros. No agrega estados nuevos del kit. Esfuerzo orientativo: tres a cinco días-persona de interfaz y uno a dos de backend.",
            "La fecha del 9 de noviembre no se mueve. Si el desvío en ruta crítica supera tres días, se replanifica antes de seguir construyendo.",
            "La tarjeta entra a Comprometido solo después de sacar la historia que reemplaza. Máximo dos tarjetas por persona.",
            "Sin partida de infraestructura nueva. El costo es tiempo del equipo ya en el techo.",
        ],
    )
    fill_row(
        clone_row(t7),
        [
            "C-05 fase 1, condicionada",
            "Se agrega integración de API, prompts acotados y registros de uso internos. Esfuerzo orientativo: cuatro a seis días-persona de integración y dos a tres de calidad.",
            "Las tareas quedan bajo el paquete de tickets. La predecesora es el tablero usable. No se construye en la semana del 5 al 9 de diciembre.",
            "Misma regla de reemplazo de historia. No se suma a C-06 en la misma persona sin sacar trabajo.",
            "Ari registra un subítem de sobre API de IA dentro del costo variable. Tope mensual escrito. Contingencia del 12 % cerrada. Desviación sobre el 10 %: se pausa la IA.",
        ],
    )
    fill_row(
        clone_row(t7),
        [
            "C-05 amplio / datalake, cerrado",
            "El alcance del piloto no cambia.",
            "No se inserta en el cronograma de esta ventana.",
            "Sin tarjeta de construcción.",
            "Sin gasto. Queda cerrado o como solicitud post-piloto.",
        ],
    )

    # --- Tabla 8 pasos ---
    for vals in [
        [
            "Confirmar si C-06 cabe: historia equivalente que sale del sprint hacia el tablero; construir cola o filtros sin cambiar los estados del kit.",
            "Giannina Guerrero en la interfaz; Nicolás Barra si hace falta filtro de datos",
            "Al armar el compromiso del sprint que alimenta el 9 de noviembre de 2026.",
        ],
        [
            "Tras el tablero usable, decidir si entra C-05 fase 1: cupo de dos tarjetas, tope de API de Ari y revisión con el soporte.",
            "Giannina Guerrero (control de cambios); Nicolás Barra (integración); Skarlett Tropan (calidad de sugerencias); Ari Araya (gasto)",
            "Ventana de noviembre a diciembre de 2026. No en la semana del 5 al 9 de diciembre.",
        ],
        [
            "Medir, bajo el indicador O6, el porcentaje de tickets con resumen o checklist usado y el porcentaje de sugerencias rechazadas. Si el rechazo es alto, congelar la fase 2.",
            "Skarlett Tropan; Nicolás Barra",
            "Al cierre del sprint que use la fase 1.",
        ],
        [
            "No abrir la fase 2 de IA ni un datalake completo sin un control de cambios nuevo y revisión de un rol senior.",
            "Giannina Guerrero, dirección",
            "Después del 4 de diciembre de 2026, o fuera de esta ventana.",
        ],
    ]:
        fill_row(clone_row(t8), vals)

    # --- Tabla 9 cortes ---
    # Actualizar filas tablero y tickets
    set_cell_text(
        t9.rows[2].cells[3],
        "Puede entrar C-06 (cola o filtros), solo a cambio de otra historia. No entra un datalake. "
        "No entra C-05 fase 1 antes del tablero usable.",
    )
    set_cell_text(
        t9.rows[3].cells[3],
        "Puede entrar la prioridad y la nota, y C-05 fase 1 si cumplió condiciones, solo a cambio "
        "de otra historia. No entra el archivo. No entra un servicio externo. No entra la fase 2 "
        "de IA ni un datalake.",
    )

    # --- Tabla 10 registro ---
    fill_row(
        clone_row(t10),
        [
            "C-05a",
            "Requisito. Copiloto de IA amplio o datalake completo.",
            "Giannina Guerrero",
            "—",
            "Cerrado",
            "No aprobado entre septiembre y diciembre de 2026. Queda fuera de la EDT y del techo. "
            "Escalamiento a la dirección si se insiste.",
        ],
    )
    fill_row(
        clone_row(t10),
        [
            "C-05b",
            "Requisito. IA fase 1 de soporte: resumen, checklist y siguiente ticket en cola.",
            "Nicolás Barra",
            "Alta",
            "Abierto",
            "Aprobado solo si C-06 o C-01b están en marcha, cabe en dos tarjetas y existe tope de "
            "API. Sin datos de hogares en un modelo externo. Escalamiento si proponen mover el 4 de diciembre.",
        ],
    )
    fill_row(
        clone_row(t10),
        [
            "C-06",
            "Requisito. Priorización visual: cola o filtros en el tablero.",
            "Giannina Guerrero",
            "Alta",
            "Abierto",
            "Aprobado solo si reemplaza una historia equivalente y no mueve el 9 de noviembre. No "
            "cambia los estados del kit. Es prerrequisito de C-05b.",
        ],
    )

    # --- §4.4 monitoreo ---
    p_def = find_para(doc, contains="El indicador de defectos es la cantidad")
    full = p_def.text
    add = (
        " Ese indicador es O1 dentro del bloque operativo. Sin código, la celda «sin base» no es "
        "alerta roja."
    )
    if "bloque operativo" not in full:
        if p_def.runs:
            p_def.runs[0].text = full.rstrip() + add
            for r in p_def.runs[1:]:
                r.text = ""

    p_reap = find_para(doc, contains="La tasa de reapertura es lo reabierto")
    full = p_reap.text
    add = (
        " Ese indicador es O2. No se mezcla con la reapertura de tickets ya en uso en terreno: eso "
        "se anota en bitácora de soporte y puede alimentar O6 o E3, no duplica O2."
    )
    if "No se mezcla" not in full:
        if p_reap.runs:
            p_reap.runs[0].text = full.rstrip() + add
            for r in p_reap.runs[1:]:
                r.text = ""

    p_ari = find_para(doc, contains="Ari registra el gasto cada dos semanas")
    full = p_ari.text
    add = (
        " El seguimiento de techo corresponde al indicador estratégico E4. El sobre de API de IA, "
        "si C-05b entra, se registra como subítem del costo variable; si la desviación supera el "
        "10 %, se detiene ese gasto antes que otras funciones del corte."
    )
    if "indicador estratégico E4" not in full:
        if p_ari.runs:
            p_ari.runs[0].text = full.rstrip() + add
            for r in p_ari.runs[1:]:
                r.text = ""

    p_control = find_para(doc, contains="El control vuelve al procedimiento")
    # Insertar bloques KPI antes del control
    cursor = find_para(doc, contains="En cada corte la contraparte deja un puntaje")
    cursor = insert_paragraph_after(
        cursor,
        "El monitoreo de C-05 y C-06 usa dos capas. Los cinco indicadores estratégicos del proyecto "
        "se leen por corte y por la dirección. Los siete indicadores operativos se leen cada semana "
        "o cada dos semanas. Los operativos alimentan a los estratégicos y disparan alerta antes de "
        "romper un corte.",
    )
    cursor = insert_paragraph_after(cursor, "Indicadores estratégicos del proyecto")
    # Reutilizar estilo de tabla 3 (riesgos) o crear tabla clonando estructura de t10 (2 cols) no basta.
    # Crear tabla 7 columnas clonando filas de una tabla existente con más columnas: usar t10 (6 cols) no.
    # Mejor: insertar tabla nueva copiando tbl de t2 (4 cols) no alcanza.
    # Usaremos t3 (5 cols) como plantilla visual y añadiremos columnas? Complejo.
    # Alternativa alineada al doc: párrafos con lista numerada estilo bullet del §4.4.

    estrategicos = [
        "E1. Cumplimiento de cortes: porcentaje de los cuatro cortes entregados con el criterio del "
        "acta. Meta: los cuatro, o causa escrita si el atraso no supera tres días. Fuente: Project "
        "Libre y acta. Dueña: Giannina. Si se rompe: control de cambios; la semana siguiente no suma "
        "trabajo nuevo si el atraso supera tres días.",
        "E2. Integridad plan–ejecución: porcentaje de actividades de ruta crítica sin desvío no "
        "registrado. Meta: 100 % en los hitos revisados. Dueños: Giannina y Nicolás. Si se rompe: "
        "replanificar; no alcanza un parche solo en Trello.",
        "E3. Alcance verificable: porcentaje de paquetes de la EDT del piloto con evidencia de "
        "aceptación al cierre de su corte. Dueño: el de cada paquete. Si se rompe: no declarar el "
        "corte cerrado; reabrir si el puntaje queda bajo 4.",
        "E4. Techo y gasto comprometido: desviación acumulada frente a US$ 20.700. Freno si supera "
        "el 10 %. Dueño: Ari. Si se rompe: detener gasto no comprometido, incluida la API de IA.",
        "E5. Cambios bajo control: porcentaje de cambios aprobados con alcance, Project Libre y "
        "Trello actualizados antes de construir, y cero cambios en producción sin fila en la Tabla "
        "10. Meta: 100 % en cambios constructivos. Dueña: Giannina. Si se rompe: detener la "
        "construcción y volver al procedimiento.",
    ]
    for line in estrategicos:
        cursor = insert_paragraph_after(cursor, line)

    cursor = insert_paragraph_after(cursor, "Indicadores operativos")
    operativos = [
        "O1. Defectos por líneas cambiadas: defectos del período sobre líneas cambiadas. Meta: 5 o "
        "menos y cero bloqueos abiertos. Sin código: «sin base», no alerta roja. Dueños: Skarlett y Nicolás.",
        "O2. Tasa de reapertura de desarrollo: reabierto sobre cerrado. Meta: bajo el 20 %. Dueña: "
        "Skarlett. No confundir con tickets operativos reabiertos en terreno.",
        "O3. Cumplimiento del sprint: porcentaje de historias comprometidas completadas, sobre la "
        "lista ya reemplazada si hubo control de cambios. Meta: 80 % o más. Dueña: Giannina.",
        "O4. Trabajo en curso y bloqueos: máximo dos tarjetas por persona; un bloqueo de más de "
        "cinco días dispara C-04. Dueña: Giannina.",
        "O5. Kits con estado verificable: porcentaje de kits del piloto con hogar, responsable y "
        "estado coherente al cierre del corte. Alineado al indicador primario del producto. Dueño: "
        "quien sostiene el inventario.",
        "O6. Atención de fallas: tiempo medio desde kit en falla hasta ticket asignado, tiempo para "
        "elegir el siguiente ticket y porcentaje de consultas fuera del tablero. Meta: mejorar "
        "después del 9 de noviembre. Submetricas de C-05: porcentaje de tickets con resumen o "
        "checklist usado y porcentaje de sugerencias rechazadas; rechazo alto congela la fase 2. "
        "Dueños: Giannina y el soporte; en IA, Nicolás y Skarlett.",
        "O7. Coordinación y datos en terreno: puntaje de la contraparte de 1 a 5 (meta 4 o más) y "
        "porcentaje de sincronizaciones de inventario por lote en la ventana planificada. Dueños: "
        "Giannina y Ari.",
    ]
    for line in operativos:
        cursor = insert_paragraph_after(cursor, line)

    insert_paragraph_after(
        cursor,
        "Los operativos O1 a O4 sostienen ritmo y calidad del equipo. O5 a O7 miden si el piloto "
        "opera con datos creíbles y soporte atendible. E1 a E3 consolidan eso en cortes y EDT; E4 "
        "y E5 en techo y control de cambios.",
    )

    # --- Tabla 11 ---
    set_cell_text(
        t11.rows[1].cells[1],
        "La prioridad y la nota de texto en el ticket, y solo si reemplazan una historia "
        "equivalente sin mover el 4 de diciembre. La regla de reasignación cuando un bloqueo "
        "supera cinco días. La priorización visual del tablero (C-06) y la IA fase 1 de soporte "
        "(C-05b), ambas condicionadas al reemplazo de historia, al límite de dos tarjetas y, en "
        "IA, al tope de API y al prerrequisito de cola.",
    )
    set_cell_text(
        t11.rows[2].cells[1],
        "La fotografía del ticket, el segundo punto de inventario dentro de esta ventana, el "
        "servicio externo del reporte, el copiloto de IA amplio, el datalake o lakehouse completo, "
        "el modelo propio y las fases 2 y 3 de IA en esta ventana.",
    )
    set_cell_text(
        t11.rows[3].cells[1],
        "Kiran no instala paneles. Ninguna solicitud de este plan modifica ese límite. Tampoco "
        "abre una app ciudadana ni una plataforma analítica aparte del piloto.",
    )

    # Cierre registro: mencionar seis ids
    p_cierre = find_para(doc, contains="Proyecto: Kiran. Organización")
    full = p_cierre.text
    if "C-05" not in full:
        # append short note
        add = (
            " Registro ampliado con C-05a (cerrado), C-05b (abierto condicionado) y C-06 (abierto "
            "condicionado)."
        )
        if p_cierre.runs:
            p_cierre.runs[0].text = full.rstrip() + add
            for r in p_cierre.runs[1:]:
                r.text = ""

    # Actualizar texto decisión abierto/cerrado
    p_dec = find_para(doc, contains="Aprobar no es lo mismo que dejar el registro en curso")
    full = p_dec.text
    add = (
        " C-05a y la formulación amplia de datalake quedan cerradas. C-05b y C-06 quedan abiertas "
        "y condicionadas."
    )
    if "C-05b" not in full:
        if p_dec.runs:
            p_dec.runs[0].text = full.rstrip() + add
            for r in p_dec.runs[1:]:
                r.text = ""

    doc.save(str(DOCX))
    print("OK", DOCX)


if __name__ == "__main__":
    main()
