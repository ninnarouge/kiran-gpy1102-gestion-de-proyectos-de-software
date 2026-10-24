# -*- coding: utf-8 -*-
"""Indicadores E/O en tablas; C-05d con estándares de protección de datos."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

DOCX = Path(__file__).resolve().parents[1] / "2.2.2-Gestion-de-cambios-Kiran v2.docx"

ESTRATEGICOS = [
    [
        "#",
        "Indicador",
        "Fórmula / lectura",
        "Meta",
        "Fuente",
        "Dueño",
        "Si se rompe",
    ],
    [
        "E1",
        "Cumplimiento de cortes",
        "% de los 4 cortes (19 oct, 9 nov, 4 dic, cierre) con criterio del acta",
        "4/4 o causa escrita si atraso ≤ 3 días",
        "Project Libre + acta",
        "Giannina",
        "CC; semana siguiente sin trabajo nuevo si atraso > 3 días",
    ],
    [
        "E2",
        "Integridad plan–ejecución",
        "% actividades de ruta crítica sin desvío no registrado en CC",
        "100 % en hitos revisados",
        "Project Libre + registro CC",
        "Giannina / Nicolás",
        "Replanificar; no basta un parche solo en Trello",
    ],
    [
        "E3",
        "Alcance verificable (EDT)",
        "% paquetes EDT del piloto con evidencia de aceptación al cierre del corte",
        "Meta por corte (inventario, tablero, tickets, reporte)",
        "Office + tablero",
        "Dueño de cada paquete",
        "No declarar corte cerrado; reabrir si puntaje < 4",
    ],
    [
        "E4",
        "Techo y gasto comprometido",
        "Desviación acumulada vs techo vigente (20.700; 21.200 si Escenario C)",
        "Freno si desviación > 10 %",
        "Excel quincenal / consola GCloud",
        "Ari",
        "Detener gasto no comprometido (Gemini/GCloud); sin gastar C-05b sin escenario A/B/C",
    ],
    [
        "E5",
        "Cambios bajo control",
        "% cambios aprobados con alcance/PL/Trello actualizados antes de construir; 0 en producción sin Tabla 10",
        "100 % en cambios constructivos",
        "Tabla 10 + Trello",
        "Giannina",
        "Detener construcción; volver al procedimiento",
    ],
]

OPERATIVOS = [
    [
        "#",
        "Indicador",
        "Fórmula / lectura",
        "Meta",
        "Fuente",
        "Dueño",
        "Si se rompe",
    ],
    [
        "O1",
        "Defectos por líneas cambiadas",
        "Defectos del período ÷ líneas cambiadas",
        "≤ 5; 0 bloqueos. Sin código: «sin base» (no alerta roja)",
        "Revisión de sprint",
        "Skarlett / Nicolás",
        "No cerrar sprint sin pasar líneas a calidad",
    ],
    [
        "O2",
        "Tasa de reapertura (desarrollo)",
        "Reabierto ÷ cerrado (historias/defectos de sprint)",
        "< 20 %",
        "Trello + calidad",
        "Skarlett",
        "No sumar historias; no mezclar con tickets operativos en terreno",
    ],
    [
        "O3",
        "Cumplimiento del sprint",
        "% historias comprometidas completadas (lista ya reemplazada si hubo CC)",
        "≥ 80 %",
        "Trello",
        "Giannina",
        "Resto a backlog; no apilar CC encima",
    ],
    [
        "O4",
        "WIP y bloqueos",
        "Tarjetas por persona; días en Bloqueado",
        "≤ 2 tarjetas; > 5 días → C-04",
        "Trello",
        "Giannina",
        "Reasignación registrada",
    ],
    [
        "O5",
        "Kits con estado verificable",
        "% kits con hogar, responsable y estado coherente al cierre del corte",
        "Alineado al KPI primario del producto",
        "Inventario / tablero",
        "Dueño del inventario",
        "No cerrar corte de inventario/tablero",
    ],
    [
        "O6",
        "Atención de fallas y chatbot (C-06 / C-05)",
        "Tiempo falla→ticket; tiempo para elegir siguiente; % consultas fuera del tablero; % FAQ sin escalar; % escala a persona; gasto Gemini/GCloud vs soporte evitado",
        "Mejora post 9 nov; contención baja o gasto IA > ahorro → pausar/congelar fase 2",
        "Tablero + bitácora + consola GCloud",
        "Giannina / soporte; chatbot: Nicolás / Skarlett; gasto: Ari",
        "Priorizar cola y FAQ antes que ampliar IA",
    ],
    [
        "O7",
        "Coordinación, datos en terreno y protección",
        "Puntaje contraparte 1–5; % sync por lote; cumplimiento de minimización/roles en datalake (C-05d)",
        "Puntaje ≥ 4; sync según plan; 0 PII innecesaria en lake/modelo",
        "Office + Excel + revisión privacidad",
        "Giannina / Ari / Nicolás",
        "Escalar; no ampliar datalake sin CC ni sin control de datos",
    ],
]


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


def ensure_rows(table: Table, n: int) -> None:
    while len(table.rows) < n:
        table._tbl.append(deepcopy(table.rows[-1]._tr))
    while len(table.rows) > n:
        table.rows[-1]._tr.getparent().remove(table.rows[-1]._tr)


def fill_table(table: Table, rows: list[list[str]]) -> None:
    # Expand columns if template has fewer than needed
    ensure_rows(table, len(rows))
    ncols = len(table.rows[0].cells)
    for i, vals in enumerate(rows):
        # If template has fewer columns, put remaining text in last cell
        if len(vals) <= ncols:
            for cell, val in zip(table.rows[i].cells, vals):
                set_cell_text(cell, val)
            for j in range(len(vals), ncols):
                set_cell_text(table.rows[i].cells[j], "")
        else:
            for j in range(ncols - 1):
                set_cell_text(table.rows[i].cells[j], vals[j])
            set_cell_text(table.rows[i].cells[ncols - 1], " | ".join(vals[ncols - 1 :]))


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
        if src.font.size:
            run.font.size = src.font.size
        if src.font.name:
            run.font.name = src.font.name
    else:
        new_para.add_run(text)
    return new_para


def insert_table_after(paragraph: Paragraph, template: Table) -> Table:
    new_tbl = deepcopy(template._tbl)
    paragraph._p.addnext(new_tbl)
    return Table(new_tbl, paragraph._parent)


def remove_para(p: Paragraph) -> None:
    p._element.getparent().remove(p._element)


def main() -> None:
    doc = Document(str(DOCX))

    # Evitar duplicar tablas de indicadores
    if any("Tabla 12." in (p.text or "") for p in doc.paragraphs):
        print("Tablas de indicadores ya existen; solo actualiza C-05d si hace falta.")
    else:
        # Enfasis intro en 4.4
        try:
            h44 = next(p for p in doc.paragraphs if (p.text or "").startswith("4.4. Monitoreo"))
            # Ampliar primer párrafo de monitoreo si existe
            for p in doc.paragraphs:
                if (p.text or "").startswith("El monitoreo no observa"):
                    set_para(
                        p,
                        "El monitoreo no observa el esfuerzo por sí mismo. Observa si lo "
                        "aprobado sigue alineado con los cortes y con el techo vigente. Los "
                        "indicadores se comunican en tablas (estratégicos y operativos) para "
                        "que dirección, contraparte y el equipo lean la misma información de "
                        "forma organizada. Los instrumentos ya están definidos y no se reemplazan.",
                    )
                    break
        except StopIteration:
            pass

        # Plantilla con muchas columnas: usar tabla 7d (5 cols) o clonar y aceptar 5 cols
        # Mejor: usar tabla de registro (6 cols) o crear from tabla 3 (5) - for 7 cols we need
        # a wide table. Clone Tabla 7b (5) and put compact columns, OR clone and add columns via XML.
        # Simplest for "formato tal cual": use 5 columns by merging some fields.
        # User asked for organized table - 5 cols is fine: Id | Indicador | Meta y fórmula | Dueño | Si se rompe

        E_COMPACT = [
            ["Id.", "Indicador", "Fórmula / meta", "Fuente y dueño", "Si se rompe"],
            [
                "E1",
                "Cumplimiento de cortes",
                "% de 4 cortes con criterio del acta. Meta: 4/4 o causa si atraso ≤ 3 días",
                "Project Libre + acta · Giannina",
                "CC; sin trabajo nuevo la semana siguiente si atraso > 3 días",
            ],
            [
                "E2",
                "Integridad plan–ejecución",
                "% ruta crítica sin desvío no registrado. Meta: 100 % en hitos revisados",
                "PL + registro CC · Giannina / Nicolás",
                "Replanificar; no parche solo en Trello",
            ],
            [
                "E3",
                "Alcance verificable (EDT)",
                "% paquetes con evidencia de aceptación al cierre del corte",
                "Office + tablero · dueño del paquete",
                "No cerrar corte; reabrir si puntaje < 4",
            ],
            [
                "E4",
                "Techo y gasto comprometido",
                "Desviación vs techo vigente (20.700; 21.200 si Escenario C). Freno > 10 %",
                "Excel / consola GCloud · Ari",
                "Detener Gemini/GCloud no comprometido",
            ],
            [
                "E5",
                "Cambios bajo control",
                "% CC con alcance/PL/Trello al día; 0 en producción sin Tabla 10. Meta: 100 %",
                "Tabla 10 + Trello · Giannina",
                "Detener build; volver al procedimiento",
            ],
        ]

        O_COMPACT = [
            ["Id.", "Indicador", "Fórmula / meta", "Fuente y dueño", "Si se rompe"],
            [
                "O1",
                "Defectos / líneas cambiadas",
                "Defectos ÷ líneas. Meta ≤ 5; 0 bloqueos. Sin código: «sin base»",
                "Revisión sprint · Skarlett / Nicolás",
                "No cerrar sprint sin revisión de calidad",
            ],
            [
                "O2",
                "Reapertura (desarrollo)",
                "Reabierto ÷ cerrado. Meta < 20 %",
                "Trello + calidad · Skarlett",
                "No sumar historias; no mezclar con tickets de terreno",
            ],
            [
                "O3",
                "Cumplimiento del sprint",
                "% historias comprometidas hechas (lista ya reemplazada). Meta ≥ 80 %",
                "Trello · Giannina",
                "Resto a backlog",
            ],
            [
                "O4",
                "WIP y bloqueos",
                "≤ 2 tarjetas/persona; Bloqueado > 5 días → C-04",
                "Trello · Giannina",
                "Reasignación registrada",
            ],
            [
                "O5",
                "Kits con estado verificable",
                "% kits con hogar, responsable y estado coherente",
                "Inventario / tablero · dueño inventario",
                "No cerrar corte de inventario/tablero",
            ],
            [
                "O6",
                "Fallas, cola y chatbot",
                "Tiempos de atención; % fuera del tablero; % FAQ sin escalar; gasto Gemini/GCloud vs soporte evitado. Mejora post 9 nov",
                "Tablero + bitácora + GCloud · Giannina / Nicolás / Skarlett / Ari",
                "Pausar ampliación IA; priorizar cola y FAQ",
            ],
            [
                "O7",
                "Coordinación y protección de datos",
                "Puntaje contraparte ≥ 4; sync por lote; 0 PII innecesaria en datalake/modelo (C-05d)",
                "Office + Excel + revisión privacidad · Giannina / Ari / Nicolás",
                "Escalar; no ampliar datalake sin CC ni control de datos",
            ],
        ]

        # Template 5-col: find table with 5 columns
        template = None
        for t in doc.tables:
            if len(t.rows[0].cells) >= 5:
                template = t
                break
        assert template is not None

        # Find headings
        h_est = next(p for p in doc.paragraphs if (p.text or "").strip() == "Indicadores estratégicos del proyecto")
        h_op = next(p for p in doc.paragraphs if (p.text or "").strip() == "Indicadores operativos")

        # Remove old E* and O* paragraphs
        to_remove = []
        for p in doc.paragraphs:
            t = (p.text or "").strip()
            if t.startswith(("E1.", "E2.", "E3.", "E4.", "E5.", "O1.", "O2.", "O3.", "O4.", "O5.", "O6.", "O7.")):
                to_remove.append(p)
        for p in to_remove:
            remove_para(p)

        # Refresh heading refs after removal - find again
        h_est = next(p for p in doc.paragraphs if (p.text or "").strip() == "Indicadores estratégicos del proyecto")
        set_para(
            h_est,
            "Indicadores estratégicos del proyecto (comunicación organizada)",
        )
        p = insert_paragraph_after(
            h_est,
            "Se leen por corte y por dirección. Resume si el piloto sostiene acta, línea base, "
            "techo y control de cambios.",
        )
        t_est = insert_table_after(p, template)
        fill_table(t_est, E_COMPACT)
        # caption after table
        cap1 = deepcopy(p._p)
        for child in list(cap1):
            if child.tag == qn("w:r"):
                cap1.remove(child)
        t_est._tbl.addnext(cap1)
        c1 = Paragraph(cap1, p._parent)
        r = c1.add_run(
            "Tabla 12. Indicadores estratégicos del proyecto (E1–E5). Lectura por corte y dirección."
        )
        if p.runs and p.runs[0].font.size:
            r.font.size = p.runs[0].font.size

        h_op = next(p for p in doc.paragraphs if (p.text or "").strip().startswith("Indicadores operativos"))
        set_para(
            h_op,
            "Indicadores operativos (comunicación organizada)",
        )
        p2 = insert_paragraph_after(
            h_op,
            "Se leen semanal o quincenalmente. Alimentan a los estratégicos y alertan antes de "
            "romper un corte. Incluyen calidad de código, operación del piloto, chatbot y "
            "protección de datos en el datalake (C-05d).",
        )
        t_op = insert_table_after(p2, template)
        fill_table(t_op, O_COMPACT)
        cap2 = deepcopy(p2._p)
        for child in list(cap2):
            if child.tag == qn("w:r"):
                cap2.remove(child)
        t_op._tbl.addnext(cap2)
        c2 = Paragraph(cap2, p2._parent)
        r2 = c2.add_run(
            "Tabla 13. Indicadores operativos (O1–O7). Lectura semanal/quincenal para el equipo y contraparte."
        )
        if p2.runs and p2.runs[0].font.size:
            r2.font.size = p2.runs[0].font.size

        # Relación entre capas — si el párrafo existe, ok; si no, insertar tras caption 13
        if not any("O1 a O4 sostienen" in (p.text or "") for p in doc.paragraphs):
            insert_paragraph_after(
                c2,
                "Los operativos O1 a O4 sostienen ritmo y calidad del equipo. O5 a O7 miden si "
                "el piloto opera con datos creíbles, soporte atendible y protección de datos. "
                "E1 a E3 consolidan cortes y EDT; E4 y E5, techo y control de cambios.",
            )

    # --- C-05d: estándares de protección de datos ---
    for table in doc.tables:
        for row in table.rows:
            if (row.cells[0].text or "").startswith("C-05d"):
                set_cell_text(
                    row.cells[1],
                    "Datos. Datalake como base de información del piloto (mínimo usable: "
                    "inventario, tickets, logs de chat agregados). Se diseñan con estándares "
                    "de protección de datos: minimización, roles de acceso y alineación con "
                    "ISO/IEC 27701; sin PII innecesaria ni bases de hogares en el repositorio "
                    "ni en prompts a modelos externos.",
                )
                set_cell_text(
                    row.cells[5],
                    "Aprobado en alcance mínimo alineado a C-05b (base para FAQ y fases "
                    "posteriores), condicionado a controles de protección de datos "
                    "(minimización, roles, ISO/IEC 27701). Lakehouse completo no. "
                    "Financiamiento dentro del Escenario C o CC si el storage supera el margen "
                    "GCloud. Dueños: Nicolás y Ari. Evidencia de roles y minimización antes "
                    "de cargar dato real.",
                )

    # Párrafo §2 o tras responsabilidad si falta protección
    if not any("ISO/IEC 27701" in (p.text or "") and "datalake" in (p.text or "").lower() for p in doc.paragraphs):
        for p in doc.paragraphs:
            if "datalake como base de información" in (p.text or "") and "Nicolás Barra y Ari":
                t = p.text or ""
                if "27701" not in t:
                    set_para(
                        p,
                        t.rstrip()
                        + " El datalake mínimo se implementa con estándares de protección de "
                        "datos (minimización, roles, alineación ISO/IEC 27701); no se suben "
                        "bases de hogares ni PII innecesaria a modelos externos.",
                    )
                break

    # Tabla 11 si hay fila datalake/ADK
    t11 = doc.tables[-1]
    if "Pregunta" in (t11.rows[0].cells[0].text or ""):
        for row in t11.rows:
            if "datalake" in (row.cells[0].text or "").lower() or "ADK" in (row.cells[0].text or ""):
                a = row.cells[1].text or ""
                if "27701" not in a and "protección" not in a:
                    set_cell_text(
                        row.cells[1],
                        a.rstrip()
                        + " El datalake mínimo aplica estándares de protección de datos "
                        "(minimización, roles, ISO/IEC 27701).",
                    )

    # O7 in prose measurement if still there
    doc.save(str(DOCX))
    print("OK", DOCX)


if __name__ == "__main__":
    main()
