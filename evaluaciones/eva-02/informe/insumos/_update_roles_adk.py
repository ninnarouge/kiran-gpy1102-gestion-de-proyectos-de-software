# -*- coding: utf-8 -*-
"""Asigna a Nicolás y Ari el desarrollo agéntico (GCloud + ADK)."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

DOCX = Path(__file__).resolve().parents[1] / "2.2.2-Gestion-de-cambios-Kiran v2.docx"


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


def set_para(p: Paragraph, text: str) -> None:
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.text = text


def find_para(doc: Document, contains: str = None, startswith: str = None):
    for p in doc.paragraphs:
        t = p.text or ""
        if startswith is not None and t.startswith(startswith):
            return p
        if contains is not None and contains in t:
            return p
    raise KeyError(contains or startswith)


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


def main() -> None:
    doc = Document(str(DOCX))

    # §2.5 C-05 — roles en cuerpo
    try:
        p = find_para(doc, startswith="En los términos pedidos (chatbot para usuarios")
        t = p.text or ""
        if "ADK" not in t:
            set_para(
                p,
                "En los términos pedidos (chatbot para usuarios con FAQ y comunicación de "
                "soporte, para ahorrar contrato de personal), el cambio toca la interfaz de la "
                "plataforma, la claridad de la experiencia de uso, la integración con Gemini en "
                "Google Cloud, la privacidad, la calidad de las respuestas y el flujo hacia el "
                "ticket. Giannina sostiene la interfaz del chat y la UI/UX asociada. Skarlett "
                "valida la calidad de las respuestas y el FAQ. Nicolás Barra y Ari Araya quedan "
                "encargados de lo que requiera desarrollo agéntico de esta solución: manejo de "
                "Google Cloud y del Agent Development Kit (ADK) de Google, integración del "
                "modelo y controles de cuota/gasto. Un modelo propio, un fine-tuning fuera de "
                "ese stack, un datalake, una app para cada hogar o un módulo de monitoreo y "
                "alertas con IA sobre todos los equipos no están en el plan de esta ventana "
                "(quedan como fase posterior, con los mismos dueños técnicos si se aprueba).",
            )
    except KeyError:
        # Intentar párrafo más corto actual
        try:
            p = find_para(doc, contains="chatbot para usuarios con FAQ")
            if "ADK" not in (p.text or ""):
                set_para(
                    p,
                    (p.text or "").rstrip()
                    + " Nicolás Barra y Ari Araya quedan encargados de lo que requiera "
                    "desarrollo agéntico: Google Cloud y Agent Development Kit (ADK).",
                )
        except KeyError:
            pass

    # §3.1 C-05 — agregar dueños ADK
    try:
        p = find_para(doc, startswith="C-05 se aprueba solo por fases")
        t = p.text or ""
        if "ADK" not in t:
            set_para(
                p,
                t.rstrip()
                + " En todo lo agéntico de esta solución (fase 1 y, si más adelante se aprueba, "
                "fases posteriores), los responsables técnicos son Nicolás Barra y Ari Araya, "
                "con Google Cloud y ADK; no se incorpora un especialista externo en esta ventana.",
            )
    except KeyError:
        pass

    # Tabla 8 — pasos: actualizar fila C-05 / agregar paso ADK
    for table in doc.tables:
        if (table.rows[0].cells[0].text or "") != "Paso":
            continue
        updated = False
        for row in table.rows:
            p0 = row.cells[0].text or ""
            if "C-05 fase 1" in p0 or "chatbot FAQ" in p0:
                set_cell_text(
                    row.cells[1],
                    "Giannina Guerrero (control de cambios e interfaz del chat); "
                    "Nicolás Barra y Ari Araya (Google Cloud, ADK y desarrollo agéntico / "
                    "integración Gemini); Skarlett Tropan (calidad del FAQ y respuestas); "
                    "Ari Araya (gasto y topes en Excel)",
                )
                updated = True
        # Añadir paso explícito si no existe
        if not any("ADK" in (r.cells[0].text or "") for r in table.rows):
            tr = deepcopy(table.rows[-1]._tr)
            table._tbl.append(tr)
            set_cell_text(
                table.rows[-1].cells[0],
                "Definir y mantener en Google Cloud el entorno del chatbot y, cuando el "
                "alcance lo exija, los componentes agénticos con Agent Development Kit (ADK): "
                "cuotas, secretos, logs y límites de gasto Gemini.",
            )
            set_cell_text(
                table.rows[-1].cells[1],
                "Nicolás Barra y Ari Araya (co-responsables técnicos de GCloud y ADK)",
            )
            set_cell_text(
                table.rows[-1].cells[2],
                "Al activar C-05b (tras decisión de financiamiento) y en cada revisión "
                "quincenal de gasto mientras el chat esté en uso.",
            )
        break

    # Tabla 7 CAPEX — fila integración
    for table in doc.tables:
        blob = " ".join(c.text for r in table.rows for c in r.cells)
        if "CAPEX" not in blob and "puesta en marcha" not in blob:
            continue
        for row in table.rows:
            c0 = row.cells[0].text or ""
            if "Integración Gemini" in c0 or "despliegue inicial" in c0:
                set_cell_text(
                    row.cells[4],
                    "Nicolás Barra y Ari Araya (GCloud + ADK)",
                )
            if "API Gemini" in c0:
                set_cell_text(row.cells[4], "Ari (gasto); Nicolás/Ari (ADK/uso)")
        break

    # Tabla 10 C-05b — propietario
    for table in doc.tables:
        if len(table.columns) < 6:
            continue
        if (table.rows[0].cells[0].text or "") != "Id.":
            continue
        for row in table.rows:
            if (row.cells[0].text or "").startswith("C-05b"):
                # Propietario: puede ser celda 2
                set_cell_text(
                    row.cells[2],
                    "Nicolás Barra y Ari Araya (GCloud/ADK); Giannina (CC)",
                )
                just = row.cells[5].text or ""
                if "ADK" not in just:
                    set_cell_text(
                        row.cells[5],
                        just.rstrip()
                        + " Desarrollo agéntico de la solución a cargo de Nicolás y Ari "
                        "(Google Cloud y ADK); sin especialista externo en esta ventana.",
                    )
            if (row.cells[0].text or "").startswith("C-05a"):
                just = row.cells[5].text or ""
                if "ADK" not in just:
                    set_cell_text(
                        row.cells[5],
                        just.rstrip()
                        + " Si en el futuro se reabre, el desarrollo agéntico sigue a cargo "
                        "de Nicolás Barra y Ari Araya (GCloud y ADK).",
                    )

    # Párrafo corto tras hoja de ruta C-05 si no existe
    if not any("Agent Development Kit" in (x.text or "") for x in doc.paragraphs):
        try:
            anchor = find_para(doc, contains="Hoja de ruta del hilo C-05")
            insert_paragraph_after(
                anchor,
                "Responsabilidad técnica agéntica: lo que esta solución requiera en "
                "desarrollo agéntico (integración Gemini, orquestación con Agent Development "
                "Kit —ADK— y operación en Google Cloud) queda a cargo de Nicolás Barra y Ari "
                "Araya. No se contrata un perfil externo para eso en sep–dic 2026. Giannina "
                "mantiene el control de cambios y la UI; Skarlett, la calidad del FAQ y de las "
                "respuestas.",
            )
        except KeyError:
            # Insertar tras 2.5 título
            try:
                anchor = find_para(doc, startswith="2.5. C-05")
                # skip to last body - use efecto positivo
                anchor = find_para(doc, contains="efecto positivo acotado")
                insert_paragraph_after(
                    anchor,
                    "Responsabilidad técnica agéntica: Nicolás Barra y Ari Araya (Google Cloud "
                    "y Agent Development Kit —ADK—). Sin especialista externo en esta ventana.",
                )
            except KeyError:
                pass
    else:
        # Ya hay mención ADK en algún lado; asegurar párrafo dedicado
        pass

    # Mensaje cliente CAPEX — reforzar dueños
    try:
        p = find_para(doc, contains="Mensaje al cliente: aprobar C-05b")
        t = p.text or ""
        if "ADK" not in t:
            set_para(
                p,
                t.rstrip()
                + " El desarrollo agéntico (GCloud y ADK) lo ejecutan Nicolás y Ari dentro del "
                "equipo, sin línea de consultoría externa en esta ventana.",
            )
    except KeyError:
        pass

    doc.save(str(DOCX))
    print("OK", DOCX)


if __name__ == "__main__":
    main()
