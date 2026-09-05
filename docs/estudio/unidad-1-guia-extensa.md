# GPY1102 — Gestión de Proyectos de Software

# Unidad 1 · Guía extensa de estudio

**Asignatura:** Gestión de Proyectos de Software  
**Sigla:** GPY1102 · **Créditos:** 10 Duoc / 4 SCT · **Línea:** FOL · **Formato:** presencial, Sala de Proyectos  
**Prerrequisito:** GPY1101  
**Experiencia de aprendizaje:** *Planificación de Proyectos de Software* (RA1)  
**Material cubierto:** 1.1.1 + 1.1.2 · 1.2.1 + 1.2.2 · 1.3.1 + 1.3.2 · IL1.4 (herramientas; no hay PPT en carpeta) · Eva Parcial 1  
**Fuentes:** Programa de Asignatura, presentaciones de clase, actividades, rúbrica Eva 1, Caso 7, bibliografía oficial (PMBOK 6.ª 2017, SBOK 4.ª 2023, ITIL 4)  
**Fuera de alcance:** Unidad 2 (monitoreo y control) y Unidad 3 (cierre), salvo cuando se necesita el hilo del semestre.

Las definiciones están **parafraseadas para estudio**. En informe y oral, el lenguaje de referencia es **PMBOK 6.ª**. La 7.ª solo se usa cuando el material de Eva 1 pregunta por **valor** e **interesados**. La 8.ª no es bibliografía del ramo.

---

## Índice

- 0. Cómo aprobar esta unidad
- 1. Mapa de la Unidad 1
- 2. Cimientos y léxico
- 3. Bloque 1.1 — Plan preliminar (IL1.1)
- 4. Bloque 1.2 — Factores ambientales y estándares (IL1.2)
- 5. Bloque 1.3 — Estrategias de planificación (IL1.3)
- 6. Bloque 1.4 — Selección de herramientas (IL1.4)
- 7. El plan preliminar como sistema
- 8. Caso 7 aplicado (Kiran)
- 9. Eva Parcial 1
- 10. Glosario
- 11. Banco de respuestas orales
- 12. Autoevaluación
- 13. Referencias

---

## 0. Cómo aprobar esta unidad

Quien aprueba la Unidad 1 no recita listas: **planifica un proyecto de software y lo defiende** con el vocabulario del ramo. Debe poder:

1. **Definir** el proyecto con enunciado de alcance, exclusiones, supuestos y restricciones.
2. **Descomponer** el trabajo en EDT, estimar duraciones y determinar la ruta crítica.
3. **Clasificar** costos y recursos, y armar un presupuesto inicial con contingencia.
4. **Analizar** factores ambientales internos y externos, y estándares (PMBOK, CMMI, COBIT, ITIL), **sobre el caso**.
5. **Elegir** un enfoque (predictivo, adaptativo o híbrido) y **justificarlo** con el contexto organizacional.
6. **Usar** una herramienta de industria (MS Project, Project Libre u Office 365) y explicar **por qué esa**.
7. **Defender oralmente** todo lo anterior, de forma individual, sin leer el informe.

### Resultado de aprendizaje (RA1)

> Planifica un proyecto de software, considerando requerimientos y procesos del cliente, factores ambientales y estándares de la industria, para gestionarlo e integrarlo de manera eficiente en la organización.

### Indicadores de logro

| IL | Horas | Qué hay que demostrar |
|---|---|---|
| **IL1.1** | 4 | Define alcance, recursos, cronograma y costos en un **plan preliminar**, con herramientas de la industria. |
| **IL1.2** | 4 | Analiza factores ambientales y estándares, **evaluando su impacto en un caso real**. |
| **IL1.3** | 6 | Define estrategias de planificación (predictivo / adaptativo / híbrido) mediante **planes contextualizados**. |
| **IL1.4** | 6 | Utiliza herramientas de planificación y **selecciona las más adecuadas** según el estándar y la organización. |

### Cómo estudiar esta guía

1. Leer cada bloque: **definición → matices → ejemplo del Caso 7 → nombre técnico**.
2. Reproducir en voz alta la **síntesis exigida** al final de cada parte.
3. Cerrar con la autoevaluación de la sección 12, **sin apuntes**.
4. Ensayar las seis preguntas del pitch (secciones 9 y 11) como defensa individual.

El Caso 7 (plataforma de operación de kits solares; producto **Kiran**) es el hilo de **toda** la guía. El semestre trabaja **un solo caso** desde la semana 4 hasta el ET.

---

## 1. Mapa de la Unidad 1

```
                         RA1 · PLANIFICAR EL PROYECTO
                    (para gestionarlo e integrarlo después)
                                      │
     ┌──────────────┬─────────────────┼─────────────────┬──────────────┐
     ▼              ▼                 ▼                 ▼              ▼
   IL1.1          IL1.2             IL1.3             IL1.4          Eva 1
   Plan           EEF y             Enfoque           Herramienta    Informe 30%
   preliminar     estándares        predictivo /      y justificación + oral 70%
                  (impacto)         adaptativo /
                                    híbrido
```

**Competencia del programa (C4):** evaluar y gestionar proyectos en todo el ciclo de vida, con buenas prácticas y herramientas, en contextos **tradicionales y ágiles**. La Unidad 1 cubre solo el arranque: planificar. Monitoreo y cierre se hacen después, **sobre el mismo caso**.

### Hilo del semestre

| Momento | Entrega | Peso en el bloque de parciales | Impacto aprox. en nota final |
|---|---|---|---|
| Parcial 1 · Planificar | Informe ejecutivo + pitch analógico | 30% de 60% | ≈ 18% |
| Parcial 2 · Monitorear | Reporte + video 5–7 min | 35% de 60% | ≈ 21% |
| Parcial 3 · Cerrar | 3 láminas + reunión de cierre | 35% de 60% | ≈ 21% |
| ET | Defensa 15 min con PPT/Canva | 40% directo | 40% |

Los quizzes formativos (Eva For 1, 2 y 3) **no ponderan**.

### Bibliografía: no mezclar ediciones

| Fuente | Edición | Rol en el ramo |
|---|---|---|
| Guía del PMBOK | **6.ª, 2017** | Bibliografía obligatoria. Lenguaje de los PPT 1.1, 1.2 y 1.3 (EDT, EEF, CPM, grupos de procesos). |
| Guía SBOK | 4.ª, 2023 | Bibliografía obligatoria. Nutre el enfoque **adaptativo** (Scrum). |
| ITIL 4 (Baud) | 2020 | Bibliografía obligatoria. Comparativa de estándares en 1.2. |
| PMBOK | 7.ª, 2021 | Extracto local de Eva 1 (interesados y valor). Útil en el pitch. Etiquetar la edición. |
| PMBOK | 8.ª, 2025/26 | Apunte de apoyo en `docs/estudio/`. **No** es biblio oficial. No citarla en el informe. |

En prueba y rúbrica: hablar **PMBOK 6**. Usar la 7.ª solo si preguntan por **valor** e **interesados**.

---

## 2. Cimientos y léxico

La clase 1.1 arranca en el alcance, pero el acta (actividad 1.1.2, paso 1) y el material de valor de Eva 1 exigen estos cimientos.

### 2.1 Distinciones que hay que poder decir

| Término A | Término B | Diferencia |
|---|---|---|
| Proyecto | Operaciones | Temporal y único frente a continuo y repetitivo |
| Output | Outcome | Lo producido frente al efecto que genera |
| Alcance del producto | Alcance del proyecto | Características del resultado frente al trabajo para entregarlo |
| Acta (charter) | Plan de dirección | Autoriza y da autoridad frente a describe *cómo* se hará |
| Exclusión | Restricción | Lo que **no se hará** frente a un **límite** de lo que sí se hace |
| Supuesto | Riesgo | Se da por verdadero frente a evento incierto; un supuesto que falla **es** un riesgo |
| EEF | OPA | Condiciones que no se controlan frente a activos internos que sí se usan |
| Paquete de trabajo | Cuenta de control | Nivel más bajo estimable frente a punto de medición integrada |
| CPM | PERT | Duraciones deterministas y camino más largo frente a tres puntos y incertidumbre |
| Costo hundido | Costo futuro | Ya gastado (no debe decidir) frente a lo que aún se puede elegir |
| Predictivo | Adaptativo | Plan detallado al inicio frente a iteración y ajuste |
| PMBOK | CMMI | Dirige **el proyecto** frente a madura **los procesos de la organización** |
| ITIL | COBIT | Opera **el servicio** frente a gobierna **TI** |

### 2.2 Proyecto y dirección de proyectos

**Definición. Proyecto.** Esfuerzo **temporal** (inicio y fin definidos) para crear un **producto, servicio o resultado único**. «Temporal» no significa breve: significa que termina. «Único» no significa inédito en la historia: significa que *este* resultado, para *este* piloto, no existía.

**Definición. Dirección de proyectos.** Aplicación de conocimientos, habilidades, herramientas y técnicas a las actividades del proyecto para cumplir los requisitos.

**Definición. Operaciones.** Trabajo continuo y repetitivo que mantiene el negocio. Al cierre, el proyecto transfiere su resultado a operaciones.

| | Proyecto | Operaciones |
|---|---|---|
| Tiempo | Inicio y fin | Continuo |
| Resultado | Único | Repetitivo |
| Propósito | **Cambiar** el estado de la organización | **Mantener** el negocio |
| Ejemplo Caso 7 | Construir Kiran para el piloto | Atender tickets cuando ya esté en producción |

**Definición. Triple restricción (triángulo de hierro).** Relación entre **alcance, tiempo y costo** (con calidad como criterio transversal). Un cambio en uno suele mover a los otros. En Eva 1 todavía no se controla el triángulo (eso es Unidad 2); sí se **declara** en el plan preliminar.

### 2.3 Entregable, output, outcome y valor

**Definición. Entregable (*deliverable*).** Producto, resultado o capacidad **verificable** producido para completar un proceso, una fase o el proyecto.

**Definición. Output.** Lo que el proyecto produce de forma observable (la plataforma, un informe, una capacitación).

**Definición. Outcome.** Efecto que el output genera (las fallas se ven a tiempo; el soporte prioriza tickets reales).

**Definición. Valor.** Importancia de los beneficios —tangibles o intangibles— respecto del costo, el tiempo y el riesgo. Puede realizarse durante el proyecto, al cierre o **después**, en operaciones.

El extracto de Eva 1 (PMBOK 7.ª, principio «enfocarse en el valor») insiste: si el software se entrega y **no mejora** lo prometido, los interesados pueden juzgar el proyecto como fracaso aunque el código «funcione». En el Caso 7 el valor no es «hay un tablero»: es que un kit dado de baja no siga contando como activo, que el soporte local atienda fallas reales y que un inversor reciba un informe usable.

**Definición. Caso de negocio (*business case*).** Justificación de la inversión: necesidad u oportunidad, opciones, costos, beneficios esperados y recomendación. Los proyectos suelen nacer de una **necesidad de negocio** + **justificación** + **estrategia**.

### 2.4 Interesados (*stakeholders*)

**Definición. Interesado.** Persona, grupo u organización que **afecta**, **es afectada** o **se percibe afectada** por una decisión, actividad o resultado del proyecto. La influencia puede ser positiva o negativa. No son estáticos: entran, salen y cambian de interés.

Según el material de Eva 1, los interesados pueden influir en alcance, cronograma, costo, equipo, planes, resultados, cultura, beneficios, umbrales de riesgo, calidad y criterio de éxito.

Habilidades asociadas: iniciativa, integridad, honestidad, colaboración, respeto, empatía, confianza y comunicación **bidireccional** frecuente.

**Interesados mínimos del Caso 7**

- Patrocinadores: inversores de impacto, agencia de subsidios, empresas tecnológicas asociadas.
- Beneficiarios: comunidades y hogares (no necesariamente usuarios del software en esta fase).
- Operación: técnicos de soporte local.
- Equipo del proyecto: desarrollo, diseño, datos, QA, responsable de impacto.
- Dirección de la empresa social; autoridades locales y donantes si aplica; PMO si existe.

### 2.5 Gobernanza

**Definición. Gobernanza organizacional.** Marco de autoridad, políticas y cumplimiento de **toda** la empresa (quién aprueba, con qué reglas).

**Definición. Gobernanza del proyecto.** Marco específico de **este** proyecto: quién decide qué, con qué límite de autoridad y cómo se escala un problema.

El RA1 pide planes **integrables** en la organización (IL1.3): no un plan aislado.

### 2.6 Acta de constitución (*Project Charter*)

**Definición.** Documento emitido por el sponsor o la gobernanza que **autoriza formalmente** el proyecto, nombra al director o directora y le otorga autoridad para aplicar recursos organizacionales.

**No es** el plan detallado. El plan nace **después**, usando el acta como techo.

Mínimo que debe quedar claro (PMBOK 6 y paso 1 de la actividad 1.1.2):

- propósito y justificación
- objetivos medibles de alto nivel
- requisitos de alto nivel
- riesgos de alto nivel
- cronograma resumido de hitos
- presupuesto resumido
- interesados principales
- criterios de aprobación
- director o directora y nivel de autoridad
- patrocinador que firma

---

## 3. Bloque 1.1 — Elaboración del plan preliminar (IL1.1)

**Material:** PPT 1.1.1 · Actividad 1.1.2 (duplas, 2 h)  
**Objetivo:** planificar desde cero alcance, cronograma, costos y recursos.

El plan preliminar **es** esas cuatro piezas más el acta. No es un informe de 40 páginas: es el primer mapa **defendible**.

### 3.1 Alcance del proyecto

**Definición. Alcance del producto.** Características y funciones del resultado.

**Definición. Alcance del proyecto.** Trabajo necesario para entregar ese producto con las características acordadas, **incluido el trabajo de gestión**.

**Definición. Enunciado del alcance.** Descripción detallada del proyecto y del producto que permite un **entendimiento común** y deja las **exclusiones explícitas**. El proceso suele ser **iterativo**.

**Definición. Scope creep.** Expansión no controlada del alcance sin ajuste de tiempo, costo o recursos y sin control de cambios.

#### Mínimo del enunciado (lámina de clase)

| Elemento | Definición / pregunta | Ejemplo Caso 7 |
|---|---|---|
| Descripción del alcance del producto | ¿Qué se construye? | Plataforma para registrar kits, tablero, tickets de mantención e informes de impacto de un piloto. |
| Criterios de aceptación | Condiciones para dar por bueno un entregable | Un kit se puede crear, cambiar de estado (activo / en falla / dado de baja) y verse en el tablero el mismo día. |
| Entregables | Resultados verificables | Módulo inventario, tablero, módulo tickets, reporte periódico, capacitación al soporte local. |
| Exclusiones | Trabajo que **explícitamente** no se hará | Fabricar paneles, instalar en techos, tendido eléctrico, expansión a otras regiones en esta fase. |
| Restricciones | Límites obligatorios | Presupuesto de piloto, conectividad irregular, fecha de reporte a donantes, equipo pequeño. |
| Supuestos | Factores dados por ciertos sin prueba plena | Hay conectividad mínima; el soporte local carga datos; los inversores aceptan reporte mensual. |

Si un supuesto falla (no hay señal), el plan debe decir **qué se hace**. Un supuesto sin plan B es un **riesgo no declarado**.

#### Plantilla del enunciado (lámina 11)

**Cabecera:** fecha, nombre del proyecto, versión, director/a, patrocinador, cliente, equipo, otros interesados.

**Cuerpo:**

- **Antecedentes:** justificación, necesidad, oportunidad.
- **Descripción del producto o servicio:** el entregable final.
- **Objetivos:** qué se logra **con** ese entregable (outcome, no solo output).

#### Herramientas y técnicas para definir alcance

1. **Analizar objetivos del producto y convertirlos en requisitos.**  
   **Definición. Requisito.** Condición o capacidad que debe cumplirse. «Mejorar la calidad de vida» no es requisito. «Registrar cada kit con estado operativo» sí lo es.

2. **Generación de alternativas.**  
   ¿Aplicación móvil para el técnico o solo web? ¿Tickets por un canal externo o módulo interno?

3. **Técnica Delphi.**  
   **Definición.** Método de consenso entre expertos **en anónimo**: un facilitador envía un cuestionario, resume respuestas y las devuelve para otra ronda. Reduce el sesgo de autoridad. Útil cuando terreno, software e impacto social no coinciden en la primera reunión.

### 3.2 EDT / WBS

**Definición. EDT (Estructura de Desglose del Trabajo) o WBS (*Work Breakdown Structure*).** Descomposición jerárquica de **todo** el trabajo del proyecto. Regla del PMBOK 6: la EDT cubre el **100%** del alcance acordado. Lo que no está en la EDT **no se hace** (o entra como cambio).

#### Diagrama de descomposición (lámina 7)

```
Identificar entregables
        │
        ▼
 ¿Se puede estimar tiempo y costo?
        │
   NO ──► Subdividir ──► (volver a preguntar)
        │
   SÍ ──► Identificar cada paquete de trabajo ──► Verificar
```

Se subdivide hasta el nivel en que **sí** se puede estimar.

#### Niveles que pide la clase (lámina 9)

| Nombre | Definición | Para qué |
|---|---|---|
| **Cuenta de control (*control account*)** | Punto de gestión donde se integran alcance, plazo y presupuesto | Medir desempeño (Unidad 2) |
| **Paquete de planificación (*planning package*)** | Debajo de la cuenta de control: se conoce el trabajo, **aún no** las actividades detalladas | No fingir detalle inexistente |
| **Paquete de trabajo (*work package*)** | Nivel más bajo de la EDT | Aquí hay duración, costo y responsable |

Numeración típica: `2.2.3` cuenta de control → `2.2.3.1` paquete de planificación → `2.2.3.2.1` paquete de trabajo.

**Definición. Descomposición.** Técnica de dividir entregables y trabajo del proyecto en componentes más pequeños y manejables.

**Definición. Elaboración progresiva.** Detallar el plan a medida que aumenta la información. No es improvisación.

#### Diccionario de la EDT (lámina 10)

**Definición.** Documento que detalla cada componente de la EDT: descripción, responsable, criterios de aceptación, supuestos, recursos, duración, hitos y costo. La EDT sola es un árbol; el diccionario es la ficha que permite estimar.

Ejemplo de la clase (componente `2.2.2.1 Mercado`):

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

**Traducción al Caso 7** (paquete `1.2.1 Tablero operativo`):

- Criterio de aceptación: se ve el estado de cada kit y el recuento de tickets abiertos/cerrados en una sola pantalla.
- Entregable: vista de tablero usable en navegador por el soporte local.
- Supuesto: hay datos de inventario cargados.
- Recursos: 1 front, 1 back, 1 QA.
- Hito: demostración al patrocinador.

Sin diccionario, la EDT no se puede estimar ni asignar.

### 3.3 Cronograma

**Definición. Desarrollar el cronograma.** Integrar actividades, secuencias, recursos y duraciones para crear el **modelo de programación**: fechas de inicio y fin planificadas, e **hitos**. Es **iterativo**.

**Definición. Hito (*milestone*).** Punto o evento significativo. Duración cero.

**Definición. Actividad.** Porción de trabajo programable, por lo general derivada de un paquete de trabajo.

#### Los dos pases que pide la clase

1. **Primera vez:** sin retrasos, sin adelantos, sin dependencias finas, **recursos ilimitados**. Muestra la duración «en bruto».
2. **Segunda vez:** con retrasos, adelantos, dependencias y **recursos limitados**. Esta es la agenda defendible.

**Definición. Adelanto (*lead*).** Solapamiento permitido: la sucesora empieza antes de que termine la predecesora.  
**Definición. Retraso (*lag*).** Espera impuesta entre actividades.

#### Insumos típicos (lámina 18)

Lista de actividades, EDT, diagrama de red, calendarios de recursos, estimaciones de duración, enunciado del alcance y **OPA** (plantillas, lecciones, calendarios de la empresa).

#### Tres representaciones, tres audiencias (lámina 24)

| Formato | Definición | Audiencia |
|---|---|---|
| **Cronograma de hitos** | Pocos eventos de control | Dirección / patrocinadores |
| **Diagrama de Gantt** | Barras de tiempo: tareas, duraciones, solapes, responsables | Equipo y director/a |
| **Diagrama de red** | Nodos y dependencias; permite ver caminos y ruta crítica | Planificación técnica |

Un Gantt de 80 barras no sirve para un inversor. Cuatro hitos no le dicen al equipo qué hacer el martes.

#### CPM — Método de la ruta crítica

**Definición. CPM (*Critical Path Method*).** Técnica que estima la duración **mínima** del proyecto calculando inicios y fines **tempranos y tardíos**, **sin** limitar recursos en el cálculo clásico.

**Definición. Ruta crítica.** Secuencia de actividades que forma el **camino más largo**. Cualquier atraso en ella mueve la fecha final, salvo que se comprima el cronograma.

**Definición. Holgura (*float* / *slack*).** Tiempo que una actividad puede atrasarse sin afectar la fecha de término del proyecto (holgura total). Si la holgura es **0**, la actividad es crítica.

- **Forward pass (hacia adelante):** inicios y fines tempranos; duración mínima / camino crítico.
- **Backward pass (hacia atrás):** inicios y fines tardíos; holguras.

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

Fórmulas de la clase (convención de días calendario; la duración «ocupa» días inclusive):

- **Fin temprano (EF)** = (Inicio temprano + Duración) − 1
- **Inicio tardío (LS)** = (Fin tardío − Duración) + 1
- **Holgura** = Fin tardío − Fin temprano  
  (equivalente: Inicio tardío − Inicio temprano)

#### Ejemplo resuelto de la clase (actividades A–G)

| N.º | Actividad | Predecesora | Duración |
|---|---|---|---|
| 1 | A | — | 2 |
| 2 | B | — | 5 |
| 3 | C | — | 1 |
| 4 | D | B | 10 |
| 5 | E | A, D | 3 |
| 6 | F | C | 6 |
| 7 | G | E, F | 8 |

| Ruta | Suma | ¿Crítica? |
|---|---|---|
| Inicio → A → E → G → Fin | 2 + 3 + 8 = **13** | No |
| Inicio → B → D → E → G → Fin | 5 + 10 + 3 + 8 = **26** | **Sí** |
| Inicio → C → F → G → Fin | 1 + 6 + 8 = **15** | No |

Nodos con holgura 0: **B, D, E, G**. Duración del proyecto: **26**.  
Holguras del diagrama: A = 13, C = 11, F = 11.

Si A se atrasa más allá de su holgura, **también** pasa a ser crítica.

**Para el oral:** la ruta crítica no es «la más importante por fama»; es la **más larga**. En el piloto, si se atrasa la carga de inventario, se atrasan el tablero y el reporte a donantes.

#### PERT — tres valores

**Definición. PERT (*Program Evaluation and Review Technique*).** Estimación por tres valores cuando no hay un único número fiable.

- **O** = optimista  
- **M** = más probable  
- **P** = pesimista  

Fórmulas de la clase:

- Duración esperada = **(O + 4M + P) / 6**
- Desviación estándar = **(P − O) / 6**

Ejemplo de la lámina: O = 4, M = 7, P = 16  

- Duración = (4 + 4×7 + 16) / 6 = **8 días**  
- Desviación = (16 − 4) / 6 = **2 días**

Útil en software con incertidumbre de terreno (Caso 7).

### 3.4 Costos

**Definición. Presupuesto.** Suma autorizada para ejecutar el proyecto o un componente, construida a partir de los costos identificados **por fase** o por paquete.

**Definición. Reserva de contingencia.** Monto (o tiempo) reservado para riesgos **identificados**. Sin este paso, el primer imprevisto deja el plan en cero.

#### Cómo hacer un presupuesto (8 pasos de la lámina)

1. Definir la EDT.  
2. Especificar detalles de las tareas.  
3. Introducir valores de costos.  
4. Obtener costos totales.  
5. Incluir **contingencias y costos extra**.  
6. Obtener la **aprobación**.  
7. Hacer seguimiento (mira a la Unidad 2).  
8. Sacar conclusiones.

Sin el paso 1, el presupuesto es un número sin base. Sin el paso 6, el número no existe para la organización.

#### Principales tipos de costo (evaluación frecuente)

| Tipo | Definición | Ejemplo Caso 7 |
|---|---|---|
| **Variable** | Cambia con el volumen de trabajo o de unidades | Horas extra de un consultor; más kits = más filas que cargar |
| **Fijo** | No cambia con el volumen (en el rango del piloto) | Sueldo mensual de la *product owner* |
| **Directo** | Se atribuye **a este** proyecto | Servidor del piloto; viaje para presentar el plan |
| **Indirecto** | Beneficia a varios proyectos; hay que prorratearlo | Luz, contabilidad, PMO |
| **De oportunidad** | Valor de la mejor alternativa no elegida | El mismo equipo podría haber desarrollado otro producto |
| **Hundido / enterrado** | Ya se gastó; **no debe** decidir si continuar | Estudio previo de terreno ya pagado |

**Falacia del costo hundido:** «ya gastamos tanto, hay que seguir». La decisión se toma con costos **futuros** y valor **futuro**.

### 3.5 Recursos

**Definición. Estimar los recursos de las actividades.** Identificar **tipo, cantidad y características** de los recursos necesarios para completar las actividades. Permite estimar costo y duración con más precisión.

**Definición. RBS (*Resource Breakdown Structure*).** Desglose jerárquico de **todos** los recursos (humanos y materiales), por categoría y tipo, con cantidad y **disponibilidad**.

Ejemplo de la clase (curso PMP): personas (edición, ventas, técnicos) y materiales (tecnología e instalaciones).

**Traducción Caso 7 (mínimo)**

| Categoría | Ejemplos |
|---|---|
| Personas | Front, back, QA, diseño, responsable de impacto, soporte local, *product owner* |
| Tecnología | Nube, repositorio, herramientas de tickets, dispositivos de terreno, conectividad |
| Instalaciones | Espacio de la empresa social; punto de apoyo en la comunidad |
| Financieros | Aporte de inversores, subsidio, reserva de contingencia |

### 3.6 Actividad 1.1.2 — entregables en 2 horas

Situación: ejecución práctica, duplas, Sala de Proyectos, evalúa **IL1.1**.

| Paso | Entregable | Criterio |
|---|---|---|
| 1 | Acta de constitución | Autoriza y nombra director/a |
| 2 | Alcance + EDT | Incluidos / no incluidos; fases, paquetes de trabajo |
| 3 | Cronograma | Hitos, duraciones, asignación de recursos |
| 4 | Recursos | Humanos, técnicos, financieros |
| 5 | Presentar | Plantillas en Word + **análogo** (pizarra, kraft) |

### 3.7 Síntesis exigida 1.1

> Un plan preliminar no es un cronograma suelto. Es **acta** (autorización) + **enunciado de alcance** (qué / qué no, criterios, exclusiones, supuestos, restricciones) + **EDT con diccionario** (el 100% del trabajo) + **modelo de programación** (red, CPM/PERT, Gantt, hitos) + **recursos y costos clasificados**, con contingencia y aprobación. La ruta crítica es el camino más largo; PERT pondera incertidumbre; los costos hundidos no deciden el futuro.

Preguntas de reflexión de la clase (ensayo):

1. ¿Qué elementos son más importantes al planificar un proyecto de software?  
2. ¿Cómo asegurar precisión en la estimación de recursos?  
3. ¿Qué desafíos aparecen al crear el cronograma y cómo resolverlos?  
4. ¿Qué tan claro quedó el alcance?  
5. ¿Se identificaron todos los recursos?  
6. ¿El cronograma es realista?  
7. ¿Se consideraron los costos más relevantes?

---

## 4. Bloque 1.2 — Factores ambientales, normas y estándares (IL1.2)

**Material:** PPT 1.2.1 · Actividad 1.2.2 (equipos, 2 h)

### 4.1 Definición de EEF y OPA (PMBOK 6)

**Definición. Factores ambientales de la empresa (EEF, *Enterprise Environmental Factors*).** Condiciones que **el equipo no controla** y que influyen, restringen o dirigen el proyecto. Pueden ser **internos o externos**. Son **entrada** de muchos procesos, sobre todo de planificación. Pueden ampliar o recortar opciones.

No equivalen al «clima laboral» en sentido coloquial: son el sistema completo en el que el proyecto opera.

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

**Definición. OPA (*Organizational Process Assets*).** Planes, procesos, políticas, procedimientos y bases de conocimiento de la organización ejecutora, que el equipo **sí puede usar** (plantillas, lecciones aprendidas, repositorios).

#### Tres focos narrativos de la clase

1. Entorno organizacional  
2. Regulaciones gubernamentales  
3. Avances tecnológicos y estándares de la industria  

### 4.2 Entorno organizacional

**Definición.** Conjunto de cultura, valores, estructura y políticas en el que vive el proyecto. Puede facilitar o bloquear la integración (IL1.3).

- **Cultura:** ambiente que permite reportar malas noticias o que las oculta.
- **Estructura:** funcional, matricial o proyectizada; determina autoridad del director de proyecto y flujo de información.
- **Políticas y procedimientos:** quién aprueba un gasto, cómo se pide un ambiente en la nube.

**Caso 7.** Empresa social + inversores de impacto + subsidio + *partner* tecnológico. No es un equipo de tres personas sin rendición de cuentas. Un plan «ágil de garage» sin gobernanza de reporte a donantes **no se integra**.

### 4.3 Regulaciones gubernamentales

**Definición.** Marco legal y normativo externo (EEF) que el proyecto debe cumplir. Incluye, entre otros, privacidad de datos, seguridad y conformidad. Cumplir no es solo evitar sanciones: es condición de **confianza** de usuarios e inversores.

La clase insiste: las regulaciones no son solo obstáculos; abordadas de forma proactiva, orientan una operación íntegra.

#### ISO/IEC 27701 (lámina 15)

**Definición.** Extensión de gestión de **información de privacidad** sobre las normas de seguridad de la información (familia ISO/IEC 27000). Permite demostrar un sistema de gestión de información personal.

Ideas que hay que poder enunciar:

- se integra con las normas principales de seguridad de la información
- genera confianza en la gestión de datos personales
- apoya el cumplimiento de leyes y requisitos de privacidad
- es flexible a particularidades jurisdiccionales (Chile ≠ India ≠ un donante europeo)
- aporta transparencia entre interesados
- facilita acuerdos comerciales cuando los procesos están alineados

**Aplicación al Caso 7 (sin inventar leyes específicas):** el piloto trata datos de hogares en India, con posibles inversores internacionales. En el plan hay que declarar **qué datos** se guardan, **dónde** (nube), **quién** accede (soporte local) y **qué** sale hacia donantes. En el oral basta: «privacidad de hogares y reportes a terceros son EEF legales; el plan incluye minimización de datos y roles de acceso». No es necesario recitar números de leyes que no están en el caso.

### 4.4 Avances tecnológicos

Cada avance es oportunidad o restricción (EEF tecnológico):

- **Inteligencia artificial:** puede apoyar la detección de kits anómalos; exige cuidado con sesgos y con datos de población vulnerable.
- **Computación en la nube:** escala y acceso; implica dependencia de conectividad y costos variables.
- **Tecnologías emergentes:** obligan a adaptar el plan.

Cierre de la introducción de 1.2: el entorno no se espera de forma pasiva; se analiza y se arma plan B.

### 4.5 Estándares de la industria

**Definición. Estándar.** Documento establecido por consenso que provee reglas, pautas o características para uso común. En esta clase se usan como **lentes**, no como receta única.

#### PMBOK 6.ª (bibliografía del ramo)

**Definición.** Guía de fundamentos para la dirección de proyectos. En la 6.ª edición se organiza en **cinco grupos de procesos** (inicio, planificación, ejecución, monitoreo y control, cierre) y **diez áreas de conocimiento** (integración, alcance, cronograma, costos, calidad, recursos, comunicaciones, riesgos, adquisiciones, interesados).

Puntos clave de la clase 1.2: integración (que las piezas no se contradigan), gestión del alcance, tiempo y costos. Integrar PMBOK implica un enfoque metódico, basado en datos y alineado a objetivos de la organización.

#### CMMI (*Capability Maturity Model Integration*)

**Definición.** Modelo para evaluar y mejorar la **madurez de los procesos** de una organización. No pregunta solo si *este* proyecto salió bien: pregunta qué tan sistemática es la forma de trabajar.

Puntos clave: madurez de procesos, mejora continua, calidad y eficiencia.

**Nutrición (niveles clásicos de CMMI-DEV; no es lámina obligatoria, sí sirve si preguntan «qué es madurez»):**

| Nivel | Idea |
|---|---|
| 1. Inicial | El resultado depende de individuos («héroes») |
| 2. Gestionado | El proyecto se planifica y se controla |
| 3. Definido | Los procesos están estandarizados en la organización |
| 4. Gestionado cuantitativamente | Se miden y se controlan con datos |
| 5. En optimización | Mejora continua basada en medición |

CMMI mira **la organización**, no solo el Gantt de este semestre.

#### COBIT e ITIL (comparativa de la clase)

**Definición. COBIT.** Marco de **gobierno y control de TI**: quién decide, cómo se controla la información, cómo se rinde cuentas ante el negocio.

**Definición. ITIL 4.** Conjunto de prácticas para la **gestión de servicios** (operación, incidentes, problemas, cambios, mejora continua). No está pensado como guía de *proyectos*, sino de *servicio en operación*.

Lectura de la tabla de clase (verde = cubre; rojo = no es su foco; NA = no aplica):

| Pregunta | Quién brilla |
|---|---|
| ¿Es para **proyectos**? | PMBOK, CMMI, COBIT. ITIL: NA (es de **servicio**). |
| ¿Operación del **servicio**? | CMMI, COBIT, ITIL. PMBOK no es su fuerte. |
| ¿**Infraestructura**? | ITIL. PMBOK no. |
| ¿**Desarrollo**? | PMBOK, CMMI, COBIT. ITIL: NA. |
| ¿Gestión de **incidencias** y métricas de proceso? | CMMI, COBIT, ITIL. PMBOK NA o débil. |
| ¿Definir operativa concreta de procesos? | ITIL. |
| ¿**Mejora continua**, seguimiento, ciclo de producto, cambio? | Los cuatro. |
| ¿Compatible ISO 9001 e ISO 20000? | Los cuatro (según la tabla). |
| ¿Certifica a la **organización** por sí solo? | La tabla marca NA en los cuatro (otra cosa es evaluarse en CMMI o certificarse PMP). |

**Uso en el Caso 7 (sin recitar la tabla):**

- **PMBOK:** planificar el piloto (alcance, tiempo, costo, interesados).
- **CMMI:** no depender de que una persona «se acuerde» de cargar el Excel.
- **ITIL:** cuando el piloto pase a operación (tickets, incidentes, cambios). Conecta con la Unidad 2 y con la transición a operaciones.
- **COBIT:** gobierno de TI si los inversores piden trazabilidad de la información.

No se usa **un** estándar para todo. Se **elige el lente** según la pregunta.

### 4.6 Actividad 1.2.2

Equipos, 2 h, entrega + presentación, evalúa **IL1.2**.

1. Identificar factores ambientales relevantes.  
2. Métodos para analizar el **impacto** (no basta listar).  
3. Ejemplos en proyectos de software previos.  
4. Documentar y presentar.

Métodos simples de impacto:

- matriz factor × efecto (alcance / plazo / costo / calidad / riesgo)
- semáforo (alto / medio / bajo) + dueño del factor
- «si este factor empeora, ¿qué actividad de la ruta crítica se mueve?»

### 4.7 Mapa de factores del Caso 7

| Factor | Interno / externo | Impacto en el plan |
|---|---|---|
| Cultura de la empresa social y de la comunidad | Interno + externo cultural | El tablero debe servir al técnico local, no solo al inversor. |
| Financiamiento mixto | Interno + financiero externo | Los hitos de reporte a donantes entran al cronograma. |
| Distribución geográfica (equipo vs terreno) | Interno geográfico | Desfase horario, visitas costosas, supuestos de conectividad. |
| Privacidad de datos de hogares | Legal externo | Minimizar datos, roles, posible ISO 27701 / leyes locales. |
| Conectividad física | Ambiental físico | Modo sin conexión o carga por lotes; si no, el inventario miente. |
| Nube + costos variables | Tecnológico + financiero | Hosting variable; contingencia. |
| Estándar PMBOK | Industria | Acta, EDT, ruta crítica, interesados. |
| ITIL (tickets) | Industria / operación | El módulo de mantención es gestión de incidentes, no solo un formulario. |

### 4.8 Síntesis exigida 1.2

> Los EEF son condiciones **fuera del control del equipo** que entran a la planificación. Se clasifican en internos y externos. Los OPA sí se usan. PMBOK dirige **el proyecto**; CMMI madura **procesos**; ITIL opera **el servicio**; COBIT gobierna **TI**. En un caso real hay que enunciar el **impacto**, no la lista. Privacidad y seguridad son requisito de confianza, no un anexo.

Preguntas de reflexión de la clase:

1. ¿Qué factores ambientales influyen más en proyectos de software?  
2. ¿Cómo asegurar cumplimiento de estándares en *este* proyecto?  
3. ¿Qué desafíos aparecen al analizar factores y cómo resolverlos?

---

## 5. Bloque 1.3 — Estrategias de planificación (IL1.3)

**Material:** PPT 1.3.1 · Actividad 1.3.2 (equipos, 2 h)

La clase ilustra el riesgo de construir **sin plano**. Un proyecto de software sin estrategia de planificación es esa construcción.

### 5.1 Por qué planificar (también en ágil)

| Aporte (clase) | Definición operativa |
|---|---|
| Fundamento del éxito | Reduce la improvisación en lo que ya se puede anticipar |
| Visión clara | Objetivos y expectativas compartidos |
| Gestión de riesgos | Problemas visibles **antes** de producción |
| Optimización de recursos | Evita sobrecarga de personas, plazo y presupuesto |

**Definición.** Ágil **no** es «no planificar». Es planificar en **ciclos cortos** y volver a planificar cuando cambia el contexto. Eso es el enfoque adaptativo.

### 5.2 Enfoque predictivo

**Definición.** Enfoque **secuencial y estructurado** en el que una fase se completa antes de iniciar la siguiente (la familia clásica «cascada» pertenece aquí). Alcance, tiempo y costo se detallan de forma temprana; los cambios se controlan de forma formal.

**Características:** requisitos claros al inicio; control por fases; pocos cambios; entorno relativamente estable.

**Beneficios:** predecible; fácil de supervisar por hitos.  
**Desventajas:** rígido; un cambio tardío es costoso.

**Caso de la clase:** sistema de contabilidad corporativo, requisitos estrictos, cronograma detallado.

**Caso 7 — dónde calza:** inventario de kits (estados finitos), estructura de reporte a donantes, cumplimiento de privacidad. Eso no debe «descubrirse» cada *sprint* como si fuera una red social.

Herramientas asociadas en la clase: **Microsoft Project**, diagramas de Gantt.

### 5.3 Enfoque adaptativo

**Definición.** Enfoque **iterativo e incremental** que ajusta requisitos y solución con la retroalimentación. Plan de alto nivel al inicio y replanificación frecuente. La clase lo ilustra con la metáfora del GPS: se recablea cuando el camino cambia.

**Características:** adaptación a cambios; colaboración continua con interesados.

**Beneficios:** el producto se acerca a lo que el cliente **ahora** necesita.  
**Desventajas:** sin gestión, el alcance se desvía («siempre una cosa más»).

**Caso de la clase:** plataforma en un mercado rápido.

**Caso 7 — dónde calza:** UX del tablero en terreno, qué ticket es útil para el técnico local, cómo medir impacto sin un indicador vanidoso.

Herramientas asociadas: **Jira**, **Trello**, **Asana**.

#### Nutrición SBOK / Scrum (biblio oficial)

**Definición. Scrum.** Marco adaptativo con roles, eventos y artefactos para entregar incrementos de valor en ciclos cortos.

| Pieza | Definición |
|---|---|
| *Product Owner* | Maximiza valor; ordena el *backlog* |
| *Scrum Master* | Cuida el proceso; quita impedimentos |
| *Developers* | Construyen el incremento |
| *Product backlog* | Lista viva y priorizada de trabajo |
| *Sprint* | Ciclo corto de planificación y entrega |
| Incremento | Resultado usable al final del ciclo |
| Daily / Review / Retro | Inspeccionar y adaptar |

No es obligatorio montar Scrum de libro en un equipo de cuatro. Sí lo es el **espíritu**: entregar algo usable, inspeccionar, ajustar.

### 5.4 Enfoque híbrido

**Definición. Hibridación (clase 1.3).** Combinar de forma **deliberada** elementos predictivos y adaptativos según el contexto. No es «un poco de cada uno sin criterio»: se congela lo que exige certeza y se itera lo que exige aprendizaje.

Estrategias de adaptación que lista la clase:

1. **Análisis del contexto** — ¿el entorno es estable o volátil?  
2. **Hibridación** — predictivo donde hay certeza; adaptativo donde hay aprendizaje.  
3. **Participación de interesados** — sin ellos no hay destino que ajustar.  
4. **Evaluación continua** — el plan no se talla en piedra.

**Recomendación defendible para el Caso 7 (IL1.3):**

```
CAPA PREDICTIVA (cumplimiento y datos maestros)
  Inventario · estados del kit · roles y privacidad · calendario de reportes a donantes

CAPA ADAPTATIVA (aprendizaje de terreno)
  UX del tablero · flujo de tickets · indicadores de impacto · soporte local
```

Eso es un plan **contextualizado**: no «somos ágiles» ni «somos cascada».

### 5.5 Herramientas según enfoque (puente a IL1.4)

| Enfoque | Herramientas de la clase | Uso en el Caso 7 |
|---|---|---|
| Predictivo | MS Project, Gantt | Ruta crítica del piloto, hitos de subsidio |
| Adaptativo | Jira, Trello, Asana | *Backlog* del tablero y de tickets |
| Híbrido | Una de cada, o Project Libre + Kanban | Gantt de hitos + Kanban semanal |

La herramienta **sigue** a la estrategia, no al revés.

### 5.6 Actividad 1.3.2

Equipos, 2 h, entrega + presentación, evalúa **IL1.3**.

1. Identificar enfoques (predictivo, adaptativo, **híbrido**).  
2. Analizar necesidades del proyecto **y de la organización**.  
3. Desarrollar estrategias con herramientas y técnicas.  
4. Aplicarlas al caso.  
5. Documentar y presentar.

### 5.7 Síntesis exigida 1.3

> Planificar es la columna vertebral, también en ágil. **Predictivo** = requisitos estables, control por fases, Gantt/Project. **Adaptativo** = iteración, interesados cerca, Jira/Kanban. **Híbrido** = se congela lo regulado y se itera lo que se aprende. La estrategia se argumenta con el **contexto de la organización**, no con la moda del equipo.

Preguntas de reflexión de la clase:

1. ¿Cómo integrar predictivo y adaptativo en un solo proyecto?  
2. ¿Qué papel juegan las herramientas tecnológicas?  
3. ¿Cómo asegurar la participación de los interesados?

---

## 6. Bloque 1.4 — Selección de herramientas (IL1.4)

**Material en carpeta:** no está el PPT 1.4 ni la actividad 1.4.2.  
**Material que sí obliga:** Programa (Act 1.4, 6 h), rúbrica Eva 1, herramientas nombradas en 1.3.1 y en la pauta.

IL1.4 no pide reconocer logotipos. Pide **usar** la herramienta y **justificarla** según características y necesidades de la organización.

### 6.1 Qué pide Duoc

Recursos de la Eva 1: Office 365, **Microsoft Project**, **Project Libre**, etc. El pitch es **analógico** (pizarra, kraft, muro).

Criterio de rúbrica (nivel 100%): demuestra uso **y** justifica la selección. El oral vuelve a preguntar el «por qué».

### 6.2 Menú y criterio de elección

| Herramienta | En qué brilla | Límite | Argumento Caso 7 |
|---|---|---|---|
| **Microsoft Project** | CPM, recursos, línea base, reportes a gerencia | Licencia y curva de aprendizaje | Si la empresa social o el *partner* ya lo usa |
| **Project Libre** | Gantt, red, recursos, sin licencia comercial cara | Menos ecosistema corporativo | Si el piloto es de impacto y el presupuesto es acotado |
| **Excel / Office 365** | EDT, presupuesto, diccionario, RACI simple | Se rompe con muchas dependencias | Complemento; insuficiente como única herramienta de ruta crítica |
| **Jira** | *Backlog*, *sprints*, tickets | No reemplaza un Gantt de hitos para donantes | Capa adaptativa (tablero + mantención) |
| **Trello / Asana** | Kanban simple, equipo pequeño | Poca ruta crítica, poca línea base | Equipo de cuatro que aún no necesita Jira |
| **Pizarra / kraft** | Pitch de 15 min, entendimiento común | No es el plan oficial | **Obligatorio** en Eva 1 |

### 6.3 Plantilla de justificación (informe)

> Se elige **Project Libre** para la línea base predictiva (EDT, precedencias, ruta crítica, recursos y costos del piloto) porque el equipo no cuenta con licencia de MS Project y el patrocinador exige ver hitos de subsidio. Se complementa con **tablero Kanban** (Trello o Jira) para la capa adaptativa del tablero y los tickets, porque el flujo de mantención se descubrirá en terreno. Office 365 queda para el diccionario de la EDT y el presupuesto. El kraft se usa en el pitch, no como fuente de verdad.

Eso cubre IL1.4 y la pregunta 6 del banco oral.

### 6.4 Síntesis exigida 1.4

> La herramienta óptima es la que la **organización puede usar de verdad** y que cubre el enfoque elegido. En híbrido suele haber **dos** herramientas (línea base + flujo ágil), más el análogo para comunicar. Justificar es decir **contexto + restricción + para qué sirve cada una**, no «es la más popular».

---

## 7. El plan preliminar como sistema

```
                    NECESIDAD DE NEGOCIO / CASO DE NEGOCIO
                                    │
                                    ▼
                         ACTA DE CONSTITUCIÓN
                     (autoriza, nombra, techo de presupuesto)
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
                                    ▼
                         HERRAMIENTAS ELEGIDAS
                                    ▼
                     PLAN PRELIMINAR DEFENDIBLE
```

Si una pieza falta, la rúbrica lo registra:

- sin exclusiones → alcance incompleto  
- sin EDT → cronograma sin base  
- sin ruta crítica → el plazo no tiene criterio técnico  
- sin EEF → plan de laboratorio, no de industria  
- sin enfoque → herramientas huérfanas  
- sin justificación de herramienta → IL1.4 insuficiente  

---

## 8. Caso 7 · síntesis aplicada

**Nombre del caso:** Provisión de energía sostenible en comunidades desfavorecidas.  
**Producto del equipo:** **Kiran**.  
**Equipo:** Giannina Guerrero (dirección y frontend), Nicolás Barra (backend), Ari Araya (infraestructura y nube), Skarlett Tropan (calidad e impacto).  
**Contexto:** región desfavorecida de India, sin energía confiable; potencial solar; infraestructura débil. Financiamiento mixto (inversores de impacto, subsidios, *partners* tecnológicos).

**Problemas de negocio (no son el software):** falta de acceso a energía, desarrollo económico limitado, dependencia de fósiles.

**Solución de software (proyecto GPY1102):** plataforma para registrar kits de una comunidad piloto, monitorear estado, gestionar mantención y generar reportes para la dirección e inversores. El software **no** resuelve por sí solo los tres problemas de negocio: los hace **operables** en un piloto.

**Funcionalidades pedidas:**

1. Inventario (comunidades, hogares, kits; estados activo / falla / baja).  
2. Tablero operativo (visión general e individual).  
3. Monitoreo y mantención (rendimiento + tickets + soporte local).  
4. Impacto social y ambiental (informes periódicos a inversores y donantes).

### 8.1 Borrador de enunciado de alcance

- **Producto:** Kiran, sistema web (con posible apoyo móvil o carga sin conexión) de operación de kits solares del piloto.
- **Criterios de aceptación (ejemplos):** cada kit tiene hogar asociado y estado; un ticket se abre desde un kit en falla; un reporte periódico exportable llega a patrocinadores.
- **Entregables:** módulos 1–4, capacitación breve al soporte local, documento de roles y privacidad, plan preliminar (esta Eva).
- **Exclusiones:** fabricación e instalación de paneles, microfinanzas, expansión a otras regiones, aplicación ciudadana masiva.
- **Restricciones:** presupuesto de piloto, conectividad, equipo de cuatro personas, fecha del primer reporte a donantes.
- **Supuestos:** hay comunidad piloto identificada; hay al menos un técnico local; los inversores aceptan indicadores simples en esta fase.

No inventar montos de subsidio, leyes indias ni datos de hogares que no estén en el caso.

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

### 8.3 Lógica de ruta crítica (no son números finales)

Camino largo probable:

**datos maestros (inventario) → tablero que lee esos datos → tickets sobre kits reales → reporte de impacto que usa operación real.**

Si el inventario se atrasa, el resto es una demostración vacía. Equivale, en lógica, al B–D–E–G del PPT.

### 8.4 Estrategia híbrida

Predictivo en inventario, privacidad y reportes (2, 6 y 5). Adaptativo en tablero y tickets (3 y 4). La dirección del proyecto (1) usa PMBOK 6 para integrar.

### 8.5 Valor e interesados (lenguaje Eva 1; etiquetar PMBOK 7.ª)

Valor = kits observables + fallas atendibles + reportes creíbles.  
No es valor = pantallas si el técnico no las usa o el donante no entiende el indicador.

---

## 9. Eva Parcial 1 — de la unidad a la nota

**Nombre:** Planificando un proyecto de software  
**Cuándo:** semana 5 (el caso se elige en semana 4)  
**Tiempo:** 5 horas · Sala de Proyectos  
**Equipos:** sugeridos de 3; este grupo tiene 4 → **los cuatro hablan**  
**Ponderación:** 30% del bloque de parciales (≈ 18% de la nota final)

### 9.1 Dos dimensiones

| Dimensión | Peso dentro de la Eva 1 | Carácter |
|---|---|---|
| Informe grupal (resumen ejecutivo) | **30%** | Grupal |
| Presentación-defensa oral | **70%** | **Individual** (preguntas a cada integrante sobre **todas** las temáticas) |

Formato informe: PDF, Arial o Times 12, interlineado 1.5, márgenes 2.5 cm, **máximo 7 planas**, citas **APA**. Apoyo del pitch: **analógico**.

### 9.2 Contenido del informe (los cuatro IL)

1. Alcance, recursos, cronograma; contexto y necesidades; plan inicial con herramientas de industria.  
2. Factores ambientales y estándares; impacto en el caso; influencia del contexto organizacional.  
3. Estrategias de planificación e integración **contextualizadas**.  
4. Herramientas usadas en cada sección, **justificadas**.

### 9.3 Niveles de logro

| Nivel | % | Significado |
|---|---|---|
| Muy buen desempeño | 100 | Precisión y detalle técnico en todos los aspectos |
| Buen desempeño | 80 | Claro, con omisiones o errores menores |
| Aceptable | 60 | Básico; omisiones notables |
| Incipiente | 30 | Errores graves; no competente |
| No logrado | 0 | Ausente o incorrecto |

### 9.4 Banco de preguntas del pitch

1. ¿Cuál es el contexto y las necesidades de la organización?  
2. ¿Cómo se determinaron alcance y recursos?  
3. ¿Con qué criterio técnico se definió el cronograma?  
4. ¿Qué beneficios dan las estrategias de planificación e integración?  
5. ¿Qué elementos del contexto organizacional se incorporaron?  
6. ¿Qué herramientas se usaron y por qué se eligieron?

### 9.5 Lo que el oral mira (≈ 70%)

- dominio de los componentes del plan **y** del contexto de la organización  
- **aporte personal** a las estrategias (no «lo hizo el grupo»)  
- justificación de herramientas según necesidades de la organización  
- el visual **refuerza**; no es un dibujo decorativo  

---

## 10. Glosario de la Unidad 1

| Término | Definición de estudio |
|---|---|
| **Acta de constitución** | Documento que autoriza el proyecto y nombra al director o directora |
| **Actividad** | Trabajo programable derivado, en general, de un paquete de trabajo |
| **Adaptativo** | Enfoque iterativo e incremental; replanificación frecuente |
| **Adelanto (*lead*)** | Solapamiento entre actividades |
| **Alcance del producto** | Características y funciones del resultado |
| **Alcance del proyecto** | Trabajo para entregar el producto, incluida la gestión |
| **Caso de negocio** | Justificación de la inversión |
| **CMMI** | Modelo de madurez de procesos de la organización |
| **COBIT** | Marco de gobierno y control de TI |
| **Contingencia** | Reserva para riesgos identificados |
| **Costo directo / indirecto** | Atribuible a este proyecto / compartido entre varios |
| **Costo fijo / variable** | Independiente / dependiente del volumen (en un rango) |
| **Costo hundido** | Ya gastado; no debe decidir el futuro |
| **Costo de oportunidad** | Valor de la alternativa no elegida |
| **CPM** | Método de la ruta crítica; camino más largo |
| **Criterios de aceptación** | Condiciones para dar por bueno un entregable |
| **Cronograma** | Modelo de fechas planificadas e hitos |
| **Cuenta de control** | Punto de medición integrada de alcance, plazo y costo |
| **Descomposición** | Dividir el trabajo en partes manejables |
| **Diagrama de red** | Representación de dependencias entre actividades |
| **Diccionario de la EDT** | Ficha de cada componente (criterio, recursos, costo, hitos) |
| **EDT / WBS** | Árbol del 100% del trabajo acordado |
| **EEF** | Factor ambiental que el equipo no controla |
| **Elaboración progresiva** | Detallar el plan cuando hay más información |
| **Enunciado del alcance** | Descripción de qué entra, qué no, criterios, supuestos y restricciones |
| **Entregable** | Resultado verificable |
| **Exclusión** | Trabajo que explícitamente no se hará |
| **Gantt** | Barras de tiempo para el equipo |
| **Gobernanza** | Marco de autoridad y decisión (organización o proyecto) |
| **Grupos de procesos (PMBOK 6)** | Inicio, planificación, ejecución, monitoreo y control, cierre |
| **Híbrido** | Combinación deliberada de predictivo y adaptativo |
| **Hito** | Evento significativo de duración cero |
| **Holgura** | Tiempo que una actividad puede atrasarse sin mover el fin |
| **Hundido** | Costo ya incurrido |
| **Interesado** | Quien afecta o se percibe afectado |
| **ISO/IEC 27701** | Extensión de privacidad sobre seguridad de la información |
| **ITIL** | Prácticas de gestión de **servicio** |
| **OPA** | Activos de proceso de la organización (plantillas, lecciones) |
| **Outcome / output** | Efecto / producto del trabajo |
| **Paquete de planificación** | Trabajo conocido sin actividades aún detalladas |
| **Paquete de trabajo** | Nivel más bajo de la EDT, estimable y asignable |
| **PERT** | (O + 4M + P) / 6; desviación (P − O) / 6 |
| **PMBOK 6.ª** | Guía oficial del ramo para dirigir el proyecto |
| **Predictivo** | Plan detallado al inicio; fases secuenciales |
| **Presupuesto** | Suma autorizada para ejecutar el trabajo |
| **Proyecto** | Esfuerzo temporal para un resultado único |
| **RBS** | Estructura de desglose de recursos |
| **Requisito** | Condición o capacidad que debe cumplirse |
| **Restricción** | Límite obligatorio (presupuesto, plazo, ley, tecnología) |
| **Retraso (*lag*)** | Espera entre actividades |
| **Ruta crítica** | Camino más largo; manda la fecha de término |
| **Scope creep** | Crecimiento de alcance sin control de cambios |
| **Scrum / SBOK** | Marco / guía adaptativos (biblio oficial del ramo) |
| **Supuesto** | Factor dado por cierto; si falla, hay riesgo |
| **Tailoring** | Ajustar el rigor de la gestión al contexto (idea; no citar 8.ª en el informe) |
| **Técnica Delphi** | Consenso anónimo de expertos por rondas |
| **Triple restricción** | Alcance, tiempo y costo (calidad transversal) |
| **Valor** | Beneficio real ponderado; no se agota en el entregable |

---

## 11. Banco corto de respuestas orales

Practicar **en voz alta**. Sustituir números cuando el equipo tenga Gantt real. No leer en la Eva.

**1. Contexto y necesidades.**  
«Es una empresa social que impulsa un piloto de kits solares en una comunidad de India sin energía confiable. El software no instala paneles: opera inventario, tablero, mantención y reportes de impacto para inversores y donantes.»

**2. Alcance y recursos.**  
«El alcance se descompuso en EDT: inventario, tablero, tickets, impacto, privacidad y capacitación. Se excluyen fabricación e instalación. Recursos: equipo de desarrollo reducido, soporte local, nube y reserva de contingencia. Cada paquete del diccionario tiene responsable y criterio de aceptación.»

**3. Criterio del cronograma.**  
«De la EDT salieron actividades y precedencias. El inventario alimenta el tablero, los tickets y el reporte; ese es el camino más largo, la ruta crítica. Se usa lógica CPM; donde hay incertidumbre de terreno, PERT. A gerencia se muestran hitos; al equipo, Gantt.»

**4. Beneficios de la estrategia.**  
«Híbrido: se congelan datos maestros, privacidad y calendario de donantes (predictivo) para no fallar cumplimiento. Se iteran tablero y tickets (adaptativo) porque el técnico local corregirá el flujo. Así el plan se integra a una organización que debe ser flexible en terreno y estricta con financiamiento de terceros.»

**5. Contexto organizacional incorporado.**  
«Financiamiento mixto implica hitos de reporte. Distancia geográfica y cultura comunitaria implican supuestos de conectividad y una interfaz simple. La gobernanza de inversores entra al plan de interesados y de comunicaciones, no al final.»

**6. Herramientas.**  
«Project Libre o MS Project para línea base y ruta crítica, porque hay que defender el plazo del piloto. Kanban para el trabajo semanal adaptativo. Office para diccionario y costos. Kraft solo para explicar en quince minutos. La elección responde a licencia, tamaño del equipo y doble audiencia: donantes y desarrollo.»

---

## 12. Autoevaluación (sin apuntes)

Si una respuesta no sale en 60 segundos, volver al bloque.

1. Nombre los seis mínimos del enunciado de alcance.  
2. Diferencie paquete de trabajo, paquete de planificación y cuenta de control.  
3. ¿Qué cubre el diccionario de la EDT que el árbol no cubre?  
4. En el ejemplo de clase, ¿cuál es la ruta crítica y cuánto dura el proyecto?  
5. Calcule PERT con O = 4, M = 7, P = 16.  
6. Fórmulas de EF, LS y holgura según la lámina.  
7. Seis tipos de costo, con un ejemplo cada uno.  
8. EEF interno frente a externo: tres de cada lado.  
9. EEF frente a OPA, en una frase.  
10. PMBOK frente a CMMI frente a ITIL: una frase cada uno.  
11. Según la tabla de clase: ¿ITIL se enfoca en proyectos? ¿PMBOK en operación de servicio?  
12. Tres aportes de ISO/IEC 27701.  
13. Predictivo frente a adaptativo: una ventaja y una desventaja de cada uno.  
14. Proponga el híbrido del Caso 7 en dos capas.  
15. ¿Qué documento autoriza el proyecto?  
16. Output frente a outcome frente a valor, con el Caso 7.  
17. Nombre cinco tipos de interesado del Caso 7.  
18. ¿Por qué el oral vale 70% y qué ocurre si solo se estudió «la parte propia»?  
19. Justifique una herramienta para **esta** organización, no en abstracto.  
20. ¿Qué queda **fuera** del Caso 7 y por qué hay que escribirlo?

### Clave breve

1. Producto, criterios de aceptación, entregables, exclusiones, restricciones, supuestos.  
2. Trabajo más bajo estimable / trabajo conocido sin actividades detalladas / punto de medición integrada.  
3. Criterios, supuestos, recursos, duración, hitos, costo, responsable, firma.  
4. B–D–E–G, 26.  
5. 8 días; desviación 2.  
6. EF = (ES + Dur) − 1; LS = (LF − Dur) + 1; holgura = LF − EF.  
7. Variable, fijo, directo, indirecto, oportunidad, hundido.  
8. Interno: cultura, estructura, infraestructura, software, disponibilidad, capacidad. Externo: mercado, social, legal, estándares, financiero, físico, etc.  
9. EEF no se controlan; OPA sí se usan (plantillas, lecciones).  
10. Dirigir el proyecto / madurar procesos / operar el servicio.  
11. ITIL: NA en foco a proyectos. PMBOK: no es fuerte en operación de servicio.  
12. Confianza, apoyo a leyes de privacidad, integración con seguridad, transparencia, flexibilidad jurisdiccional.  
13. Predictivo: control frente a rigidez. Adaptativo: flexibilidad frente a desvío.  
14. Inventario y cumplimiento predictivos; tablero y tickets adaptativos.  
15. Acta de constitución.  
16. Plataforma / kits atendibles / energía e informes creíbles.  
17. Inversores, subsidio, comunidad, soporte local, equipo, dirección, *partner* tecnológico.  
18. La rúbrica evalúa dominio **individual** de **toda** la unidad.  
19. Licencia + audiencia (donantes frente a desarrollo) + enfoque híbrido.  
20. Fabricar e instalar paneles: si no se excluye, el alcance se infla.

---

## 13. Referencias (clases + programa)

1. Project Management Institute. (2017). *Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK)* (6.ª ed.).  
2. Wysocki, R. K. (2019). *Effective project management: Traditional, agile, extreme, hybrid* (8th ed.). Wiley.  
3. Layton, M. C. (2022). *Scrum for dummies* (3rd ed.). Wiley.  
4. Peters, L. J. (2024). *Software project management: Methods and techniques*. CRC Press.  
5. SCRUMstudy. (2023). *Guía SBOK* (4.ª ed., español).  
6. Baud, J.-L. (2020). *ITIL 4: Entender el enfoque y adoptar las buenas prácticas*. ENI.  
7. PMI. (2021). *Guía del PMBOK* (7.ª ed.) — solo el extracto de valor e interesados usado en Eva 1.

---

## 14. Cierre

Planificar un proyecto de software en este ramo es producir un plan que la **organización pueda usar**: autorizado (acta), limitado (alcance y exclusiones), descompuesto (EDT), fechado con criterio (ruta crítica), costoso de forma honesta (tipos de costo y contingencia), situado en su entorno (EEF y estándares), con una forma de avanzar (predictivo, adaptativo o híbrido) y con una herramienta justificada. El Caso 7 es ese plan, no un relato sobre paneles solares. La Eva 1 se gana en la pizarra, con dominio individual de toda la unidad.
