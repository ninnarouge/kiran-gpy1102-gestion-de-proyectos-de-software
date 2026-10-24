# Capa Scrum de Kiran

Cómo se opera el piloto en **híbrido**. La línea base (EDT, CPM, hitos a donantes) sigue en Project Libre. Scrum no la reemplaza: la recorre en ciclos.

Metáfora: la receta del queque (estados del kit, privacidad, fecha del reporte) no se inventa cada domingo. Sprint 0 deja la cocina lista. S1–S4 sirven porciones y prueban el gusto con el técnico. Si una porción no alcanza, no se alarga el almuerzo: vuelve a la lista.

## Por qué es híbrido (y no Scrum de punta a punta)

La rúbrica (IL1.3) pide un plan **contextualizado**. Aquí el híbrido es la respuesta defendible.

| Capa | Qué hace | Por qué |
|---|---|---|
| Predictiva (línea base + hitos) | Congela estados del kit, roles, privacidad, fecha del donante | Un kit no cambia de semántica en una retro |
| Adaptativa (Scrum: Sprint 0 + S1–S4) | Prepara, itera tablero y tickets, inspecciona con el técnico | El terreno corrige pantallas y el flujo |

Si preguntan “¿por qué no puro Scrum?”: el hito 8.4 está fijo por financiamiento mixto y los datos de hogares no se rediseñan cada sprint.

Fuente de ciclos: SCRUMstudy (2023), *Guía SBOK* 4.ª. Línea base: PMBOK 6.ª (PMI, 2017). Sprint 0 es **práctica de industria** en híbrido (arranque habilitador); la Guía Scrum no lo nombra y aquí se declara con ese nombre.

## Holgura, reserva y timebox (concepto de industria)

Tres cosas distintas. Mezclarlas en el oral es el error típico.

| Concepto | Qué es | Dónde está en Kiran | Qué pasa si “fallamos” |
|---|---|---|---|
| **Holgura** (*slack* / *float*) | Tiempo que una actividad puede atrasarse **sin mover el fin del piloto**. Sale de la red (CPM). | Camino B: **23 d** en 6.4. Camino C: **25 d** en 5.2/5.3 (la suma de duraciones del C es 17: no es holgura). La ruta crítica tiene **0**, por definición. | Si se atrasa algo **no crítico**, se come holgura. Si se atrasa algo **crítico**, se mueve el 9 dic… salvo que entre la reserva. |
| **Reserva de contingencia de tiempo** | Tiempo (o capacidad) guardado para riesgos **identificados**. No es holgura: es una decisión de dirección, dentro de la línea base (PMI, 2017). | (1) PERT en 4.4: el pesimista ya está en los 8 días (σ ≈ 1,3 d). (2) Cada sprint Scrum compromete **8 de 10 días** (20 % libre). (3) Contingencia de **costo** 12 % si el terreno se alarga (hosting + horas locales). | Se **consume** la reserva. No se inventa un día extra después del 9 dic. |
| **Timebox Scrum** | El sprint **no se alarga**. Lo que no alcanza vuelve al *product backlog*. El margen de fallo del adaptativo es de **alcance**, no de fecha. | S1–S4. El hito 8.4 (4 dic) no se mueve porque una historia quedó a medias. | El incremento de ese sprint es más chico. El PO reordena. Dirección sigue viendo la fecha. |

No alargamos el piloto para “tener holgura en la ruta crítica”: eso contradice el CPM y el techo 14 sep–9 dic. El margen de fallo se diseña **adentro**: caminos paralelos con holgura, PERT en lo incierto, 20 % de capacidad sin comprometer, y alcance que flexiona.

Reserva de **gestión** (desconocidos no identificados) queda **fuera** de esta línea base, como pide PMBOK 6. Si aparece un cisne negro, es escalamiento a dirección, no un sticker en Trello.

## Roles

| Rol Scrum | Quién | Qué decide |
|---|---|---|
| *Product Owner* | Giannina Guerrero | Ordena el backlog; dice qué incremento vale más |
| *Scrum Master* | Skarlett Tropan | Cuida el timebox; saca impedimentos |
| *Developers* | Nicolás, Ari, Giannina (frontend) | Construyen el incremento |

El soporte local entra al *Sprint Review*, no al Daily.

## Artefactos

1. **Product backlog** — Trello, lista *Product backlog*. Lo ordena el PO.
2. **Sprint backlog** — lo comprometido en *este* sprint (el 80 % de capacidad).
3. **Incremento** — usable al cierre, según Definition of Done.

### Product backlog inicial

| Orden | Ítem | EDT | Sprint |
|---|---|---|---|
| — | Acta, backlog, DoD, ambiente, inventario, roles | 1.x, 2.1–2.3, 6.1–6.3 | **Sprint 0** |
| 1 | Vista general de la comunidad | 3.1 | S1 |
| 2 | Vista individual del kit | 3.2 | S2 |
| 3 | Indicadores de estado | 3.3 | S2 |
| 4 | Ajustes de usabilidad con técnico | 3.4 | S2 |
| 5 | Flujo de tickets | 4.2 | S2–S3 |
| 6 | Asignación al soporte local | 4.3 | S3 |
| 7 | Prueba en terreno | 4.4 | S3–S4 |

Estados del kit, privacidad y fecha de reporte **no** se “descubren” en el backlog de S1–S4. Si cambian, es control de cambios.

### Definition of Done

1. Se muestra en el ambiente (6.3 / 6.4).
2. Cumple el criterio del paquete.
3. Skarlett dejó evidencia de prueba.
4. Si toca dato de hogar: roles 6.1.

## Eventos (en todos los sprints, incluido Sprint 0)

| Evento | Cuándo | Cuánto | Quién |
|---|---|---|---|
| *Sprint Planning* | Día 1 | 2–4 h | Equipo + PO |
| *Daily Scrum* | Cada día hábil | 15 min | Developers + SM |
| *Sprint Review* | Último día | 1 h | Equipo + técnico o dirección |
| *Sprint Retrospective* | Después del review | 45–90 min | Equipo |
| Refinamiento | Mitad de sprint | 1 h | PO + quien construye |

No alargan los 63 días: caben dentro del timebox. No se dibujan como barras extra en la EDT.

## Calendario de sprints

Lunes a viernes. S1–S3 = 10 días hábiles (se comprometen 8). S4 = 11 días hasta el cierre. Sprint 0 dura 22 días hábiles: es un sprint **habilitador** de dos timeboxes, porque inventario + privacidad + ambiente no caben en diez días sin mentir.

| Sprint | Fechas | Meta | Incremento | Hito |
|---|---|---|---|---|
| **Sprint 0** (habilitador) | 14 sep – 13 oct | Dejar la cocina lista | Acta, backlog ordenado, kits cargables, roles, ambiente | Prepara 8.1 |
| **S1** | 14 – 27 oct | El técnico ve la comunidad | Tablero de comunidad (3.1) | 8.1 el 19 oct |
| **S2** | 28 oct – 10 nov | El técnico abre un kit y entiende el estado | Tablero usable (3.2–3.4) | **8.2** el 9 nov |
| **S3** | 11 – 24 nov | Una falla nace como ticket asignable | Flujo + asignación (4.2–4.3) | Prepara 8.3 |
| **S4** | 25 nov – 9 dic | Terreno prueba; el donante recibe dato real | Prueba + reporte + traspaso | **8.3** 1 dic · **8.4** 4 dic · **8.5** 9 dic |

Sprint 0 *Review*: “¿podemos empezar S1 sin dato fantasma?”. El incremento no es una pantalla para el técnico; es *Ready* para construir.

## Cómo se habla en el oral

> “Híbrido. Sprint 0 habilita inventario, privacidad y ambiente (la Guía Scrum no lo nombra: es práctica de industria). S1 a S4 entregan incremento de tablero y tickets. La ruta crítica no tiene holgura: eso es CPM, no pesimismo. El margen de fallo es otra cosa: 23 días en 6.4, 25 en 5.2/5.3, PERT en la prueba de terreno, y 20 % de capacidad sin comprometer en cada sprint. Si una historia no alcanza, no alargamos el sprint ni el 4 de diciembre: vuelve al backlog.”
