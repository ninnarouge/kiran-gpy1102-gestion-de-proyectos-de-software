"""Zip portable y PDF 16:9 de la presentación Eva 1."""

from __future__ import annotations

import http.server
import shutil
import socketserver
import subprocess
import tempfile
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
PRESENT = ROOT / "evaluaciones" / "eva-01" / "presentacion"
EXPORT = PRESENT / "export"
ZIP_NAME = "Kiran-Eva01-presentacion.zip"
PDF_NAME = "Kiran-Eva01-presentacion.pdf"
PRINT_NAME = "_print.html"
PORT = 4178
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

ZIP_FILES = [
    PRESENT / "index.html",
    PRESENT / "gantt-ruta-critica.html",
    PRESENT / "README.md",
    PRESENT / "STORYBOARD.md",
    PRESENT / "BRIEF.md",
    PRESENT / "frame.md",
]

PRINT_CSS = """
      html.is-pdf,
      html.is-pdf body {
        width: 1920px !important;
        height: auto !important;
        overflow: visible !important;
        transform: none !important;
        background: #f3eee4 !important;
      }

      html.is-pdf::before,
      html.is-pdf::after {
        display: none !important;
      }

      @page {
        size: 1920px 1080px;
        margin: 0;
      }

      html.is-pdf .scene {
        position: relative !important;
        width: 1920px !important;
        height: 1080px !important;
        opacity: 1 !important;
        visibility: visible !important;
        pointer-events: none !important;
        overflow: hidden;
        page-break-after: always;
        break-after: page;
        background: #f3eee4;
      }

      html.is-pdf #scene-cover,
      html.is-pdf #scene-value,
      html.is-pdf #scene-close {
        background: #0a1520;
      }

      html.is-pdf .scene:last-of-type {
        page-break-after: auto;
        break-after: auto;
      }

      html.is-pdf .deck-chrome,
      html.is-pdf .handoff,
      html.is-pdf #timeline-root,
      html.is-pdf .deck-nav {
        display: none !important;
      }

      html.is-pdf [stroke-dashoffset] {
        stroke-dashoffset: 0 !important;
      }

      html.is-pdf #cover-clip { r: 112px; }
      html.is-pdf #cover-glow { r: 58px; }
      html.is-pdf #cover-origin { r: 13px; }
      html.is-pdf #pert-area { opacity: 0.16 !important; }
      html.is-pdf #pert-band { opacity: 0.12 !important; }
      html.is-pdf .critical-pop { display: none !important; }

      html.is-pdf #cover-stem,
      html.is-pdf #cover-origin,
      html.is-pdf #cover-glow,
      html.is-pdf #cover-name,
      html.is-pdf #cover-promise,
      html.is-pdf .cover-subtitle,
      html.is-pdf .cover-hud-names,
      html.is-pdf .cover-hud .chip,
      html.is-pdf .cover-mark-caption,
      html.is-pdf .origin-halo,
      html.is-pdf #close-brand,
      html.is-pdf #close-title,
      html.is-pdf #close-lead,
      html.is-pdf #close-ask,
      html.is-pdf #close-colophon {
        opacity: 1 !important;
      }

      html.is-pdf .beam-edge { opacity: 0.35 !important; }
      html.is-pdf #close-duoc { opacity: 0.72 !important; }
"""


def make_zip() -> Path:
    EXPORT.mkdir(parents=True, exist_ok=True)
    zip_path = EXPORT / ZIP_NAME
    if zip_path.exists():
        zip_path.unlink()
    prefix = "Kiran-Eva01-presentacion"
    with ZipFile(zip_path, "w", ZIP_DEFLATED) as zf:
        for path in ZIP_FILES:
            zf.write(path, f"{prefix}/{path.name}")
        for asset in sorted((PRESENT / "assets").iterdir()):
            if asset.is_file() and not asset.name.startswith("."):
                zf.write(asset, f"{prefix}/assets/{asset.name}")
    return zip_path


def build_print_html() -> Path:
    source = (PRESENT / "index.html").read_text(encoding="utf-8")
    source = source.replace(
        '<html lang="es" class="stage-dark" data-resolution="landscape">',
        '<html lang="es" class="is-pdf" data-resolution="landscape">',
        1,
    )
    source = source.replace("</style>", PRINT_CSS + "\n    </style>", 1)
    last = source.rfind("<script>")
    close = source.rfind("</script>")
    if last != -1 and close > last:
        source = source[:last] + "<script>/* PDF estático: sin GSAP */</script>" + source[close + len("</script>") :]
    out = PRESENT / PRINT_NAME
    out.write_text(source, encoding="utf-8")
    return out


def start_server() -> socketserver.TCPServer:
    socketserver.TCPServer.allow_reuse_address = True

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            return

    def handler(*args, **kwargs):
        return Quiet(*args, directory=str(PRESENT), **kwargs)

    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    import threading

    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def make_pdf() -> Path:
    if not CHROME.exists():
        raise RuntimeError(f"No encuentro Chrome en {CHROME}")

    print_html = build_print_html()
    pdf_path = EXPORT / PDF_NAME
    profile = Path(tempfile.mkdtemp(prefix="kiran-pdf-"))
    if pdf_path.exists():
        pdf_path.unlink()

    httpd = start_server()
    try:
        cmd = [
            str(CHROME),
            "--headless=new",
            "--disable-gpu",
            "--disable-extensions",
            "--no-first-run",
            "--no-pdf-header-footer",
            "--hide-scrollbars",
            f"--user-data-dir={profile}",
            "--virtual-time-budget=8000",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={pdf_path}",
            f"http://127.0.0.1:{PORT}/{PRINT_NAME}",
        ]
        subprocess.run(cmd, check=True, capture_output=True)
    finally:
        httpd.shutdown()
        httpd.server_close()
        print_html.unlink(missing_ok=True)
        shutil.rmtree(profile, ignore_errors=True)

    if not pdf_path.exists() or pdf_path.stat().st_size < 20_000:
        raise RuntimeError("Chrome no generó el PDF.")
    return pdf_path


def main() -> None:
    zip_path = make_zip()
    print(f"ZIP  {zip_path}  ({zip_path.stat().st_size / 1024 / 1024:.2f} MB)")
    pdf_path = make_pdf()
    print(f"PDF  {pdf_path}  ({pdf_path.stat().st_size / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    main()
