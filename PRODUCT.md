# PRODUCT.md

## Job to be done

Cuando un equipo de terreno y quienes financian un piloto solar necesitan **ver el estado real de los kits**, poder **abrir una falla** y **mostrar impacto** sin armar un Excel a mano, esta plataforma lo registra y lo muestra.

## Audience

| Quién | Qué necesita |
|---|---|
| Técnico / soporte local | Ver kits, cambiar estado, abrir ticket |
| Dirección de la empresa social | Tablero simple del piloto |
| Inversores de impacto y donantes | Informe periódico creíble |
| Hogares / comunidad | No son usuarios directos del software en esta fase |

## In scope (piloto)

- Inventario: comunidades, hogares, kits (activo / en falla / dado de baja)
- Tablero operativo (visión general e individual)
- Monitoreo y mantención (tickets + soporte local)
- Reportes de impacto social y ambiental para patrocinadores
- Roles de acceso y cuidado de datos personales del hogar

## Out of scope

- Fabricar o vender paneles
- Instalar kits en techos
- Tendido eléctrico
- App masiva para cada familia
- Expansión a otras regiones en esta fase
- Microcréditos o cobranza

Si no está en la EDT, **no se hace** en el piloto. Se escribe como exclusión.

## Primary KPI

Kits del piloto con estado **actualizado** y fallas **visibles** en el tablero (no “pantallas listas” si el dato es mentira).

KPI de valor (más adelante): tiempo entre falla reportada y ticket cerrado, y un informe que el patrocinador pueda usar.

## Constraints

- Equipo de 4 estudiantes, jornada vespertina
- Presupuesto y plazo del piloto académico (Eva 1 en semana 5)
- Conectividad irregular en terreno
- Financiamiento mixto: hay que respetar hitos de reporte
- Datos de hogares: minimización y roles (no subir bases reales al repo)

## Enfoque de planificación

Híbrido:

- **Predictivo:** inventario, estados, privacidad, calendario de reportes
- **Adaptativo:** tablero y flujo de tickets (se aprende en terreno)

## Glossary

| Término | Significado aquí |
|---|---|
| Kit | Equipo solar instalado en un hogar del piloto |
| Tablero | Vista operativa de kits y tickets |
| Ticket | Solicitud de mantención o falla |
| Patrocinador | Inversor de impacto, subsidio o partner que financia |
| EDT | Árbol de todo el trabajo del proyecto |

## Banned (para el equipo y para IA)

- Prometer instalación de paneles o “electrificar la región”
- Subir datos reales de hogares, fotos de menores, o archivos `.env`
- Mezclar PMBOK 6 / 7 / 8 en un mismo párrafo del informe sin decir la edición
- Tratar el Gantt como adorno: si no hay precedencias, no es plan
