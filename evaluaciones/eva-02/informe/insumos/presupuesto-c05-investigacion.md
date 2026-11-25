# Investigación de presupuesto — C-05 (chatbot FAQ + canal) y C-06 (UI cola)

**Propósito:** que el control de cambios sea honesto, transparente y creíble.  
**No es cotización firmada** ni precio de un proveedor adjudicado. Son **órdenes de magnitud** con fuente pública o supuesto declarado, para decidir si C-05b cabe en el techo **US$ 20.700** sin abrir la contingencia del **12 % (US$ 1.890)** sin razón escrita.

**Fecha de revisión de precios de API:** octubre 2026 (páginas oficiales OpenAI / Anthropic).

---

## 1. Qué se presupuesta ahora vs después

| Ítem | ¿En sep–dic 2026? | Por qué |
|------|-------------------|---------|
| C-06 cola / UI amigable | Sí (condicionado) | Casi solo HH del equipo |
| C-05 fase 1: FAQ + canal + escalamiento | Sí (condicionado) | API gestionada + HH + poco hosting extra |
| Especialista externo en desarrollo agéntico | **No** | Sale del techo y del foco; fase 3 |
| Fine-tuning / modelo propio / GPU | **No** | Innecesario para FAQ; costo alto |
| Monitoreo + alertas + IA de flota | **No** (solo identificado) | Fase posterior; otro CC y otro sobre |
| Datalake / lakehouse | **No** | Fuera de EDT del piloto |

---

## 2. Stack elegido: Google Cloud + Gemini (fase 1)

Objetivo fase 1: FAQ curado + canal con escalamiento a humano. Stack de referencia del equipo:

| Capa | Elección | Por qué |
|------|----------|---------|
| Nube | **Google Cloud** (Cloud Run o Firebase App Hosting para el módulo de chat; logs/cuotas en la misma cuenta del piloto) | Una factura; Ari ya sostiene nube; sin GPU |
| Modelo | **Gemini Flash-Lite** (primera opción) o **Gemini Flash** si hace falta más calidad | API gestionada; precios públicos; ventana del piloto cae en 2026 |
| No | Vertex “enterprise agent platform” completo, fine-tuning, GPU | Fuera de fase 1 y del techo |

### Precios de referencia Gemini (oct 2026, publicados)

| Modelo | Input / 1M tok | Output / 1M tok | Fuente |
|--------|----------------|-----------------|--------|
| **Gemini 2.5 Flash-Lite** (recomendado FAQ) | ≈ **US$ 0,10** | ≈ **US$ 0,40** | [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) / resúmenes de mercado |
| Gemini Flash (3.x intro hasta 31 dic 2026) | ≈ **US$ 0,75** | ≈ **US$ 3,75** | Mismo sitio / Cloud |
| Modelo propio / fine-tuning | — | — | **Fuera** |

Alternativas (OpenAI mini / Claude Haiku) quedan solo como respaldo de comparación; **la línea base del informe es GCloud + Gemini**.

**Supuesto de tráfico del piloto (declarado):** zona compleja, una comunidad, usuarios de la plataforma (no app masiva).

| Escenario | Conversaciones / día | Meses en ventana (post 9 nov → cierre) | API estimada (modelo mini) |
|-----------|----------------------|----------------------------------------|----------------------------|
| Bajo | 20–50 | 1–1,5 | **US$ 5–25** |
| Base (planificar) | 50–150 | 1–1,5 | **US$ 25–80** |
| Estrés | 300–500 | 1–5 | **US$ 80–200** |

Cálculo orientativo (base): ~1.500 tok input + 400 tok output por consulta × 100 consultas/día × 30 días ≈ costo del orden de **decenas de USD/mes** en modelo mini (no cientos), alineado a estimadores públicos de chatbots de soporte de bajo volumen.

**Tope propuesto en Excel (Ari):** **US$ 120** para toda la ventana (API chatbot), con alerta al **80 %** del tope y pausa si la desviación total de nube/API supera **10 %** del plan (E4).

---

## 3. Infraestructura Google Cloud

Línea base Eva 1 (insumo Ari): hosting piloto ~**US$ 480** / ~3 meses + dominio ~**US$ 120**.

| Ítem | Fase 1 | Monto propuesto | Nota |
|------|--------|-----------------|------|
| App + DB del piloto | = | Ya en techo | Chat como módulo |
| Cloud Run / App Hosting (chat) | + | **US$ 40–80** | Tráfico bajo; free tier posible; sin min-instances caros |
| Logs / cuotas / secretos | + | Incluido en margen | Misma cuenta GCloud |
| GPU / GKE / datalake | No | 0 | Fuera |

**Subtotal GCloud C-05b:** **US$ 60** (punto medio), máximo **US$ 100**.

---

## 4. Horas-hombre (HH) — equipo de cuatro (sin contratar)

El sueldo del equipo **ya está** en el techo como costo directo. Aquí se mide **esfuerzo replanificado** (si entra C-05/C-06, sale otra historia).

| Trabajo | Roles | HH (días-persona) | Equivalente interno* |
|---------|-------|-------------------|----------------------|
| C-06 cola / filtros / UX tablero | Giannina (+ Nicolás si API datos) | 4–7 | Ya en techo |
| C-05b UI chat + flujos escalamiento | Giannina | 2–3 | Ya en techo |
| Integración API + prompts + logs | Nicolás | 4–6 | Ya en techo |
| Corpus FAQ + pruebas calidad | Skarlett (+ apoyo dominio) | 2–4 | Ya en techo |
| Tope gasto, ambiente, secretos | Ari | 1–2 | Ya en techo |
| **Total fase 1 + C-06** | | **13–22 pd** | No suma caja si no se contrata afuera |

\*No se inventa tarifa de mercado chilena/india: el informe dice “horas del equipo ya remuneradas en el techo”, no una línea de consultoría fantasma.

**Especialista externo en desarrollo agéntico**

| Concepto | ¿Fase 1? | Orden de magnitud (referencia industria) | Decisión |
|----------|----------|------------------------------------------|----------|
| Consultor / eng. agéntico part-time | No | Suele cotizarse en **miles USD** por sprint o retainer; supera holgura del piloto | **Fuera**. El equipo (Nicolás + Skarlett) cubre FAQ+canal. |
| Capacitación corta (opcional) | Solo si sobra cupo | Taller 4–8 h (monto a cotizar; no comprometido) | No en línea base C-05b |

---

## 5. Resumen para el control de cambios (caja nueva vs replanificación)

### A. Costo incremental de **caja** (variable, dentro del techo)

| Rubro | Tipo | Propuesta US$ | Máximo US$ | Dueño |
|-------|------|---------------|------------|-------|
| API **Gemini** (Flash-Lite/Flash) | Variable / directo | 60 | 120 | Ari |
| **Google Cloud** (Run/Hosting + logs) | Variable / directo | 60 | 100 | Ari |
| **Subtotal caja C-05b** | | **120** | **220** | |
| Contingencia 12 % | Reserva | 0 (cerrada) | Solo con acta | Giannina |

El subtotal (**US$ 120–220**) es ~10–18 % del bloque variable (~US$ 1.240), no del techo entero.

### B. Medición: ¿el ahorro de soporte compensa Gemini + GCloud?

**Sí, esa es la hipótesis — y se mide, no se afirma de antemano.**

| Paso | Qué | Quién | Cuándo |
|------|-----|-------|--------|
| 1. Línea base | Contar consultas fuera del tablero (nº y minutos) ≥ 1 semana con tablero usable **antes** de activar el chatbot | Skarlett + soporte | Post 9 nov, pre-chat |
| 2. Gasto IA | Leer factura/consola: Gemini + Cloud Run/Hosting del período | Ari | Cada 2 semanas (con Excel) |
| 3. Soporte evitado | (consultas o minutos baseline − actuales) × costo hora soporte local (el del plan variable) | Skarlett + Ari | Misma cadencia |
| 4. Regla | **Sostenible** si `ahorro_soporte_estimado ≥ gasto_Gemini + GCloud`. Si el gasto IA gana **dos revisiones seguidas** → pausar chatbot o nuevo CC | Giannina | Review / corte |

No se escribe en el acta un “ahorro US$ X” hasta tener la línea base.

### C. Lo que **rompería** credibilidad (no incluir como aprobado)

- Contratar especialista agéntico + modelo propio + datalake en el mismo techo.
- Prometer API “gratis”.
- Usar contingencia sin razón escrita.

---

## 6. Texto corto para pegar en el Word (§4.1 / después de Tabla 7)

> Stack: **Google Cloud + Gemini** (Flash-Lite/Flash). Caja fase 1: **US$ 120–220** (API + GCloud), tope Gemini **US$ 120**, techo **20.700** intacto. Se **mide** ahorro de soporte vs gasto Gemini/GCloud con línea base post 9 nov; si el gasto IA supera el ahorro de forma sostenida, se pausa o hay CC nuevo.

### Tabla (Tabla 7b del Word)

| Rubro | Tipo | US$ propuesto | US$ máximo | Control |
|-------|------|---------------|------------|---------|
| API Gemini | Variable | 60 | 120 | Consola Google / Excel Ari |
| Google Cloud (chat) | Variable | 60 | 100 | Misma cuenta; sin GPU |
| HH equipo | Ya en techo | 0 caja | 13–22 pd | Replanificación |
| Ahorro soporte | Beneficio (medir) | Baseline | ≥ gasto IA del período | O6 + bitácora |
| **Total caja** | | **120** | **220** | Contingencia cerrada |

---

## 7. Decisión recomendada al CC

1. Aprobar C-05b/C-06 **condicionados** con esta banda.  
2. Ari crea en Excel las líneas “API chatbot” y “margen hosting chat”.  
3. Si el uso real supera el tope → pausar chatbot o CC nuevo (no “ajustar en silencio”).  
4. Fase 3 (agéntico / monitoreo IA) = **nuevo presupuesto** o post-piloto.
