# Redimensionamiento presupuestario por C-05 / C-06

**Actividad 2.2.2 — impacto de costo completo.**  
No basta decir “entra sin subir el techo”. Hay que mostrar **de dónde sale la plata**, qué se **reasigna**, qué se **come de contingencia** y cuándo el techo **debe subir**.

Stack de referencia: **Google Cloud + Gemini** (Flash-Lite / Flash) + **datalake** como base de información.  
**Dueños técnicos (GCloud, ADK, datalake):** Nicolás Barra y Ari Araya.

---

## 1. Techo y composición de partida (Eva 1 / acta)

| Concepto | US$ | Nota |
|----------|-----|------|
| Techo autorizado | **20.700** | Incluye contingencia |
| Contingencia 12 % | **1.890** | Riesgos **identificados**; cerrada sin razón escrita |
| Base implícita (techo − contingencia) | **18.810** | Trabajo planificado del piloto |
| Variable (soporte local + hosting) | **1.240** | De eso, hosting ~480; horas soporte local ~760 |
| Hundido (estudio terreno) | 2.800 | **Fuera** del techo; no decide |

Las filas de clasificación (fijo/variable/directo) **no se suman** entre sí; el número que autoriza dirección es el techo.

---

## 2. Qué agrega C-05b + C-06 (costo completo)

### 2.1 Caja nueva (no estaba en el plan inicial como partida)

| Rubro | US$ propuesto | US$ máximo | Tipo |
|-------|---------------|------------|------|
| API Gemini | 60 | 120 | Variable |
| Google Cloud (chat: Run/Hosting, logs) | 60 | 100 | Variable |
| Colchón de sobrecosto IA (riesgo de uso) | 80 | 120 | Reserva nombrada / parte de contingencia |
| **Subtotal caja C-05b** | **200** | **340** | |

### 2.2 Esfuerzo (ya en sueldos, pero **sí** desplaza alcance)

| Rubro | Días-persona | Efecto |
|-------|--------------|--------|
| C-06 UI/cola | 4–7 | Sale otra historia del tablero/sprint |
| C-05b chat + FAQ + integración Gemini | 9–15 | Sale historia de tickets/pulido |
| **Total** | **13–22** | Capacidad no disponible para otro alcance del EDT |

Eso **no es gratis**: o se reduce alcance entregable, o se alarga plazo (aquí el plazo no se mueve → **se corta alcance**), o se paga más gente (rompe techo).

### 2.3 Soporte local (no se puede “borrar” del presupuesto)

En zona compleja el chatbot **no elimina** al técnico 0,4 FTE de inmediato. La hipótesis es **bajar horas**, no dejar la partida en cero. Por eso **no es honesto** financiar Gemini solo quitando todo el bloque de ~US$ 760 de soporte.

---

## 3. Tres escenarios (la actividad debe mostrarlos)

### Escenario A — Absorber sin subir techo (reasignación dura)

| Movimiento | US$ |
|------------|-----|
| Quitar del variable “horas soporte / holgura” | −220 a −340 |
| Crear partidas Gemini + GCloud | +220 a +340 |
| Techo | **20.700** sin cambio |

**Riesgo:** en zona compleja puede faltar soporte humano justo cuando más se necesita. Solo aceptable si la medición (línea base) muestra contención alta **rápido**.

### Escenario B — Usar contingencia con razón escrita (techo nominal igual)

| Movimiento | US$ |
|------------|-----|
| Abrir parte de la contingencia 1.890 para “costo variable Gemini/GCloud del chatbot C-05b” | 200–340 |
| Techo | Sigue **20.700**, pero la reserva disponible baja |

**Riesgo:** se gasta la reserva pensada para alargue de terreno/hosting (prueba 4.4). Hay que **nombrar el riesgo** en Tabla 4 y en el registro.

### Escenario C — Redimensionar el techo (recomendado para credibilidad)

| Concepto | US$ |
|----------|-----|
| Techo anterior | 20.700 |
| Incremento por C-05b (caja + colchón IA) | **+500** |
| **Techo propuesto** | **21.200** |
| Contingencia: mantener ~12 % sobre la nueva base o conservar 1.890 y sumar el +500 a la base | Decisión de dirección |

**Por qué +500 y no solo +220:** incluye tope Gemini (120) + GCloud (100) + colchón (80) + redondeo de integración/secretos/cuotas (~200) para no vender el cambio “al filo”.

Justificación al CC: el alcance nuevo (chatbot FAQ + canal en GCloud/Gemini) **no estaba** en la línea base del acta; la zona compleja exige **mantener** soporte humano y **además** pagar IA/infra; reasignar solo el variable de soporte es arriesgado; por eso se pide **ampliación de techo**, no un “ajuste invisible”.

---

## 4. Decisión propuesta para el documento 2.2.2

| Id | Decisión de costo |
|----|-------------------|
| C-06 | Absorber por **HH** (Escenario A solo esfuerzo). Sin caja nueva material. |
| C-05b | **Escenario C:** solicitar techo **US$ 21.200** (+500), con partidas Gemini + GCloud en Excel. Mientras dirección no apruebe, el registro queda **abierto condicionado** a esa ampliación (o, en alternativa explícita, Escenario B con acta de contingencia). |
| C-05a / fase 3 | Sin presupuesto en esta ventana (agéntico, monitoreo flota, datalake). |

Medición (sigue vigente): línea base de soporte post 9 nov; comparar ahorro vs gasto Gemini/GCloud; si el gasto IA supera el ahorro de forma sostenida → pausar o nuevo CC (aunque el techo ya se haya subido).

---

## 5. CAPEX y OPEX (dimensión para el cliente)

| Concepto | CAPEX / OPEX | Lectura para dirección |
|----------|--------------|------------------------|
| UI/UX C-06 + chat + integración Gemini + FAQ + setup GCloud | **CAPEX** (puesta en marcha en la ventana) | Inversión del cambio; HH del equipo + setup |
| Tokens Gemini + Cloud Run/logs | **OPEX** recurrente | Escala con uso; tope Excel; medible en consola |
| Soporte humano local | **OPEX** recurrente | Se mantiene en zona compleja; el chatbot busca bajarlo |
| Colchón +500 del Escenario C | OPEX / reserva | Evita picos sin techo informal |
| Monitoreo/alertas IA (fase 3) | CAPEX+OPEX futuros | Otro CC |

En cloud casi todo es OPEX contable; igual se separa **puesta en marcha** vs **cuenta mes a mes** para el cliente.

## 6. Mensaje claro (para no contradecir el oral)

> Agregar C-05b **sí implica plata nueva** (Gemini + Google Cloud) y **capacidad de desarrollo redirigida**. Eso no cabe “de gratis” en el plan inicial. O se **reasigna** variable de soporte (A), o se **abre contingencia** con razón (B), o se **redimensiona el techo a US$ 21.200** (C, recomendado). El equipo recomienda C porque la zona compleja no permite vaciar el presupuesto de soporte humano para pagar la IA. Para el cliente: **CAPEX** = dejar el chatbot listo; **OPEX** = Gemini + GCloud + soporte que sigue.
