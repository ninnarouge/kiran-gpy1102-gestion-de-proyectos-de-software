# Informe de monitoreo y control del proyecto Kiran

**Asignatura:** GPY1102 Gestión de Proyectos de Software — Duoc UC  
**Evaluación:** Parcial N.° 2 — Informe grupal  
**Resultado de aprendizaje:** RA2 — Monitoreo y control del proyecto de software  
**Proyecto:** Kiran (piloto de plataforma de gestión operativa de kits solares)  
**Equipo:** Giannina Guerrero, Nicolás Barra, Ari Araya, Skarlett Tropan  
**Periodo del piloto:** 14 de septiembre de 2026 – 9 de diciembre de 2026  
**Presupuesto de referencia:** US$ 20.700 (línea base); US$ 21.200 propuesto ante incorporación del módulo de asistencia con IA  

---

## 1. Identificación del encargo

| Campo | Contenido |
|-------|-----------|
| Organización / caso | Emprendimiento social con piloto de kits solares; Kiran es el software de operación (no instala paneles) |
| Alcance del producto | Inventario, tablero operativo, tickets de mantención, reportes de impacto, roles y tratamiento de datos |
| Restricciones | Equipo de cuatro desarrolladores; técnico local no full time; conectividad irregular; techo presupuestario; cortes de entrega fijos |
| Objeto de este informe | Sistema de monitoreo y control; gestión de cambios; asignación de recursos; reporte de estado para partes interesadas |

El informe se estructura según los indicadores de evaluación de la dimensión grupal escrita: propuesta de monitoreo y control (IL 2.1), gestión del cambio (IL 2.2), asignación de recursos (IL 2.3) y documentación del estado del proyecto (IL 2.4).

---

## 2. Sistema de monitoreo y control

### 2.1 Propósito

El sistema de monitoreo y control tiene por objeto resguardar la planificación e integración del piloto: verificar el avance respecto de los hitos, detectar desvíos de alcance, tiempo, costo y calidad, y entregar información única a dirección y contraparte. No sustituye la ejecución; condiciona las decisiones de continuar, replanificar o detener gasto no autorizado.

### 2.2 Componentes e interacción

| Componente | Función | Responsable | Periodicidad |
|------------|---------|-------------|--------------|
| Project Libre (modelo de programación) | Fechas planificadas, ruta crítica, desvíos de hito | Dirección / backend | Por sprint y en cada hito |
| Trello (tablero de flujo) | Compromiso de sprint, trabajo en curso, bloqueos | Equipo completo; dirección en reasignaciones | Continuo |
| Excel de seguimiento financiero y consola de nube | Gasto acumulado, alertas de desviación, topes de API | Infraestructura | Quincenal |
| Indicadores estratégicos | Lectura consolidada para dirección | Dirección | En cada hito |
| Indicadores operativos | Detección temprana de calidad, capacidad y operación | Calidad / backend / dirección | Semanal o quincenal |
| Evaluación de hito por contraparte | Puntaje de aceptación del entregable del corte | Dirección y contraparte | En cada hito |
| Registro formal de cambios | Trazabilidad de solicitudes que alteran línea base | Dirección | Ante cada solicitud |

La interacción entre componentes es obligatoria: el flujo de Trello sin actualización de Project Libre genera divergencia plan–ejecución; el reporte financiero sin contraste con el trabajo real invalida la lectura de costo; un incremento construido fuera del registro de cambios rompe la integridad del plan inicial.

### 2.3 Representación del flujo de información

| Etapa | Origen | Salida | Destino de control |
|-------|--------|--------|--------------------|
| 1 | Operación en terreno y aplicación Kiran | Estados de kit, tickets, sincronización por lote | Base de datos del aplicativo |
| 2 | Desarrollo | Incremento según Definition of Done | Ambiente desplegado y tablero de flujo |
| 3 | Tablero de flujo | Capacidad, bloqueos, cumplimiento de sprint | Indicadores operativos de ritmo y calidad |
| 4 | Project Libre | Cumplimiento de hitos y ruta crítica | Indicadores estratégicos de tiempo e integridad |
| 5 | Excel y factura de nube | Desviación presupuestaria | Indicador de techo; detención de gasto no comprometido |
| 6 | Bitácora de soporte y, si aplica, registro del canal asistido | Carga de consultas y escalamiento | Indicadores de atención operativa |
| 7 | Consolidado de indicadores y puntaje de hito | Lectura única | Dirección y partes interesadas |

### 2.4 Hitos clave

| Hito | Fecha | Entregable de control | Criterio de cierre |
|------|-------|----------------------|--------------------|
| Inventario validado | 19 de octubre de 2026 | Un inventario confiable del piloto | Aceptación de contraparte; sin ampliación a segundo punto de acopio en esta ventana |
| Tablero operativo | 9 de noviembre de 2026 | Visibilidad operativa sobre el inventario | Tablero usable; priorización visual condicionada a capacidad |
| Tickets, pruebas y primer reporte | 4 de diciembre de 2026 | Tickets operativos, evidencia de prueba y reporte | Sin desplazar el cierre a la semana de entrega |
| Cierre y traspaso | 5 al 9 de diciembre de 2026 | Entrega formal | Sin construcción de alcance pendiente |

Un atraso de hasta tres días hábiles en un hito puede documentarse con causa; un atraso mayor no se absorbe con trabajo nuevo en la semana siguiente.

### 2.5 Indicadores

**Estratégicos (dirección / hito)**

| Indicador | Definición operativa | Umbral / acción |
|-----------|---------------------|-----------------|
| Cumplimiento de hitos | Entrega de los cuatro cortes con criterio del acta | 4/4 o causa si atraso ≤ 3 días; si mayor, sin trabajo nuevo la semana siguiente |
| Integridad plan–ejecución | Actividades de ruta crítica sin desvío no registrado | 100 % en hitos revisados; replanificar, no parchar solo el tablero de flujo |
| Alcance verificable | Paquetes con evidencia de aceptación al cierre del hito | No declarar hito cerrado sin evidencia; reapertura si puntaje < 4 |
| Techo presupuestario | Desviación acumulada respecto del techo vigente | Detener gasto no comprometido si desviación > 10 % |
| Cambios bajo control | Cambios constructivos con plan actualizado antes de construir | Cero construcción en producción sin registro |

**Operativos (equipo / periodo corto)**

| Indicador | Definición operativa | Umbral / acción |
|-----------|---------------------|-----------------|
| Defectos sobre líneas cambiadas | Defectos del periodo / líneas modificadas | ≤ 5; cero bloqueos abiertos |
| Tasa de reapertura (desarrollo) | Ítems reabiertos / cerrados del sprint | < 20 % |
| Cumplimiento de sprint | Historias comprometidas completadas | ≥ 80 % |
| Trabajo en curso y bloqueos | Tarjetas abiertas por persona; días en bloqueado | Máx. 2 por persona; > 5 días dispara reasignación formal |
| Integridad de estados de kit | Kits con hogar, responsable y estado coherente | Meta del inventario; sin cierre de hito si falla |
| Atención de fallas y soporte | Tiempos de atención; consultas fuera del sistema; contención del canal asistido | Mejora tras tablero usable; baja contención congela ampliación del canal |
| Coordinación y datos en terreno | Puntaje de contraparte; sincronización por lote | Puntaje ≥ 4; sin ampliar alcance sin control de cambios |

---

## 3. Gestión del cambio

### 3.1 Enfoque

La gestión del cambio asegura que las modificaciones a alcance, plazo, costo o capacidad no alteren de facto el plan inicial. Toda solicitud relevante se identifica, evalúa (impacto, costo, tiempo, factibilidad y riesgo), decide y, si se aprueba, actualiza los instrumentos del plan antes de construirse (Project Management Institute [PMI], 2017). La prioridad no se define por la insistencia del solicitante, sino por el efecto sobre los hitos y el techo.

### 3.2 Línea base previa a la ampliación de soporte asistido

La línea base del piloto (planificación Eva 1) contempla inventario, tablero, tickets y reporte; soporte predominantemente humano; presupuesto US$ 20.700; equipo de cuatro roles; límite de dos trabajos en curso por persona. Sobre esa base se evalúan las eventualidades del caso. La ampliación relevante a nivel de proyecto es la incorporación condicionada de priorización visual en el tablero, un canal de asistencia con preguntas frecuentes (fase 1) y un depósito mínimo de información operativa, con redimensionamiento presupuestario asociado.

### 3.3 Eventualidades del caso, estrategias y justificación

Se documentan a continuación las situaciones de cambio de **nivel proyecto** (no microtareas de implementación) y la decisión informada.

| Eventualidad | Estrategia adoptada | Justificación respecto del plan inicial |
|--------------|---------------------|----------------------------------------|
| Exigencia de evidencia fotográfica en cada ticket | Rechazo de la formulación con archivo; aceptación condicionada de prioridad y nota textual | La fotografía implica almacenamiento y esfuerzo que desplazan pruebas o reporte del hito de diciembre; la prioridad textual mejora la operación sin abrir gasto ni producto nuevo |
| Validación de inventario en un segundo punto de acopio en la misma fecha del primer corte | No implementación en la ventana del piloto | El hito del 19 de octubre compromete un inventario validado; duplicar el punto altera alcance y arrastra el tablero |
| Uso de un servicio externo de pago para producir el reporte | Rechazo; el reporte se elabora con medios del equipo | Introduce gasto no comprometido y dependencia en la semana de cierre; el objetivo del reporte ya está en el hito |
| Reasignación informal de trabajo ante bloqueos prolongados | Formalización como regla de capacidad: bloqueo superior a cinco días se resuelve o se reasigna entre los cuatro roles, con actualización del plan | Evita divergencia entre tablero operativo y Project Libre/Excel; protege la integridad plan–ejecución |
| Priorización visual en el tablero (cola o filtros de atención) | Aprobación condicionada a capacidad (reemplazo de trabajo equivalente) y sin alterar la semántica de estados del kit | Reduce consultas informales; es prerrequisito operativo de cualquier canal de asistencia que escale a persona |
| Incorporación de asistencia automatizada (preguntas frecuentes y canal con escalamiento humano) | Aprobación solo por fases: fase 1 condicionada a tablero usable, priorización visual, tope de gasto de API y corpus curado; el sistema no cierra tickets ni cambia estados de kit de forma autónoma | Atiende la presión de soporte en zona compleja sin abrir app ciudadana ni reemplazo total del técnico; limita el riesgo de alcance y de alucinación |
| Ampliaciones posteriores (aplicación masiva por hogar, monitoreo automatizado de flota, modelo propio, lago de datos completo) | Identificación como solicitud futura; rechazo en la ventana septiembre–diciembre 2026 | Exceden el 100 % de la EDT del piloto y el techo; se diferencian explícitamente de la fase 1 |
| Depósito mínimo de información operativa (logs/trazas agregadas) | Aceptación condicionada a minimización de datos, roles de acceso y alineación con ISO/IEC 27701; sin bases de hogares ni datos personales innecesarios en modelos externos | Sostiene el canal asistido y el reporte sin autorizar un lakehouse empresarial |

### 3.4 Orden de adopción de los cambios constructivos

1. Regla de capacidad y registro (permanente).  
2. Priorización visual en el tablero (hacia el hito de noviembre).  
3. Canal de asistencia fase 1 y depósito mínimo de información (tras tablero usable; no en la semana de cierre).  
4. Prioridad y nota en el ticket, solo si existe capacidad en el sprint del hito de diciembre.  
5. Fuera de ventana: segundo punto de inventario, servicio externo de reporte, fotografía en ticket, app ciudadana, lago de datos completo y monitoreo de flota con IA.

### 3.5 Efecto conjunto sobre costo, tiempo y esfuerzo

| Dimensión | Línea base | Con paquete de cambios aprobado |
|-----------|------------|----------------------------------|
| Presupuesto techo | US$ 20.700 | US$ 21.200 (redimensionamiento propuesto) |
| Partidas nuevas | Sin API de modelo generativo ni módulo de chat en el desglose inicial | Orden de magnitud US$ 200–340 (API y nube), con tope de control |
| Fechas de hito | 19 oct / 9 nov / 4 dic / cierre | Sin modificación de calendario |
| Esfuerzo | Cuatro roles; sin módulo de asistencia | Estimación adicional del orden de 13 a 22 días-persona, absorbida por sustitución de trabajo comprometido, no por ampliación de plantilla |
| Soporte | Predominio de atención humana e informal | Contención parcial por preguntas frecuentes; escalamiento humano obligatorio |

**Decisión presupuestaria:** la asistencia automatizada no se financia “en silencio” dentro de US$ 20.700. El equipo propone ampliar el techo autorizado a US$ 21.200. Alternativa: uso parcial de la contingencia del 12 % con acta. Reasignar recortando soporte humano en zona compleja no es la primera opción. Mientras no exista autorización, no se construye el módulo de asistencia.

---

## 4. Plan de asignación de recursos

### 4.1 Criterio general

La asignación de recursos identifica tipo, cantidad y disponibilidad de personas, presupuesto e infraestructura necesarios para ejecutar el plan y controlar su uso (PMI, 2017). El recurso crítico no exclusivo del equipo de software es el técnico local: su disponibilidad condiciona la veracidad del inventario y de los tickets.

### 4.2 Recursos humanos

| Rol | Responsabilidad principal | Efecto del paquete de cambios | Mecanismo de control |
|-----|---------------------------|-------------------------------|----------------------|
| Dirección y frontend | Alcance, control de cambios, interfaz del tablero y del canal | Priorización visual e interfaz del canal de asistencia | Límite de dos trabajos en curso; reasignación formal ante bloqueos |
| Backend / datos | Inventario, tickets, integraciones | Integración del canal asistido y depósito mínimo de información | Definition of Done; indicadores de defectos y reapertura |
| Infraestructura y nube | Ambientes, accesos, seguimiento de gasto | Topes de API, despliegue y lectura de consumo en nube | Control quincenal; freno si desviación > 10 % |
| Calidad e impacto | Pruebas, reporte, traspaso | Curaduría de preguntas frecuentes y revisión de respuestas | Evidencia de prueba en cada incremento |
| Técnico / soporte local | Carga de estados y atención en terreno | Menor carga informal si priorización y canal funcionan; mantiene escalamiento humano | Participación en revisión de hito; no sustituible por automatización total |

No se incorpora un quinto perfil ni un especialista externo en desarrollo agéntico en la ventana del piloto. La capacidad adicional se obtiene por reordenamiento del backlog (sustitución de historias), no por ampliación de dotación.

### 4.3 Recursos financieros

| Concepto | Asignación | Seguimiento |
|----------|------------|-------------|
| Techo de línea base | US$ 20.700 | Excel quincenal |
| Techo propuesto con módulo de asistencia | US$ 21.200 | Condición de construcción del módulo |
| Contingencia (12 %) | US$ 1.890 | Solo con razón escrita |
| Consumo variable de modelo y nube del canal | Orden US$ 200–340; tope de API definido | Consola de nube; pausa ante incumplimiento de umbral |
| Horas de soporte humano | Partida variable del plan | No se vacía para financiar automatización |

### 4.4 Recursos técnicos

Infraestructura en nube, API de modelo gestionado, kit de desarrollo de agentes, herramientas de planificación (Project Libre), flujo de trabajo (Trello), seguimiento financiero (Excel) y depósito mínimo de información. Quedan fuera de la ventana: procesamiento con GPU dedicado, lago de datos empresarial y hospedaje de modelo propio.

### 4.5 Estrategias de viabilidad y rentabilidad

**Viabilidad.** Los cambios constructivos solo se incorporan si existe capacidad (sustitución de trabajo), si se respetan los hitos y si el financiamiento del módulo de asistencia está autorizado (techo redimensionado o contingencia con acta). El canal asistido no opera sin priorización visual ni sin corpus de preguntas frecuentes curado.

**Rentabilidad.** No se declara un ahorro fijo en dólares en el acta sin medición. Se establece una línea base de consultas de soporte tras el tablero usable y antes de activar el canal; en operación se compara el costo de soporte evitado con el gasto real de API y nube. Si el gasto de automatización supera de forma sostenida el ahorro (dos revisiones consecutivas), se suspende el canal o se abre un nuevo control de cambios. Se distingue la inversión de puesta en marcha (esfuerzo de integración) del gasto recurrente de operación (consumo de API, hosting y soporte humano residual).

---

## 5. Estado actual del proyecto e información para partes interesadas

### 5.1 Audiencias y valor de la información

| Parte interesada | Información de valor | Uso en la decisión |
|------------------|----------------------|--------------------|
| Dirección / comisión del caso | Estado de hitos, techo, cambios abiertos y riesgos | Autorizar redimensionamiento; condicionar o diferir el canal asistido |
| Contraparte / soporte local | Usabilidad del tablero, cola de atención, puntaje de hito | Validar entregables; reducir trabajo informal |
| Equipo de desarrollo | Capacidad, calidad, registro de cambios | Comprometer solo trabajo factible |
| Inversores / donantes (vía reporte del hito) | Coherencia entre operación y cifra reportada | Confianza en el informe de impacto |

### 5.2 Estado consolidado (según el plan de control vigente)

| Dimensión | Estado | Observación para la gestión |
|-----------|--------|-----------------------------|
| Periodo | Piloto en ventana septiembre–diciembre 2026 | Cierre formal el 9 de diciembre |
| Hito inventario | Compromiso: un inventario validado | Segundo punto de acopio no incorporado |
| Hito tablero | Compromiso vigente | Priorización visual condicionada a capacidad |
| Hito tickets y reporte | Compromiso vigente | Asistencia automatizada solo condicionada y post tablero usable |
| Presupuesto | Línea base 20.700; propuesta 21.200 | Sin construcción del canal asistido sin autorización |
| Capacidad | Cuatro roles; máx. dos trabajos en curso por persona | Reasignación formal ante bloqueos prolongados |
| Cambios aprobados / condicionados | Regla de capacidad; priorización visual; asistencia fase 1; depósito mínimo; prioridad textual en ticket | Sujetos a WIP y financiamiento |
| Cambios rechazados o diferidos en ventana | Fotografía en ticket; segundo inventario; servicio externo de reporte; app ciudadana; lago completo; monitoreo de flota con IA | Quedan registrados para evitar reingreso informal |
| Calidad y privacidad | Controles operativos activos; minimización de datos | Sin carga de bases reales al repositorio |

### 5.3 Cifras relevantes para la toma de decisiones

| Indicador o cifra | Valor de referencia | Implicancia |
|-------------------|---------------------|-------------|
| Techo línea base → propuesto | 20.700 → 21.200 | Condición de viabilidad del canal asistido |
| Costo variable estimado del canal | US$ 200–340 (orden); tope de API acotado | Control de factura y pausa ante desvío |
| Esfuerzo adicional estimado | 13–22 días-persona | Exige sustitución de alcance, no contratación |
| Umbral de desviación de gasto | > 10 % | Detención de gasto no comprometido |
| Límite de trabajo en curso | 2 por persona | Protección de calidad e integración |
| Puntaje mínimo de hito | 4 / 5 | Reapertura del corte si no se alcanza |

### 5.4 Síntesis para dirección

El plan inicial permanece como referencia única: los hitos no se modifican por acumulación informal de alcance. Se solicita autorización para redimensionar el techo a US$ 21.200 si se incorpora la asistencia automatizada en fase 1. El orden técnico es priorización visual antes del canal asistido; este último no sustituye al soporte humano. La rentabilidad se verificará con línea base de consultas versus consumo de nube. Las ampliaciones de producto (aplicación ciudadana, lago de datos completo, monitoreo de flota) permanecen fuera de la ventana y exigen un nuevo ciclo de control de cambios.

---

## 6. Conclusiones

El sistema de monitoreo y control articula herramientas de planificación, flujo de trabajo, seguimiento financiero e indicadores estratégicos y operativos, con hitos explícitos y flujo de información trazable. La gestión del cambio documenta eventualidades de nivel proyecto, estrategias aplicadas y justificación orientada a la integridad del plan. El plan de recursos prioriza la capacidad humana limitada, el techo financiero y la infraestructura cloud, con criterios de viabilidad y rentabilidad medibles. El estado reportado a las partes interesadas concentra las cifras y decisiones que habilitan o detienen la ampliación de soporte asistido sin comprometer los cortes del piloto.

---

## Referencias

Project Management Institute. (2017). *Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK)* (6.ª ed.). Project Management Institute.

Peters, L. J. (2024). *Software project management: Methods and techniques*. CRC Press, Taylor & Francis Group.

---

## Anexo A. Correspondencia con indicadores de evaluación del informe

| Indicador de evaluación | Contenido | Sección |
|-------------------------|-----------|---------|
| IE1 — Sistema de monitoreo y control, flujos e hitos | Componentes, flujo, hitos, indicadores | §2 |
| IE3 — Estrategias de gestión del cambio, problemáticas y justificación | Eventualidades, estrategias, orden, efecto conjunto | §3 |
| IE5 — Plan de asignación de recursos, viabilidad y rentabilidad | Humanos, financieros, técnicos, estrategias | §4 |
| IE7 — Estado actual e información de valor | Audiencias, tablero de estado, cifras, síntesis | §5 |
