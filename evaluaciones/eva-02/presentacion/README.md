# Presentación Eva 02 — Kiran

Deck de 13 láminas para la presentación de monitoreo y control ante la comisión o alta dirección, en 15 minutos. Usa la misma línea gráfica de Eva 1. Cada lámina muestra el umbral o la decisión asociada, no solo el nombre de la herramienta.

## Abrir para presentar

Desde esta carpeta:

```powershell
python -m http.server 4174
```

Después abre [http://localhost:4174](http://localhost:4174). También se puede abrir `index.html` directamente con doble clic.

- `→`, `↑`, `Espacio` o el botón de la derecha: avanzar.
- `←`, `↓` o el botón de la izquierda: volver.
- Puntero láser con botones arriba/abajo: arriba avanza, abajo retrocede.
- Para abrir una lámina específica: `index.html?slide=8#slide-8`.
- Figuras ampliables (láminas 2, 3, 4 y 8): clic o `Enter`/`Espacio` para ampliar; `Esc`, clic fuera o el botón Cerrar para volver. Mientras está ampliada, las teclas no cambian de lámina.

Funciona sin conexión: tipografías, animación, figuras e imágenes están en `assets/`.

## Quién habla

| Lámina | Quién | Minutos | Contenido |
|---|---|---|---|
| 1 Portada | Giannina | 0:45 | Caso, fechas y techo vigente (agenda en las notas) |
| 2 Sistema | Nicolás | 1:00 | Qué controla cada herramienta; captura de Project Libre, de Trello y del tablero en Excel |
| 3 Flujo | Nicolás | 1:30 | Figura 1: del dato a la decisión |
| 4 Indicadores | Nicolás | 1:15 | Cinco indicadores, Figura 2 (tablero en Excel al 19 oct) y enlace al tablero interactivo |
| 5 Hitos | Skarlett | 1:00 | Línea de tiempo, estado y reglas de control |
| 6 Caso | Skarlett | 1:30 | Cinco pasos del cambio con el caso foto |
| 7 Decisiones | Skarlett | 1:15 | Qué entra con condición y qué queda fuera |
| 8 Recursos | Ari | 1:15 | Matriz rol × fase y técnico local 0,4 FTE |
| 9 Viabilidad | Ari | 1:15 | Techo US$ 20.700 a US$ 21.040 (+ US$ 340) y gasto del canal |
| 10 Reportes | Ari | 1:15 | Reporte por parte interesada |
| 11 Progreso | Giannina | 1:30 | Cuatro cifras al corte con semáforo |
| 12 Estado | Giannina | 1:00 | Decisión solicitada: opciones A y B |
| 13 Cierre | Giannina | 0:30 | Solicitud y preguntas |

Total 15:00; 3:45 por integrante. Títulos, traspasos y pendientes están en `STORYBOARD.md`; las notas de cada lámina, en el bloque de notas de `index.html`.

## Archivos

- `index.html`: láminas, animación y notas.
- `STORYBOARD.md`: estructura, tiempos, traspasos y pendientes del equipo.
- `frame.md`: la misma línea gráfica de Eva 1.
- `tablero/index.html`: tablero interactivo de indicadores por corte, con los datos de `Tablero-KPI-Kiran.xlsx`; funciona sin conexión.
- `assets/`: isotipo y marca Kiran, marca Duoc, afiche de cierre (`publicidad-kiran-foto.png`), Figura 1 (`flujo-monitoreo-control.png`), cronograma base en Project Libre (`gantt-kiran-projectlibre.png`), captura del tablero Trello al 19 de octubre (`trello-kiran-19oct.png`), Figura 2: tablero de indicadores en Excel al 19 de octubre (`tablero-kpi-excel.png`, completo, y `tablero-kpi-excel-corte.png`, recorte de la lámina 4), `gsap.min.js` y `fonts/` (Montserrat, IBM Plex Sans e IBM Plex Mono).
