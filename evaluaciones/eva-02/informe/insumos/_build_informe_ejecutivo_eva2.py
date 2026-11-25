# -*- coding: utf-8 -*-
"""Genera Informe-ejecutivo-Eva2-Kiran.docx (Arial 12, 1.5, márgenes 2.5 cm). Tono técnico."""
from __future__ import annotations

import shutil
from pathlib import Path

from docx import Document
from docx.enum.text import WD_LINE_SPACING, WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Cm, Pt

ROOT = Path(__file__).resolve().parents[1]
OUT_REPO = ROOT / "Informe-ejecutivo-Eva2-Kiran.docx"
OUT_DL = Path(r"e:\DOWNLOADS\Informe-ejecutivo-Eva2-Kiran.docx")
FONT = "Arial"
SIZE = 12


def set_run_font(run, *, bold=False, size=SIZE, italic=False):
    run.bold = bold
    run.italic = italic
    run.font.name = FONT
    run.font.size = Pt(size)
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn("w:ascii"), FONT)
    rFonts.set(qn("w:hAnsi"), FONT)
    rFonts.set(qn("w:eastAsia"), FONT)


def style_paragraph(p, *, bold=False, size=SIZE, space_after=6, align=None):
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(0)
    if align is not None:
        p.alignment = align
    for run in p.runs:
        set_run_font(run, bold=bold or bool(run.bold), size=size, italic=bool(run.italic))


def add_p(doc, text, *, bold=False, size=SIZE, space_after=6, align=None):
    p = doc.add_paragraph()
    run = p.add_run(text)
    set_run_font(run, bold=bold, size=size)
    style_paragraph(p, bold=bold, size=size, space_after=space_after, align=align)
    return p


def add_h(doc, text, *, level=1):
    size = 14 if level == 1 else 12
    return add_p(doc, text, bold=True, size=size, space_after=8)


def set_cell_shading(cell, hex_color: str):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def add_table(doc, rows: list[list[str]], *, header=True):
    cols = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=cols)
    table.style = "Table Grid"
    for i, row_vals in enumerate(rows):
        for j in range(cols):
            cell = table.rows[i].cells[j]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(row_vals[j] if j < len(row_vals) else "")
            is_header = header and i == 0
            set_run_font(run, bold=is_header, size=9)
            pf = p.paragraph_format
            pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
            pf.space_after = Pt(2)
            pf.space_before = Pt(2)
            if is_header:
                set_cell_shading(cell, "D9E2F3")
    doc.add_paragraph()
    return table


def setup_doc() -> Document:
    doc = Document()
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)
    style = doc.styles["Normal"]
    style.font.name = FONT
    style.font.size = Pt(SIZE)
    style._element.rPr.rFonts.set(qn("w:ascii"), FONT)
    style._element.rPr.rFonts.set(qn("w:hAnsi"), FONT)
    style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    return doc


def main() -> None:
    doc = setup_doc()

    add_p(doc, "DUOC UC — Escuela de Informática y Telecomunicaciones", bold=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(doc, "GPY1102 · Gestión de Proyectos de Software", size=11, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_p(
        doc,
        "Informe de monitoreo y control del proyecto Kiran",
        bold=True,
        size=16,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=8,
    )
    add_p(
        doc,
        "Evaluación Parcial N.° 2 — Informe grupal (RA2 · IL 2.1, 2.2, 2.3 y 2.4)",
        size=11,
        align=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=12,
    )

    add_h(doc, "1. Identificación del encargo")
    add_table(
        doc,
        [
            ["Campo", "Contenido"],
            ["Organización / caso", "Emprendimiento social con piloto de kits solares; Kiran es el software de operación (no instala paneles)"],
            ["Alcance del producto", "Inventario, tablero operativo, tickets de mantención, reportes de impacto, roles y tratamiento de datos"],
            ["Equipo", "Giannina Guerrero; Nicolás Barra; Ari Araya; Skarlett Tropan"],
            ["Periodo del piloto", "14 de septiembre de 2026 – 9 de diciembre de 2026"],
            ["Presupuesto de referencia", "US$ 20.700 (línea base); US$ 21.200 propuesto ante módulo de asistencia con IA"],
            ["Restricciones", "Cuatro desarrolladores; técnico local no full time; conectividad irregular; techo y cortes fijos"],
            ["Objeto del informe", "Monitoreo y control; gestión de cambios; asignación de recursos; estado para partes interesadas"],
            ["Extensión", "Autorización docente para no ceñirse al tope de 7 planas; largo según cobertura del caso"],
        ],
    )
    add_p(
        doc,
        "El informe se estructura según los indicadores de evaluación de la dimensión grupal escrita: "
        "propuesta de monitoreo y control, gestión del cambio, asignación de recursos y documentación "
        "del estado del proyecto para partes interesadas.",
    )

    # ---- 2 Monitoreo ----
    add_h(doc, "2. Sistema de monitoreo y control")
    add_h(doc, "2.1 Propósito", level=2)
    add_p(
        doc,
        "El sistema de monitoreo y control tiene por objeto resguardar la planificación e integración del piloto: "
        "verificar el avance respecto de los hitos, detectar desvíos de alcance, tiempo, costo y calidad, y entregar "
        "información única a dirección y contraparte. No sustituye la ejecución; condiciona las decisiones de "
        "continuar, replanificar o detener gasto no autorizado.",
    )
    add_h(doc, "2.2 Componentes e interacción", level=2)
    add_table(
        doc,
        [
            ["Componente", "Función", "Responsable", "Periodicidad"],
            ["Project Libre", "Fechas, ruta crítica, desvíos de hito", "Dirección / backend", "Por sprint y en cada hito"],
            ["Trello", "Compromiso de sprint, trabajo en curso, bloqueos", "Equipo; dirección en reasignaciones", "Continuo"],
            ["Excel financiero y consola de nube", "Gasto acumulado, alertas, topes de API", "Infraestructura", "Quincenal"],
            ["Indicadores estratégicos", "Lectura consolidada para dirección", "Dirección", "En cada hito"],
            ["Indicadores operativos", "Detección temprana de calidad, capacidad y operación", "Calidad / backend / dirección", "Semanal o quincenal"],
            ["Evaluación de hito por contraparte", "Puntaje de aceptación del entregable", "Dirección y contraparte", "En cada hito"],
            ["Registro formal de cambios", "Trazabilidad de solicitudes que alteran línea base", "Dirección", "Ante cada solicitud"],
        ],
    )
    add_p(
        doc,
        "La interacción entre componentes es obligatoria: el flujo de Trello sin actualización de Project Libre "
        "genera divergencia plan–ejecución; el reporte financiero sin contraste con el trabajo real invalida la "
        "lectura de costo; un incremento construido fuera del registro de cambios rompe la integridad del plan inicial.",
    )
    add_h(doc, "2.3 Representación del flujo de información", level=2)
    add_table(
        doc,
        [
            ["Etapa", "Origen", "Salida", "Destino de control"],
            ["1", "Terreno y aplicación Kiran", "Estados de kit, tickets, sync por lote", "Base del aplicativo"],
            ["2", "Desarrollo", "Incremento según Definition of Done", "Ambiente y tablero de flujo"],
            ["3", "Tablero de flujo", "Capacidad, bloqueos, cumplimiento de sprint", "Indicadores operativos"],
            ["4", "Project Libre", "Cumplimiento de hitos y ruta crítica", "Indicadores estratégicos de tiempo"],
            ["5", "Excel y factura de nube", "Desviación presupuestaria", "Indicador de techo; detención de gasto"],
            ["6", "Bitácora de soporte / canal asistido", "Carga de consultas y escalamiento", "Indicadores de atención"],
            ["7", "Consolidado de indicadores y puntaje", "Lectura única", "Dirección y partes interesadas"],
        ],
    )
    add_h(doc, "2.4 Hitos clave", level=2)
    add_table(
        doc,
        [
            ["Hito", "Fecha", "Entregable de control", "Criterio de cierre"],
            ["Inventario validado", "19 de octubre de 2026", "Un inventario confiable", "Aceptación; sin segundo punto de acopio en esta ventana"],
            ["Tablero operativo", "9 de noviembre de 2026", "Visibilidad sobre el inventario", "Tablero usable; priorización visual condicionada a capacidad"],
            ["Tickets, pruebas y reporte", "4 de diciembre de 2026", "Tickets, prueba y primer reporte", "Sin desplazar el cierre a la semana de entrega"],
            ["Cierre y traspaso", "5 al 9 de diciembre de 2026", "Entrega formal", "Sin construcción de alcance pendiente"],
        ],
    )
    add_p(
        doc,
        "Un atraso de hasta tres días hábiles en un hito puede documentarse con causa; un atraso mayor no se "
        "absorbe con trabajo nuevo en la semana siguiente.",
    )
    add_h(doc, "2.5 Indicadores estratégicos", level=2)
    add_table(
        doc,
        [
            ["Indicador", "Definición operativa", "Umbral / acción"],
            ["Cumplimiento de hitos", "Entrega de los cuatro cortes con criterio del acta", "4/4 o causa si atraso ≤ 3 días"],
            ["Integridad plan–ejecución", "Ruta crítica sin desvío no registrado", "100 % en hitos; replanificar, no parchar solo el flujo"],
            ["Alcance verificable", "Paquetes con evidencia de aceptación", "No cerrar hito sin evidencia; reapertura si puntaje < 4"],
            ["Techo presupuestario", "Desviación acumulada vs techo vigente", "Detener gasto no comprometido si desviación > 10 %"],
            ["Cambios bajo control", "Cambios constructivos con plan actualizado antes de construir", "Cero construcción sin registro"],
        ],
    )
    add_h(doc, "2.6 Indicadores operativos", level=2)
    add_table(
        doc,
        [
            ["Indicador", "Definición operativa", "Umbral / acción"],
            ["Defectos / líneas cambiadas", "Defectos del periodo sobre líneas modificadas", "≤ 5; cero bloqueos abiertos"],
            ["Tasa de reapertura (desarrollo)", "Ítems reabiertos / cerrados del sprint", "< 20 %"],
            ["Cumplimiento de sprint", "Historias comprometidas completadas", "≥ 80 %"],
            ["Trabajo en curso y bloqueos", "Tarjetas abiertas por persona; días en bloqueado", "Máx. 2/persona; > 5 días → reasignación formal"],
            ["Integridad de estados de kit", "Kits con hogar, responsable y estado coherente", "Sin cierre de hito si falla"],
            ["Atención de fallas y soporte", "Tiempos; consultas fuera del sistema; contención del canal", "Mejora tras tablero usable; baja contención congela ampliación"],
            ["Coordinación y datos en terreno", "Puntaje de contraparte; sync por lote", "Puntaje ≥ 4; sin ampliar alcance sin control de cambios"],
        ],
    )

    # ---- 3 Cambios ----
    add_h(doc, "3. Gestión del cambio")
    add_h(doc, "3.1 Enfoque", level=2)
    add_p(
        doc,
        "La gestión del cambio asegura que las modificaciones a alcance, plazo, costo o capacidad no alteren "
        "de facto el plan inicial. Toda solicitud relevante se identifica, evalúa (impacto, costo, tiempo, "
        "factibilidad y riesgo), decide y, si se aprueba, actualiza los instrumentos del plan antes de construirse "
        "(Project Management Institute [PMI], 2017). La prioridad no se define por la insistencia del solicitante, "
        "sino por el efecto sobre los hitos y el techo.",
    )
    add_h(doc, "3.2 Línea base previa a la ampliación de soporte asistido", level=2)
    add_p(
        doc,
        "La línea base del piloto contempla inventario, tablero, tickets y reporte; soporte predominantemente "
        "humano; presupuesto US$ 20.700; equipo de cuatro roles; límite de dos trabajos en curso por persona. "
        "La ampliación relevante a nivel de proyecto es la incorporación condicionada de priorización visual en "
        "el tablero, un canal de asistencia con preguntas frecuentes (fase 1) y un depósito mínimo de información "
        "operativa, con redimensionamiento presupuestario asociado.",
    )
    add_h(doc, "3.3 Eventualidades, estrategias y justificación", level=2)
    add_p(
        doc,
        "Se documentan las situaciones de cambio de nivel proyecto y la decisión informada.",
    )
    add_table(
        doc,
        [
            ["Eventualidad", "Estrategia adoptada", "Justificación respecto del plan inicial"],
            [
                "Evidencia fotográfica en cada ticket",
                "Rechazo de la formulación con archivo; aceptación condicionada de prioridad y nota textual",
                "La fotografía implica almacenamiento y esfuerzo que desplazan pruebas o reporte; la prioridad textual mejora la operación sin gasto nuevo",
            ],
            [
                "Segundo punto de acopio en la fecha del primer corte",
                "No implementación en la ventana del piloto",
                "El hito del 19 de octubre compromete un inventario validado; duplicar el punto altera alcance y arrastra el tablero",
            ],
            [
                "Servicio externo de pago para el reporte",
                "Rechazo; reporte con medios del equipo",
                "Gasto no comprometido y dependencia en semana de cierre",
            ],
            [
                "Reasignación informal ante bloqueos prolongados",
                "Regla formal: bloqueo > 5 días se resuelve o se reasigna entre los cuatro roles, actualizando el plan",
                "Evita divergencia entre flujo operativo y Project Libre/Excel",
            ],
            [
                "Priorización visual en el tablero",
                "Aprobación condicionada a capacidad; sin alterar estados del kit",
                "Reduce consultas informales; prerrequisito de un canal que escale a persona",
            ],
            [
                "Asistencia automatizada (FAQ y canal con escalamiento humano)",
                "Solo fase 1: condicionada a tablero usable, priorización visual, tope de API y corpus curado; no cierra tickets ni cambia estados sola",
                "Atiende presión de soporte sin app ciudadana ni reemplazo total del técnico",
            ],
            [
                "App ciudadana, monitoreo de flota con IA, modelo propio, lago de datos completo",
                "Identificación futura; rechazo en sep–dic 2026",
                "Exceden la EDT del piloto y el techo",
            ],
            [
                "Depósito mínimo de información operativa",
                "Condicionado a minimización, roles e ISO/IEC 27701; sin PII innecesaria en modelos externos",
                "Sostiene el canal y el reporte sin autorizar lakehouse empresarial",
            ],
        ],
    )
    add_h(doc, "3.4 Orden de adopción de cambios constructivos", level=2)
    add_p(doc, "1. Regla de capacidad y registro (permanente).")
    add_p(doc, "2. Priorización visual en el tablero (hacia el hito de noviembre).")
    add_p(doc, "3. Canal de asistencia fase 1 y depósito mínimo (tras tablero usable; no en semana de cierre).")
    add_p(doc, "4. Prioridad y nota en el ticket, solo si existe capacidad en el sprint del hito de diciembre.")
    add_p(
        doc,
        "5. Fuera de ventana: segundo punto de inventario, servicio externo de reporte, fotografía en ticket, "
        "app ciudadana, lago de datos completo y monitoreo de flota con IA.",
    )
    add_h(doc, "3.5 Efecto conjunto sobre costo, tiempo y esfuerzo", level=2)
    add_table(
        doc,
        [
            ["Dimensión", "Línea base", "Con paquete de cambios aprobado"],
            ["Presupuesto techo", "US$ 20.700", "US$ 21.200 (redimensionamiento propuesto)"],
            ["Partidas nuevas", "Sin API de modelo ni módulo de chat en el desglose inicial", "Orden US$ 200–340 (API y nube), con tope de control"],
            ["Fechas de hito", "19 oct / 9 nov / 4 dic / cierre", "Sin modificación de calendario"],
            ["Esfuerzo", "Cuatro roles; sin módulo de asistencia", "13 a 22 días-persona adicionales por sustitución de trabajo, no por ampliar plantilla"],
            ["Soporte", "Predominio de atención humana e informal", "Contención parcial por FAQ; escalamiento humano obligatorio"],
        ],
    )
    add_p(
        doc,
        "Decisión presupuestaria: la asistencia automatizada no se financia en silencio dentro de US$ 20.700. "
        "El equipo propone ampliar el techo autorizado a US$ 21.200. Alternativa: uso parcial de la contingencia "
        "del 12 % con acta. Reasignar recortando soporte humano en zona compleja no es la primera opción. "
        "Mientras no exista autorización, no se construye el módulo de asistencia.",
    )

    # ---- 4 Recursos ----
    add_h(doc, "4. Plan de asignación de recursos")
    add_h(doc, "4.1 Criterio general", level=2)
    add_p(
        doc,
        "La asignación de recursos identifica tipo, cantidad y disponibilidad de personas, presupuesto e "
        "infraestructura necesarios para ejecutar el plan y controlar su uso (PMI, 2017). El recurso crítico "
        "no exclusivo del equipo de software es el técnico local: su disponibilidad condiciona la veracidad "
        "del inventario y de los tickets.",
    )
    add_h(doc, "4.2 Recursos humanos", level=2)
    add_table(
        doc,
        [
            ["Rol", "Responsabilidad principal", "Efecto del paquete de cambios", "Mecanismo de control"],
            ["Dirección y frontend", "Alcance, control de cambios, interfaz", "Priorización visual e interfaz del canal", "Máx. 2 trabajos en curso; reasignación formal"],
            ["Backend / datos", "Inventario, tickets, integraciones", "Integración del canal y depósito mínimo", "Definition of Done; defectos y reapertura"],
            ["Infraestructura y nube", "Ambientes, accesos, gasto", "Topes de API y lectura de consumo", "Control quincenal; freno si desviación > 10 %"],
            ["Calidad e impacto", "Pruebas, reporte, traspaso", "Curaduría de FAQ y revisión de respuestas", "Evidencia de prueba en cada incremento"],
            ["Técnico / soporte local", "Estados en terreno y atención", "Menor carga informal; mantiene escalamiento", "Revisión de hito; no sustituible por automatización total"],
        ],
    )
    add_p(
        doc,
        "No se incorpora un quinto perfil ni un especialista externo en desarrollo agéntico en la ventana del "
        "piloto. La capacidad adicional se obtiene por reordenamiento del backlog, no por ampliación de dotación.",
    )
    add_h(doc, "4.3 Recursos financieros", level=2)
    add_table(
        doc,
        [
            ["Concepto", "Asignación", "Seguimiento"],
            ["Techo de línea base", "US$ 20.700", "Excel quincenal"],
            ["Techo propuesto con módulo de asistencia", "US$ 21.200", "Condición de construcción del módulo"],
            ["Contingencia (12 %)", "US$ 1.890", "Solo con razón escrita"],
            ["Consumo variable de modelo y nube", "Orden US$ 200–340; tope de API definido", "Consola de nube; pausa ante incumplimiento"],
            ["Horas de soporte humano", "Partida variable del plan", "No se vacía para financiar automatización"],
        ],
    )
    add_h(doc, "4.4 Recursos técnicos", level=2)
    add_p(
        doc,
        "Infraestructura en nube, API de modelo gestionado, kit de desarrollo de agentes, Project Libre, Trello, "
        "Excel y depósito mínimo de información. Quedan fuera de la ventana: GPU dedicado, lago de datos "
        "empresarial y hospedaje de modelo propio.",
    )
    add_h(doc, "4.5 Estrategias de viabilidad y rentabilidad", level=2)
    add_p(
        doc,
        "Viabilidad. Los cambios constructivos solo se incorporan si existe capacidad (sustitución de trabajo), "
        "si se respetan los hitos y si el financiamiento del módulo de asistencia está autorizado (techo "
        "redimensionado o contingencia con acta). El canal asistido no opera sin priorización visual ni sin "
        "corpus de preguntas frecuentes curado.",
    )
    add_p(
        doc,
        "Rentabilidad. No se declara un ahorro fijo en dólares en el acta sin medición. Se establece una línea "
        "base de consultas de soporte tras el tablero usable y antes de activar el canal; en operación se "
        "compara el costo de soporte evitado con el gasto real de API y nube. Si el gasto de automatización "
        "supera de forma sostenida el ahorro (dos revisiones consecutivas), se suspende el canal o se abre un "
        "nuevo control de cambios. Se distingue la inversión de puesta en marcha del gasto recurrente de operación.",
    )

    # ---- 5 Estado ----
    add_h(doc, "5. Estado actual del proyecto e información para partes interesadas")
    add_h(doc, "5.1 Audiencias y valor de la información", level=2)
    add_table(
        doc,
        [
            ["Parte interesada", "Información de valor", "Uso en la decisión"],
            ["Dirección / comisión del caso", "Hitos, techo, cambios abiertos y riesgos", "Autorizar redimensionamiento; condicionar o diferir el canal"],
            ["Contraparte / soporte local", "Usabilidad del tablero, cola, puntaje de hito", "Validar entregables; reducir trabajo informal"],
            ["Equipo de desarrollo", "Capacidad, calidad, registro de cambios", "Comprometer solo trabajo factible"],
            ["Inversores / donantes (vía reporte)", "Coherencia entre operación y cifra reportada", "Confianza en el informe de impacto"],
        ],
    )
    add_h(doc, "5.2 Estado consolidado", level=2)
    add_table(
        doc,
        [
            ["Dimensión", "Estado", "Observación para la gestión"],
            ["Periodo", "Piloto en ventana sep–dic 2026", "Cierre formal el 9 de diciembre"],
            ["Hito inventario", "Un inventario validado", "Segundo punto de acopio no incorporado"],
            ["Hito tablero", "Compromiso vigente", "Priorización visual condicionada a capacidad"],
            ["Hito tickets y reporte", "Compromiso vigente", "Asistencia automatizada solo condicionada y post tablero usable"],
            ["Presupuesto", "Línea base 20.700; propuesta 21.200", "Sin construcción del canal sin autorización"],
            ["Capacidad", "Cuatro roles; máx. dos trabajos en curso por persona", "Reasignación formal ante bloqueos prolongados"],
            ["Cambios condicionados", "Regla de capacidad; priorización visual; asistencia fase 1; depósito mínimo; prioridad textual", "Sujetos a capacidad y financiamiento"],
            ["Cambios rechazados o diferidos", "Fotografía en ticket; segundo inventario; servicio externo; app ciudadana; lago completo; monitoreo de flota con IA", "Registrados para evitar reingreso informal"],
            ["Calidad y privacidad", "Controles operativos activos; minimización de datos", "Sin bases reales en el repositorio"],
        ],
    )
    add_h(doc, "5.3 Cifras relevantes para la toma de decisiones", level=2)
    add_table(
        doc,
        [
            ["Indicador o cifra", "Valor de referencia", "Implicancia"],
            ["Techo línea base → propuesto", "20.700 → 21.200", "Condición de viabilidad del canal asistido"],
            ["Costo variable estimado del canal", "US$ 200–340 (orden); tope de API acotado", "Control de factura y pausa ante desvío"],
            ["Esfuerzo adicional estimado", "13–22 días-persona", "Exige sustitución de alcance, no contratación"],
            ["Umbral de desviación de gasto", "> 10 %", "Detención de gasto no comprometido"],
            ["Límite de trabajo en curso", "2 por persona", "Protección de calidad e integración"],
            ["Puntaje mínimo de hito", "4 / 5", "Reapertura del corte si no se alcanza"],
        ],
    )
    add_h(doc, "5.4 Síntesis para dirección", level=2)
    add_p(
        doc,
        "El plan inicial permanece como referencia única: los hitos no se modifican por acumulación informal "
        "de alcance. Se solicita autorización para redimensionar el techo a US$ 21.200 si se incorpora la "
        "asistencia automatizada en fase 1. El orden técnico es priorización visual antes del canal asistido; "
        "este último no sustituye al soporte humano. La rentabilidad se verificará con línea base de consultas "
        "versus consumo de nube. Las ampliaciones de producto (aplicación ciudadana, lago de datos completo, "
        "monitoreo de flota) permanecen fuera de la ventana y exigen un nuevo ciclo de control de cambios.",
    )

    add_h(doc, "6. Conclusiones")
    add_p(
        doc,
        "El sistema de monitoreo y control articula herramientas de planificación, flujo de trabajo, seguimiento "
        "financiero e indicadores estratégicos y operativos, con hitos explícitos y flujo de información trazable. "
        "La gestión del cambio documenta eventualidades de nivel proyecto, estrategias aplicadas y justificación "
        "orientada a la integridad del plan. El plan de recursos prioriza la capacidad humana limitada, el techo "
        "financiero y la infraestructura cloud, con criterios de viabilidad y rentabilidad medibles. El estado "
        "reportado a las partes interesadas concentra las cifras y decisiones que habilitan o detienen la "
        "ampliación de soporte asistido sin comprometer los cortes del piloto.",
    )

    add_h(doc, "Referencias")
    add_p(
        doc,
        "Project Management Institute. (2017). Guía de los fundamentos para la dirección de proyectos "
        "(Guía del PMBOK) (6.ª ed.). Project Management Institute.",
    )
    add_p(
        doc,
        "Peters, L. J. (2024). Software project management: Methods and techniques. "
        "CRC Press, Taylor & Francis Group.",
    )

    add_h(doc, "Anexo A. Correspondencia con indicadores de evaluación del informe")
    add_table(
        doc,
        [
            ["Indicador de evaluación", "Contenido", "Sección"],
            ["IE1 — Sistema de monitoreo y control, flujos e hitos", "Componentes, flujo, hitos, indicadores", "§2"],
            ["IE3 — Estrategias de gestión del cambio, problemáticas y justificación", "Eventualidades, estrategias, orden, efecto conjunto", "§3"],
            ["IE5 — Plan de asignación de recursos, viabilidad y rentabilidad", "Humanos, financieros, técnicos, estrategias", "§4"],
            ["IE7 — Estado actual e información de valor", "Audiencias, estado, cifras, síntesis", "§5"],
        ],
    )

    OUT_REPO.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(OUT_REPO))
    shutil.copy2(OUT_REPO, OUT_DL)
    print(f"OK: {OUT_REPO}")
    print(f"OK: {OUT_DL}")
    print(f"paras={len(doc.paragraphs)} tables={len(doc.tables)}")
    blob = "\n".join(p.text for p in doc.paragraphs)
    for bad in ["REQ-01", "SOP-01", "UX-01", "DAT-01", "CAP-01", "WhatsApp", "en simple"]:
        print(("LEAK" if bad in blob else "clean"), bad)


if __name__ == "__main__":
    main()
