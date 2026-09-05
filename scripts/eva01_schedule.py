"""Caso 7: EDT, CPM y export a Project Libre (MSPDI XML) + Gantt HTML."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from pathlib import Path
from xml.etree.ElementTree import Element, ElementTree, SubElement

START = date(2026, 9, 14)
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evaluaciones" / "eva-01" / "planificacion"
PRODUCT = "Kiran"


def is_workday(d: date) -> bool:
    return d.weekday() < 5


def add_n_workdays_inclusive(start: date, n: int) -> date:
    """n-ésimo día hábil contando start si es hábil (n=1 -> start)."""
    if n <= 0:
        return start
    cur = start
    seen = 0
    while True:
        if is_workday(cur):
            seen += 1
            if seen == n:
                return cur
        cur += timedelta(days=1)


def workday_date(index: int) -> date:
    """Índice 0 = primer día hábil del proyecto (START)."""
    return add_n_workdays_inclusive(START, index + 1)


@dataclass
class Task:
    code: str
    name: str
    dur: int
    preds: list[str] = field(default_factory=list)
    outline: int = 2
    summary: bool = False
    milestone: bool = False
    resource: str = ""
    es: int = 0
    ef: int = 0
    ls: int = 0
    lf: int = 0
    slack: int = 0
    uid: int = 0

    @property
    def start_date(self) -> date:
        if self.dur <= 0:
            return workday_date(max(self.ef - 1, 0)) if self.ef else START
        return workday_date(self.es)

    @property
    def finish_date(self) -> date:
        if self.dur <= 0:
            return workday_date(max(self.ef - 1, 0)) if self.ef else START
        return workday_date(self.ef - 1)


TASKS: list[Task] = [
    Task("1", "Dirección del proyecto", 0, [], 1, True),
    Task("1.1", "Acta de constitución e interesados", 3, [], resource="Directora de proyecto"),
    Task("1.2", "Plan preliminar y línea base", 5, ["1.1"], resource="Directora de proyecto"),
    Task("1.3", "Riesgos de alto nivel y comunicación", 4, ["1.1"], resource="Directora de proyecto"),
    Task("2", "Inventario de kits y hogares", 0, [], 1, True),
    Task("2.1", "Modelo de datos (comunidad, hogar, kit)", 8, ["1.1"], resource="Desarrollador backend"),
    Task("2.2", "Estados operativos del kit", 5, ["2.1"], resource="Desarrollador backend"),
    Task("2.3", "Carga inicial del piloto", 6, ["2.2"], resource="Soporte local"),
    Task("2.4", "Validación con soporte local", 4, ["2.3"], resource="Soporte local"),
    Task("3", "Tablero operativo", 0, [], 1, True),
    Task("3.1", "Vista general de la comunidad", 8, ["2.3"], resource="Desarrollador frontend"),
    Task("3.2", "Vista individual del kit", 6, ["3.1"], resource="Desarrollador frontend"),
    Task("3.3", "Indicadores de estado", 5, ["3.1"], resource="Desarrollador frontend"),
    Task("3.4", "Ajustes de usabilidad con técnico local", 5, ["3.2", "3.3", "2.4"], resource="Desarrollador frontend"),
    Task("4", "Monitoreo, tickets y mantención", 0, [], 1, True),
    Task("4.1", "Registro de rendimiento", 6, ["2.2"], resource="Desarrollador backend"),
    Task("4.2", "Flujo de tickets", 8, ["4.1", "3.2"], resource="Desarrollador backend"),
    Task("4.3", "Asignación a soporte local", 5, ["4.2"], resource="Desarrollador backend"),
    Task("4.4", "Prueba en terreno (PERT)", 8, ["4.3", "3.4", "6.4"], resource="Soporte local"),
    Task("5", "Impacto y reportes a patrocinadores", 0, [], 1, True),
    Task("5.1", "Definición de indicadores de impacto", 4, ["1.1"], resource="Analista de impacto / QA"),
    Task("5.2", "Generación de informe periódico", 6, ["5.1", "4.1"], resource="Analista de impacto / QA"),
    Task("5.3", "Exportación para inversores y donantes", 4, ["5.2"], resource="Analista de impacto / QA"),
    Task("5.4", "Primera entrega al patrocinador", 3, ["5.3", "4.4"], resource="Directora de proyecto"),
    Task("6", "Privacidad, accesos y despliegue", 0, [], 1, True),
    Task("6.1", "Roles y permisos", 5, ["1.1"], resource="Desarrollador backend"),
    Task("6.2", "Tratamiento de datos de hogares", 6, ["6.1"], resource="Desarrollador backend"),
    Task("6.3", "Ambiente de despliegue", 5, ["6.2"], resource="Infraestructura y nube"),
    Task("6.4", "Puesta en marcha del piloto", 4, ["6.3", "2.3"], resource="Infraestructura y nube"),
    Task("7", "Capacitación y transición", 0, [], 1, True),
    Task("7.1", "Material de capacitación", 4, ["3.2", "4.2"], resource="Analista de impacto / QA"),
    Task("7.2", "Taller al soporte local", 3, ["7.1", "6.4"], resource="Soporte local"),
    Task("7.3", "Traspaso operativo del piloto", 3, ["7.2", "5.4"], resource="Directora de proyecto"),
    Task("8", "Hitos de control", 0, [], 1, True),
    Task("8.1", "Hito: inventario validado", 0, ["2.4"], milestone=True),
    Task("8.2", "Hito: tablero usable", 0, ["3.4"], milestone=True),
    Task("8.3", "Hito: tickets en terreno", 0, ["4.4"], milestone=True),
    Task("8.4", "Hito: primer reporte al patrocinador", 0, ["5.4"], milestone=True),
    Task("8.5", "Hito: piloto entregado", 0, ["7.3"], milestone=True),
]


def compute_cpm(tasks: list[Task]) -> int:
    by = {t.code: t for t in tasks}
    leaves = [t for t in tasks if not t.summary]
    # topo forward
    remaining = {t.code: len(t.preds) for t in leaves}
    succs: dict[str, list[Task]] = defaultdict(list)
    for t in leaves:
        for p in t.preds:
            succs[p].append(t)
    queue = [t for t in leaves if remaining[t.code] == 0]
    order: list[Task] = []
    while queue:
        t = queue.pop(0)
        order.append(t)
        if not t.preds:
            t.es = 0
        else:
            t.es = max(by[p].ef for p in t.preds)
        t.ef = t.es + t.dur
        for s in succs[t.code]:
            remaining[s.code] -= 1
            if remaining[s.code] == 0:
                queue.append(s)
    if len(order) != len(leaves):
        missing = [t.code for t in leaves if t not in order]
        raise RuntimeError(f"Ciclo o pred inválida: {missing}")

    finish = max(t.ef for t in leaves)
    # backward: reverse topo
    for t in reversed(order):
        children = succs[t.code]
        if not children:
            t.lf = finish
        else:
            t.lf = min(s.ls for s in children)
        t.ls = t.lf - t.dur
        t.slack = t.ls - t.es
    return finish


def rollup_summaries(tasks: list[Task]) -> None:
    for t in tasks:
        if not t.summary:
            continue
        kids = [k for k in tasks if k.code.startswith(t.code + ".") and not k.summary]
        if not kids:
            continue
        t.es = min(k.es for k in kids)
        t.ef = max(k.ef for k in kids)
        t.dur = t.ef - t.es
        t.ls = min(k.ls for k in kids)
        t.lf = max(k.lf for k in kids)
        t.slack = min(k.slack for k in kids)


def iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def xml_text(parent: Element, tag: str, value) -> None:
    el = SubElement(parent, tag)
    el.text = str(value)


def build_xml(tasks: list[Task], finish: int, dest: Path) -> None:
    for i, t in enumerate(tasks, start=1):
        t.uid = i
    by = {t.code: t for t in tasks}

    project_finish = datetime.combine(workday_date(finish - 1), time(17, 0))
    project_start = datetime.combine(START, time(8, 0))

    root = Element("Project")
    root.set("xmlns", "http://schemas.microsoft.com/project")
    xml_text(root, "SaveVersion", 14)
    xml_text(root, "Name", "Kiran — piloto de operación de kits solares")
    xml_text(root, "Title", "Kiran — piloto de operación de kits solares")
    xml_text(root, "Company", "Empresa social de energía solar comunitaria")
    xml_text(root, "Manager", "Giannina Guerrero")
    xml_text(root, "Author", "Guerrero, Barra, Araya, Tropan")
    xml_text(root, "ScheduleFromStart", 1)
    xml_text(root, "StartDate", iso(project_start))
    xml_text(root, "FinishDate", iso(project_finish))
    xml_text(root, "FYStartDate", 1)
    xml_text(root, "CriticalSlackLimit", 0)
    xml_text(root, "CurrencyDigits", 0)
    xml_text(root, "CurrencySymbol", "US$")
    xml_text(root, "CurrencyCode", "USD")
    xml_text(root, "CalendarUID", 1)
    xml_text(root, "DefaultStartTime", "08:00:00")
    xml_text(root, "DefaultFinishTime", "17:00:00")
    xml_text(root, "MinutesPerDay", 480)
    xml_text(root, "MinutesPerWeek", 2400)
    xml_text(root, "DaysPerMonth", 20)
    xml_text(root, "DefaultTaskType", 0)
    xml_text(root, "DurationFormat", 7)
    xml_text(root, "WorkFormat", 2)
    xml_text(root, "WeekStartDay", 1)

    cals = SubElement(root, "Calendars")
    cal = SubElement(cals, "Calendar")
    xml_text(cal, "UID", 1)
    xml_text(cal, "Name", "Estándar")
    xml_text(cal, "IsBaseCalendar", 1)
    xml_text(cal, "IsBaselineCalendar", 0)
    weekdays = SubElement(cal, "WeekDays")
    for day in range(1, 8):
        wd = SubElement(weekdays, "WeekDay")
        xml_text(wd, "DayType", day)
        working = 0 if day in (1, 7) else 1  # 1=domingo
        xml_text(wd, "DayWorking", working)
        if working:
            tw = SubElement(wd, "WorkingTimes")
            wt = SubElement(tw, "WorkingTime")
            xml_text(wt, "FromTime", "08:00:00")
            xml_text(wt, "ToTime", "12:00:00")
            wt2 = SubElement(tw, "WorkingTime")
            xml_text(wt2, "FromTime", "13:00:00")
            xml_text(wt2, "ToTime", "17:00:00")

    xml_tasks = SubElement(root, "Tasks")
    # project summary UID 0
    proj = SubElement(xml_tasks, "Task")
    xml_text(proj, "UID", 0)
    xml_text(proj, "ID", 0)
    xml_text(proj, "Name", "Kiran — piloto")
    xml_text(proj, "Type", 1)
    xml_text(proj, "IsNull", 0)
    xml_text(proj, "OutlineLevel", 0)
    xml_text(proj, "WBS", "0")
    xml_text(proj, "Summary", 1)
    xml_text(proj, "Start", iso(project_start))
    xml_text(proj, "Finish", iso(project_finish))
    xml_text(proj, "Duration", f"PT{finish * 8}H0M0S")
    xml_text(proj, "ManualStart", iso(project_start))
    xml_text(proj, "ManualFinish", iso(project_finish))
    xml_text(proj, "DurationFormat", 7)
    xml_text(proj, "Milestone", 0)
    xml_text(proj, "Priority", 500)
    xml_text(proj, "Critical", 1)

    for t in tasks:
        el = SubElement(xml_tasks, "Task")
        xml_text(el, "UID", t.uid)
        xml_text(el, "ID", t.uid)
        xml_text(el, "Name", t.name)
        xml_text(el, "Type", 1)
        xml_text(el, "IsNull", 0)
        xml_text(el, "OutlineLevel", t.outline)
        xml_text(el, "WBS", t.code)
        xml_text(el, "Priority", 500)
        xml_text(el, "Start", iso(datetime.combine(t.start_date, time(8, 0))))
        xml_text(el, "Finish", iso(datetime.combine(t.finish_date, time(17, 0))))
        xml_text(el, "Duration", f"PT{t.dur * 8}H0M0S")
        xml_text(el, "DurationFormat", 7)
        xml_text(el, "ManualStart", iso(datetime.combine(t.start_date, time(8, 0))))
        xml_text(el, "ManualFinish", iso(datetime.combine(t.finish_date, time(17, 0))))
        xml_text(el, "Work", f"PT{t.dur * 8}H0M0S")
        xml_text(el, "Milestone", 1 if t.milestone else 0)
        xml_text(el, "Summary", 1 if t.summary else 0)
        xml_text(el, "Critical", 1 if t.slack == 0 else 0)
        xml_text(el, "ConstraintType", 0)
        xml_text(el, "CalendarUID", -1)
        xml_text(el, "RemainingDuration", f"PT{t.dur * 8}H0M0S")
        xml_text(el, "Estimated", 0)
        if t.slack == 0:
            xml_text(el, "Notes", "Ruta crítica (holgura 0). Cualquier atraso mueve el fin del piloto.")
        for p in t.preds:
            pred = by[p]
            link = SubElement(el, "PredecessorLink")
            xml_text(link, "PredecessorUID", pred.uid)
            xml_text(link, "Type", 1)
            xml_text(link, "CrossProject", 0)
            xml_text(link, "LinkLag", 0)
            xml_text(link, "LagFormat", 7)

    resources_spec = [
        (1, "Directora de proyecto"),
        (2, "Desarrollador backend"),
        (3, "Desarrollador frontend"),
        (4, "Analista de impacto / QA"),
        (5, "Soporte local"),
        (6, "Infraestructura y nube"),
    ]
    xml_res = SubElement(root, "Resources")
    dummy = SubElement(xml_res, "Resource")
    xml_text(dummy, "UID", 0)
    xml_text(dummy, "ID", 0)
    xml_text(dummy, "Name", "")
    xml_text(dummy, "Type", 1)
    name_to_uid = {}
    for uid, name in resources_spec:
        name_to_uid[name] = uid
        r = SubElement(xml_res, "Resource")
        xml_text(r, "UID", uid)
        xml_text(r, "ID", uid)
        xml_text(r, "Name", name)
        xml_text(r, "Type", 1)
        xml_text(r, "MaxUnits", 1.0)
        xml_text(r, "CalendarUID", 1)

    xml_asg = SubElement(root, "Assignments")
    aid = 1
    for t in tasks:
        if t.summary or t.milestone or not t.resource:
            continue
        a = SubElement(xml_asg, "Assignment")
        xml_text(a, "UID", aid)
        xml_text(a, "TaskUID", t.uid)
        xml_text(a, "ResourceUID", name_to_uid[t.resource])
        xml_text(a, "Units", 1)
        xml_text(a, "Work", f"PT{t.dur * 8}H0M0S")
        xml_text(a, "Start", iso(datetime.combine(t.start_date, time(8, 0))))
        xml_text(a, "Finish", iso(datetime.combine(t.finish_date, time(17, 0))))
        aid += 1

    dest.parent.mkdir(parents=True, exist_ok=True)
    tree = ElementTree(root)
    tree.write(dest, encoding="UTF-8", xml_declaration=True)


def build_html(tasks: list[Task], finish: int, dest: Path) -> None:
    leaves = [t for t in tasks if not t.summary]
    rows = []
    for t in leaves:
        left = 100.0 * t.es / finish
        width = max(100.0 * max(t.dur, 0.4) / finish, 0.8)
        color = "#b45309" if t.slack == 0 else "#64748b"
        if t.milestone:
            color = "#0f766e"
            width = 0.8
        crit = "sí" if t.slack == 0 else "no"
        rows.append(
            f"""<tr>
            <td>{t.code}</td>
            <td>{t.name}</td>
            <td>{t.dur}</td>
            <td>{', '.join(t.preds) or '—'}</td>
            <td>{t.start_date.isoformat()}</td>
            <td>{t.finish_date.isoformat()}</td>
            <td>{t.slack}</td>
            <td>{crit}</td>
            <td class="barcell"><div class="track"><div class="bar" style="left:{left:.2f}%;width:{width:.2f}%;background:{color}"></div></div></td>
            </tr>"""
        )
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<title>Gantt y ruta crítica — Kiran</title>
<style>
body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 24px; color: #111; }}
h1 {{ font-size: 20px; margin-bottom: 4px; }}
p {{ color: #444; max-width: 920px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 12px; }}
th, td {{ border-bottom: 1px solid #ddd; padding: 6px 8px; text-align: left; vertical-align: middle; }}
th {{ background: #f4f4f5; }}
.barcell {{ width: 38%; }}
.track {{ position: relative; height: 14px; background: #f4f4f5; border-radius: 2px; }}
.bar {{ position: absolute; top: 0; height: 14px; border-radius: 2px; }}
.legend span {{ display: inline-block; width: 12px; height: 12px; margin-right: 6px; vertical-align: middle; }}
</style>
</head>
<body>
<h1>Cronograma de Kiran — piloto de kits solares</h1>
<p>Inicio: {START.isoformat()} · Término: {workday_date(finish - 1).isoformat()} · {finish} días hábiles · Calendario lunes a viernes, 8 h.</p>
<p class="legend"><span style="background:#b45309"></span>Ruta crítica (holgura 0) &nbsp; <span style="background:#64748b"></span>Con holgura &nbsp; <span style="background:#0f766e"></span>Hito</p>
<table>
<thead><tr><th>EDT</th><th>Actividad</th><th>Días</th><th>Predecesora</th><th>Inicio</th><th>Fin</th><th>Holgura</th><th>Crítica</th><th>Gantt</th></tr></thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
<p>Criterio técnico: CPM (camino más largo). 4.4 usa PERT (O=5, M=7, P=13) → 8 días. Abrir el XML en Project Libre para la línea base oficial.</p>
</body>
</html>"""
    dest.write_text(html, encoding="utf-8")


def critical_chain(tasks: list[Task]) -> list[Task]:
    leaves = [t for t in tasks if not t.summary and not t.milestone and t.slack == 0]
    by_ef = sorted(leaves, key=lambda t: (t.es, t.ef))
    return by_ef


def run() -> dict:
    finish = compute_cpm(TASKS)
    rollup_summaries(TASKS)
    OUT.mkdir(parents=True, exist_ok=True)
    xml_path = OUT / "Cronograma-Kiran.xml"
    html_path = OUT / "Gantt-ruta-critica.html"
    csv_path = OUT / "Cronograma-actividades.csv"
    build_xml(TASKS, finish, xml_path)
    build_html(TASKS, finish, html_path)
    import csv

    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(
            [
                "EDT",
                "Actividad",
                "Duracion_dias",
                "Predecesoras",
                "ES",
                "EF",
                "LS",
                "LF",
                "Holgura",
                "Critica",
                "Inicio",
                "Fin",
                "Recurso",
            ]
        )
        for t in TASKS:
            if t.summary:
                continue
            w.writerow(
                [
                    t.code,
                    t.name,
                    t.dur,
                    ", ".join(t.preds),
                    t.es,
                    t.ef,
                    t.ls,
                    t.lf,
                    t.slack,
                    "sí" if t.slack == 0 else "no",
                    t.start_date.isoformat(),
                    t.finish_date.isoformat(),
                    t.resource,
                ]
            )
    crit = critical_chain(TASKS)
    info = {
        "finish_days": finish,
        "start": START,
        "end": workday_date(finish - 1),
        "critical": crit,
        "tasks": TASKS,
        "xml": xml_path,
        "html": html_path,
        "csv": csv_path,
    }
    print(f"Duración: {finish} días hábiles")
    print(f"Término: {info['end']}")
    print("Ruta crítica:")
    print(" → ".join(f"{t.code} {t.name} ({t.dur}d)" for t in crit))
    return info


if __name__ == "__main__":
    run()
