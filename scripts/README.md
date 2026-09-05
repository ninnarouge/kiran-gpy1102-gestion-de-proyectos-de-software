# Scripts

Regenerar el plan de Kiran (informe Word, alcance, XML de Project Libre, Gantt):

```bash
python scripts/eva01_docs.py
```

Solo cronograma:

```bash
python scripts/eva01_schedule.py
```

Si Word tiene el `.docx` abierto, el script guarda una copia `*-actualizado.docx`. Ciérralo y vuelve a correr para dejar un solo archivo.
