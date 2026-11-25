# Planificación de proyectos de software

# Guía de estudio

Material para aprender a **planificar un proyecto de software**: alcance, trabajo, tiempo, costo, entorno, enfoque y herramientas.

Las definiciones siguen el lenguaje de la *Guía del PMBOK* **6.ª edición** (2017). Donde se habla de **valor** e **interesados** con más énfasis, se indica PMBOK 7.ª.

Un ejemplo recorre la guía: **Kiran**, una plataforma para operar kits solares de un piloto (inventario, tablero, tickets e informes). Sirve para ver los conceptos en un caso concreto, no para describir una evaluación.

Cómo leer cada término: **qué es**, **qué no es**, **para qué sirve** y **un ejemplo**. Si dos palabras se parecen, la guía las contrapone a propósito.

---

## Índice

- 1. Cimientos y léxico
- 2. El plan preliminar: alcance, EDT, cronograma, costos y recursos
- 3. Factores ambientales y estándares
- 4. Estrategias de planificación
- 5. Selección de herramientas
- 6. El plan como sistema
- 7. Ejemplo aplicado (Kiran)
- 8. Glosario
- 9. Autoevaluación
- 10. Referencias

---

## 1. Cimientos y léxico

Antes del alcance hace falta un vocabulario compartido: qué es un proyecto, quién autoriza, quién es interesado y qué cuenta como valor.

### 1.1 Distinciones que hay que poder decir

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

### 1.2 Proyecto y dirección de proyectos

**Definición. Proyecto.** Esfuerzo **temporal** (tiene inicio y fin definidos) destinado a crear un **producto, servicio o resultado único**.

Para entenderla hay que separar las dos palabras clave. **Temporal** no quiere decir «corto»: un proyecto puede durar meses o años; lo que lo define es que **termina**. Cuando el resultado pasa a usarse de forma continua, eso ya no es el proyecto: son **operaciones**. **Único** no quiere decir «nunca visto en el mundo»: quiere decir que *este* resultado, para *esta* organización y *este* conjunto de requisitos, no existía antes. Dos plataformas de inventario pueden parecerse; el piloto Kiran sigue siendo un proyecto único porque sus interesados, restricciones y datos son los de ese piloto.

Error frecuente: tratar el mantenimiento diario (cargar kits, cerrar tickets) como si fuera el proyecto. Eso es operación. El proyecto **construye** la capacidad; la operación **la usa**.

**Definición. Dirección de proyectos.** Aplicación de conocimientos, habilidades, herramientas y técnicas a las actividades del proyecto para cumplir los requisitos.

No es «administrar gente» en abstracto. Es hacer que alcance, plazo, costo, calidad, riesgos e interesados **queden alineados** con lo autorizado. Sin dirección, hay trabajo; no hay proyecto gobernado.

**Definición. Operaciones.** Trabajo continuo y repetitivo que mantiene el negocio. Al cierre, el proyecto transfiere su resultado a operaciones.

| | Proyecto | Operaciones |
|---|---|---|
| Tiempo | Inicio y fin | Continuo |
| Resultado | Único | Repetitivo |
| Propósito | **Cambiar** el estado de la organización | **Mantener** el negocio |
| Ejemplo (Kiran) | Construir la plataforma del piloto | Atender tickets cuando ya esté en producción |

**Definición. Triple restricción (triángulo de hierro).** Relación entre **alcance, tiempo y costo**, con la **calidad** como criterio que atraviesa los tres. Si aumenta el alcance y no se mueven plazo ni presupuesto, la calidad o el riesgo se degradan. Si se acorta el plazo, o se reduce alcance o se sube costo.

En la planificación se **declara** esa relación (qué entra, para cuándo, con qué techo). El control —medir desvíos y corregir— ocurre después, cuando el trabajo ya está en marcha.

Error frecuente: cambiar el alcance («agreguemos un módulo más») y dejar intactos fecha y presupuesto. Eso no es flexibilidad: es romper la restricción sin decirlo.

### 1.3 Entregable, output, outcome y valor

**Definición. Entregable (*deliverable*).** Producto, resultado o capacidad **verificable** producido para completar un proceso, una fase o el proyecto.

**Verificable** es la palabra que importa: alguien puede comprobar si está o no. «Mejorar la operación» no es entregable. «Tablero en el que el técnico ve el estado de cada kit» sí lo es, porque se puede abrir y contrastar con un criterio de aceptación.

**Definición. Output.** Lo que el proyecto produce de forma observable: la plataforma, un informe, una capacitación, un XML de cronograma.

**Definición. Outcome.** El **efecto** que ese output genera en el trabajo real. El tablero (output) no es el outcome; el outcome es que una falla deja de pasar desapercibida.

**Definición. Valor.** Importancia de los beneficios —tangibles o intangibles— ponderada frente a costo, tiempo y riesgo. El valor puede aparecer durante el proyecto, al cierre o **después**, cuando el resultado ya está en operaciones.

El PMBOK 7.ª (principio de enfocarse en el valor) precisa: si el software se entrega y **no mejora** lo prometido, los interesados pueden juzgar el proyecto como fracaso aunque el código «funcione». En Kiran el valor no es «hay un tablero». El valor es que un kit dado de baja no siga contando como activo, que el soporte atienda fallas reales y que un financiador reciba un informe usable.

Cadena para no mezclarlos: **entregable/output** (lo que se produce) → **outcome** (lo que cambia en el uso) → **valor** (si ese cambio justifica lo invertido).

**Definición. Caso de negocio (*business case*).** Documento o argumento que **justifica la inversión**: necesidad u oportunidad, opciones consideradas, costos, beneficios esperados y recomendación (hacer / no hacer / hacer de otra forma). Los proyectos suelen nacer de una necesidad de negocio + esa justificación + una estrategia. Sin caso de negocio, el acta no tiene por qué existir.

### 1.4 Interesados (*stakeholders*)

**Definición. Interesado.** Persona, grupo u organización que **afecta**, **es afectada** o **se percibe afectada** por una decisión, actividad o resultado del proyecto.

Tres cláusulas, no una. Quien **afecta** puede imponer fecha o presupuesto (un donante). Quien **es afectada** recibe el resultado (el técnico, el hogar). Quien **se percibe afectada** también cuenta: si una autoridad local cree que el software expone datos, hay que gestionarla aunque no use la plataforma. La influencia puede ser a favor o en contra. La lista no es fija: entran, salen y cambian de interés.

Error frecuente: reducir «interesados» a «el cliente que paga». En software de piloto hay operación, comunidad, financiadores, equipo y dirección; cada uno mueve una parte distinta del plan (alcance, plazo, costo, calidad, riesgo, criterio de éxito).

La comunicación con ellos es **bidireccional**: no basta informar; hay que recoger lo que necesitan y lo que rechazan.

**Interesados mínimos en Kiran**

- Patrocinadores: inversores de impacto, agencia de subsidios, empresas tecnológicas asociadas.
- Beneficiarios: comunidades y hogares (no necesariamente usuarios del software en esta fase).
- Operación: técnicos de soporte local.
- Equipo del proyecto: desarrollo, diseño, datos, QA, responsable de impacto.
- Dirección de la empresa social; autoridades locales y donantes si aplica; PMO si existe.

### 1.5 Gobernanza

**Definición. Gobernanza organizacional.** Marco de autoridad, políticas y cumplimiento de **toda** la empresa: quién aprueba gastos, con qué reglas de privacidad, qué estándares son obligatorios.

**Definición. Gobernanza del proyecto.** Marco **de este** proyecto: quién decide un cambio de alcance, hasta qué monto puede comprometer la directora, y a quién se escala si el terreno no carga datos.

La diferencia es de alcance. La organizacional vale para todos los proyectos. La del proyecto se diseña para *este*. Un plan que contradice la gobernanza de la empresa (por ejemplo, subir datos de hogares a un repositorio público) no es integrable: la organización no puede usarlo.

### 1.6 Acta de constitución (*Project Charter*)

**Definición.** Documento emitido por el patrocinador (*sponsor*) o por la gobernanza que **autoriza formalmente** el proyecto, nombra al director o directora y le otorga autoridad para aplicar recursos de la organización.

Sin acta, el trabajo puede existir de hecho; no está **autorizado**. El acta responde: ¿por qué existe este proyecto?, ¿quién lo dirige?, ¿con qué techo de plazo y presupuesto?, ¿quién firma?

**No es** el plan detallado. No trae EDT completa ni ruta crítica. El plan se elabora **después**, usando el acta como límite: no se puede planificar un alcance o un costo que el acta no contempla, salvo control de cambios.

Mínimo que debe quedar claro:

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

## 2. El plan preliminar

El plan preliminar reúne **acta**, **enunciado de alcance** (con EDT), **cronograma** y **costos/recursos**. No es un informe de 40 páginas: es el primer conjunto de documentos con el que se puede defender qué se hará, para cuándo y con qué techo.

### 2.1 Alcance del proyecto

**Definición. Alcance del producto.** Características y funciones que debe tener el **resultado**. Responde: ¿cómo es el software (o el bien) cuando está listo?

No es la lista de tareas del equipo. «Tablero con estado de cada kit» es alcance de producto. «Reuniones de seguimiento semanales» no lo es: eso es trabajo de gestión, y entra en el alcance del **proyecto**.

**Definición. Alcance del proyecto.** Todo el trabajo necesario para entregar ese producto con las características acordadas, **incluido el trabajo de gestión** (acta, interesados, pruebas, capacitación, despliegue).

Error frecuente: definir solo pantallas y olvidar capacitación, privacidad o transición a operaciones. El producto puede estar «terminado» y el proyecto, no.

**Definición. Enunciado del alcance.** Descripción detallada del proyecto y del producto que permite un **entendimiento común** entre interesados y deja las **exclusiones explícitas**. El proceso suele ser **iterativo**: se precisa a medida que hay más información.

No es el acta. El acta **autoriza**. El enunciado **delimita** qué entra y qué no. Sin exclusiones escritas, cualquier pedido posterior parece «parte de lo acordado».

**Definición. Scope creep.** Expansión **no controlada** del alcance: se agrega trabajo sin ajustar tiempo, costo o recursos y **sin** pasar por control de cambios.

No es lo mismo que un cambio aprobado. Si el patrocinador pide un módulo extra, se evalúa impacto y se firma: eso es cambio controlado. Si el módulo entra «porque era chico», es *scope creep*.

**Definición. Control de cambios.** Proceso formal para evaluar, aprobar o rechazar una modificación al alcance, plazo, costo o línea base, y dejar registro. Sin este proceso, todo pedido se cuela como si ya estuviera autorizado.

#### Mínimo del enunciado

| Elemento | Definición / pregunta | Ejemplo (Kiran) |
|---|---|---|
| Descripción del alcance del producto | ¿Qué se construye? | Plataforma para registrar kits, tablero, tickets de mantención e informes de impacto de un piloto. |
| Criterios de aceptación | Condiciones para dar por bueno un entregable | Un kit se puede crear, cambiar de estado (activo / en falla / dado de baja) y verse en el tablero el mismo día. |
| Entregables | Resultados verificables | Módulo inventario, tablero, módulo tickets, reporte periódico, capacitación al soporte local. |
| Exclusiones | Trabajo que **explícitamente** no se hará | Fabricar paneles, instalar en techos, tendido eléctrico, expansión a otras regiones en esta fase. |
| Restricciones | Límites obligatorios | Presupuesto de piloto, conectividad irregular, fecha de reporte a donantes, equipo pequeño. |
| Supuestos | Factores dados por ciertos sin prueba plena | Hay conectividad mínima; el soporte local carga datos; los inversores aceptan reporte mensual. |

**Definición. Criterios de aceptación.** Condiciones **verificables** que un entregable debe cumplir para darse por bueno. No son deseos («que sea fácil de usar»): son pruebas («el técnico cambia el estado del kit y el tablero lo muestra el mismo día»).

**Definición. Exclusión.** Trabajo que **explícitamente no se hará** en este proyecto o fase. Se escribe para que no se asuma incluido. Fabricar paneles, en Kiran, es exclusión: si no está escrita, un interesado puede creer que «kits solares» incluye instalarlos.

**Definición. Restricción.** Límite **obligatorio** sobre lo que sí se hace: presupuesto, plazo, ley, tamaño del equipo, tecnología impuesta. A diferencia de la exclusión, la restricción no saca trabajo: **acota** cómo se hace el trabajo que sí entra.

**Definición. Supuesto.** Factor que se da por **verdadero** sin prueba plena, para poder planificar. Si se demuestra falso, aparece un riesgo (o un problema). «El soporte local carga datos» es supuesto; si no carga, el inventario no sirve. Un supuesto sin qué hacer si falla es un **riesgo no declarado**.

Las tres se confunden. Pregunta de control: ¿esto **no se hará** (exclusión), **se hará pero con un techo** (restricción), o **se asume cierto para seguir** (supuesto)?

#### Plantilla del enunciado

No es un ensayo: es una ficha que dirección puede firmar.

**Cabecera (quién y cuándo):** fecha, nombre del proyecto, versión, director/a, patrocinador, cliente, equipo, otros interesados.

**Cuerpo (qué y para qué):**

- **Antecedentes:** justificación, necesidad de mercado u oportunidad.
- **Descripción del producto o servicio:** el entregable final.
- **Objetivos:** qué se logra **con** ese entregable (outcome, no solo output).

Después se completan los seis mínimos (producto, criterios, entregables, exclusiones, restricciones, supuestos). Sin la cabecera, el enunciado no tiene dueño; sin los seis mínimos, no tiene borde.

#### Herramientas y técnicas para definir alcance

1. **Analizar objetivos del producto y convertirlos en requisitos.**  
   **Definición. Requisito.** Condición o capacidad que el producto o el proyecto **debe** cumplir, formulada de modo que se pueda verificar.

   Un objetivo de negocio («mejorar la calidad de vida») no es requisito: no se puede aceptar o rechazar en una demostración. «Registrar cada kit con estado operativo (activo / falla / baja)» sí lo es, porque se prueba con un registro concreto.

2. **Generación de alternativas.**  
   Comparar formas distintas de cumplir el mismo objetivo antes de fijar una. ¿Aplicación móvil para el técnico o solo web? ¿Tickets por un canal externo o módulo interno? Elegir sin alternativas es decidir por inercia.

3. **Técnica Delphi.**  
   **Definición.** Método de consenso entre expertos **en anónimo**: un facilitador envía un cuestionario, resume las respuestas y las devuelve para otra ronda, hasta que las estimaciones o juicios se acercan.

   El anónimo es el mecanismo: evita que la persona de más rango imponga el número. No es una encuesta de opinión ni una votación a mano alzada. Sirve cuando hay incertidumbre y varias disciplinas (operación en terreno, software, impacto social) no coinciden en la primera reunión.

### 2.2 EDT / WBS

**Definición. EDT (Estructura de Desglose del Trabajo) o WBS (*Work Breakdown Structure*).** Descomposición **jerárquica** de **todo** el trabajo del proyecto, organizada por entregables (no por departamentos).

Regla del PMBOK 6: la EDT cubre el **100%** del alcance acordado. Lo que no está en la EDT **no se hace**, o entra solo por control de cambios. No es un organigrama ni una lista de tareas diarias: el organigrama dice *quién*; la lista de tareas dice *cuándo*; la EDT dice *qué trabajo existe*.

Error frecuente: poner «frontend» y «backend» como ramas. Eso describe al equipo, no el trabajo. Las ramas deben ser entregables (inventario, tablero, tickets, reportes).

#### Diagrama de descomposición

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

#### Niveles de la EDT

Cada nivel tiene una función distinta. No se baja por costumbre ni para «llenar» el diagrama: se baja hasta que el trabajo se pueda estimar y asignar.

- La **cuenta de control** es el nivel en el que se miden juntos alcance, plazo y presupuesto.
- El **paquete de planificación** está debajo: se sabe qué trabajo es, pero **aún no** se han detallado las actividades.
- El **paquete de trabajo** es el nivel más bajo de la EDT: ahí hay duración, costo y responsable.

Una numeración típica:

```
Proyecto
 ├── 1 …
 └── 2 …
      ├── 2.1 …
      ├── 2.2                    ← rama
      │     ├── 2.2.1
      │     ├── 2.2.2
      │     └── 2.2.3            ← cuenta de control
      │           ├── 2.2.3.1    ← paquete de planificación
      │           └── 2.2.3.2
      │                 ├── 2.2.3.2.1  ← paquete de trabajo
      │                 └── 2.2.3.2.2  ← paquete de trabajo
      └── 2.3 …
```

| Nombre | Definición | Para qué |
|---|---|---|
| **Cuenta de control (*control account*)** | Punto de gestión donde se integran alcance, plazo y presupuesto | Medir desempeño más adelante |
| **Paquete de planificación (*planning package*)** | Debajo de la cuenta de control: se conoce el trabajo, **aún no** las actividades detalladas | No fingir detalle inexistente |
| **Paquete de trabajo (*work package*)** | Nivel más bajo de la EDT | Aquí hay duración, costo y responsable |

**Definición. Descomposición.** Técnica de dividir entregables y trabajo del proyecto en componentes más pequeños y manejables, hasta el paquete de trabajo.

No es «partir por partir». Si un componente ya se puede estimar con confianza (tiempo, costo, responsable), se detiene. Si no, se subdivide. El diagrama de más arriba es esa regla, no un adorno.

**Definición. Elaboración progresiva.** Ir detallando el plan **a medida que aumenta la información disponible**. Al inicio se conocen entregables; las actividades finas aparecen después.

No es improvisación ni *scope creep*. Improvisar es cambiar el trabajo sin criterio. Elaboración progresiva es completar el detalle **dentro** del alcance ya acordado. Un paquete de planificación existe precisamente para eso: reservar el trabajo sin fingir un cronograma que aún no se puede escribir.

#### Diccionario de la EDT

**Definición. Diccionario de la EDT.** Documento que detalla cada componente de la EDT: descripción, responsable, criterios de aceptación, supuestos, recursos, duración, hitos y costo.

La EDT muestra la **estructura** (qué paquetes existen y cómo se anidan). El diccionario muestra el **contenido** de cada paquete (qué se acepta, quién lo hace, cuánto cuesta). Sin diccionario, la EDT no se puede estimar ni asignar: solo se sabe que «existe un tablero», no cuándo está bueno.

Ejemplo (componente `2.2.2.1 Mercado`):

| Campo | Ejemplo |
|---|---|
| ID | 2.2.2.1 |
| Cuenta de control | 2.2 |
| Última actualización | 15 de julio |
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

**Traducción a Kiran** (tablero operativo):

- Criterio de aceptación: se ve el estado de cada kit y el recuento de tickets abiertos/cerrados en una sola pantalla.
- Entregable: vista de tablero usable en navegador por el soporte local.
- Supuesto: hay datos de inventario cargados.
- Recursos: 1 front, 1 back, 1 QA.
- Hito: demostración al patrocinador.

Sin diccionario, la EDT no se puede estimar ni asignar.

### 2.3 Cronograma

**Definición. Desarrollar el cronograma.** Proceso de integrar actividades, secuencias, recursos y duraciones para crear el **modelo de programación**: fechas de inicio y fin planificadas, e **hitos**. Es **iterativo**: la primera versión se corrige cuando hay duraciones reales y recursos limitados.

No es «poner fechas en un calendario». El calendario es una **representación**. El modelo es la lógica: qué precede a qué, cuánto dura cada actividad y qué pasa si una se atrasa.

**Definición. Hito (*milestone*).** Punto o evento **significativo** en el proyecto. Duración **cero**: no consume trabajo; marca que algo se alcanzó (acta firmada, inventario cargado, primer reporte a donantes).

Error frecuente: tratar un hito como una tarea de varios días. Si «capacitación» dura una semana, es actividad. El hito es «capacitación completada».

**Definición. Actividad.** Porción de trabajo **programable** (tiene duración, predecesora y recursos), por lo general derivada de un paquete de trabajo. La EDT dice *qué* hay que producir; la actividad dice *cómo se programa* ese trabajo en el tiempo.

#### Los dos pases del cronograma

1. **Primera vez:** sin retrasos, sin adelantos, sin dependencias finas, **recursos ilimitados**. Muestra la duración «en bruto».
2. **Segunda vez:** con retrasos, adelantos, dependencias y **recursos limitados**. Esta es la agenda defendible.

**Definición. Adelanto (*lead*).** Solapamiento **permitido**: la actividad sucesora puede empezar **antes** de que termine la predecesora. Ejemplo: empezar a diseñar el tablero cuando el modelo de datos ya está acordado, aunque la carga de kits aún no termine.

**Definición. Retraso (*lag*).** Espera **impuesta** entre el fin de una actividad y el inicio de otra, aunque no haya trabajo en medio. Ejemplo: tres días de espera después de pedir acceso a un servidor hasta que el proveedor lo habilita.

Lead adelanta el inicio; lag lo posterga. Ninguno cambia la duración de la actividad misma: cambian la **relación** entre dos actividades.

#### Insumos típicos

Lista de actividades, EDT, diagrama de red, calendarios de recursos, estimaciones de duración, enunciado del alcance y **OPA** (plantillas, lecciones, calendarios de la empresa).

Se puede esbozar en papel. Un **software de gestión de proyectos** facilita crear, actualizar y **compartir** el cronograma con el equipo.

#### Tres representaciones, tres audiencias

| Formato | Definición | Audiencia |
|---|---|---|
| **Cronograma de hitos** | Pocos eventos de control | Dirección / patrocinadores |
| **Diagrama de Gantt** | Barras de tiempo: tareas, duraciones, solapes, responsables | Equipo y director/a |
| **Diagrama de red** | Nodos y dependencias; permite ver caminos y ruta crítica | Planificación técnica |

Un Gantt de 80 barras no sirve para un inversor. Cuatro hitos no le dicen al equipo qué hacer el martes.

#### CPM — Método de la ruta crítica

**Definición. CPM (*Critical Path Method*).** Técnica que estima la **duración mínima** del proyecto calculando, para cada actividad, inicios y fines **tempranos** y **tardíos**. En el cálculo clásico **no** se limitan recursos: se asume que hay gente y materiales cuando se necesitan.

Sirve para responder: si cada actividad dura lo estimado y se respeta el orden, ¿cuál es la fecha de término más temprana posible? No responde, por sí solo, si el equipo de dos personas puede hacer tres actividades en paralelo.

**Definición. Ruta crítica.** Secuencia de actividades que forma el **camino más largo** (mayor suma de duraciones) desde el inicio hasta el fin. Cualquier atraso en ella mueve la fecha final, salvo que se comprima el cronograma (más recursos, recorte de alcance, o paralelismo nuevo).

No es «la más importante por fama» ni «la más difícil». Es la más **larga**. En Kiran: si se atrasa la carga de inventario, se atrasan el tablero y el reporte a donantes, porque dependen de esos datos.

**Definición. Holgura (*float* / *slack*).** Tiempo que una actividad puede atrasarse **sin** afectar la fecha de término del proyecto (holgura **total**). Si la holgura es **0**, la actividad está en la ruta crítica.

Holgura no es «tiempo libre del equipo». Es margen **respecto de la fecha final**. Si A tiene holgura 13 y se atrasa 14 días, A pasa a ser crítica y el proyecto se alarga.

- **Forward pass (hacia adelante):** inicios y fines tempranos; duración mínima / camino crítico.
- **Backward pass (hacia atrás):** inicios y fines tardíos; holguras.

#### Lectura del nodo

```
┌─────────────────┬──────────┬─────────────────┐
│ Inicio temprano │ Duración │  Fin temprano   │
├─────────────────┴──────────┴─────────────────┤
│              ACTIVIDAD (nombre)              │
├─────────────────┬──────────┬─────────────────┤
│ Inicio tardío   │ Holgura  │   Fin tardío    │
└─────────────────┴──────────┴─────────────────┘
```

Fórmulas (convención de días calendario; la duración «ocupa» días inclusive):

- **Fin temprano (EF)** = (Inicio temprano + Duración) − 1
- **Inicio tardío (LS)** = (Fin tardío − Duración) + 1
- **Holgura** = Fin tardío − Fin temprano  
  (equivalente: Inicio tardío − Inicio temprano)

#### Ejemplo resuelto (actividades A–G)

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

La ruta crítica no es «la más importante por fama»; es la **más larga**. En el ejemplo, B–D–E–G suma 26; las otras rutas son más cortas y por eso tienen holgura.

#### PERT — tres valores

**Definición. PERT (*Program Evaluation and Review Technique*).** Método de estimación de duración que usa **tres valores** cuando no hay un único número fiable: optimista (O), más probable (M) y pesimista (P).

CPM trabaja con **una** duración por actividad (determinista). PERT trabaja con **incertidumbre**: admite que el mismo trabajo puede salir rápido, normal o lento. No reemplaza al CPM: alimenta duraciones más realistas **para** luego calcular la red.

- **O** = optimista: si todo sale bien, el menor tiempo razonable.  
- **M** = más probable: el tiempo que el experto espera en condiciones normales.  
- **P** = pesimista: si aparecen problemas creíbles, el mayor tiempo razonable (no un desastre absurdo).

Fórmulas:

- Duración esperada = **(O + 4M + P) / 6**  
- Desviación estándar = **(P − O) / 6**

El 4 en el numerador da más peso a M: se asume que lo más probable ocurre con más frecuencia que los extremos.

Ejemplo de clase: O = 4, M = 7, P = 16  

- Duración = (4 + 4×7 + 16) / 6 = **8 días**  
- Desviación = (16 − 4) / 6 = **2 días**

En Kiran, una actividad de carga en terreno puede ser O = 5, M = 7, P = 13 → (5 + 28 + 13) / 6 = **7,67 ≈ 8 días**. Usar solo 5 días sería planificar el caso optimista como si fuera el esperado.

### 2.4 Costos

**Definición. Presupuesto.** Suma **autorizada** para ejecutar el proyecto o un componente, construida a partir de los costos identificados **por fase** o por paquete de trabajo.

No es «lo que creemos que va a costar» (eso es una **estimación**). La estimación es un cálculo. El presupuesto es esa estimación **aprobada**, con techo. Sin aprobación (paso 6 más abajo), el número no existe para la organización.

**Definición. Reserva de contingencia.** Monto (o tiempo) reservado para riesgos **ya identificados**. Ejemplo: «si falla la conectividad, hay X días y Y dinero para carga por lotes».

No es la reserva de **gestión** (esa cubre riesgos no identificados y la usa la dirección). Sin contingencia, el primer imprevisto conocido deja el plan en cero. Error frecuente: llamar «contingencia» a un recargo del 20% sin nombrar ningún riesgo.

#### Cómo hacer un presupuesto (8 pasos)

1. Definir la EDT.  
2. Especificar detalles de las tareas.  
3. Introducir valores de costos.  
4. Obtener costos totales.  
5. Incluir **contingencias y costos extra**.  
6. Obtener la **aprobación**.  
7. Hacer seguimiento.  
8. Sacar conclusiones.

Sin el paso 1, el presupuesto es un número sin base. Sin el paso 6, el número no existe para la organización.

#### Principales tipos de costo

| Tipo | Definición | Ejemplo (Kiran) |
|---|---|---|
| **Variable** | Cambia con el volumen de trabajo o de unidades | Horas extra de un consultor; más kits = más filas que cargar |
| **Fijo** | No cambia con el volumen (en el rango del piloto) | Sueldo mensual de la *product owner* |
| **Directo** | Se atribuye **a este** proyecto | Servidor del piloto; viaje para presentar el plan |
| **Indirecto** | Beneficia a varios proyectos; hay que prorratearlo | Luz, contabilidad, PMO |
| **De oportunidad** | Valor de la mejor alternativa no elegida | El mismo equipo podría haber desarrollado otro producto |
| **Hundido / enterrado** | Ya se gastó; **no debe** decidir si continuar | Estudio previo de terreno ya pagado |

**Falacia del costo hundido:** «ya gastamos tanto, hay que seguir». La decisión se toma con costos **futuros** y valor **futuro**.

### 2.5 Recursos

**Definición. Estimar los recursos de las actividades.** Identificar **tipo, cantidad y características** de los recursos necesarios para completar cada actividad. Con eso se estiman costo y duración con más precisión.

«Tipo» es la clase (desarrolladora frontend, servidor, vehículo). «Cantidad» es cuántos y por cuánto tiempo. «Características» es el perfil (¿alguien que ya conoce el dominio, o un perfil junior?). Sin este paso, el cronograma asume recursos ilimitados: el primer pase de CPM.

**Definición. RBS (*Resource Breakdown Structure*).** Desglose **jerárquico** de **todos** los recursos (humanos y materiales), por categoría y tipo, con **cantidad** y **disponibilidad**.

No es un organigrama (quién reporta a quién) ni la EDT (qué trabajo hay). Es *con qué* se hace el trabajo. Se arma en **dos tiempos**:

1. Primero el **tipo** (¿qué clases de recurso hay?).
2. Después la **cantidad** (¿cuántos de cada uno?, y se suman hacia arriba).

Ejemplo (curso PMP): 9 personas + 10 materiales = **19** recursos en total. Personas se parten en edición (4), ventas (2) y técnicos (3). Materiales, en tecnología (8) e instalaciones (2). El asterisco del software significa «se usa, pero no se cuenta como unidad física».

**Traducción a Kiran (mínimo)**

| Categoría | Ejemplos | Pregunta de cantidad |
|---|---|---|
| Personas | Front, back, QA, diseño, impacto, soporte local, *product owner* | ¿Cuántas horas / cabezas por paquete? |
| Tecnología | Nube, repositorio, herramienta de tickets, dispositivos de terreno | ¿Un ambiente o tres? ¿Licencias? |
| Instalaciones | Espacio de la empresa social; punto de apoyo en la comunidad | ¿Visitas a terreno cuántas? |
| Financieros | Aporte de inversores, subsidio, reserva de contingencia | ¿Cuánto queda después de la reserva? |

Sin cantidad, el RBS no se puede costear ni permite ver si hay personas de más o de menos. Esa información alimenta el **segundo pase** del cronograma, con recursos **limitados**.

### 2.6 Para recordar

> Un plan preliminar no es un cronograma suelto. Es **acta** (autorización) + **enunciado de alcance** (qué / qué no, criterios, exclusiones, supuestos, restricciones) + **EDT con diccionario** (el 100% del trabajo) + **modelo de programación** (red, CPM/PERT, Gantt, hitos) + **recursos y costos clasificados**, con contingencia y aprobación. La ruta crítica es el camino más largo; PERT pondera incertidumbre; los costos hundidos no deciden el futuro.

Para pensar:

1. ¿Qué elementos son más importantes al planificar un proyecto de software?  
2. ¿Cómo asegurar precisión en la estimación de recursos?  
3. ¿Qué desafíos aparecen al crear el cronograma y cómo resolverlos?  
4. ¿Qué tan claro quedó el alcance?  
5. ¿Se identificaron todos los recursos?  
6. ¿El cronograma es realista?  
7. ¿Se consideraron los costos más relevantes?

---

## 3. Factores ambientales y estándares

### 3.1 EEF y OPA

**Definición. Factores ambientales de la empresa (EEF, *Enterprise Environmental Factors*).** Condiciones que **el equipo no controla** y que influyen, restringen o dirigen el proyecto. Pueden ser **internos** (cultura, infraestructura, software de la empresa) o **externos** (ley, mercado, clima, estándares de industria). Son **entrada** de muchos procesos, sobre todo de planificación. Pueden **ampliar o recortar** opciones, e influir de forma **positiva o negativa**.

No se eligen: se **identifican** y se planifica **dentro** de ellos. El equipo no decide si hay conectividad irregular en la comunidad; sí decide si el inventario permite carga por lotes. No equivalen al «clima laboral» en sentido coloquial: son el conjunto de condiciones en las que el proyecto opera.

Error frecuente: listar EEF («hay ley de datos», «hay donantes») sin decir **qué cambia en el plan** (roles de acceso, hitos de reporte). La lista sola no demuestra análisis.

#### EEF internos

- cultura, estructura y gobernanza de la organización
- distribución geográfica de instalaciones y recursos
- infraestructura
- software informático
- disponibilidad de recursos
- capacidad de los empleados

#### EEF externos

- condiciones de mercado
- influencias sociales y culturales
- restricciones legales
- bases de datos comerciales
- investigaciones académicas
- estándares gubernamentales o de la industria
- consideraciones financieras
- elementos ambientales físicos

**Definición. OPA (*Organizational Process Assets*).** Planes, procesos, políticas, procedimientos y bases de conocimiento de la organización ejecutora, que el equipo **sí puede usar**: plantillas de acta, lecciones de proyectos anteriores, repositorios, calendarios oficiales.

Diferencia con EEF: el EEF **restringe o dirige** y no se modifica en este proyecto (la ley de privacidad, la cultura de la empresa). El OPA **se aprovecha** y a veces se actualiza al cierre (se guarda una lección aprendida). Una plantilla de enunciado de alcance es OPA. Una ley de protección de datos es EEF.

#### Tres focos: organización, regulación y tecnología

1. Entorno organizacional  
2. Regulaciones gubernamentales  
3. Avances tecnológicos y estándares de la industria  

### 3.2 Entorno organizacional

**Definición. Entorno organizacional.** Conjunto de cultura, valores, estructura y políticas **internas** en el que se ejecuta el proyecto. Forma parte de los EEF internos. Puede facilitar la integración (información fluye, hay PMO) o bloquearla (nadie aprueba cambios, cada área trabaja aislada).

- **Cultura:** normas no escritas de cómo se trabaja. Colaboración y comunicación abierta impulsan el plan; ocultar malas noticias lo frena (los riesgos llegan tarde).
- **Estructura:** define roles, responsabilidades y flujo de información (funcional, matricial o proyectizada). Determina cuánta autoridad real tiene la directora del proyecto. En una estructura funcional, el equipo «pertenece» a jefaturas de área; la directora negocia recursos. En una proyectizada, el equipo reporta al proyecto.
- **Políticas y procedimientos:** reglas internas escritas: quién aprueba un gasto, cómo se pide un ambiente en la nube.

**Ejemplo (Kiran).** Empresa social + inversores de impacto + subsidio + *partner* tecnológico. Hay rendición de cuentas a donantes. Un plan que ignore esa gobernanza (sin hitos de reporte, sin roles de acceso) no se puede integrar: la organización no lo puede usar. El análisis del entorno sirve para **alinear** el plan con esas reglas, no para ignorarlas.

### 3.3 Regulaciones gubernamentales

**Definición. Regulaciones gubernamentales.** Marco legal y normativo **externo** (EEF) que el proyecto debe cumplir. Incluye, entre otros, privacidad de datos, seguridad y conformidad sectorial.

Cumplir no es solo evitar sanciones: es condición de **confianza** de usuarios y financiadores. Las regulaciones no son un anexo al final del plan: si el piloto guarda datos de hogares, el enunciado de alcance y la EDT deben incluir el trabajo de roles, minimización y resguardo. Abordadas de forma temprana, orientan una operación íntegra y pueden ser ventaja competitiva (el financiador elige quien demuestra control). Tres focos: cumplimiento legal, privacidad de datos, seguridad y conformidad.

#### ISO/IEC 27701

**Definición. ISO/IEC 27701.** Extensión de **gestión de información de privacidad** sobre las normas de seguridad de la información (familia ISO/IEC 27000). Permite demostrar un sistema de gestión de información personal (PIMS, *Privacy Information Management System*).

No es una ley. Es un **estándar** voluntario que ayuda a **demostrar** prácticas. Tampoco reemplaza la ley local: si Chile o un donante europeo exigen algo, eso sigue siendo EEF legal. La norma sirve para organizar controles (qué datos, con qué fin, quién accede) de forma auditable.

Aportes que conviene poder explicar:

- se integra con las normas principales de seguridad de la información
- demuestra un nivel alto de protección de datos
- genera confianza en la gestión de información personal
- apoya el cumplimiento de leyes, reglamentos y requisitos de privacidad
- es flexible a particularidades jurisdiccionales (Chile ≠ India ≠ un donante europeo)
- aporta transparencia entre interesados (confianza y respeto mutuo)
- facilita acuerdos comerciales cuando los procesos de sistemas están alineados

**Aplicación a Kiran:** el piloto trata datos de hogares, con posibles financiadores internacionales. El plan declara **qué datos** se guardan, **dónde** (nube), **quién** accede (soporte local) y **qué** sale hacia donantes. Privacidad y reportes a terceros son EEF legales: minimización de datos y roles de acceso. No hace falta inventar leyes que el caso no nombra.

### 3.4 Avances tecnológicos

Cada avance es oportunidad o restricción (EEF tecnológico):

- **Inteligencia artificial:** puede apoyar la detección de kits anómalos; exige cuidado con sesgos y con datos de población vulnerable.
- **Computación en la nube:** escala y acceso; implica dependencia de conectividad y costos variables.
- **Tecnologías emergentes:** obligan a adaptar el plan.

El entorno no se espera de forma pasiva: se analiza y se arma un plan B.

### 3.5 Estándares de la industria

**Definición. Estándar.** Documento establecido por **consenso** de un organismo reconocido, que provee reglas, pautas o características para uso común y repetido.

No es una ley (la ley obliga; el estándar se adopta). No es «la forma única» de dirigir el proyecto: se **elige el que responde la pregunta**. PMBOK responde cómo dirigir **este** proyecto; CMMI, qué tan maduros son los **procesos de la organización**; ITIL, cómo operar el **servicio** cuando ya está en marcha; COBIT, quién **gobierna** TI. Usar los cuatro a la vez, sin criterio, diluye el plan.

#### PMBOK 6.ª

**Definición. PMBOK 6.ª (*A Guide to the Project Management Body of Knowledge*).** Guía de fundamentos para la **dirección de proyectos**. En la 6.ª edición se organiza en **cinco grupos de procesos** (inicio, planificación, ejecución, monitoreo y control, cierre) y **diez áreas de conocimiento** (integración, alcance, cronograma, costos, calidad, recursos, comunicaciones, riesgos, adquisiciones, interesados).

No es una metodología prescrita paso a paso ni una certificación de la organización. Es un **cuerpo de conocimiento**: describe procesos, entradas, herramientas y salidas. Integrarlo implica un enfoque metódico (alcance-tiempo-costo coherentes, interesados identificados) alineado a objetivos de la organización. Puntos clave en esta unidad: integración (que las piezas del plan no se contradigan) y gestión de alcance, tiempo y costos.

#### CMMI (*Capability Maturity Model Integration*)

**Definición. CMMI (*Capability Maturity Model Integration*).** Modelo para **evaluar y mejorar la madurez de los procesos** de una organización. No pregunta solo si *este* proyecto salió bien: pregunta qué tan **sistemática** es la forma de trabajar (si el resultado depende de personas concretas o de procesos repetibles).

No dirige el cronograma de un piloto. Un equipo puede tener un Gantt impecable (PMBOK) y aun así estar en nivel 1 de CMMI si cada vez se improvisa el proceso. Puntos clave: madurez de procesos, mejora continua, calidad y eficiencia.

**Niveles clásicos de CMMI-DEV** (para entender «madurez»):

| Nivel | Idea |
|---|---|
| 1. Inicial | El resultado depende de individuos, no de procesos repetibles |
| 2. Gestionado | El proyecto se planifica y se controla |
| 3. Definido | Los procesos están estandarizados en la organización |
| 4. Gestionado cuantitativamente | Se miden y se controlan con datos |
| 5. En optimización | Mejora continua basada en medición |

CMMI mira **la organización**, no solo el Gantt de un proyecto.

#### COBIT e ITIL (comparativa)

**Definición. COBIT.** Marco de **gobierno y control de TI**: quién decide sobre la información y la tecnología, cómo se controla y cómo se rinde cuentas ante el negocio.

No es una guía para armar la EDT. Entra cuando hay que responder a dirección o inversores: ¿quién autoriza accesos?, ¿cómo se traza un dato de hogar hasta el reporte?

**Definición. ITIL 4.** Conjunto de prácticas para la **gestión de servicios** en operación: incidentes, problemas, cambios, niveles de servicio, mejora continua. No está pensado como guía de *proyectos*, sino de *servicio cuando ya está en uso*.

El módulo de tickets de Kiran, una vez en producción, se parece más a gestión de incidentes (ITIL) que a un paquete de la EDT. El **proyecto** construye ese módulo (PMBOK); la **operación** lo usa (ITIL).

Comparativa (sí = cubre; no = no es su foco; NA = no aplica):

| Característica (clase) | PMBOK | CMMI | COBIT | ITIL |
|---|---|---|---|---|
| Operación del **servicio** | No | Sí | Sí | Sí |
| Enfoque a **proyectos** | Sí | Sí | Sí | NA |
| Gestión de **procesos** | Sí | Sí | Sí | Sí |
| Enfoque a **desarrollo** | Sí | Sí | Sí | NA |
| Enfoque a **infraestructura** | No | NA | NA | Sí |
| Ciclo de **producto** | Sí | Sí | Sí | Sí |
| Gestión del **cambio** | Sí | Sí | Sí | Sí |
| Gestión de **incidencias** | NA | Sí | Sí | Sí |
| **Métricas** de proceso | NA | Sí | Sí | Sí |
| Operativa concreta de procesos | No | No | NA | Sí |
| Seguimiento de actividades | Sí | Sí | Sí | Sí |
| **Mejora continua** como objetivo | Sí | Sí | Sí | Sí |
| Certifica por sí solo a la **organización** | NA | NA | NA | NA |
| Compatible ISO 9001 e ISO 20000 | Sí | Sí | Sí | Sí |

Para recordar: ITIL no es guía de proyectos; PMBOK no es fuerte en operación de servicio ni en infraestructura; la operativa detallada de procesos la cubre ITIL; ninguno de los cuatro certifica a la organización por el solo hecho de usarlo.

**Uso en Kiran:**

- **PMBOK:** planificar el piloto (alcance, tiempo, costo, interesados).
- **CMMI:** no depender de que una persona «se acuerde» de cargar el Excel.
- **ITIL:** cuando el piloto pase a operación (tickets, incidentes, cambios). Conecta con la transición a operaciones.
- **COBIT:** gobierno de TI si los inversores piden trazabilidad de la información.

No se usa **un** estándar para todo. Se **elige el lente** según la pregunta.

### 3.6 Ejemplo: factores en Kiran

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

### 3.7 Para recordar

> Los EEF son condiciones **fuera del control del equipo** que entran a la planificación. Se clasifican en internos y externos. Los OPA sí se usan. PMBOK dirige **el proyecto**; CMMI madura **procesos**; ITIL opera **el servicio**; COBIT gobierna **TI**. En un caso real hay que enunciar el **impacto**, no la lista. Privacidad y seguridad son requisito de confianza, no un anexo.

Para pensar:

1. ¿Qué factores ambientales influyen más en proyectos de software?  
2. ¿Cómo asegurar cumplimiento de estándares en *este* proyecto?  
3. ¿Qué desafíos aparecen al analizar factores y cómo resolverlos?

---

## 4. Estrategias de planificación

Un proyecto de software sin **estrategia de planificación** tiene trabajo, pero no tiene criterio para decidir *cómo* se planifica: qué se detalla al inicio, qué se deja para iterar y con qué herramientas se sostiene eso. Predictivo y adaptativo no son «el bueno y el malo»: son enfoques distintos, adecuados a **distintos grados de certeza** sobre requisitos y entorno.

### 4.1 Por qué planificar (también en ágil)

| Aporte | Qué significa |
|---|---|
| Fundamento del éxito | Reduce la improvisación en lo que ya se puede anticipar |
| Visión clara | Objetivos y expectativas compartidos |
| Gestión de riesgos | Problemas visibles **antes** de producción |
| Optimización de recursos | Evita sobrecarga de personas, plazo y presupuesto |

**Definición. Enfoque adaptativo (en relación con el plan).** Ágil **no** es «no planificar». Es planificar en **ciclos cortos** y volver a planificar cuando cambia el contexto. El plan de alto nivel existe; el detalle se completa en cada ciclo.

Error frecuente: citar «somos ágiles» para no escribir exclusiones, techo de costo ni hitos de financiamiento. Eso no es adaptativo: es ausencia de plan.

### 4.2 Enfoque predictivo

**Definición. Enfoque predictivo.** Forma de desarrollar el proyecto **secuencial y estructurada**: una fase se completa (o se controla) antes de avanzar de lleno a la siguiente. La familia clásica «cascada» pertenece aquí. Alcance, tiempo y costo se **detallan de forma temprana**; los cambios pasan por un control **formal**.

Se usa cuando los requisitos se pueden conocer con suficiente certeza al inicio y el entorno es relativamente estable. Cada fase tiene entradas y salidas definidas; el progreso se verifica por hitos.

**No es** «lo antiguo» ni «lo burocrático» por sí mismo. Es el enfoque correcto cuando un cambio tardío cuesta caro (datos maestros, privacidad, formato de reporte a un donante que ya firmó).

**Características:** claridad de requisitos al inicio; estructura y control por fases; minimización de cambios; entorno relativamente estable.

**Beneficios:** predecible y confiable; fácil de supervisar por hitos.  
**Desventajas:** rígido; un cambio tardío es costoso.

**Ejemplo típico:** sistema de contabilidad para una gran corporación, requisitos claros y estrictos, cronograma detallado, pocos cambios inesperados.

**En Kiran aplica así:** inventario de kits (estados finitos), estructura de reporte a donantes, cumplimiento de privacidad. Eso no debe redefinirse cada *sprint* como si fuera una red social.

Herramientas asociadas: **Microsoft Project**, diagramas de Gantt, Project Libre.

### 4.3 Enfoque adaptativo

**Definición. Enfoque adaptativo.** Forma de desarrollar el proyecto **iterativa e incremental**: se entrega un incremento usable, se recoge retroalimentación y se ajustan requisitos y solución. Hay un plan de **alto nivel** al inicio y **replanificación frecuente**.

Se usa cuando el entorno o los requisitos **no** se pueden fijar con certeza (interfaz que el técnico debe validar, flujo de tickets que se conoce al usarlo). El cambio no es una excepción: es un insumo del siguiente ciclo.

**No es** ausencia de alcance ni de techo de costo. El enunciado sigue existiendo; lo que cambia es **cuánto detalle** se congela al día uno.

**Características:** flexibilidad ante cambios de requisitos o entorno; ciclos con revisión; colaboración continua con interesados.

**Beneficios:** las entregas se acercan a lo que el interesado **ahora** necesita; sirve en entornos volátiles.  
**Desventajas:** si no se gestiona el *backlog*, aparecen **desvíos de tiempo y recursos** («siempre una cosa más»: *scope creep* con otro nombre).

**Ejemplo típico:** plataforma de **redes sociales** en un mercado que cambia rápido; iteraciones cortas y *feedback* constante.

**En Kiran aplica así:** diseño de la interfaz del tablero para uso en terreno, qué campos de un ticket son útiles para el técnico local, cómo medir impacto sin un indicador que se vea bien y no informe nada.

Herramientas asociadas: **Jira** (*sprints* y Kanban), **Trello**, **Asana**.

#### Scrum

**Definición. Scrum.** Marco **adaptativo** con roles, eventos y artefactos definidos para entregar **incrementos de valor** en ciclos cortos (*sprints*). Es un marco de trabajo, no una metodología que cubra toda la dirección de proyectos (no reemplaza acta, presupuesto ni EEF).

| Pieza | Definición |
|---|---|
| *Product Owner* | Responsable de maximizar el valor del producto; ordena el *backlog* |
| *Scrum Master* | Cuida que se siga el proceso; identifica y ayuda a quitar impedimentos |
| *Developers* | Quienes construyen el incremento en el *sprint* |
| *Product backlog* | Lista viva y priorizada de trabajo pendiente sobre el producto |
| *Sprint* | Ciclo de duración fija (suele ser 1–4 semanas) con plan, ejecución y entrega |
| Incremento | Resultado **usable** al final del ciclo, que suma al producto |
| Daily / Review / Retro | Eventos para inspeccionar el trabajo y adaptar el plan o el proceso |

No hace falta montar Scrum «de libro» en un equipo de cuatro. Sí el **criterio**: entregar algo usable, inspeccionar con interesados, ajustar el siguiente ciclo.

#### Cuándo usar cada uno

| | Predictivo | Adaptativo |
|---|---|---|
| Ventajas | Claridad, control, previsibilidad | Flexibilidad, adaptación, innovación |
| Desventajas | Rigidez frente al cambio | Desvío de plazo y recursos si no se cuida |
| Terreno de uso | Requisitos estables y claros | Entorno incerto o requisitos que se descubren al usar |

El híbrido aparece **después**, en las estrategias: no es un cuarto enfoque suelto, es la decisión de combinar los dos según el contexto.

### 4.4 Enfoque híbrido

**Definición. Hibridación (enfoque híbrido).** Combinar de forma **deliberada** elementos predictivos y adaptativos según el **contexto** del mismo proyecto. Se detalla y se controla de forma formal lo que exige certeza (cumplimiento, datos maestros, hitos de financiamiento) y se itera lo que exige aprendizaje (interfaz, flujo de uso).

**No es** «un poco de cada uno sin criterio» ni un tercer enfoque independiente. Es una **decisión**: qué partes del trabajo se planifican con CPM e hitos, y qué partes entran a un *backlog* por ciclo.

Las mejores estrategias **no son fijas de una vez**: se revisan si el contexto cambia.

1. **Análisis del contexto** — ¿el entorno y los requisitos son estables o volátiles?  
2. **Hibridación** — predictivo donde hay certeza; adaptativo donde hay aprendizaje.  
3. **Participación de interesados** — sin revisión con quien usa o financia, el ajuste no tiene rumbo.  
4. **Evaluación continua** — el plan se actualiza con control de cambios o con replanificación de ciclo; no se deja inmóvil si la evidencia lo contradice.

**En Kiran, un híbrido defendible:**

```
CAPA PREDICTIVA (cumplimiento y datos maestros)
  Inventario · estados del kit · roles y privacidad · calendario de reportes a donantes

CAPA ADAPTATIVA (aprendizaje de terreno)
  UX del tablero · flujo de tickets · indicadores de impacto · soporte local
```

Eso es un plan **contextualizado**: no «somos ágiles» ni «somos cascada».

### 4.5 Herramientas según enfoque

| Enfoque | Herramientas | Uso en Kiran |
|---|---|---|
| Predictivo | MS Project, Gantt | Ruta crítica del piloto, hitos de subsidio |
| Adaptativo | Jira, Trello, Asana | *Backlog* del tablero y de tickets |
| Híbrido | Una de cada, o Project Libre + Kanban | Gantt de hitos + Kanban semanal |

La herramienta **sigue** a la estrategia, no al revés.

**Definición. Tailoring (adaptación de la dirección).** Ajustar **cuánto** proceso, documento y rigor se aplica según el tamaño, riesgo y contexto del proyecto. Un piloto de cuatro personas no copia todos los procesos de un programa corporativo; tampoco se queda en cero. El criterio es: lo suficiente para gobernar, no el máximo de plantillas.

### 4.6 Para recordar

> Planificar es el soporte de la ejecución, también en ágil. **Predictivo** = requisitos estables, control por fases, Gantt/Project. **Adaptativo** = iteración, interesados cerca, Jira/Kanban. **Híbrido** = se detalla lo regulado y se itera lo que se aprende. La estrategia se argumenta con el **contexto de la organización**, no con la moda del equipo.

Para pensar:

1. ¿Cómo integrar predictivo y adaptativo en un solo proyecto?  
2. ¿Qué papel juegan las herramientas tecnológicas?  
3. ¿Cómo asegurar la participación de los interesados?

---

## 5. Selección de herramientas

Elegir herramienta es una **decisión de planificación**, no de marca. Si no cubre el enfoque elegido (ruta crítica, o tablero de flujo, o ambos) o el equipo no puede operarla, el plan queda en un archivo que nadie actualiza. No se trata de reconocer logotipos: se trata de **usar** una y **justificar** por qué es la adecuada para *esta* organización.

**Definición. Selección de herramientas.** Proceso de identificar necesidades, comparar alternativas con criterios medibles, elegir e **implementar** el software (o el análogo) con el que se planifica y se sigue el trabajo.

### 5.1 Cinco pasos para elegir

No se parte por el logo. Se parte por el negocio.

| # | Paso | Pregunta en Kiran |
|---|---|---|
| 1 | Definir las **necesidades del negocio** | ¿Hay que defender hitos a donantes *y* un flujo de tickets en terreno? |
| 2 | Considerar la **facilidad de uso** | ¿El equipo puede operarla esta semana, sin una curva imposible? |
| 3 | Evaluar la **capacidad de integración** | ¿Habla con Trello, Office y el XML de Project Libre, o queda aislada? |
| 4 | Considerar **seguridad y privacidad** | ¿Dónde viven los datos de hogares? ¿Quién tiene cuenta? |
| 5 | Evaluar **costo y retorno** | ¿La licencia de MS Project se come el techo del piloto, o Project Libre alcanza? |

Elegir y **implementar** van juntos: una herramienta que nadie usa no cuenta.

### 5.2 Evaluar: razones claras, objetivas y medibles

Evaluar una herramienta es conectarla con los **objetivos del proyecto**. Si no hay criterio, la elección es gusto.

Criterios habituales:

- facilidad de uso
- costo
- soporte técnico
- capacidad de integración
- personalización

**Comparar** es mirar rendimiento **y** alineación con los objetivos. No «cuál es más famosa».

Conviene mostrar **cómo** se decidió, no solo el nombre final. Más abajo: Project Libre + Trello + Office en Kiran.

Nueve capacidades frecuentes en un software de gestión (no todas hacen falta en un piloto):

1. Crear proyectos  
2. Añadir tareas  
3. Asignar tareas a personas  
4. Ver avance  
5. Calendario de tareas  
6. Asignar recursos  
7. Compartir archivos  
8. Integrarse con otras herramientas  
9. Ser escalable  

Si una candidata no permite ver avance ni asignar recursos, no sirve para la línea base. Si no se integra, rompe el híbrido.

### 5.3 Familias de herramientas

Hay **tres familias**. No hay que usar una de cada una: hay que elegir la que cubre la necesidad del plan (cronograma, visualización de datos ya existentes, o comunicación del equipo).

#### Gestión de proyectos (planificar y seguir el trabajo)

| Herramienta | Para qué sirve | Límite | En Kiran |
|---|---|---|---|
| **Microsoft Project** | Tareas, recursos y cronogramas. Pensada para proyectos grandes y complejos. | Licencia y curva de aprendizaje | Si la organización ya la paga |
| **Project Libre** | Misma familia (Gantt, red, recursos) sin licencia comercial cara. | Menos integraciones y comunidad que MS Project | Línea base del piloto |
| **Asana** | Colaboración y transparencia en equipos chicos/medianos; interfaz simple para tareas. | Poca ruta crítica | Posible Kanban; el equipo ya usa Trello |
| **Trello** | Tableros visuales; organizar y priorizar con flexibilidad. | No calcula CPM | Capa Scrum (backlog y sprint) |
| **Jira** | *Sprints*, Kanban y tickets. | Puede ser exceso para un equipo muy chico | Si el flujo de tickets crece |

En el mercado también aparecen Basecamp y Wrike. Existen; no hace falta elegirlas si no cubren la necesidad o el enfoque del plan.

#### Visualización de datos (entender números)

| Herramienta | Para qué sirve | En un piloto como Kiran |
|---|---|---|
| **Tableau** | Datos complejos → visuales interactivos para decidir | Útil cuando ya hay **operación y datos reales**, no para el plan vacío. |
| **Power BI** | Paneles de Microsoft para monitorear rendimiento | Igual: monitoreo. Una hoja de cálculo alcanza para el plan preliminar. |

Elegir Tableau «porque se ve profesional» sin dato de kits es un output vacío. El valor de Kiran es kit con estado verdadero.

#### Colaboración (hablarse)

Zoom, Microsoft Teams y Slack cubren la **colaboración**. La idea: sin coordinación el proyecto se cae; casi todos los equipos dependen de alguna herramienta para hablarse.

En Kiran, las reuniones cortas caben en Teams. Eso no reemplaza Project Libre ni Trello: son familias distintas (comunicación frente a modelo de programación frente a flujo de trabajo).

### 5.4 Implementar no es instalar y listo

Métodos de implementación:

1. **Capacitar** al equipo (quién abre el XML, quién mueve la tarjeta).  
2. **Adaptar** procesos que ya existen (no inventar un ritual nuevo por cada app).  
3. **Probar en pequeño** (un sprint, un Gantt) antes de declarar la herramienta oficial.

Adopción: incentivos de uso y hábitos de actualización. Una licencia sin reuniones de seguimiento es **costo hundido**.

La clase cierra: implementar bien es **invertir en la capacidad del equipo**, no en el logo.

### 5.5 Ejemplo: cómo se decide en Kiran

Aplicar los cinco pasos:

1. **Negocio:** hitos a donantes (predictivo) + tickets de terreno (adaptativo).  
2. **Facilidad:** equipo pequeño, sin curva de MS Project.  
3. **Integración:** XML de Project Libre + tablero Trello + Word/Excel.  
4. **Privacidad:** no subir bases de hogares a la nube de la herramienta; roles en Kiran (paquete 6.1).  
5. **Costo/retorno:** Project Libre cubre CPM sin licencia; Trello alcanza para el Kanban.

Plantilla para el informe:

> Se elige **Project Libre** para la línea base predictiva (EDT, precedencias, ruta crítica, recursos y costos) porque no hay licencia de MS Project y hay que ver hitos de financiamiento. Se complementa con **Trello** para la capa adaptativa (tablero y tickets), porque el flujo de mantención se descubre en terreno. Una hoja de cálculo queda para el diccionario de la EDT y el presupuesto. Tableau o Power BI se dejan para cuando haya dato real de kits.

### 5.6 Para recordar

> La herramienta óptima es la que la **organización puede usar de verdad** y que cubre el enfoque elegido. Se elige con cinco criterios (negocio, uso, integración, privacidad, costo). Se evalúa con razones medibles. Se implementa con capacitación, adaptación y prueba piloto. En híbrido suele haber **dos** herramientas (línea base + flujo ágil), más el análogo para comunicar. Visualizar datos y colaborar son familias distintas: no se justifica Tableau si el problema era la ruta crítica.

Para pensar:

1. ¿Qué herramientas de planificación son más útiles para *este* proyecto de software?  
2. ¿Cómo asegurar que el equipo las **elija y las use**?  
3. ¿Qué desafíos aparecen al evaluar y seleccionar, y cómo se resuelven?

---

## 6. El plan como sistema

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

Si una pieza falta, el plan no se sostiene:

- sin exclusiones → alcance incompleto  
- sin EDT → cronograma sin base  
- sin ruta crítica → el plazo no tiene criterio técnico  
- sin EEF → plan de laboratorio, no de industria  
- sin enfoque → las herramientas no tienen criterio de selección  
- sin justificación de herramienta → la elección no se puede defender  

---

## 7. Ejemplo aplicado: Kiran

**Contexto.** Una empresa social impulsa un piloto de kits solares en una comunidad sin energía confiable. Financiamiento mixto (inversores de impacto, subsidios, *partners* tecnológicos). **Producto:** **Kiran**.

**Problemas de negocio (no son el software):** falta de acceso a energía, desarrollo económico limitado, dependencia de fósiles.

**Solución de software:** plataforma para registrar kits de una comunidad piloto, monitorear estado, gestionar mantención y generar reportes para la dirección e inversores. El software **no** resuelve por sí solo los problemas de negocio: los hace **operables** en un piloto.

**Funcionalidades pedidas:**

1. Inventario (comunidades, hogares, kits; estados activo / falla / baja).  
2. Tablero operativo (visión general e individual).  
3. Monitoreo y mantención (rendimiento + tickets + soporte local).  
4. Impacto social y ambiental (informes periódicos a inversores y donantes).

### 7.1 Enunciado de alcance

- **Producto:** Kiran, sistema web (con posible apoyo móvil o carga sin conexión) de operación de kits solares del piloto.
- **Criterios de aceptación (ejemplos):** cada kit tiene hogar asociado y estado; un ticket se abre desde un kit en falla; un reporte periódico exportable llega a patrocinadores.
- **Entregables:** módulos 1–4, capacitación breve al soporte local, documento de roles y privacidad, plan preliminar.
- **Exclusiones:** fabricación e instalación de paneles, microfinanzas, expansión a otras regiones, aplicación ciudadana masiva.
- **Restricciones:** presupuesto de piloto, conectividad, equipo de cuatro personas, fecha del primer reporte a donantes.
- **Supuestos:** hay comunidad piloto identificada; hay al menos un técnico local; los inversores aceptan indicadores simples en esta fase.

No se inventan montos de subsidio, leyes locales ni datos de hogares que el caso no entrega.

### 7.2 EDT de primer nivel

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

### 7.3 Lógica de la ruta crítica

Camino largo probable:

**datos maestros (inventario) → tablero que lee esos datos → tickets sobre kits reales → reporte de impacto que usa operación real.**

Si el inventario se atrasa, el resto es una demostración vacía. Es la misma lógica que B–D–E–G en el ejemplo de ruta crítica.

### 7.4 Estrategia híbrida

Predictivo en inventario, privacidad y reportes (2, 6 y 5). Adaptativo en tablero y tickets (3 y 4). La dirección del proyecto (1) usa PMBOK 6 para integrar.

### 7.5 Valor e interesados (PMBOK 7.ª)

Valor = kits observables + fallas atendibles + reportes creíbles.  
No es valor = pantallas si el técnico no las usa o el donante no entiende el indicador.

---

## 8. Glosario

| Término | Definición de estudio |
|---|---|
| **Acta de constitución** | Documento que autoriza formalmente el proyecto, nombra al director o directora y le da autoridad para usar recursos |
| **Actividad** | Trabajo programable (duración, predecesoras, recursos), derivado en general de un paquete de trabajo |
| **Adaptativo** | Enfoque iterativo e incremental: plan de alto nivel y replanificación frecuente; no es ausencia de plan |
| **Adelanto (*lead*)** | La sucesora puede empezar antes de que termine la predecesora (solapamiento permitido) |
| **Alcance del producto** | Características y funciones del resultado (qué es el software o el bien) |
| **Alcance del proyecto** | Todo el trabajo para entregar ese producto, incluida la gestión |
| **Caso de negocio** | Justificación de la inversión: necesidad, opciones, costos, beneficios, recomendación |
| **CMMI** | Modelo de madurez de **procesos de la organización**, no de un solo cronograma |
| **COBIT** | Marco de gobierno y control de TI: quién decide y cómo se rinde cuentas |
| **Control de cambios** | Proceso formal para aprobar o rechazar modificaciones a la línea base |
| **Contingencia** | Reserva de dinero o tiempo para riesgos **identificados** |
| **Costo directo / indirecto** | Atribuible a este proyecto / compartido entre varios proyectos |
| **Costo fijo / variable** | Independiente / dependiente del volumen (dentro de un rango) |
| **Costo hundido** | Ya gastado; no debe decidir si continuar |
| **Costo de oportunidad** | Valor de la mejor alternativa no elegida |
| **CPM** | Método que calcula la duración mínima y el camino más largo (ruta crítica), sin limitar recursos en el cálculo clásico |
| **Criterios de aceptación** | Condiciones verificables para dar por bueno un entregable |
| **Cronograma** | Modelo de fechas planificadas e hitos, no solo un dibujo de barras |
| **Cuenta de control** | Punto de la EDT donde se miden juntos alcance, plazo y costo |
| **Descomposición** | Dividir el trabajo en partes más pequeñas hasta poder estimar y asignar |
| **Diagrama de red** | Representación de dependencias entre actividades; base del CPM |
| **Diccionario de la EDT** | Ficha de cada componente: criterio, recursos, costo, hitos, responsable |
| **EDT / WBS** | Descomposición jerárquica del 100% del trabajo acordado; lo que no está, no se hace |
| **EEF** | Condición que el equipo no controla e influye en el proyecto (interna o externa) |
| **Elaboración progresiva** | Detallar el plan cuando hay más información, **dentro** del alcance acordado |
| **Enunciado del alcance** | Descripción de qué entra, qué no, criterios, supuestos y restricciones |
| **Entregable** | Resultado verificable de un proceso, una fase o el proyecto |
| **Exclusión** | Trabajo que explícitamente no se hará |
| **Gantt** | Barras de tiempo para el equipo; una representación del modelo, no el modelo entero |
| **Gobernanza** | Marco de autoridad y decisión (de toda la organización o de este proyecto) |
| **Grupos de procesos (PMBOK 6)** | Inicio, planificación, ejecución, monitoreo y control, cierre |
| **Híbrido** | Combinación **deliberada** de predictivo y adaptativo según el contexto |
| **Hito** | Evento significativo de duración cero |
| **Holgura** | Tiempo que una actividad puede atrasarse sin mover la fecha de término |
| **Hundido** | Costo ya incurrido (ver costo hundido) |
| **Interesado** | Quien afecta, es afectado o se percibe afectado por el proyecto |
| **ISO/IEC 27701** | Estándar de gestión de privacidad, extensión de la familia ISO 27000; no es una ley |
| **ITIL** | Prácticas de gestión de **servicio en operación**, no de dirección de proyectos |
| **OPA** | Activos internos que el equipo sí usa: plantillas, lecciones, repositorios |
| **Outcome / output** | Efecto en el uso / producto observable del trabajo |
| **Paquete de planificación** | Trabajo conocido sin actividades aún detalladas |
| **Paquete de trabajo** | Nivel más bajo de la EDT: estimable, asignable, con duración y costo |
| **PERT** | Duración esperada (O + 4M + P) / 6; desviación (P − O) / 6; para incertidumbre |
| **PMBOK 6.ª** | Guía de fundamentos para dirigir **el proyecto** (procesos y áreas de conocimiento) |
| **Predictivo** | Plan detallado al inicio; fases secuenciales; cambios con control formal |
| **Presupuesto** | Suma **autorizada** para ejecutar el trabajo (la estimación aprobada) |
| **Proyecto** | Esfuerzo temporal para un resultado único; termina; no es operación |
| **RBS** | Desglose de recursos: primero tipo, después cantidad y disponibilidad |
| **Retorno de la inversión (ROI)** | Si el costo de la herramienta (o del proyecto) se justifica con el beneficio |
| **Requisito** | Condición o capacidad verificable que debe cumplirse |
| **Restricción** | Límite obligatorio sobre el trabajo que sí entra (plazo, presupuesto, ley) |
| **Retraso (*lag*)** | Espera impuesta entre el fin de una actividad y el inicio de otra |
| **Ruta crítica** | Camino más largo; determina la fecha de término |
| **Scope creep** | Crecimiento de alcance sin control de cambios ni ajuste de triple restricción |
| **Scrum** | Marco adaptativo de roles, eventos y artefactos para incrementos en ciclos cortos |
| **Supuesto** | Factor dado por cierto para planificar; si falla, hay riesgo |
| **Tailoring** | Ajustar el rigor de la gestión al contexto (no copiar todos los procesos «por si acaso») |
| **Técnica Delphi** | Consenso anónimo de expertos por rondas, para reducir sesgo de autoridad |
| **Triple restricción** | Relación entre alcance, tiempo y costo (calidad transversal) |
| **Valor** | Beneficio real ponderado frente a costo, tiempo y riesgo; no se agota en el entregable |

---

## 9. Autoevaluación

Si una respuesta no sale, volver al apartado.

1. Nombre los seis mínimos del enunciado de alcance.  
2. Diferencie paquete de trabajo, paquete de planificación y cuenta de control.  
3. ¿Qué cubre el diccionario de la EDT que la estructura jerárquica sola no cubre?  
4. En el ejemplo de clase, ¿cuál es la ruta crítica y cuánto dura el proyecto?  
5. Calcule PERT con O = 4, M = 7, P = 16.  
6. Fórmulas de EF, LS y holgura.  
7. Seis tipos de costo, con un ejemplo cada uno.  
8. EEF interno frente a externo: tres de cada lado.  
9. EEF frente a OPA, en una frase.  
10. PMBOK frente a CMMI frente a ITIL: una frase cada uno.  
11. Según la tabla de clase: ¿ITIL se enfoca en proyectos? ¿PMBOK en operación de servicio?  
12. Tres aportes de ISO/IEC 27701.  
13. Predictivo frente a adaptativo: una ventaja y una desventaja de cada uno.  
14. Proponga el híbrido de Kiran en dos capas.  
15. ¿Qué documento autoriza el proyecto?  
16. Output frente a outcome frente a valor, con Kiran.  
17. Nombre cinco tipos de interesado de Kiran.  
18. ¿Por qué no basta con un Gantt si faltan exclusiones o EEF?  
19. Justifique una herramienta para **esta** organización, no en abstracto.  
20. ¿Qué queda **fuera** de Kiran y por qué hay que escribirlo?  
21. En el RBS, ¿qué se hace primero: el tipo o la cantidad?  
22. ¿Cuándo predictivo y cuándo adaptativo?  
23. Nombre los cinco pasos para elegir una herramienta y un criterio de evaluación.

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
18. El plan queda incompleto: el Gantt no reemplaza alcance, EDT ni entorno.  
19. Licencia + audiencia (donantes frente a desarrollo) + enfoque híbrido.  
20. Fabricar e instalar paneles: si no se excluye, el alcance se infla.  
21. Primero el tipo; después la cantidad, que se suma hacia arriba.  
22. Predictivo: requisitos estables. Adaptativo: entorno incerto o innovador.  
23. Negocio, facilidad de uso, integración, privacidad, costo/retorno. Criterio: uso, costo, soporte, integración o personalización.

---

## 10. Referencias

1. Project Management Institute. (2017). *Guía de los fundamentos para la dirección de proyectos (Guía del PMBOK)* (6.ª ed.).  
2. Wysocki, R. K. (2019). *Effective project management: Traditional, agile, extreme, hybrid* (8th ed.). Wiley.  
3. Layton, M. C. (2022). *Scrum for dummies* (3rd ed.). Wiley.  
4. Peters, L. J. (2024). *Software project management: Methods and techniques*. CRC Press.  
5. SCRUMstudy. (2023). *Guía SBOK* (4.ª ed., español).  
6. Baud, J.-L. (2020). *ITIL 4: Entender el enfoque y adoptar las buenas prácticas*. ENI.  
7. PMI. (2021). *Guía del PMBOK* (7.ª ed.) — valor e interesados.

---

## 11. Cierre

Planificar un proyecto de software es producir un plan que la **organización pueda usar**: autorizado (acta), limitado (alcance y exclusiones), descompuesto (EDT), fechado con criterio (ruta crítica), costoso de forma honesta (tipos de costo y contingencia), situado en su entorno (EEF y estándares), con una forma de avanzar (predictivo, adaptativo o híbrido) y con una herramienta justificada. Kiran es ese plan aplicado: no un relato sobre paneles solares.
