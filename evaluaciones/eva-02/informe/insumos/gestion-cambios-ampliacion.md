# Insumo — ampliación gestión de cambios (C-05 / C-06)

**Para:** `evaluaciones/eva-02/informe/2.2.2-Gestion-de-cambios-Kiran.docx`  
**Uso:** borrador para pegar en la copia del Word (mismo formato, Tablas 2–11). No reemplaza el `.docx`.

Conservar C-01 a C-04. Agregar C-05 (IA interna progresiva, soporte primero) y C-06 (priorización visual). Frontera: **C-01b** = dato prioridad + nota; **C-06** = cola/filtros en UI.

---

## Introducción (ajustes)

En el párrafo del procedimiento, cambiar “cuatro cambios potenciales” por **seis cambios potenciales**.

Agregar al final de la introducción (o al cierre del párrafo de prioridad):

> C-05 y C-06 no suman encima de la fotografía, el segundo punto de inventario y el servicio externo: compiten por las mismas dos tarjetas por persona. Si entra uno, sale una historia equivalente del sprint. La contingencia del 12 % sigue cerrada sin razón escrita. Un datalake completo, un modelo hospedado por el equipo o una IA para hogares y donantes no entran en esta ventana: o se cierran, o quedan como solicitud futura fuera del piloto.

---

## §1.1 / Tabla 2 — filas nuevas

| Id. | Situación | Origen | Corte que toca |
|-----|-----------|--------|----------------|
| C-05 | Ejemplo de solicitud. La dirección pide un asistente de IA de uso interno para tickets, reportes y decisiones. En este plan la formulación completa no se aprueba: solo se contempla la fase 1 (resumen de ticket, checklist de terreno y sugerencia del siguiente ticket en cola, con confirmación humana), tras un tablero usable y sin enviar datos de hogares a un modelo externo. | Dirección / equipo | 9 de noviembre (depende del tablero) y 4 de diciembre (tickets). No la ruta crítica de inventario. |
| C-06 | Se pide una priorización visual en el tablero: cola o filtros que muestren qué atender primero (kit en falla, urgencia), para bajar consultas fuera del sistema al soporte local. No cambia los estados del kit ni abre una app ciudadana. Reutiliza la prioridad de C-01b si esa medida entra; no la sustituye. | Contraparte / soporte local | 9 de noviembre y, por uso, 4 de diciembre |

Texto bajo Tabla 2:

> C-05 se rotula como ejemplo de solicitud porque concreta el tipo de cambio de productividad con IA que el piloto puede recibir. No es un copiloto ya construido. Lo que amerita registro es la ampliación de superficie de producto y el costo variable de una API de modelo. La medida factible, si cabe, es solo la fase 1 de soporte.
>
> C-06 no es lo mismo que C-01b. C-01b agrega el dato de prioridad y la nota en el modelo del ticket. C-06 es la cola o el filtro en la interfaz para que el técnico vea el orden sin pedir por WhatsApp qué kit mirar primero. Sin C-01b (o sin un dato equivalente), la cola visual no tiene criterio; sin C-06, el dato de prioridad queda escondido en el formulario.

§1.2 — agregar:

> Explorar “IA generativa en producción” o un datalake corporativo sin registro no entra. Un ranking automático sin aprobación, o un lago de datos con pipelines y BI dedicado, es solicitud nueva y se trata como C-05 o como solicitud futura rechazada en esta ventana, no como ajuste de una historia ya comprometida.

---

## §2 — consecuencias

### 2.5. C-05. Asistente de IA (fase 1)

En los términos pedidos (copiloto para tickets, reportes y decisiones), el cambio toca integración, costo variable de API, privacidad y calidad de las sugerencias. Nicolás sostiene la integración. Skarlett valida la calidad de lo sugerido. Ari registra el tope de gasto. Giannina sostiene el control de cambios. Un modelo propio, un fine-tuning o un datalake para entrenar no están en el plan.

El efecto positivo acotado es aliviar al técnico a 0,4 FTE: menos tiempo para entender un ticket y elegir el siguiente, si la sugerencia se usa y se corrige. El efecto negativo de la formulación completa es scope creep, gasto no comprometido y riesgo de priorizar mal por una alucinación. La fase 1 no cambia el estado del kit ni redacta el reporte a donantes.

Indicadores amenazados: E1 (corte del 4 de diciembre si se adelanta la fase), E4 (desviación de nube/API sobre 10 %), E5 (si se construye sin fila en el registro). Operativos a monitorear: O1, O6 (submétricas de adopción y rechazo de sugerencias) y O4 (WIP).

### 2.6. C-06. Priorización visual

El cambio toca la interfaz del tablero y, si hace falta, filtros en backend. Giannina sostiene la UI. No abre estados nuevos del kit. El efecto positivo es bajar el costo de soporte informal. El efecto negativo es presión de esfuerzo hacia el 9 de noviembre y más líneas cambiadas antes del 4 de diciembre, con riesgo sobre O1 y, si persiste, sobre E1.

Orden: C-06 antes que la IA fase 1. La IA no adelanta a un tablero que el soporte aún no usa.

### 2.7. Efecto conjunto (texto a fusionar con el 2.5 actual)

Renumerar el “2.5. Efecto conjunto” a **2.7** y agregar:

> Aceptar a la vez la fotografía de C-01, el segundo punto de C-02, el servicio de C-03, un datalake completo y un copiloto de IA “todo en uno” no son mejoras independientes. Caen sobre el mismo techo, el mismo equipo y los mismos cortes. Un datalake o lakehouse (ingesta, catálogo, ETL, BI dedicado) queda fuera del 100 % de la EDT del piloto: se rechaza o se difiere post cierre. La línea base de datos del piloto sigue siendo la base del aplicativo más el export para el reporte del 4 de diciembre. Un depósito mínimo de logs agregados sin PII, si alguien lo pide, solo cabe condicionado y dentro del hosting variable, sin competir con C-06. C-05 fase 1 y C-06 solo entran si reemplazan historia y respetan dos tarjetas por persona. Evitar acumular superficie de producto sin capacidad de integración y prueba.

### Tabla 3 — filas

| Id. | Impacto | Costo | Tiempo | Factible en esos términos |
|-----|---------|-------|--------|---------------------------|
| C-05 completo (copiloto / datalake / modelo propio) | Alto. Abre plataforma de datos o IA fuera de la EDT. | Gasto variable y posible contingencia. Rompe E4 si supera 10 % de desviación. | Rompe o desplaza el 4 de diciembre. | No |
| C-05 fase 1 (soporte) | Medio. Integra API y prompts acotados; humano confirma. | Horas replanificadas + sobre API dentro del variable (parte de los US$ 1.240). Contingencia cerrada salvo razón escrita. | Post 9 de noviembre; no en la semana del 5 al 9 de diciembre. | Condicionado a C-06/C-01b, cupo de sprint y tope de API |
| C-06 | Medio. UX de cola/filtros; reutiliza prioridad C-01b. | Casi sin infra extra; esfuerzo UI/backend del techo. | Presión hacia el 9 de noviembre. | Condicionado a reemplazo de historia y WIP |

### Tabla 4 — riesgos nuevos

| Riesgo | Se materializa si | Mitigación |
|--------|-------------------|------------|
| La IA amplía el alcance sin control | Se construye copiloto, auto-estados o reporte a donantes sin fila nueva | Solo fase 1 asistida. Salto de fase = solicitud nueva. Revisión de impacto con rol senior (Ari o Nicolás), no con juniors en planificación/CC. |
| El costo de API o un datalake come el techo | Se contrata lago completo o se abre contingencia sin acta | Datalake completo rechazado/diferido. Ari pone tope de API en Excel. Desviación > 10 %: se pausa IA antes que el corte. |
| La cola visual se confunde con estados del kit | C-06 cambia semántica de activo/falla/baja | C-06 solo ordena y filtra. Estados siguen en el modelo del inventario. |
| Se acumula superficie sin integración | Entran C-05 y C-06 junto a foto, segundo punto y servicio externo | Un cambio constructivo a la vez además de C-04. Si entra IA o cola, sale otra historia. Mentoría docente 1 h/sprint si el CC es ambiguo. |

---

## §3 — soluciones

### 3.1 (párrafos)

> C-05 se aprueba solo por fases. La fase 1 (soporte) queda condicionada a que C-06 y, si aplica, C-01b estén en marcha o en el mismo plan de sprint, a que quepa en dos tarjetas por persona y a un tope de llamadas API en Excel. La fase 2 (borradores internos de cierre) solo post 4 de diciembre o con CC nuevo. La fase 3 (copiloto amplio, ML, IA a hogares/donantes, modelo propio) se rechaza en sep–dic 2026. No se aprueba un copiloto único “todo en uno”.
>
> C-06 se aprueba en forma condicionada: vistas de cola o filtro en el tablero hacia el 9 de noviembre, sin ML, midiendo menos consultas informales. Es prerrequisito de la IA fase 1. Si no cabe en el WIP, no entra.

### Tabla 5 — filas

| Id. | Importante | Urgente | Cuadrante | Decisión de orden |
|-----|------------|---------|-----------|-------------------|
| C-06, cola visual | Sí, si baja carga del soporte sin abrir app ciudadana. | Sí hacia el 9 de noviembre. | Planificar / hacer en ese corte. | Antes que C-05. Condicionada al reemplazo de historia. |
| C-05 fase 1 | Sí para soporte, no antes que la cola. | No antes del tablero usable. | Planificar post 9 de noviembre. | Después de C-06. Condicionada. |
| C-05 fases 2–3 / datalake completo | No en esta ventana. | No. | Sacar del camino o planificar sin fecha de construcción. | Rechazado o diferido. |

### Tabla 6 — filas

| Id. | Decisión | Alineación con el objetivo | Estado del registro | Escalamiento |
|-----|----------|----------------------------|---------------------|--------------|
| C-05 fase 1 | Aprobada condicionada (C-06/C-01b, WIP, tope API). Fases 2–3 no. | Apoya tickets sin abrir producto nuevo ni reporte automático a donantes. | Abierto condicionado | Sí, si proponen mover el 4 de diciembre o abrir contingencia por API. |
| C-05 completo / datalake C | No se aprueba en esta ventana. | El piloto usa BD + export; no un segundo producto de datos. | Cerrado (formulación amplia) | Sí, a dirección, si se insiste en lago o modelo propio. |
| C-06 | Aprobada condicionada a reemplazo de historia y WIP. | Hace usable la prioridad sin WhatsApp. | Abierto | Sí, si alguien propone cambiar estados del kit o mover el 9 de noviembre. |

Fases IA (bloque bajo 3.1, misma tipografía de tabla del doc; no inventar “Tabla 5b” si el estilo no la usa):

| Fase | Cuándo | Qué se construye | Fuera | KPI |
|------|--------|------------------|-------|-----|
| 1 Soporte | Post 9 nov / sprint a 4 dic | Resumen, checklist, siguiente en cola (humano confirma) | Auto-estado, PII en modelo, chat hogar | O6; E1/E4 |
| 2 Interna | Post 4 dic o CC | Borrador nota de cierre; agrupación similar | Reporte donantes sin revisión | O6 adopción |
| 3 | Fuera de ventana | — | Copiloto total, ML, app ciudadana | — |

---

## §4 — plan

### Tabla 7

| Decisión | Alcance | Project Libre | Trello | Excel y gasto |
|----------|---------|---------------|-------|---------------|
| C-06 condicionada | Tablero: cola/filtros; sin estados nuevos. Esfuerzo orientativo 3–5 pd UI + 1–2 pd backend. | Fecha 9 nov no se mueve. Si desvío > 3 días en crítico, replan antes de seguir. | Tarjeta solo tras sacar historia equivalente. Máx. 2/persona. | Sin partida infra nueva. |
| C-05 fase 1 condicionada | Integración API + prompts + logs de uso internos. ~4–6 pd integración + 2–3 pd calidad. | Tareas bajo tickets; predecesora tablero usable. No 5–9 dic. | Misma regla de reemplazo. | Subítem “sobre API IA” en variable; Ari tope mensual. Contingencia 12 % cerrada. Desviación > 10 %: pausar IA. |
| C-05 amplio / datalake C | Sin cambio de alcance del piloto. | No se inserta en el Gantt. | Sin tarjeta de construcción. | Sin gasto. Queda cerrado o post-piloto. |

### Tabla 8 — pasos nuevos (después de los existentes)

| Paso | Responsable | Plazo |
|------|-------------|-------|
| Confirmar C-06: historia equivalente que sale; construir cola/filtros sin cambiar estados del kit. | Giannina Guerrero (UI); Nicolás Barra si hay filtro de datos | Sprint hacia el 9 de noviembre de 2026. |
| Tras tablero usable, decidir si entra C-05 fase 1: cupo WIP, tope API de Ari, Review con soporte. | Giannina (CC); Nicolás (integración); Skarlett (calidad sugerencias); Ari (gasto) | Ventana nov–dic; no semana 5–9 dic. |
| Medir submétricas bajo O6 (% tickets con resumen/checklist; % sugerencias rechazadas). Si rechazo alto, congelar fase 2. | Skarlett Tropan; Nicolás Barra | Al cierre del sprint que use fase 1. |
| No abrir fase 2 ni datalake completo sin CC nuevo y revisión senior. | Giannina Guerrero | Post 4 de diciembre o fuera de ventana. |

### Tabla 9 — efecto en cortes

Actualizar filas:

- **9 nov:** puede entrar C-06 (cola), solo a cambio de otra historia. No entra datalake. No entra C-05 fase 1 antes del tablero usable.
- **4 dic:** puede entrar C-05 fase 1 si cumplió condiciones; no fase 2; no servicio externo; no archivo de C-01.

### Tabla 10 — registro

| Id. | Tipo | Propietario | Prioridad | Estado | Resultado y justificación |
|-----|------|-------------|-----------|--------|---------------------------|
| C-05a | Requisito. Copiloto / IA amplia / datalake completo. | Giannina Guerrero | — | Cerrado | No aprobado en sep–dic 2026. Fuera de EDT y techo. |
| C-05b | Requisito. IA fase 1 soporte (resumen, checklist, siguiente en cola). | Nicolás Barra | Alta | Abierto | Condicionado a C-06/C-01b, WIP y tope API. Sin PII en modelo externo. |
| C-06 | Requisito. Priorización visual (cola/filtros). | Giannina Guerrero | Alta | Abierto | Condicionado a reemplazo de historia. No cambia estados del kit. Prerrequisito de C-05b. |

---

## §4.4 — indicadores (5 estratégicos + 7 operativos)

Ampliar la prosa existente de defectos y reapertura (O1, O2). Agregar tabla(s) con el mismo estilo del documento.

### Estratégicos del proyecto (por corte / dirección)

| # | Indicador | Fórmula / lectura | Meta | Fuente | Dueño | Si se rompe |
|---|-----------|-------------------|------|--------|-------|-------------|
| E1 | Cumplimiento de cortes | % de los 4 cortes entregados con criterio del acta | 4/4 o causa escrita si atraso ≤3 días | Project Libre + acta | Giannina | CC; semana siguiente sin trabajo nuevo si atraso >3 días |
| E2 | Integridad plan–ejecución | % actividades de ruta crítica sin desvío no registrado en CC | 100 % en hitos revisados | PL + registro | Giannina / Nicolás | Replanificar; no parche solo en Trello |
| E3 | Alcance verificable (EDT) | % paquetes del piloto con evidencia de aceptación al cierre de su corte | Meta por corte | Office + tablero | Dueño EDT | No declarar corte cerrado; reabrir si puntaje <4 |
| E4 | Techo y gasto comprometido | Desviación acumulada vs US$ 20.700 | Freno si >10 % | Excel quincenal Ari | Ari | Detener gasto no comprometido (incl. API IA) |
| E5 | Cambios bajo control | % cambios aprobados con alcance/PL/Trello actualizados antes de construir; 0 en producción sin Tabla 10 | 100 % constructivos | Tabla 10 + Trello | Giannina | Detener build; volver a CC |

### Operativos (semanal / quincenal)

| # | Indicador | Fórmula / lectura | Meta | Fuente | Dueño | Si se rompe |
|---|-----------|-------------------|------|--------|-------|-------------|
| O1 | Defectos por líneas cambiadas | Defectos del período ÷ líneas cambiadas | ≤5; 0 bloqueos | Revisión sprint | Skarlett / Nicolás | Sin código → «sin base» (no alerta roja) |
| O2 | Tasa de reapertura (desarrollo) | Reabierto ÷ cerrado (historias/defectos de sprint) | <20 % | Trello + calidad | Skarlett | No sumar historias; no confundir con tickets operativos reabiertos |
| O3 | Cumplimiento del sprint | % historias comprometidas completadas (lista ya reemplazada si hubo CC) | ≥80 % | Trello | Giannina | Resto a backlog |
| O4 | WIP y bloqueos | Tarjetas/persona; días en Bloqueado | ≤2; >5 días → C-04 | Trello | Giannina | Reasignación registrada |
| O5 | Kits con estado verificable | % kits con hogar, responsable y estado coherente | Meta del KPI de producto | Inventario / tablero | Dueño inventario | No cerrar corte |
| O6 | Atención de fallas (C-06; submétricas C-05) | Tiempo falla→ticket asignado; tiempo para elegir siguiente; % consultas fuera del tablero; % uso resumen IA y % sugerencias rechazadas | Mejora post 9 nov; rechazo alto → congelar fase 2 | Tablero + bitácora | Giannina / técnico; IA: Nicolás/Skarlett | Priorizar cola antes que fase 2 |
| O7 | Coordinación y datos en terreno | Puntaje contraparte 1–5; % sync por lote en ventana | ≥4; sync según plan | Office + Excel | Giannina / Ari | Escalar; sin ampliar alcance sin CC |

Prosa O1/O2 (ampliar lo ya escrito):

> El indicador de defectos (O1) es la cantidad de defectos del período sobre las líneas cambiadas. La meta es 5 o menos, con cero bloqueos abiertos. Sin código, la celda queda «sin base» y no se trata como alerta roja. La tasa de reapertura (O2) es lo reabierto sobre lo cerrado en desarrollo. La meta está bajo el 20 %. No se mezcla con la reapertura de tickets ya en uso en terreno: eso se anota en bitácora de soporte y puede alimentar O6 o E3, no duplica O2.

---

## Tabla 11 — respuestas

| Pregunta | Respuesta actualizada (fusionar) |
|----------|----------------------------------|
| ¿Qué cambios se aceptan? | … más C-06 cola visual y C-05 fase 1, ambas condicionadas (reemplazo de historia, WIP, y en IA tope de API y prerrequisito de cola). |
| ¿Qué cambios se rechazan? | … más copiloto IA amplio, datalake/lakehouse completo, modelo propio y fases 2–3 de IA en esta ventana. |
| ¿Qué no se toca? | Fechas, techo US$ 20.700, contingencia 12 % cerrada, cuatro roles. |

---

## Control anti-desborde (hilo)

- Techo y contingencia 12 % cerrada sin razón escrita.
- Máximo un cambio constructivo activo además de C-04.
- C-05/C-06 compiten por las 2 tarjetas/persona.
- Ampliación de IA (hogar, auto-estados, PII en modelo) = solicitud nueva.
- Salto de fase sin métrica de uso = no implementar.
