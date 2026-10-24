# -*- coding: utf-8 -*-
"""Genera el alcance/EDT interno y el informe ejecutivo (máx. 7 planas)."""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

sys.path.insert(0, str(Path(__file__).parent))
from eva01_schedule import OUT as OUT_PLAN, run  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evaluaciones" / "eva-01" / "informe"

MESES = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
]
NAVY = RGBColor(0x10, 0x26, 0x3D)
AMBER = RGBColor(0xE5, 0x9A, 0x24)
MUTED = RGBColor(0x55, 0x55, 0x55)
MARCA = ROOT / "evaluaciones" / "eva-01" / "marca" / "final"


def fecha(d: date) -> str:
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def isotipo_png() -> Path:
    """Rasteriza el isotipo para Word (no incrusta SVG)."""
    from PIL import Image, ImageDraw

    path = MARCA / "kiran-isotipo.png"
    size = 900
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    scale = size / 240.0

    def xy(x, y):
        return (x * scale, y * scale)

    navy = (0x10, 0x26, 0x3D, 255)
    amber = (0xE5, 0x9A, 0x24, 255)
    draw.rounded_rectangle(
        [50 * scale, 28 * scale, 92 * scale, 212 * scale],
        radius=10 * scale,
        fill=navy,
    )
    draw.polygon([xy(91, 120), xy(198, 38), xy(198, 96), xy(99, 118)], fill=amber)
    draw.polygon([xy(91, 120), xy(198, 202), xy(198, 144), xy(99, 122)], fill=amber)
    rad = 9 * scale
    cx, cy = 92 * scale, 120 * scale
    draw.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=amber)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG")
    return path


def set_cell_margins(cell, **cm_kwargs):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement("w:tcMar")
    for edge, value in cm_kwargs.items():
        node = OxmlElement(f"w:{edge}")
        node.set(qn("w:w"), str(int(value * 567)))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders_none(tbl) -> None:
    tbl_el = tbl._tbl
    tblPr = tbl_el.tblPr
    if tblPr is None:
        tblPr = OxmlElement("w:tblPr")
        tbl_el.insert(0, tblPr)
    for child in list(tblPr):
        if child.tag == qn("w:tblBorders"):
            tblPr.remove(child)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        el.set(qn("w:sz"), "0")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "auto")
        borders.append(el)
    tblPr.append(borders)


def color_bar(doc, hex_color: str, height_pt: float = 8, width_cm: float = 16.0):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_borders_none(tbl)
    cell = tbl.cell(0, 0)
    cell.width = Cm(width_cm)
    set_cell_shading(cell, hex_color)
    set_cell_margins(cell, top=0, bottom=0, left=0, right=0)
    para = cell.paragraphs[0]
    para.paragraph_format.space_before = Pt(0)
    para.paragraph_format.space_after = Pt(0)
    para.paragraph_format.line_spacing = 1.0
    run = para.add_run(" ")
    set_run_font(run, size=height_pt)
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(0)
    spacer.paragraph_format.line_spacing = 1.0


def add_bottom_border(paragraph, color="10263D"):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:space"), "6")
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.append(pBdr)


def set_start_page(section, start: int = 1):
    sectPr = section._sectPr
    for child in list(sectPr):
        if child.tag == qn("w:pgNumType"):
            sectPr.remove(child)
    pg_num = OxmlElement("w:pgNumType")
    pg_num.set(qn("w:start"), str(start))
    sectPr.append(pg_num)


def configure_page(section) -> None:
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)


def clear_header_footer(section) -> None:
    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False
    section.header.paragraphs[0].clear()
    section.footer.paragraphs[0].clear()


def set_run_font(run, size=12, bold=False, italic=False, color=None, name="Times New Roman"):
    run.font.name = name
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:cs"), name)
    rFonts.set(qn("w:eastAsia"), name)


def apply_normal_style(doc: Document) -> None:
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.5
    style.paragraph_format.space_after = Pt(6)
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.get_or_add_rFonts()
    rFonts.set(qn("w:ascii"), "Times New Roman")
    rFonts.set(qn("w:hAnsi"), "Times New Roman")


def fill_body_chrome(section, header_text: str) -> None:
    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False
    hp = section.header.paragraphs[0]
    hp.clear()
    hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = hp.add_run(header_text)
    set_run_font(r, size=9, color=MUTED)
    fp = section.footer.paragraphs[0]
    fp.clear()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = fp.add_run("Kiran - ")
    set_run_font(r1, size=9, color=MUTED)
    add_page_field(fp)


def setup_section(doc: Document) -> None:
    sec = doc.sections[0]
    configure_page(sec)
    fill_body_chrome(sec, "Kiran - Plan preliminar del piloto - uso interno de dirección")
    apply_normal_style(doc)


def add_page_field(paragraph) -> None:
    run = paragraph.add_run()
    set_run_font(run, size=9, color=RGBColor(0x55, 0x55, 0x55))
    fld1 = OxmlElement("w:fldChar")
    fld1.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld2 = OxmlElement("w:fldChar")
    fld2.set(qn("w:fldCharType"), "end")
    run._r.append(fld1)
    run._r.append(instr)
    run._r.append(fld2)


def p(doc, text, *, size=12, bold=False, italic=False, align="justify", space_after=6, first_line=True):
    para = doc.add_paragraph()
    if align == "justify":
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    elif align == "center":
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == "left":
        para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    para.paragraph_format.line_spacing = 1.5
    para.paragraph_format.space_after = Pt(space_after)
    para.paragraph_format.space_before = Pt(0)
    if first_line and align == "justify":
        para.paragraph_format.first_line_indent = Cm(0.75)
    run = para.add_run(text)
    set_run_font(run, size=size, bold=bold, italic=italic)
    return para


def h(doc, text, level=1):
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    para.paragraph_format.line_spacing = 1.15
    para.paragraph_format.space_before = Pt(10 if level == 1 else 8)
    para.paragraph_format.space_after = Pt(4)
    para.paragraph_format.first_line_indent = Cm(0)
    run = para.add_run(text)
    set_run_font(run, size=13 if level == 1 else 12, bold=True, color=NAVY)
    if level == 1:
        add_bottom_border(para)
    return para


def set_cell_shading(cell, hex_color: str) -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag == qn("w:shd"):
            tcPr.remove(child)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def table(doc, headers, rows, col_widths=None, header_fill="10263D"):
    tbl = doc.add_table(rows=1 + len(rows), cols=len(headers))
    tbl.style = "Table Grid"
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = True
    for i, head in enumerate(headers):
        cell = tbl.rows[0].cells[i]
        cell.text = ""
        para = cell.paragraphs[0]
        para.paragraph_format.space_after = Pt(0)
        para.paragraph_format.space_before = Pt(0)
        para.paragraph_format.line_spacing = 1.0
        run = para.add_run(head)
        set_run_font(run, size=9, bold=True, color=RGBColor(255, 255, 255))
        set_cell_shading(cell, header_fill)
    for r_i, row in enumerate(rows):
        for c_i, val in enumerate(row):
            cell = tbl.rows[r_i + 1].cells[c_i]
            cell.text = ""
            para = cell.paragraphs[0]
            para.paragraph_format.space_after = Pt(0)
            para.paragraph_format.space_before = Pt(0)
            para.paragraph_format.line_spacing = 1.0
            run = para.add_run(str(val))
            set_run_font(run, size=9)
            if r_i % 2 == 1:
                set_cell_shading(cell, "F2F2F2")
    if col_widths:
        for row in tbl.rows:
            for i, w in enumerate(col_widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return tbl


def caption(doc, text):
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para.paragraph_format.space_before = Pt(2)
    para.paragraph_format.space_after = Pt(8)
    para.paragraph_format.line_spacing = 1.0
    para.paragraph_format.first_line_indent = Cm(0)
    run = para.add_run(text)
    set_run_font(run, size=9, italic=True, color=RGBColor(0x44, 0x44, 0x44))


def ref(doc, text):
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    para.paragraph_format.left_indent = Cm(1.25)
    para.paragraph_format.first_line_indent = Cm(-1.25)
    para.paragraph_format.line_spacing = 1.5
    para.paragraph_format.space_after = Pt(4)
    run = para.add_run(text)
    set_run_font(run, size=12)


def save_docx(doc, name: str) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    try:
        doc.save(path)
    except PermissionError:
        path = OUT / name.replace(".docx", "-actualizado.docx")
        doc.save(path)
    return path


def by_code(tasks, code):
    return next(t for t in tasks if t.code == code)


def build_informe(info) -> Path:
    tasks = info["tasks"]
    end = info["end"]
    start = info["start"]
    days = info["finish_days"]
    t11 = by_code(tasks, "1.1")
    t23 = by_code(tasks, "2.3")
    t31 = by_code(tasks, "3.1")
    t44 = by_code(tasks, "4.4")
    t52 = by_code(tasks, "5.2")
    t53 = by_code(tasks, "5.3")
    t54 = by_code(tasks, "5.4")
    t64 = by_code(tasks, "6.4")
    t73 = by_code(tasks, "7.3")
    m_inv = by_code(tasks, "8.1")
    m_tab = by_code(tasks, "8.2")
    m_tick = by_code(tasks, "8.3")
    m_rep = by_code(tasks, "8.4")
    m_fin = by_code(tasks, "8.5")

    doc = Document()
    apply_normal_style(doc)
    cover = doc.sections[0]
    configure_page(cover)
    cover.top_margin = Cm(2.2)
    cover.bottom_margin = Cm(2.2)
    clear_header_footer(cover)

    color_bar(doc, "10263D", height_pt=12)
    color_bar(doc, "E59A24", height_pt=5)

    gap = doc.add_paragraph()
    gap.paragraph_format.space_before = Pt(28)
    gap.paragraph_format.space_after = Pt(0)

    logo_p = doc.add_paragraph()
    logo_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    logo_p.paragraph_format.space_after = Pt(10)
    logo_p.paragraph_format.first_line_indent = Cm(0)
    logo_p.add_run().add_picture(str(isotipo_png()), width=Cm(3.8))

    brand = doc.add_paragraph()
    brand.alignment = WD_ALIGN_PARAGRAPH.CENTER
    brand.paragraph_format.space_after = Pt(4)
    brand.paragraph_format.first_line_indent = Cm(0)
    set_run_font(brand.add_run("KIRAN"), size=28, bold=True, color=NAVY, name="Arial")

    promise = doc.add_paragraph()
    promise.alignment = WD_ALIGN_PARAGRAPH.CENTER
    promise.paragraph_format.space_after = Pt(18)
    promise.paragraph_format.first_line_indent = Cm(0)
    set_run_font(
        promise.add_run("Visibilidad que mantiene la energía activa."),
        size=13,
        italic=True,
        color=NAVY,
    )

    kicker = doc.add_paragraph()
    kicker.alignment = WD_ALIGN_PARAGRAPH.CENTER
    kicker.paragraph_format.space_after = Pt(2)
    kicker.paragraph_format.first_line_indent = Cm(0)
    set_run_font(kicker.add_run("PLAN PRELIMINAR"), size=11, bold=True, color=AMBER, name="Arial")

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.paragraph_format.space_after = Pt(4)
    title.paragraph_format.first_line_indent = Cm(0)
    set_run_font(
        title.add_run("Piloto de operación de kits solares"),
        size=16,
        bold=True,
        color=NAVY,
    )

    org = doc.add_paragraph()
    org.alignment = WD_ALIGN_PARAGRAPH.CENTER
    org.paragraph_format.space_after = Pt(14)
    org.paragraph_format.first_line_indent = Cm(0)
    set_run_font(
        org.add_run("Empresa social de energía solar comunitaria. Comunidad piloto, India"),
        size=11,
        color=MUTED,
    )

    facts = doc.add_paragraph()
    facts.alignment = WD_ALIGN_PARAGRAPH.CENTER
    facts.paragraph_format.space_after = Pt(18)
    facts.paragraph_format.first_line_indent = Cm(0)
    set_run_font(
        facts.add_run(
            f"{fecha(start)} a {fecha(end)}. {days} días hábiles. US$ 20.700"
        ),
        size=12,
        color=NAVY,
    )

    table(
        doc,
        ["Equipo", "Rol en el piloto"],
        [
            ["Giannina Guerrero", "Directora del proyecto y frontend"],
            ["Nicolás Barra", "Backend e inventario"],
            ["Ari Araya", "Infraestructura y nube"],
            ["Skarlett Tropan", "Calidad e impacto"],
        ],
        col_widths=[8.0, 8.0],
    )

    academic = doc.add_paragraph()
    academic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    academic.paragraph_format.space_before = Pt(18)
    academic.paragraph_format.space_after = Pt(2)
    academic.paragraph_format.first_line_indent = Cm(0)
    set_run_font(
        academic.add_run(
            "GPY1102 Gestión de Proyectos de Software  ·  Docente: Juan Bautista Sáez Fernández"
        ),
        size=10,
        color=MUTED,
    )

    campus = doc.add_paragraph()
    campus.alignment = WD_ALIGN_PARAGRAPH.CENTER
    campus.paragraph_format.space_after = Pt(10)
    campus.paragraph_format.first_line_indent = Cm(0)
    set_run_font(
        campus.add_run("Duoc UC · Sede Puente Alto · jornada vespertina"),
        size=10,
        color=MUTED,
    )

    use = doc.add_paragraph()
    use.alignment = WD_ALIGN_PARAGRAPH.CENTER
    use.paragraph_format.space_before = Pt(8)
    use.paragraph_format.first_line_indent = Cm(0)
    set_run_font(
        use.add_run("Documento de uso interno para dirección"),
        size=10,
        italic=True,
        color=MUTED,
    )

    body = doc.add_section(WD_SECTION.NEW_PAGE)
    configure_page(body)
    fill_body_chrome(body, "Kiran - Plan preliminar del piloto - uso interno de dirección")
    set_start_page(body, 1)

    h(doc, "1. Contexto, necesidad de negocio y autorización")
    p(
        doc,
        "La empresa social trabaja en una comunidad de India donde la energía no es confiable. "
        "Eso afecta la escuela, la salud y el trabajo, y mantiene la dependencia de combustibles "
        "fósiles. La respuesta física ya está en marcha: kits solares en un piloto. Kiran no "
        "reemplaza esos kits; es el software que permite ver si cada kit sigue entregando luz.",
    )
    p(
        doc,
        "Hoy puede pasar esto: el panel está en el techo y, en el informe, sigue figurando como "
        "activo. La falla existe, pero no queda registrada. Quien repara no sabe a cuál ir. Quien "
        "financia recibe un número que ya no corresponde. El proyecto nace para corregir esa "
        "desinformación operativa.",
    )
    p(
        doc,
        "Kiran tiene fecha de inicio y de término. Cuando el técnico atienda tickets todos los "
        "días, eso deja de ser proyecto y pasa a ser operación. Si no se escribe esa frontera, "
        "el alcance se hincha y parece que este equipo viniera a electrificar la región.",
    )
    p(
        doc,
        "El acta autoriza el piloto de software (no una fábrica de paneles) y nombra a Giannina "
        f"Guerrero como directora, con un techo de US$ 20.700. Con ella trabajan Nicolás Barra "
        f"(backend), Ari Araya (nube) y Skarlett Tropan (calidad e impacto). El trabajo corre "
        f"del {fecha(start)} al {fecha(end)}: {days} días hábiles. Empujan este plan la dirección "
        "de la empresa social, inversores y donantes, el soporte local, el partner tecnológico y, "
        "de forma indirecta, los hogares. En esta fase las familias no usan la aplicación. Los "
        "riesgos que ya se ven: poca señal, datos incompletos y que el tablero no se use en terreno.",
    )
    table(
        doc,
        ["Campo del acta", "Definición para este piloto"],
        [
            ["Propósito", "Construir Kiran para una comunidad piloto: inventario, tablero, mantención y reporte."],
            ["Objetivos medibles", "Ningún kit fantasma en el activo; tickets desde una falla real; primer reporte el " + fecha(t54.finish_date) + "."],
            ["Presupuesto resumido", "US$ 20.700, con 12 % de contingencia. Lo ya gastado no entra."],
            ["Hitos resumidos", "Inventario " + fecha(m_inv.finish_date) + "; tablero " + fecha(m_tab.finish_date) + "; reporte " + fecha(m_rep.finish_date) + "; cierre " + fecha(end) + "."],
            ["Criterio de aprobación", "El patrocinador acepta el primer reporte con datos reales. Un kit dado de baja deja de contar como activo."],
        ],
        col_widths=[4.2, 11.8],
    )
    caption(doc, "Tabla 1. Extracto del acta de constitución. Autoriza el piloto; no reemplaza el plan.")
    table(
        doc,
        ["Persona", "Rol en Kiran", "Qué sostiene en el desarrollo"],
        [
            ["Giannina Guerrero", "Directora del proyecto y frontend", "Acta, alcance, tablero y relación con dirección"],
            ["Nicolás Barra", "Backend", "Datos, inventario, tickets y tratamiento de hogares"],
            ["Ari Araya", "Infraestructura y nube", "Ambientes, despliegue, accesos y hosting"],
            ["Skarlett Tropan", "Calidad e impacto", "Pruebas, reportes a patrocinadores y capacitación"],
        ],
        col_widths=[3.6, 4.6, 7.8],
    )
    caption(doc, "Tabla 2. Equipo de desarrollo del piloto.")

    h(doc, "2. Propuesta de valor y mejora sobre la solución del caso")
    p(
        doc,
        "Dirección ya pidió inventario, tablero, mantención y reportes. Copiar esa lista no basta. "
        "Hay que decir qué mejora Kiran respecto de una planilla o un grupo de WhatsApp.",
        first_line=True,
    )
    p(
        doc,
        "La promesa del piloto es dar visibilidad para mantener la energía activa. Cada kit "
        "queda con un estado actualizado. Las fallas se convierten en tickets asignables y el "
        "informe a donantes se alimenta de operación real, no de un ensayo de pantalla. El valor "
        "está en que un kit dado de baja deje de contar como activo, en que el técnico priorice "
        "lo que realmente está caído y en que un inversor pueda creer el reporte (PMI, 2021, "
        "7.ª ed.). Si el software funciona y el técnico no lo abre, el piloto igual puede verse "
        "como un fracaso.",
        first_line=True,
    )
    table(
        doc,
        ["Problemática de negocio", "Qué no resuelve el kit solo", "Cómo Kiran mejora la solución"],
        [
            [
                "Falta de energía confiable",
                "Un kit instalado y en silencio no ilumina: la falla no se ve ni se atiende",
                "Estados activo / falla / baja + ticket desde el kit: el técnico prioriza lo que de verdad está caído",
            ],
            [
                "Desarrollo económico limitado",
                "Sin energía estable no hay escuela ni taller; sin dato, la dirección no sabe dónde intervenir",
                "Tablero simple para soporte local: menos tiempo buscando el kit, más tiempo reparando",
            ],
            [
                "Dependencia de fósiles",
                "Si el kit inactivo sigue en el inventario, el piloto miente el desplazamiento de diésel",
                "La baja saca el kit del activo. El reporte de impacto no cuenta fantasmas",
            ],
        ],
        col_widths=[3.6, 6.2, 6.2],
    )
    caption(doc, "Tabla 3. De la problemática de negocio a lo que Kiran mejora (sin fabricar paneles).")
    table(
        doc,
        ["Interesado", "Trabajo que necesita hacer", "Dolor hoy", "Valor que le entrega el piloto"],
        [
            [
                "Soporte local",
                "Encontrar y reparar kits",
                "Lista informal, WhatsApp, no sabe qué está en falla",
                "Tablero y ticket asignable, pensados para el técnico en terreno",
            ],
            [
                "Dirección / empresa social",
                "Operar el piloto y no mentir el activo",
                "Kits instalados que dejan de aparecer en el seguimiento",
                "Inventario vivo: activo, falla o baja, con dueño (hogar)",
            ],
            [
                "Inversores y donantes",
                "Ver evidencia de impacto",
                "Informes de intención, sin dato de operación",
                "Reporte periódico alimentado por tickets y estados reales",
            ],
            [
                "Comunidad / hogares",
                "Tener luz que dure",
                "Esperan sin visibilidad de la falla",
                "Efecto esperado: menos horas sin energía si la mantención se prioriza (indirecto)",
            ],
        ],
        col_widths=[3.2, 3.6, 4.4, 4.8],
    )
    caption(doc, "Tabla 4. Propuesta de valor por interesado.")
    p(
        doc,
        "Sobre el pedido original no se agrega una app para cada familia ni sensores masivos. "
        "Lo que sí se agrega, sin salir del piloto, es la cadena kit-estado-ticket-indicador, "
        "la carga por lotes cuando no hay señal, y el cuidado de quién ve datos de un hogar.",
        first_line=True,
    )

    h(doc, "3. Alcance, EDT, cronograma, recursos y costos")
    p(
        doc,
        "El producto es Kiran: un sistema web para una comunidad piloto, con carga por lotes "
        "si la red falla. Lo damos por bueno si se cumplen tres cosas. Uno: cada kit tiene hogar "
        "y estado (activo, en falla o dado de baja), y la baja saca el kit del activo. Dos: un "
        "ticket nace desde un kit en falla y se puede asignar al soporte local. Tres: un reporte "
        "mensual exportable llega a patrocinadores con datos de operación real, no de una demostración vacía.",
        first_line=True,
    )
    p(
        doc,
        "Entregamos los cuatro módulos, un documento de roles y privacidad, una capacitación "
        "corta al soporte local, este plan y la línea base en Project Libre. Lo que aprieta: "
        "US$ 20.700, cuatro personas más un técnico local, la conectividad y la fecha del primer "
        "reporte a donantes. Damos por cierto, mientras no se demuestre lo contrario, que hay "
        "comunidad piloto, que hay al menos un técnico, que los inversores aceptan indicadores "
        "simples y que existe un procedimiento de carga sin señal permanente. Si uno de esos "
        "supuestos cae, deja de ser sorpresa y pasa a ser un riesgo.",
    )
    p(
        doc,
        "Queda fuera, a propósito: fabricar o instalar paneles, tendido eléctrico, microfinanzas, "
        "expansión a otras regiones, una app ciudadana y la operación continua después del piloto. "
        "Lo que no está en la EDT no se hace. Si alguien lo pide después, entra por control de cambios.",
    )
    p(
        doc,
        "Antes de llenar el inventario con campos de oficina, vamos a preguntar por separado al "
        "técnico, al partner y a dirección (técnica Delphi: consenso en anónimo, para que no gane "
        "solo quien habla más fuerte en la reunión).",
        first_line=True,
    )

    table(
        doc,
        ["EDT", "Cuenta de control", "Paquetes de trabajo"],
        [
            ["1", "Dirección del proyecto", "1.1 Acta e interesados; 1.2 Plan y línea base; 1.3 Riesgos y comunicación"],
            ["2", "Inventario de kits y hogares", "2.1 Modelo de datos; 2.2 Estados; 2.3 Carga inicial; 2.4 Validación local"],
            ["3", "Tablero operativo", "3.1 Vista general; 3.2 Vista individual; 3.3 Indicadores; 3.4 Ajustes de usabilidad"],
            ["4", "Monitoreo, tickets y mantención", "4.1 Rendimiento; 4.2 Flujo de tickets; 4.3 Asignación; 4.4 Prueba en terreno"],
            ["5", "Impacto y reportes", "5.1 Indicadores; 5.2 Informe periódico; 5.3 Exportación; 5.4 Primera entrega"],
            ["6", "Privacidad, accesos y despliegue", "6.1 Roles; 6.2 Datos de hogares; 6.3 Ambiente; 6.4 Puesta en marcha"],
            ["7", "Capacitación y transición", "7.1 Material; 7.2 Taller; 7.3 Traspaso operativo"],
        ],
        col_widths=[1.5, 5.2, 9.3],
    )
    caption(doc, "Tabla 5. EDT de primer nivel (el 100 % del trabajo acordado).")

    p(
        doc,
        "La EDT cubre el 100 % del trabajo del piloto. La estructura sola no alcanza: cada paquete "
        "necesita ficha (criterio, responsable, duración y costo). Acá van dos de la ruta crítica:",
        first_line=True,
    )
    table(
        doc,
        ["Campo", "2.3 Carga inicial del piloto", "3.1 Vista general de la comunidad"],
        [
            ["Cuenta de control", "2 Inventario", "3 Tablero operativo"],
            ["Responsable", "Nicolás Barra (backend) + soporte local", "Giannina Guerrero (directora / frontend)"],
            [
                "Criterio de aceptación",
                "Los kits del piloto están cargados con hogar, comunidad y estado inicial verificable.",
                "El técnico ve, en una pantalla, recuento de kits por estado y acceso al detalle.",
            ],
            ["Supuesto", "El técnico entrega el listado maestro a tiempo.", "La carga 2.3 ya ocurrió; si no, el tablero es una demo vacía."],
            ["Duración", f"{t23.dur} días hábiles", f"{t31.dur} días hábiles"],
            ["Hito asociado", f"Inventario validado ({fecha(m_inv.finish_date)})", f"Tablero usable ({fecha(m_tab.finish_date)})"],
            ["Costo directo est.", "US$ 1.240 (carga + validación parcial)", "US$ 1.360 (frontend del tablero)"],
        ],
        col_widths=[3.4, 6.3, 6.3],
    )
    caption(doc, "Tabla 6. Extracto del diccionario de la EDT.")

    p(
        doc,
        "El calendario se armó dos veces. La primera, con duraciones brutas, como si hubiera "
        "gente de sobra. La segunda, con dependencias de término a inicio y semana de lunes a "
        "viernes. El número que defendemos es el segundo. El criterio es el camino más largo "
        "(método de la ruta crítica, CPM), no lo que se siente más urgente. Sin modelo ni carga de inventario no hay tablero "
        "con datos reales. Sin vista de cada kit no hay ticket útil. Sin prueba en terreno el "
        f"reporte a donantes queda sin dato real. Esa cadena (1.1, 2.1, 2.2, 2.3, 3.1, 3.2, "
        f"4.2, 4.3, 4.4, 5.4 y 7.3) dura {days} días hábiles ({fecha(start)} al {fecha(end)}). "
        "Cualquier atraso ahí mueve el 9 de diciembre, salvo que se consuma reserva "
        "(capacidad no comprometida del sprint o PERT de 4.4). La holgura de los otros "
        "caminos no salva a esta cadena: holgura y reserva no son lo mismo.",
        first_line=True,
    )
    table(
        doc,
        ["Camino", "Secuencia", "Duración (días)", "Holgura (días)", "¿Crítica?"],
        [
            [
                "A Inventario-tablero-tickets",
                "1.1-2.1-2.2-2.3-3.1-3.2-4.2-4.3-4.4-5.4-7.3",
                str(days),
                "0",
                "Sí",
            ],
            [
                "B Privacidad y despliegue",
                "1.1-6.1-6.2-6.3-6.4 (4.4 espera a 4.3, no a 6.4)",
                "23",
                str(t64.slack),
                "No",
            ],
            [
                "C Indicadores de impacto",
                "1.1-5.1-5.2-5.3 (5.4 espera la prueba 4.4)",
                "17",
                str(t53.slack),
                "No",
            ],
        ],
        col_widths=[3.6, 5.4, 2.4, 2.4, 2.2],
    )
    caption(
        doc,
        "Tabla 7. Duración del camino y holgura son columnas distintas. La holgura sale del CPM "
        f"(paquete 6.4 = {t64.slack} d; 5.2/5.3 = {t52.slack} d), no de la suma de duraciones.",
    )
    p(
        doc,
        "Holgura y reserva se distinguen como en industria (PMI, 2017). La holgura es el tiempo "
        "que una actividad puede atrasarse sin mover el 9 de diciembre: 0 en la ruta crítica; "
        f"{t64.slack} días en 6.4 (privacidad/despliegue); {t53.slack} días en 5.2 y 5.3 "
        "(indicadores). El camino C dura 17 días: esa suma no es la holgura. En el camino B "
        f"duración y holgura coinciden en {t64.slack}; no hay que generalizar esa coincidencia. "
        "El margen de fallo de la cadena crítica se diseña aparte, como reserva de contingencia "
        "de tiempo: PERT en 4.4 ya incorpora el escenario pesimista (desviación de unos 1,3 días); "
        "cada sprint Scrum compromete 8 de 10 días hábiles (20 % de capacidad libre); si una "
        "historia no alcanza, vuelve al backlog y el timebox no se estira. El 12 % de "
        "contingencia de costo cubre un alargue de terreno (hosting y horas locales). No se "
        "mueve el 4 de diciembre.",
        first_line=True,
    )
    p(
        doc,
        "La prueba 4.4 es el caso típico de esa reserva estadística: 5 / 7 / 13 días; "
        "(5 + 4×7 + 13) / 6 = 7,67 y en el Gantt quedan 8. A dirección, hitos. Al equipo, "
        "el Gantt de Project Libre.",
        first_line=True,
    )
    table(
        doc,
        ["Hito", "Fecha", "Para quién"],
        [
            [f"Inventario validado", fecha(m_inv.finish_date), "Equipo y soporte local"],
            [f"Tablero usable", fecha(m_tab.finish_date), "Técnico local y dirección"],
            [f"Tickets en terreno", fecha(m_tick.finish_date), "Soporte local"],
            [f"Primer reporte al patrocinador", fecha(m_rep.finish_date), "Inversores y donantes"],
            [f"Piloto entregado", fecha(m_fin.finish_date), "Dirección / cierre de fase"],
        ],
        col_widths=[6.5, 4.5, 5.0],
    )
    caption(doc, "Tabla 8. Cronograma de hitos (para dirección).")

    p(
        doc,
        "En personas: Giannina (dirección y tablero), Nicolás (datos e inventario), Ari (nube y "
        "despliegue), Skarlett (calidad e impacto) y un técnico local a 0,4 FTE. Ese técnico es "
        "el recurso más frágil. Si no carga datos, la ruta crítica se rompe aunque el código esté "
        "listo. El desglose de recursos (RBS) se arma en dos tiempos: primero el tipo (personas, "
        "tecnología, instalaciones, financieros) y después la cantidad. Personas: cuatro del "
        "equipo más el técnico a 0,4 FTE. Tecnología: nube, repositorio, Project Libre, Trello. "
        "Instalaciones: punto de carga en la comunidad. El hosting se mueve con el uso (es costo "
        "variable y a la vez directo) y por eso entra a la contingencia del 12 %. El estudio de "
        "terreno ya pagado (US$ 2.800) no entra a los 20.700 y no decide si seguimos o no.",
        first_line=True,
    )
    table(
        doc,
        ["Tipo de costo", "Ejemplo en el piloto", "Cómo se trata"],
        [
            ["Fijo", "Remuneración de la directora (0,5 FTE × 3 meses)", "No se mueve con el número de kits. También es directo."],
            ["Variable", "Hosting y horas de soporte local según uso", "Sube con el volumen; entra a la contingencia."],
            ["Directo", "Equipo de desarrollo, nube del piloto, taller", "Se atribuye a este piloto (incluye lo fijo del equipo)."],
            ["Indirecto", "Cuota de administración / PMO de la empresa social", "Se prorratea; no es una partida extra del Gantt."],
            ["De oportunidad", "No construir un módulo de cobro (excluido)", "Valor de la alternativa no elegida; no sale caja."],
            ["Hundido", "Estudio de terreno ya pagado (US$ 2.800)", "Fuera del techo. No decide continuar o parar."],
        ],
        col_widths=[3.2, 6.4, 6.4],
    )
    caption(
        doc,
        "Tabla 9. Clasificación de costos: un mismo gasto puede ser, a la vez, fijo y directo. "
        "Las filas no se suman entre sí. Techo autorizado: US$ 20.700 (base del piloto + 12 % "
        "de contingencia = US$ 1.890). Hundidos excluidos.",
    )

    h(doc, "4. Factores ambientales, estándares e impacto en el caso")
    p(
        doc,
        "Hay condiciones que este equipo no maneja y igual entran al plan: la fecha que pide un "
        "donante, la señal del pueblo, los datos de una familia. El PMBOK 6.ª las llama factores "
        "ambientales de la empresa, o EEF (PMI, 2017). Por dentro nos aprietan el tamaño del equipo, una "
        "nube que todavía no es de la organización y una estructura donde conviven empresa social, "
        "partner y desarrollo. Por fuera, el financiamiento mixto, la distancia con la comunidad "
        "y el marco de privacidad. Lo que sí podemos usar (plantillas de acta y EDT, Trello y este "
        "documento) son activos de la organización (OPA). Un donante que adelanta el reporte comprime la actividad 5.4. Un técnico "
        "que no carga datos rompe la 2.3 y, con ella, toda la ruta crítica. Por eso los canales se "
        "declaran ahora, no al cierre.",
        first_line=True,
    )
    table(
        doc,
        ["Factor o estándar", "Tipo", "Impacto concreto en el piloto"],
        [
            ["Financiamiento mixto (inversores + subvención)", "EEF externo financiero", "Hitos de reporte 8.4 inamovibles: el cronograma se diseña hacia esa fecha, no al revés."],
            ["Cultura comunitaria e idioma", "EEF externo social", "Interfaz simple, pocos campos, capacitación 7.x. No se asume una inducción de aplicación urbana."],
            ["Conectividad irregular", "EEF físico", "Carga por lotes; si cae la red, el inventario miente y se rompe la ruta crítica."],
            ["Nube y costos variables", "EEF tecnológico", "Se escala sin comprar servidores, pero el hosting sube con el uso y depende de señal."],
            ["Datos de hogares", "EEF legal", "Minimizar datos, roles 6.1 y tratamiento 6.2; alineación con ISO/IEC 27701."],
            ["PMBOK 6.ª", "Estándar de dirección", "Acta, EDT, CPM, interesados y línea base. Dirige el proyecto, no la operación diaria."],
            ["CMMI", "Madurez de procesos", "El piloto apunta a disciplina básica (plan, evidencias), no a un nivel 4 o 5."],
            ["ITIL 4", "Gestión de servicio", "El módulo de tickets se diseña como incidente/mantención, no como formulario suelto."],
            ["COBIT", "Gobierno de TI", "Quién aprueba accesos y reportes hacia inversores. Evita que una sola persona de sistemas decida sola."],
        ],
        col_widths=[4.4, 3.2, 8.4],
    )
    caption(doc, "Tabla 10. Cada factor se traduce en una decisión del plan, no en una lista.")

    p(
        doc,
        "No usamos un estándar para todo. PMBOK nos sirve para planificar el piloto. CMMI sirve "
        "para que cargar un kit no dependa de que alguien se acuerde. ITIL sirve para tratar el "
        "ticket como un incidente y no como un formulario suelto (Baud, 2020). COBIT sirve para "
        "que un acceso hacia inversores no lo decida una sola persona. Los datos de hogares se "
        "minimizan: qué se guarda, dónde, quién entra y qué sale en el reporte, alineado con "
        "ISO/IEC 27701.",
        first_line=True,
    )

    h(doc, "5. Estrategia de planificación e integración a la organización")
    p(
        doc,
        "Planificar todo en cascada dejaría inventado, en septiembre, un flujo que el técnico va "
        "a corregir en noviembre. Planificar todo en iteraciones cortas pondría en duda, cada "
        "semana, los estados del kit y la fecha del reporte. Esta organización no puede "
        "permitirse ni lo uno ni lo otro. El enfoque es híbrido (Wysocki, 2019).",
        first_line=True,
    )
    p(
        doc,
        "Se congela lo que no puede descubrirse de nuevo: inventario y estados (cuenta 2), roles "
        "y privacidad (cuenta 6) y el calendario de donantes (hitos 8.4 y 8.5). Se itera lo que "
        "se aprende en terreno: pantallas del tablero (cuenta 3) y flujo de tickets (cuenta 4). "
        "La dirección (cuenta 1) integra ambas capas: Project Libre sostiene la línea base; "
        "Scrum opera el aprendizaje (SCRUMstudy, 2023). Sprint 0 es práctica de industria en "
        "híbrido (sprint habilitador: acta, inventario, privacidad, ambiente); la Guía Scrum no "
        "lo nombra y aquí se declara con ese nombre. S1 a S4 entregan incremento de tablero y "
        "tickets, comprometiendo 8 de 10 días: el 20 % libre es reserva de capacidad. Un estado "
        "nuevo del kit no entra como tarjeta en Trello: es control de cambios sobre la línea base "
        "(PMI, 2017; Wysocki, 2019).",
    )
    p(
        doc,
        "En la capa adaptativa Giannina actúa como Product Owner (ordena el backlog). Skarlett "
        "como Scrum Master (quita impedimentos). Nicolás, Ari y el frontend construyen el "
        "incremento. Planning el día 1, daily de quince minutos, review y retrospectiva el último "
        "día, también en Sprint 0. El review de Sprint 0 pregunta si S1 puede partir sin dato "
        "desactualizado. El piloto se mete en una empresa rápida en el pueblo y estricta con "
        "plata ajena: hitos para inversores, roles de acceso y traspaso al soporte local. El "
        "9 de diciembre Kiran queda con un responsable de operación en terreno.",
    )
    table(
        doc,
        ["Sprint", "Fechas", "Incremento usable", "Hito"],
        [
            ["Sprint 0 (habilitador)", "14 sep a 13 oct", "Acta, kits cargables, roles, ambiente", "Prepara 8.1"],
            ["S1", "14 a 27 oct", "Tablero de comunidad (3.1)", "8.1 inventario (19 oct)"],
            ["S2", "28 oct a 10 nov", "Tablero usable (3.2 a 3.4)", "8.2 tablero (9 nov)"],
            ["S3", "11 a 24 nov", "Tickets asignables (4.2 y 4.3)", "Prepara 8.3"],
            ["S4", "25 nov a 9 dic", "Terreno, reporte y traspaso", "8.3, 8.4 y 8.5"],
        ],
        col_widths=[3.2, 3.4, 5.8, 3.6],
    )
    caption(doc, "Tabla 11. Sprints Scrum. Sprint 0 habilita. S1 a S4 entregan incremento (8 de 10 días comprometidos).")
    table(
        doc,
        ["Cuenta", "Giannina (DP/front)", "Nicolás (backend)", "Ari (infra)", "Skarlett (QA/impacto)"],
        [
            ["1 Dirección", "R/A", "C", "C", "C"],
            ["2 Inventario", "A", "R", "C", "C"],
            ["3 Tablero", "R/A", "C", "I", "C"],
            ["4 Tickets", "A", "R", "C", "C"],
            ["5 Impacto", "A", "C", "I", "R"],
            ["6 Privacidad/despliegue", "A", "C", "R", "C"],
            ["7 Capacitación", "A", "C", "C", "R"],
        ],
        col_widths=[3.6, 3.1, 3.1, 3.2, 3.0],
    )
    caption(doc, "Tabla 12. RACI del equipo. R = hace. A = rinde. C = consulta. I = informa.")

    h(doc, "6. Herramientas utilizadas y justificación")
    p(
        doc,
        "Elegimos con cinco criterios: necesidad del negocio, facilidad de uso, integración, "
        "seguridad/privacidad y costo/retorno. No hay licencia de Microsoft Project y sí hay que "
        "defender el plazo del piloto: por eso Project Libre para EDT, precedencias, ruta crítica "
        "y Gantt. Trello es el tablero Scrum desde Sprint 0 (product backlog, sprint actual e "
        "incremento), porque el flujo del técnico todavía se descubre y el equipo ya puede "
        "operarlo. Word y Excel son el formato que dirección ya abre: diccionario, presupuesto y "
        "este informe. Los datos de hogares no se suben a la herramienta de gestión. La pizarra "
        "sirve para ponerse de acuerdo en una reunión; no reemplaza el cronograma. Tableau o "
        "Power BI se dejan para cuando haya dato real de kits.",
        first_line=True,
    )
    table(
        doc,
        ["Herramienta", "Dónde se usó en este plan", "Por qué esta organización"],
        [
            ["Project Libre", "Línea base: EDT, CPM, recursos, hitos (Cronograma-Kiran.xml)", "Hay que defender el plazo del piloto; no hay licencia de MS Project."],
            ["Excel / Office 365", "Diccionario EDT, recursos y presupuesto (Tabla 9)", "Formato que dirección y donantes ya leen; no calcula solo la ruta crítica."],
            ["Trello (Scrum)", "Backlog y sprints (Sprint 0 y S1 a S4) de tablero y tickets", "Equipo de cuatro. El 20 % de capacidad no se compromete. Lo no terminado vuelve al backlog."],
            ["Word (este informe)", "Plan que dirección lee para autorizar el piloto", "Es el formato que ya usan los patrocinadores."],
            ["Pizarra", "Alineación con dirección y técnico local", "Sirve en una reunión; no sustituye Project Libre."],
        ],
        col_widths=[3.6, 6.4, 6.0],
    )
    caption(doc, "Tabla 13. Uso de cada herramienta en este plan y motivo de la elección.")

    p(
        doc,
        "El piloto se considerará exitoso cuando cada kit tenga estado, las fallas se puedan "
        "atender y un donante lea un informe con datos reales. Programar, por sí solo, no basta.",
        first_line=True,
    )

    h(doc, "Referencias")
    ref(
        doc,
        "Baud, J.-L. (2020). ITIL 4: Entender el enfoque y adoptar las buenas prácticas. Ediciones ENI.",
    )
    ref(
        doc,
        "Project Management Institute. (2017). Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK) (6.ª ed.).",
    )
    ref(
        doc,
        "Project Management Institute. (2021). Guía de los fundamentos para la dirección de proyectos y El estándar para la dirección de proyectos (7.ª ed.).",
    )
    ref(
        doc,
        "SCRUMstudy. (2023). Guía SBOK (4.ª ed., español).",
    )
    ref(
        doc,
        "Wysocki, R. K. (2019). Effective project management: Traditional, agile, extreme, hybrid (8th ed.). Wiley.",
    )

    path = save_docx(doc, "Informe-Ejecutivo-Eva01.docx")
    return path


def build_alcance(info) -> Path:
    tasks = info["tasks"]
    doc = Document()
    setup_section(doc)
    # override header
    doc.sections[0].header.paragraphs[0].clear()
    r = doc.sections[0].header.paragraphs[0].add_run(
        "Kiran - Alcance cerrado, exclusiones y EDT - uso interno de dirección"
    )
    set_run_font(r, size=9, color=RGBColor(0x55, 0x55, 0x55))

    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run("Kiran: alcance cerrado, exclusiones y EDT")
    set_run_font(r, size=16, bold=True, color=NAVY)

    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.paragraph_format.space_after = Pt(8)
    r = t.add_run("Visibilidad que mantiene la energía activa.")
    set_run_font(r, size=12, italic=True)

    h(doc, "Qué es este proyecto y qué queda fuera")
    p(
        doc,
        "Este documento cierra el alcance antes del Gantt. Si las exclusiones y la EDT no "
        "están firmadas por el equipo, cualquier barra del cronograma queda sin base. Kiran es el "
        "proyecto de software de operación del piloto. No es un proyecto de ingeniería eléctrica.",
    )
    h(doc, "Propuesta de valor (por qué este software y no solo otra planilla)")
    p(
        doc,
        "Esta organización enfrenta falta de energía confiable, desarrollo económico limitado y "
        "dependencia de fósiles. Los kits solares son la solución física. Kiran no compite con "
        "el panel: mejora esa solución para que un kit instalado no se vuelva invisible. "
        "Valor = kits observables + fallas atendibles + reportes creíbles. Promesa: visibilidad "
        "que mantiene la energía activa. Si el técnico no usa el tablero, no hay valor aunque "
        "el código esté listo.",
    )
    p(
        doc,
        "Mejoras sobre el brief de dirección, sin hinchar alcance: cadena kit-ticket-indicador; "
        "carga por lotes u offline; ticket como incidente de servicio; privacidad de hogares; "
        "indicadores honestos (activos, tiempo de resolución, bajas). Fuera: app ciudadana, "
        "sensores masivos, paneles.",
        first_line=True,
    )

    h(doc, "Equipo de desarrollo")
    table(
        doc,
        ["Persona", "Rol", "Sostiene"],
        [
            ["Giannina Guerrero", "Directora del proyecto y frontend", "Acta, alcance, tablero, relación con dirección"],
            ["Nicolás Barra", "Backend", "Datos, inventario, tickets, tratamiento de hogares"],
            ["Ari Araya", "Infraestructura y nube", "Ambientes, despliegue, accesos técnicos, hosting"],
            ["Skarlett Tropan", "Calidad e impacto", "Pruebas, reportes a patrocinadores, capacitación"],
        ],
        col_widths=[3.6, 4.8, 7.6],
    )

    h(doc, "Enunciado de alcance")
    table(
        doc,
        ["Elemento", "Definición cerrada para el piloto"],
        [
            [
                "Producto",
                "Kiran: sistema web para registrar kits de UNA comunidad piloto, ver estado, gestionar mantención y emitir reportes. Apoyo de carga por lotes u offline si la red falla.",
            ],
            [
                "Criterios de aceptación",
                "Kit con hogar + estado (activo/falla/baja). Ticket nace de un kit en falla y se asigna. Reporte mensual exportable a patrocinadores.",
            ],
            [
                "Entregables",
                "Módulos 2 a 5, roles y privacidad (6), capacitación (7), acta y plan preliminar, línea base en Project Libre.",
            ],
            [
                "Exclusiones",
                "Ver tabla siguiente. Quedan fuera de la EDT y de la ruta crítica.",
            ],
            [
                "Restricciones",
                "Techo US$ 20.700; equipo de 4 + técnico local; conectividad irregular; primer reporte a donantes el "
                + fecha(by_code(tasks, "8.4").finish_date)
                + ".",
            ],
            [
                "Supuestos",
                "Comunidad piloto identificada; hay un técnico local; inversores aceptan indicadores simples; existe procedimiento de carga si no hay señal.",
            ],
        ],
        col_widths=[4.0, 12.0],
    )

    h(doc, "Exclusiones cerradas (con el porqué)")
    table(
        doc,
        ["Queda fuera", "Por qué se excluye", "Qué pasaría si no se escribe"],
        [
            ["Fabricar o instalar paneles y kits", "Es infraestructura energética, no software", "El alcance se hincha y el CPM deja de ser de este producto"],
            ["Tendido eléctrico / microred física", "Fuera de la competencia de este equipo de desarrollo", "Se promete algo que no se puede entregar en el plazo del piloto"],
            ["Microfinanzas o cobro de tarifas", "No está en las funcionalidades pedidas por dirección", "Nace un segundo producto (pagos) sin presupuesto"],
            ["Expansión a otras regiones", "El acta autoriza UNA comunidad piloto", "Se planifica un roll-out que nadie financió"],
            ["App ciudadana masiva", "El usuario de esta fase es el soporte local y la dirección", "UX y alcance cambian de destinatario"],
            ["Operación continua post-piloto", "Eso es operación, no proyecto", "El cierre del piloto no tendría frontera"],
        ],
        col_widths=[4.4, 5.8, 5.8],
    )
    p(
        doc,
        "Regla del equipo: si alguien pide de paso un tablero para toda India, es un cambio. "
        "No se agrega al Gantt sin control de cambios.",
        first_line=True,
    )

    h(doc, "EDT completa (regla del 100 %)")
    p(
        doc,
        "Nivel 1 = cuentas de control (ahí se medirá alcance, plazo y costo juntos). "
        "Nivel 2 = paquetes de trabajo estimables. Lo que no aparece aquí no existe para el piloto.",
        first_line=True,
    )
    rows = []
    for t in tasks:
        if t.code.startswith("8"):
            continue
        if t.summary:
            rows.append([t.code, t.name.upper(), "Cuenta de control", "-", "-"])
        else:
            crit = "Sí" if t.slack == 0 else "No"
            rows.append(
                [
                    t.code,
                    t.name,
                    "Paquete de trabajo",
                    f"{t.dur} d",
                    crit,
                ]
            )
    table(
        doc,
        ["ID", "Nombre", "Nivel", "Duración", "¿Crítica?"],
        rows,
        col_widths=[2.0, 8.2, 3.4, 2.0, 2.4],
    )
    caption(doc, "Tabla. EDT numerada. Las actividades críticas alimentan el XML de Project Libre.")

    h(doc, "Dependencia que amarra la EDT al calendario")
    p(
        doc,
        "Inventario (2) alimenta tablero (3). Tablero individual (3.2) alimenta tickets (4.2). "
        "Tickets en terreno (4.4) alimentan el primer reporte (5.4). Privacidad y despliegue (6) "
        "corren en paralelo, pero 6.4 espera la carga 2.3. Capacitación (7) espera software usable. "
        "Esa lógica, y no un plazo inventado, es la ruta crítica "
        "1.1, 2.1, 2.2, 2.3, 3.1, 3.2, 4.2, 4.3, 4.4, 5.4 y 7.3. "
        "Sprint 0 cubre el arranque de esa cadena (hasta 2.3). La holgura vive en privacidad "
        f"(6.4: {by_code(tasks, '6.4').slack} días) e indicadores (5.2 y 5.3: {by_code(tasks, '5.3').slack} días). "
        "La reserva de tiempo está en PERT de 4.4 y en el 20 % no comprometido de cada sprint.",
        first_line=True,
    )

    path = save_docx(doc, "Alcance-EDT-y-exclusiones.docx")
    return path


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    info = run()
    informe = build_informe(info)
    print("INFORME", informe)
    a = build_alcance(info)
    print("ALCANCE", a)
    print("XML", info["xml"])
    print("HTML", info["html"])


if __name__ == "__main__":
    main()
