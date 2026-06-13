"""Assignment D: circle file, line, and error type on a sample traceback."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "traceback_circled.png"

LINES = [
    "Traceback (most recent call last):",
    '  File "D:\\Nora AI Training\\day13\\assignment\\sample_error.py", line 4, in <module>',
    '    n = int("cat")',
    "        ^^^^^^^^^^",
    "ValueError: invalid literal for int() with base 10: 'cat'",
]

# (line_index, start_col, end_col, label) — 0-based columns in monospace text
CIRCLES = [
    (1, 9, 62, "file"),   # assignment\\sample_error.py
    (1, 65, 71, "line"),  # line 4
    (4, 0, 54, "error"),  # ValueError: ...
]

FONT_SIZE = 18
PAD = 40
LINE_H = 28
CHAR_W = 10


def load_font():
    for name in ("consola.ttf", "cour.ttf", "lucon.ttf"):
        try:
            return ImageFont.truetype(name, FONT_SIZE)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    font = load_font()
    width = max(len(line) for line in LINES) * CHAR_W + PAD * 2
    height = len(LINES) * LINE_H + PAD * 2 + 36

    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    y = PAD
    for i, line in enumerate(LINES):
        draw.text((PAD, y), line, fill="black", font=font)
        y += LINE_H

    colors = {"file": "#2563eb", "line": "#16a34a", "error": "#dc2626"}
    for line_i, col_start, col_end, kind in CIRCLES:
        x1 = PAD + col_start * CHAR_W - 6
        y1 = PAD + line_i * LINE_H - 4
        x2 = PAD + col_end * CHAR_W + 6
        y2 = PAD + line_i * LINE_H + LINE_H + 2
        draw.ellipse([x1, y1, x2, y2], outline=colors[kind], width=3)

    legend_y = height - 30
    draw.text(
        (PAD, legend_y),
        "Blue = file   Green = line number   Red = error type",
        fill="#444444",
        font=font,
    )

    img.save(OUT)
    print(f"Saved {OUT}")


if __name__ == "__main__":
    main()
