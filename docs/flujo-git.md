# Flujo Git del equipo (paso a paso)

Si nunca usaste Git, sigue esto en orden. Si ya lo usas, basta `CONTRIBUTING.md`.

## Instalar

- [Git](https://git-scm.com/download/win)
- Cuenta en GitHub. El repositorio es público; la invitación como colaborador/a
  solo es necesaria para subir cambios directamente.

En la primera configuración (solo una vez, en **tu** computador):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-mail@duocuc.cl"
```

Usa el mail que tienes en GitHub.

## Clonar

```bash
git clone https://github.com/ninnarouge/kiran-gpy1102-gestion-de-proyectos-de-software.git
cd kiran-gpy1102-gestion-de-proyectos-de-software
```

## Cada vez que vas a trabajar

```bash
git checkout main
git pull origin main
git checkout -b feat/nombre-corto-de-tu-tarea
```

Edita archivos. Después:

```bash
git status
git add ruta/al/archivo.md
git commit -m "feat: explica el cambio en una línea"
git push -u origin feat/nombre-corto-de-tu-tarea
```

En GitHub abre el Pull Request hacia `main`.

## Ver en qué rama estás

```bash
git branch
```

El asterisco es la rama actual.

## Actualizar tu rama con lo nuevo de main

```bash
git checkout feat/tu-rama
git pull origin main
```

Si hay conflictos, avisa en el grupo **antes** de borrar archivos.

## Nunca

- `git push --force` a `main`
- Subir `.env` o PDFs oficiales de la maleta
- Trabajar dos personas el mismo archivo en `main` al mismo tiempo sin rama
