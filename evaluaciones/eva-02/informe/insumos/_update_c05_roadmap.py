# -*- coding: utf-8 -*-
"""Prioriza soporte+UX ahora; deja monitoreo/alertas/IA operativa para fases posteriores."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

DOCX = Path(__file__).resolve().parents[1] / "2.2.2-Gestion-de-cambios-Kiran.docx"

C05_SITUACION = (
    "Ejemplo de solicitud. La dirección pide un chatbot en la plataforma para los usuarios "
    "del piloto: preguntas frecuentes (FAQ) y un canal para comunicarse por temas de soporte "
    "y asistencia, con el fin de ahorrar contrato de personal de soporte. En este plan se "
    "prioriza esa capa de soporte y una UI/UX clara (amigable para el público objetivo y la "
    "contingencia de una zona compleja), porque si el uso está bien guiado baja la carga de "
    "soporte. A futuro, el mismo manejo de tickets debería alimentar casos de usuario de uso "
    "interno, monitoreo y alertas, y la IA podría contribuir al monitoreo operativo de los "
    "equipos; esas capacidades se identifican como fases posteriores y no se construyen en "
    "esta ventana. La formulación amplia (app ciudadana masiva, reemplazo total del técnico "
    "o IA de monitoreo total) no se aprueba ahora: solo la fase 1 (FAQ más escalamiento a "
    "ticket o persona), tras un tablero usable, sin datos de hogares en un modelo externo y "
    "sin sustituir los estados del kit."
)


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


def find_row(table, startswith: str):
    for row in table.rows:
        if (row.cells[0].text or "").startswith(startswith):
            return row
    return None


def find_para(doc: Document, contains: str = None, startswith: str = None):
    for p in doc.paragraphs:
        t = p.text or ""
        if startswith is not None and t.startswith(startswith):
            return p
        if contains is not None and contains in t:
            return p
    raise KeyError(contains or startswith)


def set_para(p: Paragraph, text: str) -> None:
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.text = text


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


def replace_once(doc: Document, old: str, new: str) -> bool:
    for p in doc.paragraphs:
        t = p.text or ""
        if old in t:
            set_para(p, t.replace(old, new))
            return True
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                t = cell.text or ""
                if old in t:
                    set_cell_text(cell, t.replace(old, new))
                    return True
    return False


def main() -> None:
    doc = Document(str(DOCX))
    t2, t5, t6, t10, t11 = (
        doc.tables[1],
        doc.tables[4],
        doc.tables[5],
        doc.tables[9],
        doc.tables[10],
    )

    row = find_row(t2, "C-05")
    set_cell_text(row.cells[1], C05_SITUACION)

    # §1.1 justificación
    p = find_para(doc, contains="C-05 se rotula como ejemplo de solicitud")
    set_para(
        p,
        "C-05 se rotula como ejemplo de solicitud porque concreta el tipo de cambio de soporte "
        "al usuario con IA: un chatbot con FAQ y canal de asistencia para bajar el gasto en "
        "personal de soporte contratado. Se prioriza en esta ventana, junto con una UI/UX "
        "amigable (C-06 y la claridad del tablero), porque la zona del piloto es compleja y el "
        "público objetivo necesita un uso guiado: si está todo claro, se ahorra soporte. No es "
        "una app ciudadana ni el reemplazo total del técnico. El monitoreo operativo de equipos, "
        "las alertas automatizadas y la IA aplicada a ese monitoreo se reconocen como valor "
        "futuro del mismo hilo de tickets, pero quedan fuera de la construcción de sep–dic 2026. "
        "La medida factible ahora es solo la fase 1 (FAQ más escalamiento humano).",
    )

    # §2.5 cuerpos
    p = find_para(doc, startswith="En los términos pedidos (chatbot para usuarios")
    set_para(
        p,
        "En los términos pedidos (chatbot para usuarios con FAQ y comunicación de soporte, para "
        "ahorrar contrato de personal), el cambio toca la interfaz de la plataforma, la claridad "
        "de la experiencia de uso, la integración con una API de modelo o motor de FAQ, la "
        "privacidad, la calidad de las respuestas y el flujo hacia el ticket. Nicolás sostiene "
        "la integración. Giannina la interfaz del chat y la UI/UX asociada. Skarlett valida la "
        "calidad de las respuestas y el FAQ. Ari registra el tope de gasto. Un modelo propio, "
        "un fine-tuning, un datalake, una app para cada hogar o un módulo de monitoreo y alertas "
        "con IA sobre todos los equipos no están en el plan de esta ventana.",
    )

    p = find_para(doc, contains="El efecto positivo acotado es reducir consultas")
    set_para(
        p,
        "El efecto positivo acotado es reducir consultas repetidas al personal de soporte "
        "contratado: el usuario resuelve con FAQ o deja un mensaje que escala a ticket, sobre "
        "una interfaz clara para un público en zona compleja. El efecto negativo de la "
        "formulación completa (reemplazo total del soporte, app ciudadana o IA de monitoreo "
        "total desde ya) es ampliar el alcance, abrir gasto no comprometido y responder mal por "
        "una alucinación. La fase 1 no cambia el estado del kit, no cierra tickets sola, no "
        "genera alertas de flota ni redacta el reporte a donantes. Indicadores amenazados: E1, "
        "E4 y E5. Operativos a monitorear: O1, O4 y O6, con submétricas de contención del "
        "chatbot (% resuelto por FAQ sin escalar) y de escalamiento a persona.",
    )

    # Párrafo de roadmap futuro tras el efecto positivo de C-05 (antes de 2.6)
    p26 = find_para(doc, startswith="2.6. C-06")
    # Insertar solo si no existe ya
    already = any(
        "fases posteriores" in (x.text or "") and "monitoreo operativo" in (x.text or "")
        for x in doc.paragraphs
    )
    if not already:
        # Insert before 2.6 by finding last C-05 body para (efecto positivo)
        anchor = find_para(doc, contains="con submétricas de contención del chatbot")
        insert_paragraph_after(
            anchor,
            "Hoja de ruta del hilo C-05 (sin comprometer construcción en esta ventana): la fase 1 "
            "prioriza soporte al usuario y UI/UX amigable. En fases posteriores, el manejo de "
            "tickets debería alimentar también el uso interno de casos de usuario, el monitoreo y "
            "las alertas operativas; más adelante, la IA podría contribuir al monitoreo de los "
            "equipos y a esas alertas. Esas fases no se aprueban ni se fechan en sep–dic 2026: "
            "quedan identificadas para no perder el hilo y para no mezclarlas con el corte actual.",
        )

    # §3.1 aprobación por fases
    p = find_para(doc, startswith="C-05 se aprueba solo por fases")
    set_para(
        p,
        "C-05 se aprueba solo por fases. La fase 1 (chatbot con FAQ y canal de asistencia que "
        "escala a ticket o a persona, sobre una UI/UX clara) queda condicionada a que C-06 esté "
        "en marcha o en el mismo plan de sprint, a que quepa en dos tarjetas por persona y a un "
        "tope de llamadas API en Excel. El FAQ lo cura el equipo; el chatbot no cierra ni cambia "
        "estados solo. Se prioriza frente a monitoreo y alertas porque la contingencia de la zona "
        "y el público objetivo exigen buen soporte y un uso guiado: eso es lo que permite ahorrar "
        "en personal de soporte. La fase 2 (ampliar el corpus FAQ, mejorar el enrutamiento del "
        "canal y, si cabe, dejar trazas de casos de usuario para uso interno) solo post 4 de "
        "diciembre o con un control de cambios nuevo. La fase 3 (monitoreo y alertas operativas "
        "asistidas por IA sobre los equipos, app ciudadana masiva, reemplazo total del personal "
        "de soporte o modelo propio) se rechaza entre septiembre y diciembre de 2026 y queda "
        "como solicitud futura. No se aprueba un chatbot que sustituya de golpe al soporte "
        "contratado ni una IA de monitoreo total en esta ventana.",
    )

    # Tabla 5 fases 2-3
    row = find_row(t5, "C-05 fases")
    if row:
        set_cell_text(
            row.cells[0],
            "C-05 fases 2–3 / monitoreo-alertas con IA / app ciudadana / datalake",
        )
        set_cell_text(
            row.cells[4],
            "Identificado para después del piloto o con CC nuevo. Sin pasos en sep–dic 2026. "
            "La prioridad de esta ventana es soporte y UI/UX.",
        )

    # Tabla 6
    row = find_row(t6, "C-05 fase 1")
    if row:
        set_cell_text(
            row.cells[2],
            "Ofrece autoservicio y canal de asistencia a usuarios de la plataforma, con UI/UX "
            "clara para zona compleja y público objetivo, para ahorrar personal de soporte. No "
            "abre app ciudadana ni monitoreo con IA de flota en esta ventana.",
        )

    row = find_row(t6, "C-05 completo")
    if row:
        set_cell_text(
            row.cells[0],
            "C-05 completo / monitoreo-alertas IA / app ciudadana / datalake",
        )
        set_cell_text(
            row.cells[1],
            "No se aprueba en esta ventana. Se cierra esa formulación y se deja como fase "
            "posterior identificada.",
        )
        set_cell_text(
            row.cells[2],
            "El piloto no abre una app masiva, ni un segundo producto de datos, ni IA de "
            "monitoreo total; el soporte humano sigue para lo que el FAQ no resuelve.",
        )

    # Tabla 10
    row = find_row(t10, "C-05a")
    if row:
        set_cell_text(
            row.cells[1],
            "Requisito futuro identificado. Chatbot amplio; app ciudadana; reemplazo total del "
            "soporte; monitoreo y alertas operativas con IA sobre los equipos; o datalake completo.",
        )
        set_cell_text(
            row.cells[5],
            "No aprobado entre septiembre y diciembre de 2026. Queda identificado como fase "
            "posterior (casos internos, monitoreo, alertas, IA operativa). Fuera de la EDT y del "
            "techo de esta ventana. Escalamiento a la dirección si se insiste en construirlo ahora.",
        )

    row = find_row(t10, "C-05b")
    if row:
        set_cell_text(
            row.cells[5],
            "Aprobado solo si C-06 está en marcha, cabe en dos tarjetas, existe tope de API y el "
            "FAQ está curado. Prioridad de esta ventana: soporte y UI/UX amigable por la zona "
            "compleja y el público objetivo, para ahorrar horas de soporte contratado. Sin datos "
            "de hogares en un modelo externo. El bot no cierra ni cambia estados solo. No incluye "
            "monitoreo ni alertas de flota. Escalamiento si proponen mover el 4 de diciembre o "
            "adelantar la fase de monitoreo con IA.",
        )

    # Tabla 11
    set_cell_text(
        t11.rows[2].cells[1],
        "La fotografía del ticket, el segundo punto de inventario dentro de esta ventana, el "
        "servicio externo del reporte, el chatbot que reemplaza de golpe al soporte contratado, "
        "la app ciudadana masiva, el monitoreo y las alertas con IA sobre todos los equipos en "
        "esta ventana, el datalake o lakehouse completo, el modelo propio y las fases 2 y 3 del "
        "chatbot como construcción fechada en sep–dic 2026 (quedan solo identificadas a futuro).",
    )
    set_cell_text(
        t11.rows[3].cells[1],
        "Kiran no instala paneles. Ninguna solicitud de este plan modifica ese límite. Tampoco "
        "abre una app ciudadana masiva ni una plataforma analítica aparte del piloto. El chatbot "
        "fase 1 atiende a usuarios de la plataforma del piloto; no convierte a cada hogar en "
        "usuario de una app nueva. El monitoreo operativo asistido por IA queda para una fase "
        "posterior, cuando el soporte y la UI/UX ya estén claros.",
    )

    # Intro: una frase si aún no está
    replace_once(
        doc,
        "C-05 fase 1 es autoservicio de FAQ y canal de asistencia para usuarios de la plataforma, "
        "no un segundo producto.",
        "C-05 fase 1 es autoservicio de FAQ y canal de asistencia para usuarios de la plataforma, "
        "con UI/UX clara, no un segundo producto. Monitoreo, alertas y IA operativa sobre equipos "
        "quedan como fase posterior identificada.",
    )

    doc.save(str(DOCX))
    print("OK", DOCX)


if __name__ == "__main__":
    main()
