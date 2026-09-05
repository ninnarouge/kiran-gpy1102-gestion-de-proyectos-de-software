# Cómo colaborar

Este repo lo usamos **cuatro personas**. Si alguien sube a `main` sin avisar, se pisan el trabajo. Estas reglas son cortas a propósito.

## 1. Antes de tocar algo

- Lee `README.md` y `PRODUCT.md`.
- Trabaja en una **rama**, nunca en `main`.
- Si la tarea es de más de un archivo, abre un **issue** (plantilla “Tarea”) y enlázalo en el PR.

## 2. Ramas

Formato: `tipo/descripcion-corta`

| Prefijo | Para qué |
|---|---|
| `feat/` | Algo nuevo (sección del informe, pantalla, Gantt) |
| `fix/` | Corregir un error |
| `docs/` | Solo documentación |
| `chore/` | Orden, gitignore, plantillas |

Ejemplos:

```bash
git checkout main
git pull origin main
git checkout -b feat/enunciado-alcance
git checkout -b docs/banco-preguntas-orales
```

## 3. Commits

Una idea por commit. Mensaje en **español**, primera línea de máximo ~72 caracteres.

```
feat: agregar exclusiones del alcance del piloto

Deja fuera fabricación e instalación para que el informe no se hinche.
```

No hagas:

```
update
asdasd
WIP
```

## 4. Pull Request

1. `git push -u origin tu-rama`
2. En GitHub: **Compare & pull request** hacia `main`
3. Completa la plantilla (qué cambió, cómo probarlo, issue)
4. Pide review a **otra** persona del equipo
5. No mezcles tu propio PR sin que alguien lo mire, salvo typos minúsculos de docs

## 5. Qué sí y qué no subir

**Sí:** Markdown del equipo, HTML/XML de entregas, código, `.env.example`, capturas **sin datos personales**.

**No:** contraseñas, `.env`, PPTs oficiales de Duoc, PDF de rúbrica, libro PMBOK, bases de hogares, `node_modules`.

Si Git te muestra un archivo que no reconoces, **pregunta** antes de `git add -A`.

## 6. Conflictos

Si Git dice “conflict”:

1. No entres en pánico. No borres la carpeta.
2. `git pull origin main` en tu rama (o pide ayuda en el issue).
3. Resuelve el archivo marcando qué versión queda.
4. Commit de “resolver conflicto” y avisa en el PR.

## 7. Dudas

Usa la plantilla de issue **Duda**. Mejor una pregunta escrita que un archivo subido “por si acaso”.
