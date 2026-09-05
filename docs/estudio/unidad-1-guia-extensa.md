# GPY1102 — Gestión de Proyectos de Software

# Unidad 1 · Guía extensa de estudio

**Ramo:** Gestión de Proyectos de Software  
**Sigla:** GPY1102 · **Créditos:** 10 Duoc / 4 SCT · **Línea:** FOL · **Formato:** Presencial, Sala de Proyectos  
**Prerrequisito:** GPY1101  
**Experiencia de aprendizaje:** *Planificación de Proyectos de Software* (RA1)  
**Materiales cubiertos:** 1.1.1 + 1.1.2 · 1.2.1 + 1.2.2 · 1.3.1 + 1.3.2 · IL1.4 (herramientas; no hay PPT en carpeta) · Eva Parcial 1  
**Fuentes:** Programa de Asignatura, PPTs de clase, actividades de estudiante, rúbrica Eva 1, Caso 7, bibliografía oficial (PMBOK 6ª 2017, SBOK 4ª 2023, ITIL 4)  
**Fuera de alcance:** Unidad 2 (monitoreo y control) y Unidad 3 (cierre), salvo cuando se necesita ver el hilo del semestre.

---

## 0. Cómo aprobar esta unidad

Imagina que te piden organizar un viaje largo con amigas, con plata de varias personas, a un lugar que ninguna conoce bien.

- Si no acuerdan **adónde van y qué no van a hacer**, cada una empaca para un viaje distinto. Eso es el **alcance**.
- Si no arman **días, escalas y quién maneja**, llegan tarde o se quedan tiradas. Eso es el **cronograma** y los **recursos**.
- Si no miran **clima, visas y reglas del país**, el plan se cae en el aeropuerto. Eso son los **factores ambientales y estándares**.
- Si eligen **mapa de papel** para una ciudad que cambia cada semana, o **GPS** para un tour cerrado de museo, eligen mal la forma de planificar. Eso es **predictivo / adaptativo / híbrido**.
- Si no pueden **mostrar el itinerario** en una pizarra y defenderlo cuando pregunta la tía que puso la plata, el viaje no se aprueba. Eso es la **Eva 1**.

Quien aprueba la Unidad 1 no es quien recita definiciones. Es quien puede:

1. **Definir** un proyecto de software con enunciado de alcance, exclusiones, supuestos y restricciones.
2. **Descomponer** el trabajo en EDT, estimar duraciones y encontrar la ruta crítica.
3. **Clasificar** costos y recursos, y armar un presupuesto inicial con contingencia.
4. **Analizar** factores ambientales internos/externos y estándares (PMBOK, CMMI, y el mapa con COBIT e ITIL) **sobre un caso real**.
5. **Elegir** un enfoque de planificación (predictivo, adaptativo o híbrido) y **justificarlo** con el contexto de la organización.
6. **Usar** una herramienta de industria (MS Project, Project Libre u Office 365) y decir **por qué esa**.
7. **Defender oralmente** todo lo anterior, sola, sin leer el informe.

### Resultado de aprendizaje (RA1)

> Planifica un proyecto de software, considerando requerimientos y procesos del cliente, factores ambientales y estándares de la industria, para gestionarlo e integrarlo de manera eficiente en la organización.

### Indicadores de logro

| IL | Horas clase | Qué tienes que demostrar |
|---|---|---|
| **IL1.1** | 4 | Define alcance, recursos, cronograma y costos a través de un **plan preliminar**, usando herramientas de la industria. |
| **IL1.2** | 4 | Analiza factores ambientales y estándares relevantes, **evaluando su impacto en casos reales**. |
| **IL1.3** | 6 | Define estrategias de planificación (predictivo / adaptativo / híbrido) mediante **planes de gestión específicos y contextualizados**. |
| **IL1.4** | 6 | Utiliza herramientas de planificación, **seleccionando las más óptimas** según el estándar y las necesidades de la organización. |

### Cómo estudiar esta guía

1. Leer el bloque (metáfora → esquema → ejemplo del Caso 7 → nombre técnico).
2. Decir en voz alta la **síntesis exigida** del final de cada parte. Si no sale limpia, aún no está.
3. Cerrar con la autoevaluación de la sección 12, **sin apuntes**.
4. Ensayar las 6 preguntas del pitch (sección 11) como si el docente estuviera al lado.

El Caso 7 (plataforma solar comunitaria) se usa como hilo en **toda** la guía: no es un anexo. El semestre trabaja **un solo caso** desde la semana 4 hasta el ET.

---

## 1. El mapa de la Unidad 1 (visión de conjunto)

```
                         RA1 · PLANIFICAR EL PROYECTO
                    (para gestionarlo e integrarlo después)
                                      │
     ┌──────────────┬─────────────────┼─────────────────┬──────────────┐
     ▼              ▼                 ▼                 ▼              ▼
  ┌──────┐     ┌─────────┐      ┌──────────┐     ┌──────────┐    ┌─────────┐
  │ 1.1  │     │  1.2    │      │   1.3    │     │   1.4    │    │ Eva 1   │
  │ Plan │     │ Clima   │      │ Receta o │     │ Lápiz    │    │ Informe │
  │ pre- │────►│ y       │─────►│ GPS      │────►│ (la he-  │───►│ 30% +   │
  │ limi-│     │ normas  │      │ (enfoque)│     │ rramien- │    │ oral    │
  │ nar  │     │         │      │          │     │ ta)      │    │ 70%     │
  └──────┘     └─────────┘      └──────────┘     └──────────┘    └─────────┘
     │              │                 │                 │
     │              │                 │                 │
  Acta,          EEF internos      Predictivo        MS Project
  alcance,       / externos        Adaptativo        Project Libre
  EDT, CPM,      PMBOK, CMMI,      Híbrido           Office 365
  PERT,          COBIT, ITIL,      Stakeholders      Justificar
  costos,        ISO 27701         Jira / Gantt      por la org
  recursos
```

**Competencia del programa (C4):** evaluar y gestionar proyectos en todo el ciclo de vida, con buenas prácticas y herramientas, en contextos **tradicionales y ágiles**. La Unidad 1 solo cubre el arranque: planificar. Monitoreo y cierre vienen después, **sobre el mismo caso**.

### Hilo del semestre (para no perderse)

| Momento | Qué entregan | Peso en el bloque de parciales | Impacto aprox. en nota final |
|---|---|---|---|
| Parcial 1 · Planificar | Informe ejecutivo + pitch analógico | 30% de 60% | ≈ 18% |
| Parcial 2 · Monitorear | Reporte + video 5–7 min | 35% de 60% | ≈ 21% |
| Parcial 3 · Cerrar | 3 láminas + reunión de cierre | 35% de 60% | ≈ 21% |
| ET | Defensa 15 min con PPT/Canva | 40% directo | 40% |

Los quizzes formativos (Eva For 1, 2 y 3) **no ponderan** en el programa.

### Bibliografía: no mezclar ediciones a ciegas

| Fuente | Edición | Rol en este ramo |
|---|---|---|
| Guía del PMBOK | **6ª, 2017** | Bibliografía obligatoria. Lenguaje de los PPTs 1.1, 1.2 y 1.3 (EDT, EEF, CPM, grupos de procesos). |
| Guía SBOK | 4ª, 2023 | Bibliografía obligatoria. Nutre el enfoque **adaptativo** (Scrum). |
| ITIL 4 (Baud) | 2020 | Bibliografía obligatoria. Aparece en la comparativa de estándares de 1.2. |
| PMBOK | 7ª, 2021 | Aparece en el material oficial local de la Eva 1 (interesados y valor). Útil para el pitch. |
| PMBOK | 8ª, 2025/26 | Resumen de apoyo en la carpeta. **No** es la biblio oficial. |

Para prueba y rúbrica: habla **PMBOK 6**. Usa la 7ª cuando te pregunten por **valor** e **interesados**.

---

## 2. Cimientos que la unidad da por sabidos

Antes de planificar hay que saber **qué es un proyecto** y qué no. La clase 1.1 arranca en el alcance, pero el acta de constitución (actividad 1.1.2, paso 1) y el PDF de valor de la Eva 1 exigen estos cimientos.

### 2.1 Proyecto vs operaciones

**Metáfora:** hacer el café de todas las mañanas es **operación** (se repite, mantiene el negocio). Inventar una receta nueva para el lanzamiento de octubre es **proyecto** (tiene inicio, fin y un resultado único).

| | Proyecto | Operaciones |
|---|---|---|
| Tiempo | Temporal: inicio y fin | Continuo |
| Resultado | Único (esta app, este piloto) | Repetitivo |
| Propósito | **Cambiar** el estado de la organización | **Mantener** el negocio |
| Ejemplo Caso 7 | Construir la plataforma del piloto | Atender tickets cuando ya esté en producción |

“Temporal” no significa corto: un proyecto puede durar dos años. Significa que **termina**. “Único” no significa que nunca se haya hecho software parecido: significa que **este** resultado, para **esta** comunidad piloto, no existía.

Nombre técnico: **proyecto** = esfuerzo temporal para crear un producto, servicio o resultado único. **Dirección de proyectos** = aplicar conocimientos, habilidades, herramientas y técnicas a las actividades para cumplir los requisitos.

### 2.2 Entregable, output, outcome y valor

**Metáfora:** el pastel es el **entregable**. Que los invitados se queden conversando feliz es el **outcome**. Que la cumpleañera se sienta querida es el **valor**.

- **Entregable (deliverable):** algo verificable que se produce (informe, módulo, tablero, capacitación).
- **Output:** lo que sales a entregar (la plataforma).
- **Outcome:** el efecto (los kits en falla se ven a tiempo; la comunidad tiene energía más estable).
- **Valor:** el indicador último de éxito. Puede ser plata (ahorro, ingreso) o no plata (confianza de donantes, impacto social, aprendizaje). Puede aparecer **durante**, al **cerrar** o **después** del proyecto.

El PDF de Eva 1 (PMBOK 7, principio “enfocarse en el valor”) insiste: si entregan el software y **no mejora** lo que prometieron, los interesados pueden ver el proyecto como fracaso aunque el código “funcione”.

En el Caso 7 el valor no es “tenemos un tablero”. Es que un kit dado de baja no siga contando como activo, que el soporte local priorice fallas reales, y que un inversor de impacto reciba un informe que pueda usar.

**Caso de negocio (business case):** documento que justifica por qué invertir ahora. Trae alineación estratégica, retorno esperado y viabilidad. Los proyectos suelen nacer de una **necesidad de negocio** + **justificación** + **estrategia**.

### 2.3 Interesados (stakeholders)

**Metáfora:** en el viaje, interesados son quienes ponen plata, quienes viajan, quienes se quedan cuidando la casa y el vecino al que le van a pedir el auto. Todos pueden **ayudar o torcer** el plan.

Definición: persona, grupo u organización que **afecta**, **es afectada** o **se percibe afectada** por una decisión, actividad o resultado del proyecto. La influencia puede ser positiva o negativa. No son estáticos: entran, salen y cambian de interés.

Según el PDF de Eva 1, los interesados pueden mover:

| Área | Cómo la tuercen |
|---|---|
| Alcance / requisitos | Pedir agregar, ajustar o sacar cosas |
| Cronograma | Acelerar, frenar o parar actividades |
| Costo | Recortar o inflar con requisitos nuevos |
| Equipo | Dejar o no dejar gente clave |
| Planes | Empujar cambios a lo ya acordado |
| Resultados | Facilitar o bloquear el trabajo |
| Cultura | Subir o bajar el involucramiento |
| Beneficios | Definir qué “vale la pena” a largo plazo |
| Riesgo | Fijar umbrales (“esto sí / esto no”) |
| Calidad | Exigir un nivel específico |
| Éxito | Decidir con qué se evalúa el proyecto |

Habilidades que pide el mismo texto: iniciativa, integridad, honestidad, colaboración, respeto, empatía, confianza, comunicación **bidireccional** frecuente.

**Interesados del Caso 7 (lista mínima para el informe):**

- Patrocinadores: inversores de impacto, agencia de subsidios, empresas tecnológicas asociadas.
- Cliente / beneficiarios: comunidades, hogares, técnicos de soporte local.
- Equipo del proyecto: desarrollo, diseño, datos, QA, responsable de impacto.
- Otros: autoridades locales, donantes, dirección de la empresa social, PMO si existe.

### 2.4 Gobernanza: el condominio y el departamento

**Metáfora:** la empresa es el condominio (reglas de todos). El proyecto es tu departamento (reglas propias **dentro** de las del condominio). Si remodelas sin preguntar al comité, te paran la obra.

- **Gobernanza organizacional:** quién aprueba, políticas, cumplimiento de toda la empresa.
- **Gobernanza del proyecto:** quién decide qué **en este** proyecto, con qué límite de autoridad, cómo se escala un problema.

La Unidad 1 pide planes **integrables** en la organización (IL1.3): no un plan lindo en el vacío.

### 2.5 Acta de constitución del proyecto

**Metáfora:** el permiso notarial del viaje. Sin firma de quien pone la plata, no hay viaje. Con firma, hay director/a y se puede gastar.

Nombre técnico: **Project Charter**. Es el documento que **autoriza** formalmente el proyecto y nombra al director/a, dándole autoridad para usar recursos.

Mínimo que debe quedar claro (PMBOK 6, y es el Paso 1 de la actividad 1.1.2):

- propósito y justificación
- objetivos medibles de alto nivel
- requisitos de alto nivel
- riesgos de alto nivel
- cronograma resumido de hitos
- presupuesto resumido
- lista de interesados principales
- criterios de aprobación
- director/a del proyecto y nivel de autoridad
- patrocinador que firma

El acta **no** es el plan detallado. El plan detallado nace **después**, usando el acta como techo.

---

## 3. Bloque 1.1 — Elaboración del plan preliminar (IL1.1)

**Material:** PPT 1.1.1 (39 láminas) · Actividad 1.1.2 (duplas, 2 h)  
**Objetivo de la clase:** planificar desde cero: alcance, cronograma, costos y recursos.

La clase se parte en cuatro actos: alcance → cronograma → costos → recursos. Eso **es** el plan preliminar. No es un Word de 40 páginas: es el primer mapa defendible.

### 3.1 Alcance del proyecto

**Metáfora:** el alcance es el contrato de “qué hay en la maleta y qué se queda en casa”. Si no escribes las exclusiones, alguien va a meter un piano.

Definir el alcance es desarrollar una **descripción detallada** del proyecto y del producto, hasta generar el **enunciado del alcance**. El proceso puede ser **altamente iterativo**: se escribe, se discute, se vuelve a escribir.

El enunciado permite un **entendimiento común** y deja las exclusiones **explícitas**.

#### Mínimo del enunciado (lámina de clase)

| Elemento | Pregunta que responde | Ejemplo Caso 7 |
|---|---|---|
| Descripción del alcance del producto | ¿Qué se construye? | Plataforma para registrar kits, tablero, tickets de mantención e informes de impacto de un piloto. |
| Criterios de aceptación | ¿Cuándo se da por bueno? | Un kit se puede crear, cambiar de estado (activo / en falla / dado de baja) y verse en el tablero el mismo día. |
| Entregables | ¿Qué se entrega verificable? | Módulo inventario, tablero, módulo tickets, reporte periódico, capacitación al soporte local. |
| Exclusiones | ¿Qué queda fuera? | Fabricar paneles, instalar en techos, tendido eléctrico, expansión a otras regiones en esta fase. |
| Restricciones | ¿Qué no se puede violar? | Presupuesto de piloto, conectividad irregular, fecha de reporte a donantes, equipo chico. |
| Supuestos | ¿Qué damos por cierto? | Hay conectividad mínima en la comunidad piloto; el soporte local carga datos; los inversores aceptan reporte mensual. |

Si un supuesto se cae (no hay señal), el plan tiene que decir **qué se hace**. Un supuesto sin plan B es un riesgo disfrazado.

#### Plantilla del enunciado (lámina 11)

Cabecera: fecha, nombre del proyecto, versión, director/a, patrocinador, cliente, equipo, otros interesados.

Cuerpo:

- **Antecedentes:** justificación, necesidad, oportunidad.
- **Descripción del producto o servicio:** el entregable final.
- **Objetivos:** qué se logra **con** ese entregable (otra vez: outcome, no solo output).

#### Herramientas y técnicas para definir alcance

1. **Analizar objetivos del producto y convertirlos en requisitos tangibles.**  
   “Mejorar la calidad de vida” no es requisito. “Registrar cada kit con estado operativo” sí lo es.

2. **Generación de alternativas.**  
   Ideas creativas: ¿app móvil para el técnico o solo web? ¿tickets por WhatsApp o módulo interno?

3. **Técnica Delphi.**  
   Consenso de expertos **en anónimo**. Un facilitador manda un cuestionario, resume respuestas, las devuelve para otra ronda. Reduce sesgos y evita que “el de más rango” imponga la definición. Útil cuando hay que definir alcance con gente de terreno (India), de software y de impacto social, que no se ponen de acuerdo en la primera reunión.

### 3.2 EDT / WBS — partir el elefante

**Metáfora:** no tragas un elefante entero. Lo partes en milanesas. La EDT es el cuchillo.

Nombre técnico: **EDT (Estructura de Desglose de Trabajo)** o **WBS (Work Breakdown Structure)**. Es un árbol jerárquico de **todo el trabajo** del proyecto. Regla de oro del PMBOK: la EDT cubre el **100%** del alcance acordado. Lo que no está en la EDT, **no se hace** (o se cuela como cambio).

#### Diagrama de descomposición (lámina 7)

```
Identificar entregables
        │
        ▼
 ¿Podemos estimar tiempo y costo?
        │
   NO ──► Subdividir ──► (volver a preguntar)
        │
   SÍ ──► Identificar cada paquete de trabajo ──► Verificar
```

Se subdivide hasta el nivel en que **sí** se puede estimar. Ese nivel más bajo gestionable se llama **paquete de trabajo**.

#### Niveles que pide la clase (lámina 9)

| Nombre | Qué es | Para qué |
|---|---|---|
| **Cuenta de control (control account)** | Punto de gestión donde se juntan alcance, plazo y presupuesto | Para medir desempeño después (Unidad 2) |
| **Paquete de planificación (planning package)** | Debajo de la cuenta de control: se sabe el trabajo, **aún no** las actividades detalladas | Para no fingir detalle que no existe |
| **Paquete de trabajo (work package)** | Nivel más bajo de la EDT | Aquí sí hay duración, costo y responsable |

Numeración típica: `2.2.3` cuenta de control → `2.2.3.1` paquete de planificación → `2.2.3.2.1` paquete de trabajo.

#### Diccionario de la EDT (lámina 10)

La EDT sola es un árbol de cajitas. El **diccionario** es la ficha de cada cajita. Ejemplo de la clase (componente `2.2.2.1 Mercado`):

| Campo | Ejemplo de la lámina |
|---|---|
| ID | 2.2.2.1 |
| Cuenta de control | 2.2 |
| Responsable | Juan Roble |
| Descripción | Estudio de mercado del sector de jugos naturales |
| Criterio de aceptación | El informe incluye importaciones por país del Reino Unido, últimos 5 años |
| Entregables | Presentación multimedia + informe encuadernado |
| Supuestos | El cliente entrega el listado de ventas antes del 15 de julio |
| Recursos | 2 analistas, 1 consultor, 3 computadores |
| Duración | 65 días hábiles |
| Hitos | 15 ago informe preliminar; 20 sep presentación; 12 oct informe final |
| Costo | $32.920 |
| Firma del director | (autorización) |

**Traducción al Caso 7** (paquete inventado `1.2.1 Tablero operativo`):

- Criterio de aceptación: se ve el estado de cada kit y el recuento de tickets abiertos/cerrados en una sola pantalla.
- Entregable: vista de tablero usable en navegador por el soporte local.
- Supuesto: hay datos de inventario cargados.
- Recursos: 1 front, 1 back, 1 QA.
- Hito: demo al patrocinador.
- Si no escribes el diccionario, la EDT es un dibujo bonito que nadie puede estimar.

### 3.3 Cronograma

**Metáfora:** el cronograma es la agenda del viaje con horarios reales, no el wishlist de “ojalá el lunes ya estemos allá”.

Desarrollar el cronograma = integrar actividades, secuencias, recursos y duraciones para crear el **modelo de programación**. Es **iterativo**. Determina fechas de inicio y fin planificadas, y los **hitos**.

#### Los dos pases que pide la clase

1. **Primera vez:** sin retrasos, sin adelantos, sin dependencias finas, **recursos ilimitados**. Sirve para ver la fecha de término **pesimista** (qué tan largo puede ser el trabajo “en bruto”).
2. **Segunda vez:** con retrasos, adelantos, dependencias y **recursos limitados**. Esta es la agenda que se puede defender.

#### Insumos típicos (lámina 18)

- lista de actividades
- EDT
- diagrama de red
- calendarios de recursos
- estimaciones de duración
- enunciado del alcance
- **activos de los procesos de la organización (OPA):** plantillas, lecciones de proyectos anteriores, calendarios de la empresa

Se puede esbozar en papel, pero el software de gestión facilita actualizar y compartir.

#### Tres dibujos, tres audiencias (lámina 24)

| Formato | Para quién | Qué muestra |
|---|---|---|
| **Cronograma de hitos** | Alta gerencia / dirección | Pocos puntos grandes (“piloto en producción”) |
| **Diagrama de Gantt (barras)** | Equipo y director/a | Tareas, duraciones, solapes, responsables |
| **Diagrama de red** | Planificación técnica | Predecesoras, caminos, ruta crítica |

Si le muestras un Gantt de 80 barras a un inversor, se pierde. Si le muestras solo 4 hitos al equipo de desarrollo, no sabe qué hacer el martes.

#### CPM — Método de la ruta crítica

**Metáfora:** en un edificio, la viga que si se atrasa atrasa **todo**. Pintar las paredes puede esperar; la losa no.

Nombre técnico: **CPM (Critical Path Method)**. Estima la duración **mínima** del proyecto calculando inicios y fines **tempranos y tardíos**, **sin** limitar recursos. La **ruta crítica** es la secuencia de actividades que forma el **camino más largo**. Cualquier cambio ahí mueve la fecha final. Hay que vigilarla con cariño (y con miedo sano).

**Forward pass (hacia adelante):** sacas la duración mínima / camino crítico.  
**Backward pass (hacia atrás):** sacas la holgura de cada actividad.

#### Lectura del nodo (lámina 21)

```
┌─────────────────┬──────────┬─────────────────┐
│ Inicio temprano │ Duración │  Fin temprano   │
├─────────────────┴──────────┴─────────────────┤
│              ACTIVIDAD (nombre)              │
├─────────────────┬──────────┬─────────────────┤
│ Inicio tardío   │ Holgura  │   Fin tardío    │
└─────────────────┴──────────┴─────────────────┘
```

Fórmulas de la clase (con convención de días calendario, duración que “ocupa” días inclusive):

- **Fin temprano (EF)** = (Inicio temprano + Duración) − 1
- **Inicio tardío (LS)** = (Fin tardío − Duración) + 1
- **Holgura** = Fin tardío − Fin temprano  
  (también: Inicio tardío − Inicio temprano)

Si la holgura es **0**, la actividad es crítica.

#### Ejemplo resuelto de la clase (actividades A–G)

Tabla de precedencias:

| N° | Actividad | Predecesora | Duración |
|---|---|---|---|
| 1 | A | — | 2 |
| 2 | B | — | 5 |
| 3 | C | — | 1 |
| 4 | D | B | 10 |
| 5 | E | A, D | 3 |
| 6 | F | C | 6 |
| 7 | G | E, F | 8 |

Caminos:

| Ruta | Suma | ¿Crítica? |
|---|---|---|
| Inicio → A → E → G → Fin | 2 + 3 + 8 = **13** | No (holgura grande) |
| Inicio → B → D → E → G → Fin | 5 + 10 + 3 + 8 = **26** | **Sí** |
| Inicio → C → F → G → Fin | 1 + 6 + 8 = **15** | No |

Nodos con holgura 0 (según el diagrama de red de la clase): **B, D, E, G**. Duración del proyecto: **26**.

Holguras del diagrama: A = 13, C = 11, F = 11. Puedes atrasar A casi dos semanas y el fin no se mueve… **hasta que se coma la holgura**. Si A se atrasa 14, de pronto **también** es crítica.

**Para el oral:** “La ruta crítica no es la más importante por fama; es la más larga. En nuestro piloto, si se atrasa la carga de inventario (equivalente a B+D), se atrasa el tablero y el reporte a donantes”.

#### PERT — tres valores

**Metáfora:** para llegar al aeropuerto, el GPS dice 40 min (lo más probable), sin tráfico 25 (optimista), con protesta 90 (pesimista). No planificas con 25 ni con 90: ponderas.

Nombre técnico: **PERT (Program Evaluation and Review Technique)** o estimación por tres valores.

- **O** = optimista  
- **M** = más probable  
- **P** = pesimista  

Fórmulas de la clase:

- Duración esperada = **(O + 4M + P) / 6**
- Desviación estándar = **(P − O) / 6**

Ejemplo de la lámina: O = 4, M = 7, P = 16  

- Duración = (4 + 4×7 + 16) / 6 = **8 días**  
- Desviación = (16 − 4) / 6 = **2 días**

Útil cuando el equipo no se atreve a dar un solo número (muy típico en software con incertidumbre de terreno, como el Caso 7).

### 3.4 Costos

**Metáfora:** el presupuesto no es “cuánto sale el avión”. Es avión + comida + seguro + el Airbnb que se pagó y no se usó + lo que dejaste de ganar por no trabajar esa semana.

Los costos construyen el **presupuesto global**. Incluyen personas, materiales y más. Hay que identificarlos **por fase**.

#### Cómo hacer un presupuesto (8 pasos de la lámina)

1. Definir la EDT.  
2. Especificar detalles de las tareas.  
3. Introducir valores de costos.  
4. Obtener costos totales.  
5. Tomar en cuenta **contingencias y costos extra**.  
6. Obtener la **aprobación**.  
7. Hacer seguimiento posterior (esto ya mira a la Unidad 2).  
8. Sacar conclusiones.

Sin el paso 1, el presupuesto es un número mágico. Sin el paso 5, el primer imprevisto te deja en cero. Sin el paso 6, el número no existe para la organización.

#### Principales tipos de costo (se caen en prueba)

| Tipo | Idea | Ejemplo Caso 7 |
|---|---|---|
| **Variable** | Cambia con el volumen | Horas extra de un consultor de datos; más kits = más filas que cargar |
| **Fijo** | No cambia con el volumen (en el rango del piloto) | Sueldo mensual de la product owner |
| **Directo** | Se atribuye **a este** proyecto | Viaje para presentar el plan a inversores; servidor del piloto |
| **Indirecto** | Beneficia a varios proyectos; cuesta repartirlo | Luz, teléfono, contabilidad, PMO |
| **De oportunidad** | La mejor alternativa que dejas de lado | El mismo equipo podría haber hecho otro producto que sí cobra tarifa |
| **Hundido / enterrado** | Ya se gastó; **no debe** decidir si sigues o no | El estudio previo de terreno que ya se pagó |

Trampa clásica: “ya gastamos tanto, hay que seguir”. Eso es **falacia del costo hundido**. Se decide con costos **futuros** y valor **futuro**, no con la factura vieja.

### 3.5 Recursos

**Metáfora:** recursos son todo lo que necesitas para que el viaje ocurra: gente, auto, plata, tiempo, mapas. Si listas solo a las conductoras y te olvidas de la bencina, no llegas.

Nombre técnico: **estimar los recursos de las actividades** = identificar **tipo, cantidad y características** de los recursos para completar las actividades. Eso permite estimar costo y duración con más precisión.

**Estructura de desglose de recursos (RBS):** árbol de **todos** los recursos (humanos y materiales), por categoría y tipo. Se documenta cantidad y **disponibilidad**.

Ejemplo de la clase (proyecto “realizar un curso PMP”):

- Personas (9): edición (audio, textos), ventas, técnicos (programadores, diseñadores, instructores).
- Materiales (10): tecnología (cámaras, computadores, micrófonos, software) e instalaciones (oficinas, hospedaje).
- Total visualizado: 19 ítems de recurso (el software iba con asterisco: no siempre se cuenta igual que un micrófono).

**Traducción Caso 7 (mínimo):**

| Categoría | Ejemplos |
|---|---|
| Personas | Dev front, dev back, QA, diseño, responsable de impacto, soporte local, product owner |
| Tecnología | Nube, repo, herramientas de tickets, celulares/tablets de terreno, conectividad |
| Instalaciones | Espacio de la empresa social; punto de apoyo en la comunidad |
| Financieros | Aporte de inversores, subsidio, reserva de contingencia |

### 3.6 Actividad 1.1.2 — lo que hay que producir en 2 horas

Situación: ejecución práctica, duplas, Sala de Proyectos, evalúa **IL1.1**.

| Paso | Entregable | Truco |
|---|---|---|
| 1 | Acta de constitución | Autoriza y nombra director/a. Sin esto, el resto es un wish. |
| 2 | Alcance + EDT | Incluidos / no incluidos. Fases, actividades, tareas, paquetes de trabajo. |
| 3 | Cronograma | Hitos, duraciones, asignación de recursos a actividades. |
| 4 | Recursos | Humanos, técnicos, financieros. |
| 5 | Presentar | Word para plantillas + **análogico** (pizarra, kraft) para el grupo. |

### 3.7 Síntesis exigida 1.1 (para desarrollo / oral)

> Un plan preliminar no es un cronograma suelto. Es **acta** (autorización) + **enunciado de alcance** (qué / qué no, criterios, exclusiones, supuestos, restricciones) + **EDT con diccionario** (el trabajo al 100%) + **modelo de programación** (red, CPM/PERT, Gantt, hitos) + **recursos y costos clasificados**, con contingencia y aprobación. La ruta crítica es el camino más largo; PERT pondera incertidumbre; los costos hundidos no deciden el futuro.

Preguntas de reflexión de la clase (úsalas de ensayo):

1. ¿Qué elementos consideras más importantes en la planificación de un proyecto de software?  
2. ¿Cómo asegurar precisión en la estimación de recursos?  
3. ¿Qué desafíos al crear el cronograma y cómo resolverlos?  
4. ¿Qué tan claro quedó el alcance?  
5. ¿Identificamos todos los recursos?  
6. ¿El cronograma es realista?  
7. ¿Consideramos los costos más relevantes?

---

## 4. Bloque 1.2 — Factores ambientales, normas y estándares (IL1.2)

**Material:** PPT 1.2.1 (33 láminas) · Actividad 1.2.2 (equipos, 2 h)  
**Metáfora madre de la clase:** los factores ambientales son el **clima**. Un gestor que no mira el pronóstico no es valiente: es imprudente.

### 4.1 Qué es un factor ambiental (definición de lámina, lenguaje PMBOK 6)

**Factores ambientales de la empresa (EEF, Enterprise Environmental Factors):** condiciones que **el equipo no controla** y que influyen, restringen o dirigen el proyecto. Pueden ser **internos o externos**. Son **entrada** de muchos procesos, sobre todo de **planificación**. Pueden **ampliar o recortar** las opciones. Pueden ayudar o pegar.

No son “el ambiente de la oficina con plantitas”. Son el sistema completo en el que el proyecto respira.

#### EEF internos (lámina 4)

- cultura, estructura y gobernanza de la organización
- distribución geográfica de instalaciones y recursos
- infraestructura
- software informático
- disponibilidad de recursos
- capacidad de los empleados

#### EEF externos (lámina 4)

- condiciones de mercado
- influencias sociales y culturales
- restricciones legales
- bases de datos comerciales
- investigaciones académicas
- estándares gubernamentales o de la industria
- consideraciones financieras
- elementos ambientales físicos

**Complemento útil (PMBOK 6):** junto a los EEF viven los **OPA (Organizational Process Assets)**: lo que **sí** es de la organización y **sí** puedes usar (plantillas, políticas, lecciones aprendidas, repositorios). EEF = clima y terreno. OPA = la caja de herramientas de la casa.

#### Los tres focos narrativos de la clase

La clase agrupa el clima en tres capítulos para estudiarlos, aunque en la lámina 4 la lista es más larga:

1. **Entorno organizacional**  
2. **Regulaciones gubernamentales**  
3. **Avances tecnológicos y estándares de la industria**

### 4.2 Entorno organizacional

**Metáfora:** el ecosistema donde vive el proyecto. Cultura, valores, estructura y políticas pueden **empujar o trabar**.

- Cultura positiva (colaboración, innovación, comunicación abierta) = motor.  
- Estructura rígida o comunicación deficiente = barrera que hay que cruzar **a propósito**, no “después vemos”.

Puntos clave:

- **Cultura:** ambiente de apoyo o de miedo a reportar malas noticias.
- **Estructura:** roles, responsabilidades, flujo de información (funcional, matricial, proyectizada).
- **Políticas y procedimientos:** reglas internas (quién aprueba un gasto, cómo se pide un ambiente de nube).

**Caso 7:** empresa social + inversores de impacto + subsidio + partner tecnológico. Eso **no** es una startup de tres amigos. Hay que reportar, hay que ser transparente, hay comunidades con otra cultura y otro idioma. Un plan “ágil de garage” sin gobernanza de reporte a donantes **no se integra**.

### 4.3 Regulaciones gubernamentales

**Metáfora:** el marco legal es el reglamento del condominio del país. Cumplir no es solo “no te multen”: es **ganar confianza** de usuarios e inversores.

Puntos clave de la clase:

- cumplimiento legal
- privacidad de datos
- seguridad y conformidad

La clase insiste: las regulaciones **no son solo obstáculos**. Son guías para operar con integridad. Abordarlas proactivo = ventaja competitiva.

#### ISO/IEC 27701 (lámina 15, para nutrir privacidad)

La clase muestra esta norma como forma de **demostrar** protección de datos personales. Ideas que hay que poder decir:

- se integra con las normas principales de seguridad de la información
- genera confianza en la gestión de información personal
- apoya el cumplimiento de otras leyes y requisitos de privacidad
- es flexible a particularidades jurisdiccionales (Chile ≠ India ≠ un donante europeo)
- aporta transparencia entre interesados
- facilita acuerdos comerciales (sistemas y procesos alineados)

**Nutrición con el resto de tu malla (sin reemplazar al PPT):** en Chile pesan leyes de datos (p. ej. el marco de protección de datos personales que viste en Seguridad). En el Caso 7 el piloto es en India, con inversores internacionales: hay que preguntarse **qué datos de hogares** se guardan, **dónde** (nube), **quién** accede (soporte local) y **qué informe** sale hacia donantes. No hace falta citar de memoria el número de cada ley en el oral, pero sí decir: “privacidad de hogares y reportes a terceros son EEF legales; el plan incluye minimización de datos y roles de acceso”.

### 4.4 Avances tecnológicos

La tecnología se mueve. Cada avance es puerta o trampa.

Puntos clave de la clase:

- **Inteligencia artificial:** automatiza y apoya decisiones (en el Caso 7: detectar kits anómalos; ojo con sesgos y con datos de gente vulnerable).
- **Computación en la nube:** escala y acceso (y dependencia de conectividad + costos variables).
- **Tecnologías emergentes:** obligan a adaptar el plan.

Ser “proactivo y adaptable” es el cierre de la introducción de 1.2: el clima no se espera sentada; se lee y se arma plan B.

### 4.5 Estándares de la industria: la brújula

**Metáfora:** estándares = recetas ya probadas por mucha gente. No improvisas la higiene de un restaurante desde cero.

La clase centra **PMBOK** y **CMMI**, y en una lámina compara también **COBIT** e **ITIL** (esto último calza con la biblio oficial ITIL 4).

#### PMBOK (Project Management Body of Knowledge)

Guía de fundamentos para dirigir proyectos. En la 6ª edición (la del ramo) se organiza en **grupos de procesos** (inicio, planificación, ejecución, monitoreo y control, cierre) y **áreas de conocimiento** (integración, alcance, cronograma, costos, calidad, recursos, comunicaciones, riesgos, adquisiciones, interesados).

Puntos clave de la clase 1.2:

- **Integración:** que las piezas no se peleen entre sí.
- **Gestión del alcance:** qué se entrega.
- **Tiempo y costos:** plazos y plata.

Integrar PMBOK = enfoque metódico, basado en datos, alineado a objetivos de la organización.

#### CMMI (Capability Maturity Model Integration)

**Metáfora:** no pregunta solo “¿este proyecto salió bien?”. Pregunta “¿qué tan adulta es la forma de trabajar de la organización?”.

Es un modelo para mejorar la **madurez de procesos**. Filosofía de mejora constante: identificar huecos e implementar estrategias de eficiencia y calidad.

Puntos clave: madurez de procesos, mejora continua, calidad y eficiencia.

Niveles de madurez (nutrición clásica de CMMI, útil si preguntan “qué es madurez”): de “depende del héroe del equipo” (inicial) hacia procesos definidos, medidos y en mejora. No hace falta recitar los cinco niveles si no están en la lámina; sí hay que decir que CMMI mira **la organización**, no solo el Gantt de este semestre.

#### Comparativa de la clase: PMBOK, CMMI, COBIT, ITIL

Lectura útil de la tabla (verde = cubre; rojo = no es su foco; NA = no aplica):

| Pregunta | Quién brilla |
|---|---|
| ¿Es para **proyectos**? | PMBOK, CMMI, COBIT. ITIL queda NA (es más de **servicio**). |
| ¿Operación del **servicio**? | CMMI, COBIT, ITIL. PMBOK no es su fuerte. |
| ¿**Infraestructura**? | ITIL. PMBOK no. |
| ¿**Desarrollo**? | PMBOK, CMMI, COBIT. ITIL NA. |
| ¿Gestión de **incidencias** y métricas de proceso? | CMMI, COBIT, ITIL. PMBOK NA o débil. |
| ¿Definir operativa concreta de procesos? | ITIL. |
| ¿**Mejora continua**, seguimiento, ciclo de producto, cambio? | Los cuatro. |
| ¿Compatible ISO 9001 e ISO 20000? | Los cuatro (según la tabla). |
| ¿Certifica a la **organización** por sí solo? | La tabla marca NA en los cuatro (otra cosa es certificarse **en** CMMI o ser PMP). |

**Cómo usarlo en el Caso 7 sin recitar la tabla entera:**

- **PMBOK:** para planificar el piloto (alcance, tiempo, costo, interesados).
- **CMMI / calidad de proceso:** para no depender de que “Skarlett se acuerde de cargar el Excel”.
- **ITIL:** cuando el piloto pase a operación (tickets, incidentes, cambios). Eso **conecta** con la Unidad 2 y con el cierre hacia operaciones.
- **COBIT:** gobierno de TI (quién decide, cómo se controla la información) si los inversores piden trazabilidad.

No se usa **un** estándar para todo. Se **elige el lente** según la pregunta.

### 4.6 Actividad 1.2.2

Equipos, 2 h, entrega + presentación, evalúa **IL1.2**.

1. Identificar factores ambientales relevantes (legislación, economía, tecnología, cultura…).  
2. Métodos para analizar el impacto (no basta listar: hay que decir **cómo pega**).  
3. Ejemplos en proyectos de software previos.  
4. Documentar y presentar.

**Métodos simples de impacto (nutrición, para no dejar el paso 2 vacío):**

- matriz factor × efecto (alcance / plazo / costo / calidad / riesgo)
- semáforo (alto / medio / bajo) + dueño del factor
- “si este factor empeora, ¿qué actividad de la ruta crítica se mueve?”

### 4.7 Mapa de factores del Caso 7 (para el informe)

| Factor | Interno / externo | Impacto en el plan |
|---|---|---|
| Cultura de la empresa social y de la comunidad | Interno + externo cultural | El tablero tiene que servirle al técnico local, no solo al inversor. |
| Estructura de financiamiento mixto | Interno + financiero externo | Hitos de reporte a donantes entran al cronograma **sí o sí**. |
| Distribución geográfica (equipo vs terreno en India) | Interno geográfico | Desfase horario, visitas caras, supuestos de conectividad. |
| Privacidad de datos de hogares | Legal externo | Minimizar datos, roles, posible ISO 27701 / leyes locales. |
| Conectividad física | Ambiental físico | Modo offline o carga por lotes; si no, el inventario miente. |
| Nube + costos variables | Tecnológico + financiero | Costo variable de hosting; contingencia. |
| Estándar PMBOK | Industria | Acta, EDT, ruta crítica, interesados. |
| ITIL (tickets) | Industria / operación | El módulo de mantención no es “un form”: es gestión de incidentes. |

### 4.8 Síntesis exigida 1.2

> Los EEF son condiciones **fuera del control del equipo** que entran a la planificación. Se miran internos (cultura, estructura, infraestructura, gente, software) y externos (mercado, leyes, cultura, finanzas, físico, estándares). PMBOK dirige **el proyecto**; CMMI madura **procesos**; ITIL opera **el servicio**; COBIT gobierna **TI**. En un caso real hay que decir el **impacto**, no la lista. Privacidad y seguridad no son adorno: son requisito de confianza.

Preguntas de reflexión de la clase:

1. ¿Qué factores ambientales influyen más en proyectos de software?  
2. ¿Cómo asegurar cumplimiento de estándares en *tu* proyecto?  
3. ¿Qué desafíos al analizar factores y cómo resolverlos?

---

## 5. Bloque 1.3 — Estrategias de planificación (IL1.3)

**Material:** PPT 1.3.1 (25 láminas) · Actividad 1.3.2 (equipos, 2 h)  
**Metáfora madre:** construir una casa **sin plano**. ¿Vivirías ahí? Un proyecto de software sin estrategia de planificación es esa casa.

### 5.1 Por qué planificar (aunque “ágil” suene a no planificar)

La clase abre con cuatro aportes de la planificación:

| Aporte | En humano |
|---|---|
| Fundamento del éxito | Sin plan, hasta lo simple se tuerce |
| Visión clara | Todos entienden objetivos y expectativas |
| Gestión de riesgos | Se ven problemas **antes**, no en producción |
| Optimización de recursos | No sobrecargar gente ni reventar plazo/presupuesto |

Ágil **no** es “no planificar”. Es planificar en **ciclos cortos** y volver a planificar cuando el terreno cambia. Eso es el enfoque adaptativo.

### 5.2 Enfoque predictivo — la receta

**Metáfora de la clase:** seguir una receta. Cada paso está pensado para un resultado.

**Definición:** enfoque **secuencial y estructurado**. Una fase se completa antes de partir la siguiente (la familia clásica “cascada” vive aquí).

**Características:**

- requisitos **claros al inicio**
- estructura y control por fases
- se buscan **pocos cambios**
- sirve cuando objetivos y entorno son **estables**

**Beneficios:** predecible, fácil de supervisar por hitos.

**Desventajas:** rígido. Si el cliente cambia de idea en la fase 4, duele.

**Caso de la clase:** sistema de contabilidad para una gran corporación, requisitos claros y estrictos. Cronogramas detallados, control riguroso, pocos cambios, se cumple el plazo.

**Caso 7 — dónde sí calza lo predictivo:** inventario de kits (estados finitos: activo / falla / baja), estructura de reporte a donantes, cumplimiento de privacidad. Eso no debería “descubrirse” cada sprint como si fuera una red social.

Herramientas asociadas: **Microsoft Project**, cartas Gantt.

### 5.3 Enfoque adaptativo — el GPS

**Metáfora de la clase:** el GPS recablea cuando hay un árbol caído.

**Definición:** enfoque **dinámico y flexible**. Se ajusta mientras avanza.

**Características:**

- se adapta a cambios de requisitos o entorno
- **iterativo e incremental** (ciclos, revisiones, mejoras)
- colaboración continua con interesados

**Beneficios:** innovación; el producto se acerca a lo que el cliente **ahora** necesita.

**Desventajas:** si no se gestiona, se desvían tiempo y recursos (“siempre una cosa más”).

**Caso de la clase:** plataforma de redes sociales en mercado rápido. Iteraciones, feedback, producto que se mueve con el mercado.

**Caso 7 — dónde sí calza lo adaptativo:** cómo se ve el tablero en terreno, qué ticket es realmente útil para el técnico local, cómo medir “impacto social” sin inventar un indicador vanidoso. Eso se **descubre** con el piloto.

Herramientas asociadas: **Jira** (sprints, Kanban), **Trello**, **Asana**.

**Nutrición SBOK / Scrum (biblio oficial, para hablar fino en adaptativo):**

| Pieza Scrum | Para qué |
|---|---|
| Product Owner | Maximiza valor; ordena el backlog |
| Scrum Master | Cuida el proceso, quita impedimentos |
| Developers | Construyen el incremento |
| Product Backlog | Lista viva de trabajo |
| Sprint | Ciclo corto de planificación y entrega |
| Incremento | Pedazo usable al final del ciclo |
| Daily / Review / Retro | Inspeccionar y adaptar |

No hace falta montar Scrum de libro si el equipo es de cuatro y el piloto es chico. Sí hace falta el **espíritu**: entregar algo usable, mirar, ajustar.

### 5.4 Híbrido — el calzado según el terreno

**Metáfora de la clase:** no corres maratón en sandalias ni playa en clavos. El enfoque se elige **según el terreno**.

El PPT llama a esto **hibridación**: combinar elementos de ambos para maximizar resultados.

Estrategias de adaptación que lista la clase:

1. **Análisis del contexto** — ¿el entorno es estable o volátil?  
2. **Hibridación** — predictivo donde hay certeza; adaptativo donde hay aprendizaje.  
3. **Participación de interesados** — si no están, el GPS no tiene destino.  
4. **Evaluación continua** — el plan no se talla en piedra.

**Recomendación defendible para el Caso 7 (modelo para el informe):**

```
CAPA PREDICTIVA (cumplimiento y datos maestros)
  Inventario · estados del kit · roles y privacidad · calendario de reportes a donantes

CAPA ADAPTATIVA (aprendizaje de terreno)
  UX del tablero · flujo de tickets · indicadores de impacto · soporte local
```

Eso **es** un plan de gestión contextualizado (IL1.3): no “somos ágiles” ni “somos cascada”. Es “esto sí se congela, esto se itera”.

### 5.5 Herramientas según enfoque (puente a IL1.4)

| Enfoque | Herramientas de la clase | Cuándo se ve bien en el Caso 7 |
|---|---|---|
| Predictivo | MS Project, Gantt | Ruta crítica del piloto, hitos de subsidio |
| Adaptativo | Jira, Trello, Asana | Backlog del tablero y de tickets |
| Híbrido | Una de cada, o Project Libre + tablero Kanban | Gantt de hitos + Kanban semanal del equipo |

La herramienta **sigue** a la estrategia. No al revés.

### 5.6 Actividad 1.3.2

Equipos, 2 h, entrega + presentación, evalúa **IL1.3**.

1. Identificar enfoques (predictivo, adaptativo, **híbrido**).  
2. Analizar necesidades del proyecto **y de la organización**.  
3. Desarrollar estrategias con herramientas y técnicas.  
4. Aplicarlas al caso.  
5. Documentar y presentar.

### 5.7 Síntesis exigida 1.3

> Planificar es la columna vertebral, también en ágil. **Predictivo** = receta, requisitos estables, control por fases, Gantt/Project. **Adaptativo** = GPS, iteración, interesados cerca, Jira/Kanban. **Híbrido** = calzado según terreno: se congela lo regulado y se itera lo que se aprende. La estrategia se argumenta con el **contexto de la organización**, no con la moda del equipo.

Preguntas de reflexión de la clase:

1. ¿Cómo integrarías predictivo y adaptativo en un solo proyecto?  
2. ¿Qué papel juegan las herramientas tecnológicas?  
3. ¿Cómo asegurarías la participación de todos los stakeholders?

---

## 6. Bloque 1.4 — Selección de herramientas (IL1.4)

**Material en carpeta:** no está el PPT 1.4 ni la actividad 1.4.2.  
**Material que sí obliga:** Programa (Act 1.4, 6 h), rúbrica Eva 1, herramientas nombradas en 1.3.1 y en la pauta de implementación.

IL1.4 no pide “conocer logos”. Pide **usar** la herramienta y **justificarla** según características y necesidades de la organización.

### 6.1 Qué pide Duoc explícitamente

Recursos de la Eva 1: Office 365, **Microsoft Project**, **Project Libre**, etc. Presentación del pitch: medios **analógicos** (pizarra, kraft, muro).

Criterio de rúbrica (nivel 100%): demuestra uso **y** justifica la selección en función de las necesidades de la organización. El oral (20%) vuelve a preguntar lo mismo: si no puedes defender el “por qué”, se cae.

### 6.2 Menú y criterio de elección

| Herramienta | Brilla en | Se queda corta si… | Argumento Caso 7 |
|---|---|---|---|
| **Microsoft Project** | CPM, recursos, línea base, reportes a gerencia | El equipo no tiene licencia / curva alta | Ideal si la empresa social o el partner tecnológico ya lo usa. |
| **Project Libre** | Mismo tipo de plan (Gantt, red, recursos) **sin** licencia cara | Menos ecosistema corporativo | Fuerte si el piloto es de impacto y el presupuesto es chico. |
| **Excel / Office 365** | EDT, presupuesto, diccionario, RACI simple | Se rompe cuando hay muchas dependencias | Buen complemento; malo como única herramienta de ruta crítica. |
| **Jira** | Backlog, sprints, tickets reales | No reemplaza un Gantt de hitos para donantes | Perfecto para la capa adaptativa (tablero + mantención). |
| **Trello / Asana** | Kanban simple, equipo chico | Poca ruta crítica, poca línea base | Útil si el equipo es de 4 y no quieren Jira todavía. |
| **Pizarra / kraft** | Pitch de 15 min, entendimiento común | No es el plan oficial | **Obligatorio** en Eva 1, aunque el plan viva en Project. |

### 6.3 Cómo justificar (plantilla de párrafo para el informe)

> Elegimos **Project Libre** para la línea base predictiva (EDT, precedencias, ruta crítica, recursos y costos del piloto) porque el equipo no cuenta con licencia de MS Project y el patrocinador exige ver hitos de subsidio. Complementamos con **tablero Kanban** (Trello/Jira) para la capa adaptativa del tablero y los tickets, porque el flujo de mantención se va a descubrir en terreno. Office 365 queda para el diccionario de la EDT y el presupuesto. El kraft se usa solo para el pitch, no como fuente de verdad.

Eso cubre IL1.4 + pregunta 6 del banco oral.

### 6.4 Síntesis exigida 1.4

> La herramienta óptima es la que la **organización puede usar de verdad** y que cubre el enfoque elegido. En híbrido suele haber **dos** herramientas (línea base + flujo ágil), más el análogo para comunicar. Justificar es decir **contexto + restricción + para qué sirve cada una**, no “es la más popular”.

---

## 7. El plan preliminar como sistema (cómo se conectan las cuatro piezas)

```
                    NECESIDAD DE NEGOCIO / CASO DE NEGOCIO
                                    │
                                    ▼
                         ACTA DE CONSTITUCIÓN
                     (autoriza, nombra, techo de plata)
                                    │
                                    ▼
                      ENUNCIADO DE ALCANCE + EDT
                   (qué / qué no / paquetes de trabajo)
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
              CRONOGRAMA        RECURSOS         COSTOS
              (red, CPM,        (RBS, tipo       (tipos,
               PERT, Gantt)      y cantidad)      presupuesto)
                    │               │               │
                    └───────────────┼───────────────┘
                                    ▼
                      EEF + ESTÁNDARES + ENFOQUE
                 (clima, PMBOK/CMMI/ITIL, receta/GPS)
                                    ▼
                         HERRAMIENTAS ELEGIDAS
                                    ▼
                     PLAN PRELIMINAR DEFENDIBLE
```

Si una pieza falta, la rúbrica lo ve:

- sin exclusiones → alcance flojo  
- sin EDT → cronograma inventado  
- sin ruta crítica → “el plazo se nos ocurrió”  
- sin EEF → plan de laboratorio, no de industria  
- sin enfoque → herramientas huérfanas  
- sin justificación de herramienta → IL1.4 en 0 o 30

---

## 8. Caso 7 · de principio a fin (síntesis aplicada)

**Nombre:** Provisión de energía sostenible en comunidades desfavorecidas.  
**Equipo:** Giannina Guerrero (directora y frontend), Nicolás Barra (backend), Ari Araya (infraestructura y nube), Skarlett Tropan (calidad e impacto).  
**Contexto:** región desfavorecida de India, sin energía confiable; alto potencial solar; infraestructura débil.

**Problemas de negocio (no son el software):** falta de acceso a energía, desarrollo económico limitado, dependencia de fósiles.

**Solución de software (esto sí es el proyecto GPY1102):** **Kiran**, plataforma para registrar kits de una comunidad piloto, monitorear estado y rendimiento, gestionar mantención y generar reportes para la dirección e inversores. Promesa: *visibilidad que mantiene la energía activa*.

**Funcionalidades pedidas:**

1. Inventario (comunidades, hogares, kits; estados activo / falla / baja).  
2. Tablero operativo (visión general e individual).  
3. Monitoreo y mantención (rendimiento + tickets + soporte local).  
4. Impacto social y ambiental (informes periódicos a inversores y donantes).

### 8.1 Alcance propuesto (borrador de enunciado)

- **Producto:** **Kiran**, sistema web (con posible apoyo móvil o carga offline) de operación de kits solares del piloto.
- **Criterios de aceptación (ejemplos):** cada kit tiene dueño (hogar) y estado; un ticket se abre desde un kit en falla; un reporte mensual exportable llega a patrocinadores.
- **Entregables:** módulos 1–4, capacitación corta al soporte local, documento de roles y privacidad, plan preliminar (esta Eva).
- **Exclusiones:** fabricación e instalación de paneles, microfinanzas, expansión a otras regiones, app ciudadana masiva.
- **Restricciones:** presupuesto de piloto, conectividad, equipo de cuatro personas, fecha del primer reporte a donantes.
- **Supuestos:** hay comunidad piloto identificada; hay al menos un técnico local; los inversores aceptan indicadores simples en esta fase.

### 8.2 EDT de primer nivel (ejemplo)

```
0. Kiran — piloto de operación de kits solares
├── 1. Dirección del proyecto (acta, interesados, riesgos, reportes)
├── 2. Inventario de kits y hogares
├── 3. Tablero operativo
├── 4. Monitoreo, tickets y mantención
├── 5. Impacto y reportes a patrocinadores
├── 6. Privacidad, accesos y despliegue
└── 7. Capacitación y transición al soporte local
```

Los paquetes de trabajo viven debajo (p. ej. `2.1 Modelo de datos`, `2.2 Carga inicial`, `2.3 Estados del kit`).

### 8.3 Esbozo de ruta crítica (lógica, no números finales)

Camino largo probable:

**datos maestros (inventario) → tablero que lee esos datos → tickets sobre kits reales → reporte de impacto que usa operación real.**

Si el inventario se atrasa, todo lo demás es demo vacía. Eso es tu B–D–E–G del PPT, traducido.

### 8.4 Estrategia híbrida (ya argumentada en 5.4)

Predictivo en 2, 6 y 5 (datos, cumplimiento, reportes). Adaptativo en 3 y 4 (tablero y tickets). Dirección del proyecto (1) usa PMBOK para integrar.

### 8.5 Valor e interesados (lenguaje Eva 1)

Valor = kits observables + fallas atendibles + reportes creíbles.  
No valor = “pantallas bonitas” si el técnico no las usa o el donante no entiende el indicador.

---

## 9. Eva Parcial 1 — cómo se traduce la unidad a nota

**Nombre:** Planificando un proyecto de software  
**Cuándo:** semana 5 (el caso se elige en semana 4)  
**Tiempo:** 5 horas · Sala de Proyectos  
**Equipos:** sugeridos de 3 (el grupo actual tiene 4: hay que **repartir voz** para que nadie se esconda)  
**Ponderación del instrumento:** 30% del bloque de parciales (≈ 18% de la nota final)

### 9.1 Dos dimensiones

| Dimensión | Peso dentro de la Eva 1 | Carácter |
|---|---|---|
| Informe grupal (resumen ejecutivo) | **30%** | Grupal |
| Presentación-defensa oral | **70%** | **Individual** (preguntas a cada integrante sobre **todas** las temáticas) |

Formato informe: PDF, Arial o Times 12, interlineado 1.5, márgenes 2.5 cm, **máximo 7 planas**, citas **APA**. Apoyo del pitch: **analógico**.

### 9.2 Qué debe contener el informe (los 4 IL)

1. Alcance, recursos, cronograma; contexto y necesidades; plan inicial con herramientas de industria.  
2. Factores ambientales y estándares; impacto en el caso; cómo el contexto organizacional influye.  
3. Estrategias de planificación e integración **contextualizadas**.  
4. Herramientas usadas en cada sección, **justificadas**.

### 9.3 Niveles de logro

| Nivel | % | Qué significa |
|---|---|---|
| Muy buen desempeño | 100 | Precisión y detalle técnico en todos los aspectos |
| Buen desempeño | 80 | Claro, con omisiones o errores menores |
| Aceptable | 60 | Básico; omisiones notables |
| Incipiente | 30 | Errores graves; **no competente** |
| No logrado | 0 | Ausente o incorrecto |

### 9.4 Banco de preguntas del pitch (preparar las 6)

1. ¿Cuál es el contexto y las necesidades de la organización?  
2. ¿Cómo se determinaron alcance y recursos?  
3. ¿Con qué criterio técnico se definió el cronograma?  
4. ¿Qué beneficios dan las estrategias de planificación e integración?  
5. ¿Qué elementos del contexto organizacional se incorporaron?  
6. ¿Qué herramientas se usaron y por qué se eligieron?

### 9.5 Lo que el oral mira (aprox. 25% + 25% + 20% = 70%)

- dominio de los componentes del plan **y** del contexto de la organización  
- **aporte personal** a las estrategias (no “lo hizo el grupo”)  
- justificación de herramientas según necesidades de la org  
- el visual **refuerza**; no es un dibujo que no se usa

---

## 10. Glosario de la Unidad 1 (para hablar con las palabras del ramo)

| Término | En una frase |
|---|---|
| Proyecto | Esfuerzo temporal que entrega un resultado único |
| Acta de constitución | Documento que autoriza el proyecto y nombra al director/a |
| Enunciado del alcance | Descripción detallada de qué entra, qué no, criterios y supuestos |
| Entregable | Resultado verificable del trabajo |
| Exclusión | Trabajo que **explícitamente** no se hará |
| Supuesto | Hecho que se da por cierto; si falla, hay riesgo |
| Restricción | Límite obligatorio (plata, plazo, tecnología, ley) |
| EDT / WBS | Árbol del 100% del trabajo |
| Diccionario de la EDT | Ficha de cada paquete (criterio, recursos, costo, hitos) |
| Paquete de trabajo | Nivel más bajo de la EDT, estimable |
| Cuenta de control | Punto donde se miden alcance, plazo y costo juntos |
| Hito | Punto de control con duración cero (evento) |
| Diagrama de red | Dibujo de dependencias entre actividades |
| Gantt | Barras de tiempo para el equipo |
| CPM | Método de la ruta crítica (camino más largo) |
| Holgura | Días que una actividad puede atrasarse sin mover el fin |
| PERT | Estimación (O + 4M + P) / 6 |
| EEF | Factor ambiental que el equipo **no** controla |
| OPA | Activos de proceso de la organización (plantillas, lecciones) |
| PMBOK | Guía de dirección de proyectos (biblio: 6ª) |
| CMMI | Modelo de madurez de procesos |
| ITIL | Buenas prácticas de **servicio** (operación, incidentes, cambios) |
| COBIT | Gobierno y control de TI |
| Predictivo | Receta: plan detallado al inicio |
| Adaptativo | GPS: iterar y ajustar |
| Híbrido | Mix según el terreno |
| Interesado | Quien afecta o se siente afectado |
| Valor | Beneficio real (no solo el entregable) |
| Tailoring (idea) | No usar 40 procesos si el piloto no los necesita; **adaptar** |

---

## 11. Banco corto de respuestas orales (ensayo, no para leer)

Úsalo para practicar **en voz alta**. Cambia los números cuando el equipo tenga Gantt real.

**1. Contexto y necesidades.**  
“Es una empresa social que quiere un piloto de kits solares en una comunidad de India sin energía confiable. El software no instala paneles: opera inventario, tablero, mantención y reportes de impacto para inversores y donantes.”

**2. Alcance y recursos.**  
“El alcance se descompuso en EDT: inventario, tablero, tickets, impacto, privacidad y capacitación. Excluimos fabricación e instalación. Recursos: equipo de desarrollo chico, soporte local, nube y reserva de contingencia. Cada paquete del diccionario tiene responsable y criterio de aceptación.”

**3. Criterio del cronograma.**  
“De la EDT salieron actividades y precedencias. El inventario alimenta el tablero, los tickets y el reporte; ese es el camino más largo, o sea la ruta crítica. Usamos lógica CPM; donde había incertidumbre (terreno), PERT. A gerencia le mostramos hitos; al equipo, Gantt.”

**4. Beneficios de la estrategia.**  
“Híbrido: congelamos datos maestros, privacidad y calendario de donantes (predictivo) para no fallar cumplimiento. Iteramos tablero y tickets (adaptativo) porque el técnico local nos va a corregir el flujo. Así integramos el proyecto a una organización que debe ser ágil en terreno y estricta con plata ajena.”

**5. Contexto organizacional incorporado.**  
“Financiamiento mixto → hitos de reporte. Distancia geográfica y cultura comunitaria → supuestos de conectividad y UX simple. Gobernanza de inversores → interesados y canales de comunicación en el plan, no al final.”

**6. Herramientas.**  
“Project Libre (o MS Project) para línea base y ruta crítica, porque hay que defender plazo de piloto. Kanban para el trabajo semanal adaptativo. Office para diccionario y costos. Kraft solo para explicar en 15 minutos. Elegimos según licencia, tamaño del equipo y doble audiencia: donantes y desarrolladores.”

---

## 12. Autoevaluación (sin apuntes)

Si una respuesta no sale en 60 segundos, vuelve al bloque.

1. Nombra los 6 mínimos del enunciado de alcance.  
2. Diferencia paquete de trabajo, paquete de planificación y cuenta de control.  
3. ¿Qué cubre el diccionario de la EDT que el árbol no cubre?  
4. En el ejemplo de clase, ¿cuál es la ruta crítica y cuánto dura el proyecto?  
5. Calcula PERT con O=4, M=7, P=16.  
6. Fórmulas de EF, LS y holgura según la lámina.  
7. Seis tipos de costo, con un ejemplo cada uno.  
8. EEF interno vs externo: tres de cada lado.  
9. EEF vs OPA, en una frase.  
10. PMBOK vs CMMI vs ITIL: una frase cada uno.  
11. Un dato de la tabla: ¿ITIL se enfoca en proyectos? ¿PMBOK en operación de servicio?  
12. Tres aportes de ISO/IEC 27701.  
13. Predictivo vs adaptativo: una ventaja y una desventaja cada uno.  
14. Propón el híbrido del Caso 7 en dos capas.  
15. ¿Qué documento autoriza el proyecto?  
16. Output vs outcome vs valor, con el Caso 7.  
17. Nombra 5 tipos de interesado del Caso 7.  
18. ¿Por qué el oral vale 70% y qué pasa si solo “estudiaste tu parte”?  
19. Justifica una herramienta para **esta** organización, no en abstracto.  
20. ¿Qué queda **fuera** del Caso 7 y por qué hay que escribirlo?

### Clave breve

1. Producto, criterios de aceptación, entregables, exclusiones, restricciones, supuestos.  
2. Trabajo más bajo estimable / trabajo conocido sin actividades detalladas / punto de medición integrada.  
3. Criterios, supuestos, recursos, duración, hitos, costo, responsable, firma.  
4. B–D–E–G, 26.  
5. 8 días; desviación 2.  
6. EF=(ES+Dur)−1; LS=(LF−Dur)+1; holgura=LF−EF.  
7. Variable, fijo, directo, indirecto, oportunidad, hundido.  
8. Interno: cultura, estructura, infraestructura, software, disponibilidad, capacidad. Externo: mercado, social, legal, estándares, financiero, físico, etc.  
9. EEF no controlas; OPA sí usas (plantillas, lecciones).  
10. Dirigir el proyecto / madurar procesos / operar el servicio.  
11. ITIL: NA en foco a proyectos. PMBOK: no es fuerte en operación de servicio.  
12. Confianza, apoyo a leyes de privacidad, integración con seguridad, transparencia, flexibilidad jurisdiccional.  
13. Predictivo: control vs rigidez. Adaptativo: flexibilidad vs desvío.  
14. Inventario/cumplimiento predictivo; tablero/tickets adaptativo.  
15. Acta de constitución.  
16. Plataforma / kits atendibles / energía e informes creíbles.  
17. Inversores, subsidio, comunidad, soporte local, equipo, dirección, partner tech.  
18. Porque la rúbrica evalúa dominio individual de **toda** la unidad.  
19. Licencia + audiencia (donantes vs devs) + enfoque híbrido.  
20. Fabricar e instalar paneles: si no se excluye, el alcance se hincha.

---

## 13. Referencias (las de las clases + programa)

1. Project Management Institute. (2017). *Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK)* (6.ª ed.).  
2. Wysocki, R. K. (2019). *Effective project management: Traditional, agile, extreme, hybrid* (8th ed.). Wiley.  
3. Layton, M. C. (2022). *Scrum for dummies* (3rd ed.). Wiley.  
4. Peters, L. J. (2024). *Software project management: Methods and techniques*. CRC Press.  
5. SCRUMstudy. (2023). *Guía SBOK* (4.ª ed., español).  
6. Baud, J.-L. (2020). *ITIL 4: Entender el enfoque y adoptar las buenas prácticas*. ENI.  
7. PMI. (2021). *Guía del PMBOK* (7.ª ed.) — solo el extracto de valor e interesados usado en Eva 1.

---

## 14. Cierre: la frase que tiene que quedarte

Planificar un proyecto de software en este ramo es **dibujar un plano que la organización pueda usar**: autorizado (acta), limitado (alcance y exclusiones), partido (EDT), fechado (ruta crítica), costoso de verdad (tipos de costo + contingencia), honesto con el clima (EEF y estándares), con una forma de caminar (predictivo, adaptativo o híbrido) y con un lápiz justificado (la herramienta). El Caso 7 es ese plano, no un cuento de paneles solares. Y la Eva 1 se gana en la pizarra, con voz propia.
