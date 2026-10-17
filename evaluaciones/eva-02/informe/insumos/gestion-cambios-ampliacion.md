# Insumo — ampliación gestión de cambios (C-05 / C-06)

**Para:** `evaluaciones/eva-02/informe/2.2.2-Gestion-de-cambios-Kiran.docx`  
**Uso:** borrador para pegar en la copia del Word (mismo formato, Tablas 2–11). No reemplaza el `.docx`.

Conservar C-01 a C-04. Agregar **C-05** (chatbot FAQ + canal; UI/UX; GCloud + Gemini) y **C-06** (priorización visual). **Dueños técnicos GCloud, ADK y datalake (base de información):** Nicolás Barra y Ari Araya. Datalake mínimo con C-05b; lakehouse completo solo con CC. **Fases posteriores:** casos internos, monitoreo, alertas, IA operativa.

---

## Introducción (ajustes)

En el párrafo del procedimiento, cambiar “cuatro cambios potenciales” por **seis cambios potenciales**.

Agregar al final de la introducción (o al cierre del párrafo de prioridad):

> C-05 y C-06 no suman encima de la fotografía, el segundo punto de inventario y el servicio externo: compiten por las mismas dos tarjetas por persona. Si entra uno, sale una historia equivalente del sprint. La contingencia del 12 % sigue cerrada sin razón escrita. Un datalake completo, un modelo hospedado por el equipo, una app ciudadana masiva o un chatbot que reemplace por completo al soporte contratado no entran en esta ventana: o se cierran, o quedan como solicitud futura fuera del piloto. C-05 fase 1 es autoservicio de FAQ y canal de asistencia para usuarios de la plataforma, no un segundo producto.

---

## §1.1 / Tabla 2 — filas nuevas

| Id. | Situación | Origen | Corte que toca |
|-----|-----------|--------|----------------|
| C-05 | Ejemplo de solicitud. Chatbot en la plataforma (FAQ + canal de soporte/asistencia) para ahorrar contrato de personal. Se prioriza soporte y UI/UX clara por zona compleja y público objetivo. A futuro el hilo de tickets puede alimentar casos internos, monitoreo y alertas, e IA operativa sobre equipos — solo identificado, no construido en esta ventana. Fase 1: FAQ + escalamiento a ticket/persona tras tablero usable. | Dirección / equipo (ahorro de personal de soporte) | 9 de noviembre (tablero usable) y 4 de diciembre (tickets y canal). No inventario crítico. |
| C-06 | Se pide una priorización visual en el tablero: cola o filtros que muestren qué atender primero (kit en falla, urgencia), para bajar consultas fuera del sistema al soporte local. No cambia los estados del kit ni abre una app ciudadana. Reutiliza la prioridad de C-01b si esa medida entra; no la sustituye. | Contraparte / soporte local | 9 de noviembre y, por uso, 4 de diciembre |

Texto bajo Tabla 2:

> C-05 prioriza soporte + UI/UX amigable (junto con C-06) porque la zona es compleja y el público necesita un uso guiado: si está claro, se ahorra soporte. No es app ciudadana ni reemplazo total del técnico. Monitoreo, alertas e IA operativa sobre equipos = fases posteriores identificadas. Ahora solo fase 1 (FAQ + escalamiento humano).
>
> C-06 no es lo mismo que C-01b. C-01b agrega el dato de prioridad y la nota en el modelo del ticket. C-06 es la cola o el filtro en la interfaz para que el técnico vea el orden sin pedir por WhatsApp qué kit mirar primero. Sin C-01b (o sin un dato equivalente), la cola visual no tiene criterio; sin C-06, el dato de prioridad queda escondido en el formulario.

§1.2 — agregar:

> Explorar “IA generativa en producción” o un datalake corporativo sin registro no entra. Un ranking automático sin aprobación, o un lago de datos con pipelines y BI dedicado, es solicitud nueva y se trata como C-05 o como solicitud futura rechazada en esta ventana, no como ajuste de una historia ya comprometida.

---

## §2 — consecuencias

### 2.5. C-05. Chatbot de FAQ y canal de soporte (fase 1)

En los términos pedidos, el cambio toca interfaz, UI/UX, API/FAQ, privacidad, calidad de respuestas y flujo a ticket. Giannina: UI del chat y UX. Nicolás: integración. Skarlett: calidad FAQ. Ari: tope de gasto. Fuera de esta ventana: modelo propio, datalake, app por hogar, monitoreo/alertas con IA sobre todos los equipos.

Efecto positivo: menos consultas al personal contratado; uso guiado en zona compleja. Efecto negativo de la formulación completa: scope creep y gasto. La fase 1 no cambia estados, no cierra sola, no genera alertas de flota.

**Hoja de ruta (solo identificación):** (1) soporte + UI/UX ahora; (2) tickets → casos internos / trazas; (3) monitoreo, alertas e IA operativa sobre equipos — post piloto o CC nuevo.

Indicadores: E1, E4, E5; O1, O4, O6 (contención FAQ / escalamiento).

### 2.6. C-06. Priorización visual

El cambio toca la interfaz del tablero y, si hace falta, filtros en backend. Giannina sostiene la UI. No abre estados nuevos del kit. El efecto positivo es bajar el costo de soporte informal. El efecto negativo es presión de esfuerzo hacia el 9 de noviembre y más líneas cambiadas antes del 4 de diciembre, con riesgo sobre O1 y, si persiste, sobre E1.

Orden: C-06 (cola visible para quien atiende) antes que el chatbot fase 1: lo que escale desde el chat debe poder atenderse en la cola.

### 2.7. Efecto conjunto (texto a fusionar con el 2.5 actual)

Renumerar el “2.5. Efecto conjunto” a **2.7** y agregar:

> Aceptar a la vez la fotografía de C-01, el segundo punto de C-02, el servicio de C-03, un datalake completo y un copiloto de IA “todo en uno” no son mejoras independientes. Caen sobre el mismo techo, el mismo equipo y los mismos cortes. Un datalake o lakehouse (ingesta, catálogo, ETL, BI dedicado) queda fuera del 100 % de la EDT del piloto: se rechaza o se difiere post cierre. La línea base de datos del piloto sigue siendo la base del aplicativo más el export para el reporte del 4 de diciembre. Un depósito mínimo de logs agregados sin PII, si alguien lo pide, solo cabe condicionado y dentro del hosting variable, sin competir con C-06. C-05 fase 1 y C-06 solo entran si reemplazan historia y respetan dos tarjetas por persona. Evitar acumular superficie de producto sin capacidad de integración y prueba.

### Tabla 3 — filas

| Id. | Impacto | Costo | Tiempo | Factible en esos términos |
|-----|---------|-------|--------|---------------------------|
| C-05 completo (app ciudadana / reemplazo total / datalake) | Alto. Abre app masiva o elimina el soporte humano sin capacidad de integración. | Gasto variable alto; rompe E4 si >10 %. | Rompe o desplaza el 4 de diciembre. | No |
| C-05 fase 1 (chatbot FAQ + canal) | Medio. Chat con FAQ y escalamiento a ticket/persona; no cierra solo. | Horas replanificadas + sobre API/hosting del chat en variable. Objetivo: menos horas de soporte contratado. Contingencia cerrada. | Post 9 de noviembre; no 5–9 dic. | Condicionado a C-06, cupo, tope API y FAQ curado |
| C-06 | Medio. UX de cola/filtros; reutiliza prioridad C-01b. | Casi sin infra extra; esfuerzo UI/backend del techo. | Presión hacia el 9 de noviembre. | Condicionado a reemplazo de historia y WIP |

### Tabla 4 — riesgos nuevos

| Riesgo | Se materializa si | Mitigación |
|--------|-------------------|------------|
| El chatbot amplía el alcance sin control | Se construye app ciudadana, se elimina el soporte de golpe o el bot cierra tickets/cambia estados solo | Solo fase 1: FAQ + escalamiento humano. Salto de fase = solicitud nueva. Revisión senior (Ari o Nicolás), no juniors en CC. |
| El costo de API o un datalake come el techo | Se contrata lago, modelo propio o se abre contingencia sin acta por el chatbot | Datalake y app ciudadana rechazados/diferidos. Ari pone tope de API del chatbot. Desviación > 10 %: se pausa el chatbot antes que el corte. |
| La cola visual se confunde con estados del kit | C-06 cambia semántica de activo/falla/baja | C-06 solo ordena y filtra. Estados siguen en el modelo del inventario. |
| Se acumula superficie sin integración | Entran C-05 y C-06 junto a foto, segundo punto y servicio externo | Un cambio constructivo a la vez además de C-04. Si entra IA o cola, sale otra historia. Mentoría docente 1 h/sprint si el CC es ambiguo. |

---

## §3 — soluciones

### 3.1 (párrafos)

> C-05 se aprueba solo por fases. Fase 1 (FAQ + canal + UI/UX clara) condicionada a C-06, WIP y tope API; priorizada por zona compleja y público objetivo (ahorro de soporte). Fase 2 (más FAQ, enrutamiento, trazas de casos internos) post 4 dic o CC. Fase 3 (monitoreo/alertas con IA sobre equipos, app ciudadana, reemplazo total del soporte, modelo propio) rechazada en sep–dic 2026; queda identificada a futuro.
>
> C-06 se aprueba en forma condicionada: cola o filtro hacia el 9 de noviembre. Es prerrequisito del chatbot fase 1. Si no cabe en el WIP, no entra.

### Tabla 5 — filas

| Id. | Importante | Urgente | Cuadrante | Decisión de orden |
|-----|------------|---------|-----------|-------------------|
| C-06, cola visual | Sí, si baja carga del soporte sin abrir app ciudadana. | Sí hacia el 9 de noviembre. | Planificar / hacer en ese corte. | Antes que C-05. Condicionada al reemplazo de historia. |
| C-05 fase 1, chatbot FAQ + canal | Sí para bajar carga de personal de soporte, no antes que la cola. | No antes del tablero usable. | Planificar post 9 de noviembre. | Después de C-06. Condicionada. |
| C-05 fases 2–3 / app ciudadana / datalake | No en esta ventana. | No. | Sacar del camino o planificar sin fecha. | Rechazado o diferido. |

### Tabla 6 — filas

| Id. | Decisión | Alineación con el objetivo | Estado del registro | Escalamiento |
|-----|----------|----------------------------|---------------------|--------------|
| C-05 fase 1 | Aprobada condicionada (C-06, WIP, tope API, FAQ curado). Fases 2–3 no. El bot no cierra solo. | Autoservicio y canal para usuarios de la plataforma; ahorra personal de soporte; no app ciudadana. | Abierto condicionado | Sí, si mueven el 4 dic, abren contingencia o reemplazan de golpe al soporte. |
| C-05 completo / app ciudadana / datalake | No se aprueba en esta ventana. | Sin app masiva ni segundo producto de datos; el soporte humano sigue para lo que el FAQ no resuelve. | Cerrado | Sí, si se insiste en app ciudadana, lago o modelo propio. |
| C-06 | Aprobada condicionada a reemplazo de historia y WIP. | Hace usable la prioridad sin WhatsApp. | Abierto | Sí, si alguien propone cambiar estados del kit o mover el 9 de noviembre. |

Fases IA (bloque bajo 3.1, misma tipografía de tabla del doc; no inventar “Tabla 5b” si el estilo no la usa):

| Fase | Cuándo | Qué se construye | Fuera / diferido | KPI |
|------|--------|------------------|------------------|-----|
| 1 Soporte + UX | Post 9 nov / sprint a 4 dic | Chatbot FAQ; canal; UI/UX clara para usuarios | Cierre automático, auto-estado, PII en modelo | O6; E1/E4 |
| 2 Casos / canal | Post 4 dic o CC | Más FAQ; enrutamiento; trazas de casos para uso interno | — | O6 |
| 3 Operación / IA | Fuera de ventana | Monitoreo, alertas, IA operativa sobre equipos (identificado) | App ciudadana, modelo propio, datalake, reemplazo total soporte | — |

---

## §4 — plan

### Tabla 7

| Decisión | Alcance | Project Libre | Trello | Excel y gasto |
|----------|---------|---------------|-------|---------------|
| C-06 condicionada | Tablero: cola/filtros; sin estados nuevos. Esfuerzo orientativo 3–5 pd UI + 1–2 pd backend. | Fecha 9 nov no se mueve. Si desvío > 3 días en crítico, replan antes de seguir. | Tarjeta solo tras sacar historia equivalente. Máx. 2/persona. | Sin partida infra nueva. |
| C-05 fase 1 condicionada | Chatbot: corpus FAQ, ventana de chat, escalamiento a ticket/persona. ~4–6 pd integración + 2–3 pd calidad FAQ. | Bajo tickets/soporte; predecesora tablero usable. No 5–9 dic. | Misma regla de reemplazo. | Sobre API del chatbot en variable; Ari tope. Contingencia 12 % cerrada. >10 %: pausar chatbot. Ahorro = horas de soporte contratado. |
| C-05 amplio / app ciudadana / datalake | Sin cambio de alcance del piloto. | No se inserta en el Gantt. | Sin tarjeta. | Sin gasto. Cerrado o post-piloto. |

### Tabla 8 — pasos nuevos (después de los existentes)

| Paso | Responsable | Plazo |
|------|-------------|-------|
| Confirmar C-06: historia equivalente que sale; construir cola/filtros sin cambiar estados del kit. | Giannina Guerrero (UI); Nicolás Barra si hay filtro de datos | Sprint hacia el 9 de noviembre de 2026. |
| Tras tablero usable, decidir si entra C-05 fase 1 (chatbot FAQ + canal): cupo WIP, tope API, FAQ curado, Review con quien da soporte. | Giannina (CC + UI chat); Nicolás (integración); Skarlett (calidad FAQ); Ari (gasto) | Ventana nov–dic; no semana 5–9 dic. |
| Medir bajo O6: % consultas contenidas por FAQ sin escalar; % que escala a ticket/persona. Contención baja o alucinaciones → congelar fase 2. | Skarlett Tropan; Nicolás Barra | Al cierre del sprint que use fase 1. |
| No abrir fase 2 del chatbot, app ciudadana ni datalake sin CC nuevo y revisión senior. | Giannina Guerrero | Post 4 de diciembre o fuera de ventana. |

### Tabla 9 — efecto en cortes

Actualizar filas:

- **9 nov:** puede entrar C-06 (cola), solo a cambio de otra historia. No entra datalake ni app ciudadana. No entra chatbot C-05 antes del tablero usable.
- **4 dic:** puede entrar C-05 fase 1 (FAQ + canal) si cumplió condiciones; no fase 2; no servicio externo; no archivo de C-01.

### Tabla 10 — registro

| Id. | Tipo | Propietario | Prioridad | Estado | Resultado y justificación |
|-----|------|-------------|-----------|--------|---------------------------|
| C-05a | Futuro identificado: chatbot amplio; app ciudadana; reemplazo total soporte; monitoreo/alertas con IA sobre equipos; datalake. | Giannina Guerrero | — | Cerrado (esta ventana) | No construir en sep–dic 2026; queda como fase posterior. |
| C-05b | Chatbot fase 1: FAQ + canal + UI/UX de soporte. | Nicolás Barra | Alta | Abierto | Condicionado a C-06, WIP, tope API, FAQ curado. Prioridad: zona compleja y público objetivo → ahorro de soporte. Sin monitoreo de flota en esta fase. |
| C-06 | Requisito. Priorización visual (cola/filtros). | Giannina Guerrero | Alta | Abierto | Condicionado a reemplazo de historia. No cambia estados del kit. Prerrequisito de C-05b. |

---

## §4.4 — indicadores (5 estratégicos + 7 operativos)

En el Word: **Tabla 12** (E1–E5) y **Tabla 13** (O1–O7) para comunicar los indicadores de forma organizada. O7 incluye protección de datos del datalake (C-05d). C-05d aplica minimización, roles e **ISO/IEC 27701**.

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
| O6 | Atención de fallas (C-06; submétricas C-05) | Tiempo falla→ticket; tiempo para elegir siguiente; % consultas fuera del tablero; % consultas del chatbot contenidas por FAQ; % que escala a persona | Mejora post 9 nov; contención baja / alucinaciones → congelar fase 2 | Tablero + bitácora + log chat | Giannina / soporte; chatbot: Nicolás/Skarlett | Priorizar cola antes que fase 2 del chatbot |
| O7 | Coordinación y datos en terreno | Puntaje contraparte 1–5; % sync por lote en ventana | ≥4; sync según plan | Office + Excel | Giannina / Ari | Escalar; sin ampliar alcance sin CC |

Prosa O1/O2 (ampliar lo ya escrito):

> El indicador de defectos (O1) es la cantidad de defectos del período sobre las líneas cambiadas. La meta es 5 o menos, con cero bloqueos abiertos. Sin código, la celda queda «sin base» y no se trata como alerta roja. La tasa de reapertura (O2) es lo reabierto sobre lo cerrado en desarrollo. La meta está bajo el 20 %. No se mezcla con la reapertura de tickets ya en uso en terreno: eso se anota en bitácora de soporte y puede alimentar O6 o E3, no duplica O2.

---

## Tabla 11 — respuestas

| Pregunta | Respuesta actualizada (fusionar) |
|----------|----------------------------------|
| ¿Qué cambios se aceptan? | … más C-06 cola visual y C-05b chatbot FAQ + canal, ambas condicionadas (reemplazo de historia, WIP; en chatbot: tope API, FAQ curado, prerrequisito de cola). |
| ¿Qué cambios se rechazan? | … más chatbot que reemplaza de golpe al soporte, app ciudadana masiva, datalake/lakehouse, modelo propio y fases 2–3 del chatbot en esta ventana. |
| ¿Qué no se toca? | Fechas, techo US$ 20.700, contingencia 12 % cerrada, cuatro roles. |

---

## Control anti-desborde (hilo)

- Techo y contingencia 12 % cerrada sin razón escrita.
- Máximo un cambio constructivo activo además de C-04.
- C-05/C-06 compiten por las 2 tarjetas/persona.
- Ampliación de IA (hogar, auto-estados, PII en modelo) = solicitud nueva.
- Salto de fase sin métrica de uso = no implementar.
