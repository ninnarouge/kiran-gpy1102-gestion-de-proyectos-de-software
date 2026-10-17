# -*- coding: utf-8 -*-
"""Agrega desglose presupuestario C-05/C-06 al Word v2 (formato del doc)."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "2.2.2-Gestion-de-cambios-Kiran v2.docx"


def set_cell_text(cell, text: str) -> None:
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
    for p in cell.paragraphs[1:]:
        p._element.getparent().remove(p._element)


def insert_paragraph_after(paragraph: Paragraph, text: str) -> Paragraph:
    new_p = deepcopy(paragraph._p)
    for child in list(new_p):
        if child.tag == qn("w:r"):
            new_p.remove(child)
    paragraph._p.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
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


def find_para(doc: Document, contains: str = None, startswith: str = None):
    for p in doc.paragraphs:
        t = p.text or ""
        if startswith is not None and t.startswith(startswith):
            return p
        if contains is not None and contains in t:
            return p
    raise KeyError(contains or startswith)


def clone_table_after_paragraph(paragraph: Paragraph, template: Table) -> Table:
    new_tbl = deepcopy(template._tbl)
    paragraph._p.addnext(new_tbl)
    return Table(new_tbl, paragraph._parent)


def clear_extra_rows(table: Table, keep: int) -> None:
    while len(table.rows) > keep:
        tr = table.rows[-1]._tr
        tr.getparent().remove(tr)


def ensure_rows(table: Table, n: int) -> None:
    while len(table.rows) < n:
        tr = deepcopy(table.rows[-1]._tr)
        table._tbl.append(tr)


def main() -> None:
    if not DOCX.exists():
        raise SystemExit(f"No está el archivo: {DOCX}")

    doc = Document(str(DOCX))
    # Evitar duplicar si ya se insertó
    if any("banda de US$ 120 a US$ 220" in (p.text or "") for p in doc.paragraphs):
        print("Ya existe el bloque de presupuesto; no se duplica.")
        return

    # Ancla: caption Tabla 7 o párrafo 4.2
    try:
        caption = find_para(doc, contains="Tabla 7.")
    except KeyError:
        caption = find_para(doc, startswith="4.2.")

    # Si el caption es "Tabla 7...", insertar después; si es 4.2, insertar antes de 4.2
    if (caption.text or "").startswith("4.2"):
        # Insertar antes: usar párrafo previo (último de 4.1)
        # Buscar "Tabla 7" en paragraphs anteriores
        caption = find_para(doc, contains="Tabla 7")

    p = insert_paragraph_after(
        caption,
        "4.1.1. Estimación de costo de C-05b y C-06 (transparencia)",
    )
    p = insert_paragraph_after(
        p,
        "Para que C-05b y C-06 sean transparentes y creíbles, el equipo estima el costo "
        "incremental de caja de la fase 1 (chatbot de FAQ y canal de asistencia) en una "
        "banda de US$ 120 a US$ 220 dentro del costo variable ya asociado al piloto: API de "
        "un modelo gestionado de gama baja (tipo mini o haiku, según precios públicos "
        "revisados en octubre de 2026) más un margen de hosting y registros. El tope duro "
        "de API en Excel es US$ 120; si la desviación acumulada de nube y API supera el "
        "10 %, se pausa el chatbot (indicador E4). Ese monto no sube el techo de US$ 20.700 "
        "ni abre la contingencia del 12 %. El esfuerzo de construcción, del orden de 13 a "
        "22 días-persona sumando C-06 y C-05b, se cubre con el equipo de cuatro mediante "
        "reemplazo de historias. No se contrata en esta ventana un especialista externo en "
        "desarrollo agéntico, ni fine-tuning, ni GPU, ni IA de monitoreo de flota: eso queda "
        "como fase posterior identificada y exigiría un control de cambios con presupuesto "
        "nuevo. Las cifras son orden de magnitud con supuestos de tráfico de piloto (una "
        "comunidad, usuarios de la plataforma); no son una cotización adjudicada.",
    )

    # Clonar estructura de Tabla 7 (5 columnas) o Tabla 3 (5 cols) — usar tables[6]
    template = doc.tables[6]
    # Insertar tabla después del párrafo p
    new_table = clone_table_after_paragraph(p, template)
    clear_extra_rows(new_table, 1)
    ensure_rows(new_table, 6)
    headers = [
        "Rubro",
        "Tipo de costo",
        "US$ propuesto",
        "US$ máximo",
        "Supuesto / control",
    ]
    rows = [
        headers,
        [
            "API chatbot (modelo mini/haiku gestionado)",
            "Variable y directo",
            "60",
            "120",
            "Precios públicos de API; tráfico bajo-medio del piloto. Ari registra tope en Excel.",
        ],
        [
            "Margen hosting y registros del chat",
            "Variable y directo",
            "60",
            "100",
            "Sobre el hosting ya planificado del piloto (~US$ 480 / tres meses).",
        ],
        [
            "HH equipo (C-05b + C-06)",
            "Directo ya en el techo",
            "0 (caja)",
            "13 a 22 días-persona",
            "Replanificación: si entra el cambio, sale una historia. Sin persona nueva.",
        ],
        [
            "Especialista agéntico / fine-tuning / GPU / monitoreo IA",
            "Fuera de esta ventana",
            "0",
            "0",
            "Identificado a futuro. No se aprueba en sep–dic 2026.",
        ],
        [
            "Total caja nueva de C-05b",
            "Variable dentro del techo",
            "120",
            "220",
            "Contingencia del 12 % cerrada. No se redefine el techo de US$ 20.700.",
        ],
    ]
    for i, vals in enumerate(rows):
        for cell, val in zip(new_table.rows[i].cells, vals):
            set_cell_text(cell, val)

    # Caption después de la tabla: insertar párrafo tras el elemento tabla
    # Encontrar el párrafo que quedó justo antes y añadir caption después de la tabla
    # Buscamos el último párrafo insertado (p) — la tabla está after p; necesitamos caption after table
    # Truco: insertar caption after p, then move table before caption... más simple: caption as next after finding table in body

    # Añadir caption: clonar p y ponerlo después de la tabla
    caption_p = deepcopy(p._p)
    for child in list(caption_p):
        if child.tag == qn("w:r"):
            caption_p.remove(child)
    new_table._tbl.addnext(caption_p)
    cap = Paragraph(caption_p, p._parent)
    if p.runs:
        run = cap.add_run(
            "Tabla 7b. Estimación de costo incremental de C-05b y C-06 (orden de magnitud; "
            "no cotización adjudicada)."
        )
        src = p.runs[0]
        run.bold = src.bold
        if src.font.size:
            run.font.size = src.font.size
        if src.font.name:
            run.font.name = src.font.name
    else:
        cap.add_run(
            "Tabla 7b. Estimación de costo incremental de C-05b y C-06 (orden de magnitud; "
            "no cotización adjudicada)."
        )

    # Actualizar fila Excel de C-05 en Tabla 7 original
    t7 = doc.tables[6]
    for row in t7.rows:
        if (row.cells[0].text or "").startswith("C-05 fase 1") or (
            row.cells[0].text or ""
        ).startswith("C-05 fase 1, chatbot"):
            set_cell_text(
                row.cells[4],
                "Ari registra subítems API chatbot (tope US$ 120) y margen hosting (hasta US$ 100). "
                "Banda total US$ 120–220 dentro del variable. Contingencia del 12 % cerrada. "
                "Desviación sobre el 10 %: se pausa el chatbot. El ahorro esperado es de horas "
                "de soporte contratado, no un segundo techo. Detalle en Tabla 7b.",
            )

    # Actualizar E4 prose if mentions API IA
    for para in doc.paragraphs:
        t = para.text or ""
        if "sobre API del chatbot" in t and "US$ 120" not in t:
            # leave
            pass

    doc.save(str(DOCX))
    print("OK", DOCX)


if __name__ == "__main__":
    main()
