# GPY1102 · Plataforma solar comunitaria

Repositorio del **equipo** de Gestión de Proyectos de Software (Duoc UC, jornada vespertina, Puente Alto).

Trabajamos el **Caso 7**: una plataforma para registrar, monitorear y mantener kits solares en una comunidad piloto, y para reportar impacto a quienes financian el proyecto.

Este repo es la **carpeta compartida del equipo**: plan, entregas, acuerdos y (más adelante) el software. No reemplaza Canvas ni la maleta didáctica de Duoc.

## Equipo

| Integrante | Rol sugerido en el repo | GitHub |
|---|---|---|
| Giannina Guerrero | Coordinación del repo y alcance | [@ninna-rouge](https://github.com/ninna-rouge) |
| Ari Araya | Por definir | _invitar con usuario de GitHub_ |
| Nicolás Barra | Por definir | _invitar con usuario de GitHub_ |
| Skarlett Tropan | Por definir | _invitar con usuario de GitHub_ |

Ramo: **GPY1102** · Prerrequisito GPY1101 · Docencia en Sala de Proyectos.

## Qué hay aquí

```
.
├── README.md                 ← empiezas acá
├── PRODUCT.md                ← qué es (y qué no es) el producto
├── CONTRIBUTING.md           ← cómo se trabaja en equipo
├── CODE_OF_CONDUCT.md        ← cómo nos tratamos
├── AGENTS.md                 ← reglas si alguien usa un agente de IA
├── docs/                     ← guías del equipo (caso, eva, git)
├── Eva 01/entrega/           ← archivos que sí entregamos (Gantt, cronograma)
└── Unidad-1-Guia-Extensa.md  ← guía de estudio de la Unidad 1 (trabajo propio)
```

**No se sube** el material oficial con copyright (PPTs de Duoc, programa de asignatura, rúbrica PDF, extractos de PMBOK). Eso queda en el computador de cada persona. Ver `.gitignore`.

## Cómo entrar al repo (primera vez)

1. Crea una cuenta en [GitHub](https://github.com) si no tienes.
2. Avísale a Giannina tu **usuario** para que te invite al repo (es privado).
3. Acepta el mail de invitación.
4. En tu computador:

```bash
git clone https://github.com/ninna-rouge/gpy1102-plataforma-solar.git
cd gpy1102-plataforma-solar
```

5. Lee `PRODUCT.md` y `docs/caso-de-estudio.md` antes de editar.

## Flujo corto (el día a día)

1. Nunca trabajes directo en `main`.
2. Crea una rama: `git checkout -b feat/lo-que-vas-a-hacer`
3. Haz commits chicos, en español, que expliquen el **por qué**.
4. Sube la rama y abre un **Pull Request** hacia `main`.
5. Otra persona del equipo revisa. Recién ahí se mezcla.

Detalle en [`CONTRIBUTING.md`](CONTRIBUTING.md) y [`docs/flujo-git.md`](docs/flujo-git.md).

## Entregas del ramo

| Evaluación | Qué entra a este repo | Cuándo |
|---|---|---|
| **Parcial 1** · Planificar | Informe (borrador), Gantt/cronograma, apuntes del pitch | Semana 5 |
| **Parcial 2** · Monitorear | Reporte + guion del video | Más adelante |
| **Parcial 3** · Cerrar | Láminas y lecciones aprendidas | Más adelante |
| **ET** | Presentación de defensa | Fin de semestre |

Guía de la Eva 1: [`docs/evaluacion-1.md`](docs/evaluacion-1.md).

## Producto (en una frase)

Software de **operación** de kits solares de un piloto: inventario, tablero, tickets de mantención e informes de impacto. **No** fabricamos ni instalamos paneles.

Detalle: [`PRODUCT.md`](PRODUCT.md).

## Licencia

Uso **académico** del equipo GPY1102. Ver `LICENSE`.
