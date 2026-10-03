# Scripts

Regenerar el plan de Kiran (informe Word, alcance, XML de Project Libre, Gantt).
Todo sale en `evaluaciones/eva-01/` (informe, planificacion y una copia del Gantt
en presentacion, porque el deck se sirve desde esa carpeta).
La capa Scrum (Sprint 0, sprints, roles, reserva de capacidad) se documenta en
`evaluaciones/eva-01/planificacion/capa-scrum.md`; el generador timeboxea el
calendario sobre la EDT, no duplica paquetes de trabajo.

```bash
python scripts/eva01_docs.py
```

Solo cronograma:

```bash
python scripts/eva01_schedule.py
```

Guía de estudio Unidad 1 (Markdown → Word):

```bash
python scripts/guia_unidad1_docx.py
```

Si Word tiene el `.docx` abierto, el script guarda una copia `*-actualizado.docx`. Ciérralo y vuelve a correr para dejar un solo archivo.
