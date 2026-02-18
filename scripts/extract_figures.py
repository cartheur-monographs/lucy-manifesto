#!/usr/bin/env python3
import os
import re
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "source.pdf"
LAYOUT_TXT = Path("/tmp/source_layout.txt")
OUT_DIR = ROOT / "figures"
WORK_DIR = Path("/tmp/lucy_fig_extract")


def run(cmd):
    subprocess.run(cmd, check=True)


def parse_figure_pages():
    pages = []
    page = 1
    with LAYOUT_TXT.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if "\f" in line:
                page += line.count("\f")
                continue
            m = re.match(r"^\s*Figure\s+(\d+)\b", line)
            if m:
                pages.append((int(m.group(1)), page))
    return pages


def caption_ymin_pts(pdf_page, fig_no):
    html_path = WORK_DIR / f"page_{pdf_page:03d}.html"
    run(
        [
            "pdftotext",
            "-f",
            str(pdf_page),
            "-l",
            str(pdf_page),
            "-bbox-layout",
            str(PDF),
            str(html_path),
        ]
    )
    text = html_path.read_text(encoding="utf-8", errors="ignore")
    word_re = re.compile(
        r'<word xMin="[^"]+" yMin="([^"]+)" xMax="[^"]+" yMax="[^"]+">([^<]+)</word>'
    )
    words = [(float(y), w) for y, w in word_re.findall(text)]

    for i in range(len(words) - 1):
        y1, w1 = words[i]
        y2, w2 = words[i + 1]
        if w1.strip() == "Figure" and w2.strip() == str(fig_no) and abs(y1 - y2) < 0.8:
            return y1
    return None


def extract():
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    run(["pdftotext", "-layout", str(PDF), str(LAYOUT_TXT)])
    figures = parse_figure_pages()

    manifest_lines = [
        "# Extracted Figures (Caption-anchored crops)",
        "",
        "Source: `source.pdf`",
        "",
        "| Figure | PDF Page | File |",
        "|---|---:|---|",
    ]

    for fig_no, page in figures:
        ymin_pts = caption_ymin_pts(page, fig_no)
        if ymin_pts is None:
            continue

        base = WORK_DIR / f"figure_{fig_no:02d}_page_{page}"
        page_png = base.with_suffix(".png")
        run(
            [
                "pdftoppm",
                "-f",
                str(page),
                "-l",
                str(page),
                "-r",
                "300",
                "-png",
                "-singlefile",
                str(PDF),
                str(base),
            ]
        )

        identify = subprocess.run(
            ["identify", "-format", "%w %h", str(page_png)],
            check=True,
            capture_output=True,
            text=True,
        )
        width, height = [int(x) for x in identify.stdout.strip().split()]

        # Convert caption Y from PDF points to raster pixels.
        y_caption = int((ymin_pts / 771.840027) * height)

        # Detect figure block above caption by dark-pixel density, then crop tight.
        x0 = int(width * 0.05)
        x1 = int(width * 0.95)
        y_top_search = int(height * 0.06)
        y_bottom_search = max(y_top_search + 1, y_caption - int(height * 0.01))

        gray = np.array(Image.open(page_png).convert("L"))
        roi = gray[y_top_search:y_bottom_search, x0:x1]
        dark = roi < 235
        row_density = dark.sum(axis=1)
        row_threshold = max(12, int((x1 - x0) * 0.003))

        ink_rows = np.where(row_density > row_threshold)[0]
        if len(ink_rows) == 0:
            continue

        bottom_rel = int(ink_rows[-1])
        gap_needed = max(12, int(height * 0.012))
        blank_run = 0
        top_rel = 0
        for r in range(bottom_rel, -1, -1):
            if row_density[r] <= row_threshold:
                blank_run += 1
            else:
                blank_run = 0
            if blank_run >= gap_needed:
                top_rel = r + gap_needed
                break

        y0 = y_top_search + max(0, top_rel - 6)
        y1 = y_top_search + min(roi.shape[0] - 1, bottom_rel + 6)
        y1 = max(y1, y0 + 1)

        band = dark[max(0, top_rel - 6) : min(roi.shape[0], bottom_rel + 7), :]
        col_density = band.sum(axis=0)
        col_threshold = max(6, int((y1 - y0) * 0.01))
        ink_cols = np.where(col_density > col_threshold)[0]
        if len(ink_cols) > 0:
            x0 = x0 + max(0, int(ink_cols[0]) - 6)
            x1 = x0 + (int(ink_cols[-1]) - int(ink_cols[0]) + 12)
        x1 = min(width - 1, max(x1, x0 + 1))

        w = max(1, x1 - x0)
        h = max(1, y1 - y0)
        out_name = f"figure_{fig_no:02d}.png"
        out_file = OUT_DIR / out_name

        run(
            [
                "convert",
                str(page_png),
                "-crop",
                f"{w}x{h}+{x0}+{y0}",
                "+repage",
                "-fuzz",
                "1%",
                "-trim",
                "+repage",
                str(out_file),
            ]
        )

        manifest_lines.append(f"| {fig_no} | {page} | `figures/{out_name}` |")

    (OUT_DIR / "README.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    extract()
