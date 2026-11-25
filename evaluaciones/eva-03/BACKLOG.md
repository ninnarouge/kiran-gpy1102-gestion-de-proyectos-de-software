# Backlog Eva 03. Documentación y cierre de Kiran

Este backlog reparte el trabajo de la Evaluación Parcial 3 de GPY1102 Gestión de Proyectos de Software. El producto es una presentación de tres láminas, que funciona como hoja de ruta del piloto, y una reunión de cierre con las partes interesadas en la Sala de Proyectos.

Las tres láminas cubren la integración de Kiran en la organización, las cifras de cierre y las lecciones del equipo. En la reunión, cualquier integrante puede recibir preguntas sobre el recorrido completo. Cada persona prepara su parte y también estudia el conjunto.

Los nombres y roles se toman de los informes de las evaluaciones 1 y 2.

| Nombre | Rol en el piloto |
| --- | --- |
| Giannina Guerrero | Directora del proyecto y frontend |
| Nicolás Barra | Backend e inventario |
| Ari Araya | Infraestructura y nube |
| Skarlett Tropan | Calidad e impacto |

Antes de congelar la lámina 2 hay que resolver tres decisiones del equipo (E03-EQ-01 a E03-EQ-03). Sin ellas no se cierran las cifras ni el relato de cierre.

No se inventan cifras. Las únicas que este backlog da por escritas son las ya informadas al corte del 19 de octubre de 2026 en la Evaluación 2. Las posteriores se acuerdan en E03-EQ-02 y se transcriben al tablero.

## Orden de trabajo

1. Resolver E03-EQ-01, E03-EQ-02 y E03-EQ-03.
2. Acordar el formato de las láminas (E03-EQ-04).
3. Reunir los insumos de la lámina 1 y armar el mapa de integración.
4. Completar el tablero de cifras al corte acordado y armar la infografía de la lámina 2.
5. Hacer la retrospectiva del equipo y armar la lámina 3.
6. Escribir el guion de la reunión y las respuestas individuales.
7. Diseñar las tres láminas con la línea gráfica de Kiran (azul navy, ámbar y la K).
8. Revisar las láminas entre los cuatro.
9. Ensayar la reunión con preguntas cruzadas.
10. Armar el paquete para la Sala de Proyectos.

## Cómo se usa este archivo

Cada ítem tiene identificador, responsable, descripción, criterios de aceptación, dependencias, prioridad y estado. El estado inicial de todos es Pendiente. Cuando una tarea queda lista, se actualiza el estado en este archivo y se avisa en el grupo.

La prioridad Bloqueante indica que el resto del cierre no puede avanzar con rigor. Alta conviene terminar antes de diseñar las láminas. Media puede hacerse en paralelo cuando ya hay un borrador estable.

Los PDF de pauta y el material oficial se quedan en `Contexto/` y no se suben al repositorio.

---

## Épica EQ. Decisiones y coordinación del equipo

Responsable de la épica: los cuatro.

### E03-EQ-01. Acordar la fecha de corte que se presenta como cierre

- Responsable: Equipo (los cuatro)
- Prioridad: Bloqueante
- Estado: Pendiente
- Dependencias: ninguna

**Descripción.** El plan del piloto contempla los hitos de inventario (19 de octubre), tablero (9 de noviembre), primer informe (4 de diciembre) y cierre (9 de diciembre de 2026). Al 24 de noviembre de 2026, el corte del 9 de noviembre ya debió ocurrir y el sprint 3 (tickets, del 11 al 24 de noviembre) termina en esta fecha. Los cortes de diciembre aún no llegan. El equipo acuerda qué fecha usará como cierre informado en las láminas y en la reunión, según el día en que se presente.

**Criterios de aceptación.**

- Queda escrita la fecha de corte elegida y la razón (último hito ya cumplido, cierre del 9 de diciembre u otra que el equipo sostenga).
- Todas las cifras de la lámina 2 se refieren a ese mismo corte.
- Si la presentación es anterior al 4 o al 9 de diciembre, se deja explícito qué hitos se informan como cumplidos y cuáles siguen como compromiso vigente.

### E03-EQ-02. Acordar cómo se completan las cifras posteriores al 19 de octubre

- Responsable: Equipo (los cuatro)
- Prioridad: Bloqueante
- Estado: Pendiente
- Dependencias: E03-EQ-01

**Descripción.** En la Evaluación 2, el corte del 19 de octubre quedó informado así: avance de 54,9 % (73 de 133 días-actividad programados); hito de inventario cumplido, con puntaje 4 / 5; gasto ejecutado de US$ 10.346 (55 % de la base de US$ 18.810); desviación de 0 % frente al techo aprobado de US$ 20.700; contingencia sin uso; consumo de API de US$ 0. Los cortes del 9 de noviembre, 4 de diciembre y 9 de diciembre aparecían solo con valor planificado. El equipo acuerda cómo completar el tablero Excel al corte de E03-EQ-01, con coherencia respecto de esa línea base y de las reglas ya definidas (desviación, puntaje mínimo de hito, cumplimiento de sprint, densidad de defectos y registro de cambios). Las cifras nuevas las carga cada responsable en sus ítems de la lámina 2. Aquí solo se fija la regla común.

**Criterios de aceptación.**

- Hay una regla escrita y compartida para completar el tablero (qué se llena, quién lo carga y cómo se evita contradecir el corte del 19 de octubre, salvo un desvío posterior que quede documentado).
- Nadie publica en las láminas una cifra que el equipo no haya acordado.
- El Excel de KPI queda como fuente única para la lámina 2.

### E03-EQ-03. Resolver el estado de C-05 y del techo solicitado

- Responsable: Equipo (los cuatro)
- Prioridad: Bloqueante
- Estado: Pendiente
- Dependencias: ninguna (conviene cerrarla junto a E03-EQ-01 y E03-EQ-02)

**Descripción.** Al corte de la Evaluación 2, el canal de asistencia automatizada (C-05, propuesto por Nicolás Barra) seguía con techo solicitado de US$ 21.040, pendiente de autorización. El techo aprobado vigente era US$ 20.700. El canal no se construye sin autorización, va después de la priorización visual y no sustituye al soporte humano. El lago de datos completo quedó fuera de la ventana. El balance de cierre cambia si C-05 se da por aprobado, rechazado o diferido. El equipo deja esa decisión por escrito.

**Criterios de aceptación.**

- Queda registrado si C-05 se aprueba, se rechaza o se difiere, y con qué condiciones.
- Si se aprueba, se indica qué ocurre con el techo (se mantiene US$ 20.700, se usa contingencia con acta, o se solicita US$ 21.040) y qué entra en la ventana (fase 1, depósito mínimo, corpus de preguntas frecuentes).
- Si se rechaza o se difiere, las láminas y la reunión lo dicen con claridad, sin darlo por construido.
- Nicolás documenta el estado técnico en E03-L2-02 y Ari el efecto en el techo y en el gasto en E03-L2-01.

### E03-EQ-04. Definir el formato de las tres láminas

- Responsable: Equipo (los cuatro)
- Prioridad: Media
- Estado: Pendiente
- Dependencias: ninguna

**Descripción.** Las tres láminas pueden ser digitales (PowerPoint, Canva, Prezi u otra aplicación), analógicas (papel craft, cartulina, pizarra) o mixtas. El equipo elige un formato y se atiene a él en el diseño. Esta decisión no bloquea las cifras, pero sí el trabajo visual.

**Criterios de aceptación.**

- Hay una decisión escrita (digital, analógico o mixto) y, si es digital, la herramienta elegida.
- Las tres láminas se producen en ese formato, con la línea gráfica de Kiran.

---

## Épica L1. Lámina 1. Gestión de la integración

La lámina 1 muestra, en un esquema tipo BPMN o en un mapa conceptual, cómo se integran los componentes y procesos de Kiran en la realidad de la empresa social. No es un organigrama suelto. Tiene que verse la conexión entre inventario, tablero, tickets, informe de impacto, accesos y despliegue, capacitación y el traspaso a la operación, y su vínculo con dirección, soporte local, técnico local e inversores o donantes. En esta fase las familias no usan la aplicación. También debe verse la frontera de cierre: cuando el técnico atienda tickets todos los días, eso deja de ser proyecto y pasa a ser operación.

### E03-L1-01. Insumo de inventario, tickets y datos de hogares

- Responsable: Nicolás Barra
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: ninguna

**Descripción.** Prepara una ficha clara de los componentes de backend (inventario de kits y hogares, estados activo / falla / baja, flujo de tickets y tratamiento de datos del hogar) y de cómo se conectan con el trabajo del técnico local y con el resto de la operación. Esta ficha alimenta el mapa que arma Giannina y sirve de base para los ejemplos de la reunión.

**Criterios de aceptación.**

- La ficha nombra los componentes, el flujo kit-estado-ticket-reporte y la relación con el soporte local.
- Explica qué queda fuera (por ejemplo, una aplicación para cada familia o un segundo punto de acopio, si sigue fuera de la ventana).
- Cabe en una página o equivalente y Giannina puede usarla sin reescribirla desde cero.

### E03-L1-02. Insumo de infraestructura, accesos y despliegue

- Responsable: Ari Araya
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: ninguna

**Descripción.** Prepara una ficha de cómo la infraestructura se inserta en la operación del piloto: ambientes, despliegue, accesos, hosting y control de consumo de nube. Deja explícito lo que queda fuera de la ventana (GPU dedicado, lago de datos empresarial y hospedaje de un modelo propio).

**Criterios de aceptación.**

- La ficha describe ambientes, roles de acceso, despliegue y el lugar de la nube en el flujo de la organización.
- Lista lo que no entra en el piloto, en coherencia con la Evaluación 2.
- Cabe en una página o equivalente y se puede traspasar al mapa de la lámina 1.

### E03-L1-03. Insumo de impacto, capacitación y traspaso a la operación

- Responsable: Skarlett Tropan
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: ninguna

**Descripción.** Prepara una ficha del tramo de impacto y de la transición: indicadores e informe a patrocinadores, capacitación, taller y traspaso operativo. Este es el puente entre el piloto y la operación cotidiana del soporte local.

**Criterios de aceptación.**

- La ficha cubre reporte de impacto, quién lo recibe y cómo se traspasa el uso del tablero y de los tickets.
- Deja clara la frontera entre proyecto y operación.
- Cabe en una página o equivalente y se puede integrar al mapa.

### E03-L1-04. Mapa de integración de Kiran en la organización (lámina 1)

- Responsable: Giannina Guerrero
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-L1-01, E03-L1-02, E03-L1-03

**Descripción.** Arma la lámina 1 como mapa conceptual o esquema tipo BPMN. Integra los insumos de Nicolás, Ari y Skarlett con el relato de dirección: acta, alcance, relación con dirección y soporte local, y coherencia entre todos los componentes y procesos. Incluye la frontera proyecto / operación.

**Criterios de aceptación.**

- La lámina muestra la conexión entre todos los componentes del piloto (dirección, inventario, tablero, tickets, impacto, privacidad y despliegue, capacitación y traspaso) y los flujos de la organización.
- No deja fuera un componente que sí forma parte del plan.
- Se entiende en una lectura breve, sin texto de informe.
- Nicolás, Ari y Skarlett revisan que su tramo esté bien representado.

---

## Épica L2. Lámina 2. Datos y métricas de cierre

La lámina 2 es una infografía o un esquema simple con logros, datos y cifras clave para las partes interesadas. Cada cifra lleva su lectura. No se pega el Excel completo. Las cifras se toman del tablero de KPI y del registro de cambios, al corte acordado en E03-EQ-01.

### E03-L2-01. Cierre financiero al corte acordado

- Responsable: Ari Araya
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-EQ-01, E03-EQ-02, E03-EQ-03

**Descripción.** Completa el Excel financiero al corte de cierre. Registra gasto ejecutado frente a la base de US$ 18.810 y al techo aprobado de US$ 20.700, desviación, uso o no de la contingencia (US$ 1.890) y consumo de nube o API. Parte de lo ya informado el 19 de octubre (US$ 10.346, desviación de 0 %, contingencia sin uso, API en US$ 0) y no lo contradice, salvo un desvío posterior que quede documentado. Si E03-EQ-03 aprueba, rechaza o difiere C-05, el efecto en el techo y en el gasto queda visible.

**Criterios de aceptación.**

- El Excel tiene las cifras al corte acordado, con fuente y fecha.
- Se puede leer de un vistazo el gasto, el techo vigente, la desviación, la contingencia y el consumo de API.
- Si hay un desvío mayor a 10 %, queda anotada la acción (detener gasto no comprometido u otra ya definida por el equipo).
- Skarlett puede llevar estas cifras a la infografía sin reinterpretarlas.

### E03-L2-02. Cifras de sprint, integridad de kits y estado técnico de C-05

- Responsable: Nicolás Barra
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-EQ-01, E03-EQ-02, E03-EQ-03

**Descripción.** Entrega, al corte acordado, el cumplimiento de sprint (historias comprometidas completadas, con umbral de 80 %), la integridad de estados de kit (hogar, responsable y estado coherente), la tasa de reapertura y el estado técnico de C-05 según lo resuelto en E03-EQ-03. Qué se incorporó, qué quedó fuera y por qué el lago completo no entra en la ventana.

**Criterios de aceptación.**

- Las cifras de sprint, integridad y reapertura tienen fecha de corte y se pueden rastrear en Trello.
- El párrafo de C-05 coincide con la decisión del equipo y no da por construido lo que no está autorizado.
- Skarlett puede incorporar estas cifras a la infografía sin reinterpretarlas.

### E03-L2-03. Cifras de calidad y sincronización del tablero con Excel

- Responsable: Skarlett Tropan
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-EQ-01, E03-EQ-02, E03-L2-04

**Descripción.** Completa en el Excel de KPI la densidad de defectos del periodo (umbral de 5 o menos por cada 1.000 líneas cambiadas, cero defectos bloqueantes abiertos al corte), la coherencia de los semáforos y la sincronización entre Trello y el tablero. Recibe de Giannina los puntajes de contraparte y el estado de los hitos para dejar una lectura única de calidad y aceptación.

**Criterios de aceptación.**

- El Excel de calidad e hitos está actualizado al corte acordado, con semáforos coherentes.
- Trello y Excel no dicen cosas distintas sobre el mismo corte.
- Las cifras de defectos y de aceptación están listas para la infografía.

### E03-L2-04. Hitos, puntajes de contraparte y estado del registro de cambios

- Responsable: Giannina Guerrero
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-EQ-01, E03-EQ-03

**Descripción.** Consolida el estado de los hitos del piloto (inventario, tablero, primer informe y cierre) frente a lo planificado, los puntajes de contraparte (mínimo de aceptación 4 / 5; si no se alcanza, se reabre el corte) y el estado del registro de cambios (aprobados, rechazados o diferidos, incluida la decisión sobre C-05). Este relato alimenta tanto la infografía como el contraste entre lo esperado y lo ocurrido.

**Criterios de aceptación.**

- Cada hito aparece como cumplido, pendiente o con causa registrada, según el corte acordado.
- Los puntajes que existan al corte están anotados. El del 19 de octubre (4 / 5) se mantiene como ya informado.
- El resumen de cambios coincide con el registro (C-01 a C-06) y con E03-EQ-03.
- Skarlett y Ari pueden cruzar este relato con calidad y gasto.

### E03-L2-05. Infografía de cierre (lámina 2)

- Responsable: Skarlett Tropan
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-L2-01, E03-L2-02, E03-L2-03, E03-L2-04, E03-L2-06, E03-L2-07

**Descripción.** Traduce las cifras de los cuatro a un esquema simple para dirección, soporte local y donantes. Incluye hitos (esperado frente a logrado), avance, gasto frente a techo, desviación, contingencia, puntajes, calidad, sprints, estado de los cambios y dos o tres áreas de éxito. Cada cifra lleva una lectura breve.

**Criterios de aceptación.**

- La lámina se entiende en una lectura corta y no reproduce el Excel completo.
- Todas las cifras coinciden con el tablero al corte acordado.
- Aparecen logros, datos relevantes y el estado de los cambios, sin dejar una métrica clave solo en el archivo de respaldo.
- Ari, Nicolás y Giannina revisan que su tramo esté bien expresado.

### E03-L2-06. Contraste de alcance. Lo planificado frente a lo acordado en cambios

- Responsable: Nicolás Barra
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-EQ-03, E03-L2-04

**Descripción.** Redacta un contraste breve entre lo comprometido en la Evaluación 1 (inventario, tablero, tickets y primer informe de impacto, con soporte predominantemente humano) y lo que el registro de cambios dejó dentro o fuera de la ventana. Sirve a la hoja de ruta, que debe mostrar expectativas y realidad, y a la infografía.

**Criterios de aceptación.**

- El texto cabe en un párrafo o en un recuadro y distingue con claridad lo aprobado, lo rechazado y lo diferido.
- No introduce alcance nuevo que no esté en el registro.
- Skarlett puede usarlo en la lámina 2 y el equipo puede explicarlo en la reunión.

### E03-L2-07. Lectura del techo, la contingencia y C-05 para dirección

- Responsable: Ari Araya
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-EQ-03, E03-L2-01

**Descripción.** Escribe una lectura corta de lo que el cierre financiero implica para dirección: techo aprobado, techo solicitado si corresponde, contingencia, regla de detención si la desviación supera el 10 %, y distinción entre gasto de puesta en marcha y gasto recurrente de operación. No declara un ahorro fijo en dólares que el acta no haya medido.

**Criterios de aceptación.**

- El texto es breve y se sostiene solo con cifras acordadas.
- Deja claro qué se pide decidir o qué ya quedó resuelto sobre el techo y C-05.
- Se puede llevar a la infografía o usarse tal cual en la reunión.

---

## Épica L3. Lámina 3. Resultados y lecciones aprendidas

La lámina 3 reúne los resultados y las lecciones del equipo durante la gestión del piloto. Incluye fortalezas y debilidades, procedimientos que convendría mejorar y un recuadro para cada integrante. Las lecciones tienen que poder aplicarse en un proyecto futuro, no solo narrar lo ocurrido.

### E03-L3-01. Retrospectiva del equipo

- Responsable: Skarlett Tropan (facilita; participan los cuatro)
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: conviene tener un borrador de las láminas 1 y 2, aunque puede agendarse en paralelo

**Descripción.** Facilita una conversación breve del equipo sobre fortalezas, debilidades, lo que funcionó en el proceso de gestión (planificación, monitoreo, cambios, capacidad y comunicación) y los procedimientos que habría que mejorar. Deja notas escritas que alimentan el marco de la lámina 3 y las lecciones individuales.

**Criterios de aceptación.**

- Hay un registro escrito de fortalezas, debilidades y áreas de mejora, acordado por los cuatro.
- Aparece al menos un procedimiento concreto que el equipo mejoraría en un proyecto siguiente.
- Cada persona sale de la reunión con una idea clara para su recuadro.

### E03-L3-02. Estructura de la lámina 3

- Responsable: Giannina Guerrero
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-L3-01, E03-L3-03, E03-L3-04, E03-L3-05, E03-L3-06

**Descripción.** Arma la lámina 3 con el marco grupal (resultados, fortalezas, debilidades y procedimientos a mejorar) y los cuatro recuadros individuales. Cuida que el conjunto se lea como una síntesis del proceso de gestión, no como cuatro notas sueltas.

**Criterios de aceptación.**

- La lámina incluye el relato grupal y un espacio visible para cada integrante.
- Las lecciones grupales se reconocen en las notas de E03-L3-01.
- Los cuatro revisan que su recuadro no fue recortado de un modo que cambie el sentido.

### E03-L3-03. Recuadro de lecciones de Giannina Guerrero

- Responsable: Giannina Guerrero
- Prioridad: Media
- Estado: Pendiente
- Dependencias: E03-L3-01

**Descripción.** Escribe su lección aprendida como directora del proyecto y frontend. Puede abordar alcance, control de cambios, relación con dirección o la interfaz del tablero, siempre a partir de lo conversado en la retrospectiva y de su trabajo real en el piloto.

**Criterios de aceptación.**

- El texto es breve, en primera persona, y se entiende sin contexto extra.
- Se relaciona con su rol y con el trabajo colectivo.
- Deja al menos una idea aplicable a un proyecto futuro.

### E03-L3-04. Recuadro de lecciones de Nicolás Barra

- Responsable: Nicolás Barra
- Prioridad: Media
- Estado: Pendiente
- Dependencias: E03-L3-01

**Descripción.** Escribe su lección aprendida como backend e inventario. Puede abordar datos, tickets, capacidad del backlog, cierre de historias o el control de cambios antes de construir (incluido C-05), a partir de la retrospectiva y de su trabajo en el piloto.

**Criterios de aceptación.**

- El texto es breve, en primera persona, y se entiende sin contexto extra.
- Se relaciona con su rol y con el trabajo colectivo.
- Deja al menos una idea aplicable a un proyecto futuro.

### E03-L3-05. Recuadro de lecciones de Skarlett Tropan

- Responsable: Skarlett Tropan
- Prioridad: Media
- Estado: Pendiente
- Dependencias: E03-L3-01

**Descripción.** Escribe su lección aprendida como calidad e impacto. Puede abordar medición de defectos, sincronización del tablero con Excel, aceptación de hitos, reportes a patrocinadores o capacitación, a partir de la retrospectiva y de su trabajo en el piloto.

**Criterios de aceptación.**

- El texto es breve, en primera persona, y se entiende sin contexto extra.
- Se relaciona con su rol y con el trabajo colectivo.
- Deja al menos una idea aplicable a un proyecto futuro.

### E03-L3-06. Recuadro de lecciones de Ari Araya

- Responsable: Ari Araya
- Prioridad: Media
- Estado: Pendiente
- Dependencias: E03-L3-01

**Descripción.** Escribe su lección aprendida como infraestructura y nube. Puede abordar el registro quincenal del gasto, la regla de detener trabajo no comprometido si la desviación supera el 10 %, la viabilidad del canal de asistencia o el control de topes de API, a partir de la retrospectiva y de su trabajo en el piloto.

**Criterios de aceptación.**

- El texto es breve, en primera persona, y se entiende sin contexto extra.
- Se relaciona con su rol y con el trabajo colectivo.
- Deja al menos una idea aplicable a un proyecto futuro.

---

## Épica DEF. Reunión de cierre con las partes interesadas

La reunión comunica a las partes interesadas los hitos, las cifras y las lecciones del piloto. Cada integrante prepara las cuatro preguntas que siguen, aunque en la sala lidere de preferencia el tema de su rol. El o la docente puede consultar a cualquiera sobre cualquier parte del trabajo.

1. Cómo se integrará el software en la organización y cómo se relacionan sus componentes y procesos con el resto de los servicios o flujos.
2. Cuáles son las lecciones aprendidas y las áreas de mejora del equipo, y qué procedimientos podrían mejorarse.
3. A partir de los datos y métricas clave, cuál es el balance de cierre y cuáles son las áreas de éxito.
4. Cuál fue su contribución al trabajo colectivo y qué aprendizajes destaca del proceso de gestión.

### E03-DEF-01. Guion de apertura de la reunión de cierre

- Responsable: Giannina Guerrero
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-L1-04, E03-L2-05, E03-L3-02

**Descripción.** Redacta un guion breve de apertura para la reunión con las partes interesadas. Presenta el propósito del piloto, el recorrido de los hitos, el estado de cierre y el orden en que el equipo expondrá. No reemplaza las respuestas individuales.

**Criterios de aceptación.**

- El guion cabe en pocos minutos y se sostiene en las tres láminas.
- Deja espacio para las intervenciones de Nicolás, Ari y Skarlett, y para las preguntas.
- El equipo lo lee y acuerda ajustes antes del ensayo.

### E03-DEF-02. Respuestas de Giannina Guerrero a las cuatro preguntas

- Responsable: Giannina Guerrero
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-L1-04, E03-L2-04, E03-L3-03, E03-DEF-01

**Descripción.** Prepara respuestas propias a las cuatro preguntas, con ejemplos. En la reunión puede liderar la integración y el relato general de hitos y cambios, pero también debe poder hablar de cifras y de lecciones del equipo.

**Criterios de aceptación.**

- Hay una respuesta escrita (o en viñetas) para cada una de las cuatro preguntas.
- Incluye al menos un ejemplo concreto de vínculo entre componentes, tomado de la lámina 1.
- La pregunta 4 refleja su trabajo como directora y frontend, sin atribuirse el de las demás personas.

### E03-DEF-03. Respuestas de Nicolás Barra a las cuatro preguntas

- Responsable: Nicolás Barra
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-L1-01, E03-L2-02, E03-L2-06, E03-L3-04

**Descripción.** Prepara respuestas propias a las cuatro preguntas, con ejemplos del flujo kit-estado-ticket-reporte, del cierre de historias y del estado de C-05. Debe poder sostener la integración y el balance de cierre, no solo su componente.

**Criterios de aceptación.**

- Hay una respuesta escrita (o en viñetas) para cada una de las cuatro preguntas.
- Incluye ejemplos concretos de inventario, tickets o capacidad, y un contraste claro de lo que entró o no por control de cambios.
- La pregunta 4 refleja su trabajo como backend e inventario.

### E03-DEF-04. Respuestas de Skarlett Tropan a las cuatro preguntas

- Responsable: Skarlett Tropan
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-L1-03, E03-L2-05, E03-L3-01, E03-L3-05

**Descripción.** Prepara respuestas propias a las cuatro preguntas, con especial solidez en las lecciones del equipo y en la lectura de las métricas de cierre. También estudia la integración y su aporte individual.

**Criterios de aceptación.**

- Hay una respuesta escrita (o en viñetas) para cada una de las cuatro preguntas.
- Puede explicar la infografía y las notas de la retrospectiva sin leerlas de corrido.
- La pregunta 4 refleja su trabajo como calidad e impacto.

### E03-DEF-05. Respuestas de Ari Araya a las cuatro preguntas

- Responsable: Ari Araya
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-L1-02, E03-L2-01, E03-L2-07, E03-L3-06

**Descripción.** Prepara respuestas propias a las cuatro preguntas, con especial solidez en el balance financiero y en la integración de infraestructura. También estudia las lecciones del equipo y su aporte individual.

**Criterios de aceptación.**

- Hay una respuesta escrita (o en viñetas) para cada una de las cuatro preguntas.
- Puede explicar gasto, techo, desviación y el estado de C-05 con las cifras acordadas, sin contradecir el corte del 19 de octubre.
- La pregunta 4 refleja su trabajo como infraestructura y nube.

### E03-DEF-06. Ensayo de la reunión con preguntas cruzadas

- Responsable: Equipo (los cuatro)
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-DEF-01, E03-DEF-02, E03-DEF-03, E03-DEF-04, E03-DEF-05, E03-PRE-01

**Descripción.** El equipo ensaya la reunión de cierre con las tres láminas. Cada persona responde al menos una pregunta que no sea la de su rol habitual. Se corrigen lagunas, contradicciones entre láminas y tiempos de la exposición.

**Criterios de aceptación.**

- Se hizo al menos un ensayo completo, con las tres láminas a la vista.
- Cada integrante respondió una pregunta fuera de su tramo principal.
- Quedan anotados los ajustes acordados (cifra, relato o diseño) y se aplican antes de la sala.

---

## Épica PRE. Diseño, revisión y paquete para la sala

### E03-PRE-01. Composición visual de las tres láminas

- Responsable: Giannina Guerrero y Skarlett Tropan (co-responsables; Nicolás y Ari revisan el contenido)
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-EQ-04, E03-L1-04, E03-L2-05, E03-L3-02

**Descripción.** Pasan el contenido acordado a las tres láminas finales, con la línea gráfica de Kiran (azul navy, ámbar y la K). Giannina lidera la composición del mapa de la lámina 1. Skarlett lidera la de la infografía de la lámina 2. La lámina 3 la cierran entre las dos, respetando el marco grupal y los recuadros. Nicolás y Ari revisan que no se haya alterado el sentido de las cifras ni de los componentes.

**Criterios de aceptación.**

- Las tres láminas están en el formato elegido en E03-EQ-04 y se leen con coherencia visual entre sí.
- Se usa la línea gráfica ya definida para Kiran.
- El contenido coincide con los borradores aceptados y con el Excel de cierre.

### E03-PRE-02. Revisión conjunta de las tres láminas

- Responsable: Equipo (los cuatro)
- Prioridad: Alta
- Estado: Pendiente
- Dependencias: E03-PRE-01

**Descripción.** Los cuatro revisan las láminas juntas antes del ensayo. Buscan coherencia entre integración, cifras y lecciones, y comprueban que no falte un componente, una métrica de cierre o un recuadro individual.

**Criterios de aceptación.**

- Cada integrante dejó al menos una revisión (comentario o visto bueno) sobre las tres láminas.
- Las correcciones acordadas quedan aplicadas en la versión que se lleva al ensayo.

### E03-PRE-03. Paquete para la Sala de Proyectos

- Responsable: Equipo (Giannina Guerrero confirma la lista)
- Prioridad: Media
- Estado: Pendiente
- Dependencias: E03-PRE-02, E03-DEF-06

**Descripción.** Arma lo que se lleva a la Sala de Proyectos: las tres láminas en el formato acordado, el guion de apertura, las respuestas individuales, el Excel de KPI como respaldo y los respaldos de Trello y de gasto. Giannina verifica que no falte nada el día de la presentación.

**Criterios de aceptación.**

- Existe una lista de lo que se lleva y quién es responsable de cada pieza.
- Las láminas y los respaldos corresponden a la versión revisada después del ensayo.
- Los PDF oficiales de `Contexto/` no se suben al repositorio.

### E03-PRE-04. Respaldo del Excel financiero y de nube para la reunión

- Responsable: Ari Araya
- Prioridad: Media
- Estado: Pendiente
- Dependencias: E03-L2-01, E03-L2-07

**Descripción.** Deja lista una hoja o una captura del Excel financiero y, si corresponde, de la lectura de consumo de nube, para consultarla en la reunión si preguntan el detalle detrás de la infografía. No sustituye a la lámina 2.

**Criterios de aceptación.**

- El respaldo está actualizado al corte acordado y es legible en sala.
- Las cifras coinciden con las de la lámina 2.

### E03-PRE-05. Respaldo de Trello al corte acordado

- Responsable: Nicolás Barra
- Prioridad: Media
- Estado: Pendiente
- Dependencias: E03-EQ-01, E03-L2-02

**Descripción.** Deja un respaldo del tablero Trello al corte de cierre (historias comprometidas, cerradas y, si las hay, bloqueadas), para sostener las cifras de sprint y el relato de capacidad. El tablero del equipo está en https://trello.com/b/tpq4wSRh/kiran.

**Criterios de aceptación.**

- Hay una captura o un export con fecha de corte visible.
- Lo que se muestra coincide con las cifras de E03-L2-02.

---

## Resumen de carga por integrante

Los ítems de equipo (E03-EQ-01 a E03-EQ-04, E03-DEF-06, E03-PRE-02 y E03-PRE-03) los resuelven los cuatro. La tabla cuenta solo las tareas con responsable principal. E03-PRE-01 queda a cargo de Giannina y Skarlett, con revisión de Nicolás y Ari.

| Integrante | Ítems a cargo | Identificadores | Enfoque |
| --- | ---: | --- | --- |
| Giannina Guerrero | 6 | E03-L1-04, E03-L2-04, E03-L3-02, E03-L3-03, E03-DEF-01, E03-DEF-02 | Mapa de integración, hitos y cambios, marco de la lámina 3, guion de la reunión. Además co-lidera E03-PRE-01. |
| Nicolás Barra | 6 | E03-L1-01, E03-L2-02, E03-L2-06, E03-L3-04, E03-DEF-03, E03-PRE-05 | Componentes de inventario y tickets, sprints, contraste de alcance, C-05 en lo técnico, respaldo de Trello. |
| Skarlett Tropan | 6 | E03-L1-03, E03-L2-03, E03-L2-05, E03-L3-01, E03-L3-05, E03-DEF-04 | Impacto y traspaso, calidad, infografía de cierre, retrospectiva del equipo. Además co-lidera E03-PRE-01. |
| Ari Araya | 6 | E03-L1-02, E03-L2-01, E03-L2-07, E03-L3-06, E03-DEF-05, E03-PRE-04 | Infraestructura, cierre financiero, lectura del techo para dirección, respaldo de Excel y nube. |

## Dependencia crítica

Sin E03-EQ-01 (fecha de corte), E03-EQ-02 (regla para las cifras posteriores al 19 de octubre) y E03-EQ-03 (estado de C-05), no se puede cerrar la lámina 2 ni el balance de la reunión. Esas tres decisiones son el primer trabajo del equipo.
