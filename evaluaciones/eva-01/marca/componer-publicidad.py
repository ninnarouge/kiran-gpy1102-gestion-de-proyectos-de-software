"""Compone la campaña Kiran: foto + identidad (isotipo, tipo geométrica, acento ámbar)."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = Path(
    r"C:\Users\Admin\.cursor\projects\c-Users-Admin-Desktop-Duoc-GESTION-DE-PROYECTOS-DE-SOFTWARE\assets"
)
SRC = ASSETS / "publicidad-kiran-base.png"
OUT = ROOT / "publicidad-kiran.png"
OUT_FOTO = ROOT / "publicidad-kiran-foto.png"

NAVY = (16, 38, 61, 255)
AMBER = (229, 154, 36, 255)
IVORY = (247, 243, 234, 255)
SOFT = (215, 223, 229, 255)
WHITE = (255, 255, 255, 255)

W, H = 1920, 1080


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    path = Path(r"C:\Windows\Fonts") / name
    return ImageFont.truetype(str(path), size)


def draw_tracked(draw: ImageDraw.ImageDraw, text: str, xy, face, fill, tracking: float) -> None:
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=face, fill=fill)
        x += face.getlength(ch) + tracking


def draw_isotipo_reverso(draw: ImageDraw.ImageDraw, origin, scale: float) -> None:
    ox, oy = origin

    def sx(x: float, y: float):
        return (ox + x * scale, oy + y * scale)

    x, y = sx(50, 28)
    draw.rounded_rectangle(
        [x, y, x + 42 * scale, y + 184 * scale],
        radius=max(2, 10 * scale),
        fill=WHITE,
    )
    draw.polygon([sx(91, 120), sx(198, 38), sx(198, 96), sx(99, 118)], fill=AMBER)
    draw.polygon([sx(91, 120), sx(198, 202), sx(198, 144), sx(99, 122)], fill=AMBER)
    cx, cy = sx(92, 120)
    r = 9 * scale
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=AMBER)


def main() -> None:
    photo = Image.open(SRC).convert("RGBA").resize((W, H), Image.Resampling.LANCZOS)
    photo.save(OUT_FOTO)

    canvas = photo.copy()
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Columna de marca a la izquierda: el palo de la K, en el espacio vacío.
    for i in range(640):
        alpha = int(72 * (1 - i / 640) ** 1.35)
        draw.line([(i, 0), (i, H)], fill=(16, 38, 61, alpha))

    draw_isotipo_reverso(draw, (78, 52), 0.5)
    kiran = font("arialbd.ttf", 56)
    slogan = font("arial.ttf", 20)
    line = font("arialbd.ttf", 40)

    draw_tracked(draw, "KIRAN", (210, 108), kiran, WHITE, 12)
    draw.text(
        (212, 176),
        "Visibilidad que mantiene la energía activa.",
        font=slogan,
        fill=SOFT,
    )

    # Acento de marca: la misma raya ámbar del sistema gráfico, no un pie de foto.
    draw.rounded_rectangle([96, 872, 200, 878], radius=3, fill=AMBER)
    draw_tracked(draw, "SI NO SE VE, SE APAGA.", (96, 900), line, IVORY, 8)

    composed = Image.alpha_composite(canvas, overlay).convert("RGB")
    composed.save(OUT, quality=95)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
