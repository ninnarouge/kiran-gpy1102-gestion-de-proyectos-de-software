# Insumo Ari — factores del entorno y presupuesto de nube

**Para:** Informe ejecutivo Eva 1 (máx. 7 planas).  
**Quién:** Ari Araya (infraestructura y nube). Revisa factores: Giannina. Revisa nube: Nicolás.  
**Dónde entra:** sección 4 + Tabla 10 (bloque 2); Tabla 9 y RBS (bloque 1); criterios de la cuenta 6 de la EDT.

Esto es **insumo**. El Word no puede tragarse el archivo entero: usar los párrafos “para pegar” y las tablas; el resto es para que el equipo (y el oral) sepa por qué.

No se inventan montos de subsidio ni leyes de India. El techo US$ 20.700 y los tipos de costo ya están en el plan del repo (`scripts/eva01_docs.py`). El desglose de hosting es una **propuesta interna** para que se vea la nube; la suma final la cierra el equipo.

---

## 1. Bloque 2 — factores ambientales y estándares

### Qué pide la rúbrica

Factores ambientales y estándares con **impacto en este caso**. Una lista (“hay conectividad, hay PMBOK”) no basta: hay que decir qué se mueve en alcance, plazo, costo, calidad o riesgo.

Lenguaje de referencia: **PMBOK 6.ª** (PMI, 2017).

### Definiciones (una frase cada una)

| Término | Definición aquí | Ejemplo Kiran |
|---|---|---|
| **EEF** | Condición que el equipo **no controla** y que entra a la planificación | Conectividad del pueblo; fecha de reporte que pide un donante |
| **OPA** | Activo que el equipo **sí usa** (plantillas, lecciones, repositorios) | Acta, EDT, Gantt de Project Libre, listas de Trello, este plan |
| **EEF interno** | Viene de adentro de la organización ejecutora | Equipo de cuatro; nube aún no institucionalizada |
| **EEF externo** | Viene de afuera | Financiamiento mixto; marco de datos de hogares; clima/conectividad |

### Párrafo para pegar (sección 4 del informe)

Los factores ambientales de la empresa (EEF) son condiciones que el equipo no controla y que entran a la planificación (Project Management Institute [PMI], 2017). En este piloto los que más aprietan son el financiamiento mixto, la conectividad irregular, los datos de hogares y una infraestructura de nube que todavía no está institucionalizada en la empresa social. Internos: cultura de transparencia exigida por donantes; estructura matricial débil (empresa social + partner tecnológico + equipo de software de cuatro personas); capacidad limitada. Externos: distancia cultural y geográfica con la comunidad piloto; marco legal de datos de hogares; condiciones físicas de conectividad; estándares de la industria. Los OPA (plantillas de acta y EDT, este plan, lecciones en Trello) sí se pueden usar; el clima, no.

La nube permite desplegar el piloto sin comprar servidores, pero el costo es variable y el técnico en terreno no puede depender de una sesión permanente: el diseño asume carga por lotes. Privacidad y reportes a terceros son EEF legales: se declara qué dato se guarda, dónde (nube), quién accede (roles) y qué sale a donantes, alineado con ISO/IEC 27701, sin inventar leyes locales. Un donante que pide el reporte antes comprime la actividad 5.4; un técnico que no carga datos rompe la 2.3 y, con ella, la ruta crítica. Por eso los canales se declaran ahora: hitos para inversores, taller para el técnico, roles para privacidad.

### Tabla para pegar (Tabla 10 — EEF y estándares)

La fila de **nube** no estaba en el borrador del generador. Es el aporte específico de este insumo.

| Factor o estándar | Tipo | Impacto concreto en el piloto |
|---|---|---|
| Financiamiento mixto (inversores + subvención) | EEF externo financiero | El hito 8.4 (primer reporte al patrocinador, 4 dic 2026) es inamovible: el cronograma se diseña hacia esa fecha, no al revés. |
| Cultura comunitaria e idioma | EEF externo social | UX simple, pocos campos, capacitación 7.x. No se asume un onboarding “tipo app urbana”. |
| Conectividad irregular | EEF físico | Supuesto de carga por lotes. Si cae la red, el inventario miente y se rompe la ruta crítica. |
| Datos de hogares | EEF legal | Minimizar datos; roles 6.1 y tratamiento 6.2; alineación con ISO/IEC 27701. No se suben bases reales al repositorio. |
| Nube + costos variables | EEF tecnológico y financiero | Se escala sin comprar hardware, pero el hosting se mueve con el uso y depende de conectividad. El hosting va a costo variable; la contingencia 12 % cubre un alza en la prueba de terreno. No se promete “siempre en línea” en el pueblo. |
| PMBOK 6.ª | Estándar de dirección | Acta, EDT, CPM, interesados y línea base. Dirige el **proyecto**, no la operación diaria de tickets. |
| CMMI | Madurez de procesos | El piloto apunta a disciplina básica (plan + evidencias), no a un nivel 4 o 5. Evita que “una persona se acuerde” de cargar el Excel. |
| ITIL 4 | Gestión de servicio | El módulo de tickets se diseña como incidente / mantención, no como formulario suelto. |
| COBIT | Gobierno de TI | Quién aprueba un acceso y qué sale hacia inversores. Evita que “el de sistemas” decida solo. |

### Estándares: un lente cada uno (para no recitar tablas)

- **PMBOK 6.ª:** planificar el piloto (alcance, tiempo, costo, interesados).
- **CMMI:** que el proceso de cargar kits y abrir tickets no dependa de la memoria de una persona.
- **ITIL 4:** cuando el piloto pasa a operación, el ticket es gestión de incidente, no un campo en una planilla.
- **COBIT:** gobierno de accesos y de la información que viaja a donantes.
- **ISO/IEC 27701:** extensión de privacidad sobre seguridad de la información. En el oral basta: genera confianza, apoya cumplimiento, es flexible entre jurisdicciones (India ≠ un donante europeo) y obliga a decir qué se guarda, dónde, quién ve y qué se exporta.

No se usa un estándar para todo. Se elige el lente según la pregunta.

### Qué no va en el informe (para no pasarse de 7 planas)

- Números de leyes de India o de la Unión Europea que no están en el caso.
- Comparativa larga PMBOK / CMMI / COBIT / ITIL (eso se defiende en el oral).
- Arquitectura de nube (regiones, instancias, proveedores). Eva 1 planifica; el ambiente 6.3 es octubre.

---

## 2. Costos de nube y accesos (bloque 1: recursos / Tabla 9)

### Qué lidera este insumo

En la RBS, la **tecnología** del piloto es nube + repositorio + punto de carga en la comunidad. El techo autorizado del acta es **US$ 20.700**. Los hundidos **no** entran.

El borrador actual mezcla el hosting con otras líneas:

- Variable US$ 1.240 = “horas de soporte local **y** hosting según uso”
- Directo US$ 14.470 = “equipo de desarrollo, **nube del piloto**, taller”

Hace falta **clasificar** la parte nube (eso evalúa la unidad), no cotizar un proveedor.

### Tipos de costo aplicados a la nube

| Tipo | Definición corta | Cómo aparece la nube / accesos |
|---|---|---|
| **Variable** | Cambia con el volumen | Hosting (app, base, respaldos) según uso y meses de prueba |
| **Fijo** | No cambia en el rango del piloto | Dominio y casillas de acceso del piloto (~3 meses) |
| **Directo** | Se atribuye a **este** proyecto | Todo el hosting y el dominio de Kiran |
| **Indirecto** | Se comparte con otros trabajos | No se carga “la nube corporativa” entera al piloto |
| **De oportunidad** | Alternativa no elegida | Comprar un servidor en sitio: más plata y peor para terreno |
| **Hundido** | Ya se gastó; **no** decide el futuro | Estudio de terreno previo (US$ 2.800, **fuera** del techo) |
| **Contingencia** | Reserva para riesgos **identificados** | 12 % (US$ 1.890): un mes extra de hosting o alza en la prueba 4.4 |

Falacia que hay que poder nombrar: “ya gastamos el estudio de terreno, hay que seguir”. La decisión usa costos **futuros** y valor **futuro**.

### Desglose propuesto (interno; el equipo cierra la suma)

No son precios de un proveedor. Son una partición del techo **ya publicado**, para que la nube deje de ser un adjetivo dentro de otras filas.

| Ítem | Tipo | Monto propuesto (US$) | Nota |
|---|---|---|---|
| Hosting del piloto (~3 meses: app + base + respaldos) | Variable y directo | 480 | Sale de los 1.240 variables (el resto, ~760, queda en horas de soporte local) |
| Dominio y accesos del ambiente | Fijo y directo | 120 | Subítem de los 14.470 directos; no es el sueldo del equipo |
| Contingencia que cubre nube | Reserva 12 % | Parte de 1.890 | Riesgo identificado: alza de uso o mes extra en 4.4 |
| Estudio de terreno ya pagado | Hundido | 2.800 | Fuera de los 20.700 |

Si el equipo no quiere números internos en el PDF, el informe puede dejar la Tabla 9 como está y **solo agregar** la frase de abajo. Los US$ 480 / 120 quedan para el oral y el diccionario.

### Párrafo para pegar (después de la RBS / Tabla 9)

En la RBS, la tecnología del piloto es nube, repositorio, Project Libre, tablero Kanban y un punto de carga en la comunidad. El hosting es costo variable y directo: si el técnico carga más o la prueba en terreno se alarga, sube. Por eso no se trata como sueldo fijo y sí entra a la contingencia del 12 %. El dominio del ambiente es fijo y directo, de monto menor. El costo hundido del estudio de terreno previo no entra al techo de US$ 20.700 y no decide si se despliega o no. No se promete un servicio “siempre en línea”: el supuesto de conectividad irregular obliga a carga por lotes; si ese supuesto falla, el inventario miente aunque el hosting esté pagado.

### Criterios de aceptación — cuenta 6 (Ari es R en el RACI)

Para el enunciado de alcance o el diccionario de la EDT. Una viñeta cada uno; no es diseño de servidores.

| Paquete | Criterio de aceptación |
|---|---|
| **6.1 Roles y permisos** | El soporte local ve kits y tickets de su comunidad. No exporta la base de hogares. Dirección ve el tablero. Un patrocinador recibe el **reporte**, no la base. |
| **6.2 Tratamiento de datos** | Se guarda lo mínimo para operar: comunidad, hogar, kit, estado. No hay fotos de menores ni bases reales en el repositorio. |
| **6.3 Ambiente de despliegue** | Existe un ambiente del piloto distinto de pruebas. Secretos fuera de Git (solo `.env.example` en el repo). |
| **6.4 Puesta en marcha** | El técnico puede cargar o actualizar un kit **sin sesión permanente** (lote). Un kit dado de baja deja de contar como activo. |

### Relación con el cronograma (no es trabajo de Eva 1)

6.3 ambiente: 2–8 oct 2026. 6.4 puesta en marcha: 14–19 oct 2026. Holgura alta: no están en la ruta crítica. Eva 1 **planifica** estos paquetes; no los ejecuta.

---

## 3. Cómo usarlo al armar el Word

1. Pegar el párrafo de la sección 1 y la tabla (con la fila de nube).
2. Pegar el párrafo de costos junto a la Tabla 9. Sumar las dos líneas de hosting solo si el equipo acepta el desglose.
3. Meter las cuatro viñetas de la cuenta 6 en alcance / diccionario.
4. Recortar. Si pasa de una plana el bloque 2, sobra texto: ganar el oral con las definiciones, no hinchar el PDF.

Citas mínimas (APA), las mismas del generador: PMI (2017) para EEF; Baud (2020) si se nombra ITIL. Si se habla de interesados que mueven el éxito, etiquetar PMI (2021) y no mezclarlo en la misma frase que la definición de EEF.

---

## 4. Frases para el oral (no leer)

**EEF frente a OPA.** “EEF no los controlamos: la conectividad, la fecha del donante, el techo de presupuesto. OPA sí los usamos: la plantilla del acta, el Gantt, Trello.”

**Nube.** “Escala sin comprar hardware, pero es costo variable y depende de la red. Por eso hosting a variable, contingencia 12 %, y carga por lotes. No prometemos siempre online.”

**Privacidad.** “Qué se guarda, dónde (nube), quién entra (roles) y qué sale al donante. ISO 27701 nos da el marco; no recitamos una ley de India que el caso no trae.”

**Estándares.** “PMBOK dirige el proyecto. CMMI pide que el proceso no sea memoria de una persona. ITIL trata el ticket como incidente. COBIT dice quién aprueba un acceso.”

**Hundido.** “Los 2.800 del estudio previo ya se gastaron. No entran a los 20.700 y no deciden si desplegamos.”
