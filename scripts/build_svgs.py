"""Builds the profile artwork in assets/ to match the tanim.my.id brand.

Palette and type are taken from the portfolio:
  obsidian #0c0d0e · card #141517 · border white/12% · text #fafafa
  muted zinc #a1a1aa / #71717b · accent orange #F65802 (light #FF9A63)
  Clash Display (titles) · Inter (body) · Geist Mono (labels)

Fonts are subset and embedded so the images render identically everywhere.
Put the font files in scripts/fonts/ (git-ignored, see scripts/fonts/README.md):
  ClashDisplay-Bold.woff2, Inter.woff2, GeistMono.woff2

Run:  pip install fonttools brotli && python3 scripts/build_svgs.py
"""
import base64
import io
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
FONTS = Path(__file__).resolve().parent / "fonts"

OBSIDIAN = "#0c0d0e"
CARD = "#141517"
BORDER = "#ffffff1f"
PILL_BG = "#ffffff0d"
WHITE = "#fafafa"
ZINC300 = "#d4d4d8"
ZINC400 = "#a1a1aa"
ZINC500 = "#71717b"
ORANGE = "#F65802"
INK = "#0c0d0e"  # text colour on light backgrounds

FONT_FILES = {"display": "ClashDisplay-Bold.woff2", "body": "Inter.woff2", "mono": "GeistMono.woff2"}
FAMILY = {"display": "TDisplay", "body": "TBody", "mono": "TMono"}
STACK = {
    "display": "TDisplay,'Arial Black',Helvetica,sans-serif",
    "body": "TBody,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif",
    "mono": "TMono,ui-monospace,Menlo,Consolas,monospace",
}
_ttf = {k: TTFont(FONTS / v) for k, v in FONT_FILES.items()}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text_width(kind, s, size, tracking=0.0):
    """Width in px of a string (default instance of the font)."""
    t = _ttf[kind]
    cmap, hmtx, upm = t.getBestCmap(), t["hmtx"], t["head"].unitsPerEm
    adv = sum(hmtx[cmap.get(ord(c), cmap.get(32))][0] for c in s)
    return adv / upm * size + tracking * size * max(len(s) - 1, 0)


class Svg:
    """Tracks which characters each font draws, then embeds minimal subsets."""

    def __init__(self, w, h, title):
        self.w, self.h, self.title = w, h, title
        self.used = {k: set() for k in FONT_FILES}
        self.body = []

    def text(self, kind, s, x, y, size, fill, weight=None, anchor="start", tracking=0.0, extra=""):
        self.used[kind].update(s)
        ls = f' letter-spacing="{tracking * size:.2f}"' if tracking else ""
        wt = f' font-weight="{weight}"' if weight else ""
        self.body.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{STACK[kind]}" font-size="{size}"{wt}{ls} '
            f'fill="{fill}" text-anchor="{anchor}"{extra}>{esc(s)}</text>')

    def spans(self, kind, parts, x, y, size, tracking=0.0, anchor="start"):
        """parts: [(text, fill), ...] laid out inline."""
        for s, _ in parts:
            self.used[kind].update(s)
        ls = f' letter-spacing="{tracking * size:.2f}"' if tracking else ""
        inner = "".join(f'<tspan fill="{f}">{esc(s)}</tspan>' for s, f in parts)
        self.body.append(f'<text x="{x}" y="{y}" font-family="{STACK[kind]}" font-size="{size}"{ls} text-anchor="{anchor}">{inner}</text>')

    def add(self, raw):
        self.body.append(raw)

    def _font_face(self, kind):
        chars = "".join(sorted(self.used[kind] | {" "}))
        opts = subset.Options()
        opts.flavor = "woff2"
        opts.layout_features = ["kern", "liga"]
        opts.name_IDs = []
        opts.drop_tables += ["FFTM"]
        opts.notdef_outline = True
        f = TTFont(FONTS / FONT_FILES[kind])
        sub = subset.Subsetter(opts)
        sub.populate(text=chars)
        sub.subset(f)
        buf = io.BytesIO()
        f.flavor = "woff2"
        f.save(buf)
        b64 = base64.b64encode(buf.getvalue()).decode()
        weight = "100 900" if "fvar" in f else "700"
        return f"@font-face{{font-family:{FAMILY[kind]};font-weight:{weight};src:url(data:font/woff2;base64,{b64}) format('woff2')}}"

    def render(self, defs=""):
        faces = "".join(self._font_face(k) for k, v in self.used.items() if v)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{esc(self.title)}">\n'
                f'<title>{esc(self.title)}</title>\n<defs><style>{faces}</style>{defs}</defs>\n'
                + "\n".join(self.body) + "\n</svg>\n")


def arrow_ne(x, y, s, color, sw=2):
    return (f'<path d="M{x},{y + s} L{x + s},{y} M{x + s * 0.3},{y} L{x + s},{y} L{x + s},{y + s * 0.7}" '
            f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')


def arrow_down(x, y, s, color, sw=2):
    return (f'<path d="M{x + s / 2},{y} V{y + s} M{x},{y + s * 0.55} L{x + s / 2},{y + s} L{x + s},{y + s * 0.55}" '
            f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')


def sparkle(cx, cy, r, color):
    """Four-point star, the portfolio's section marker."""
    k = r * 0.22
    return (f'<path d="M{cx},{cy - r} Q{cx + k},{cy - k} {cx + r},{cy} Q{cx + k},{cy + k} {cx},{cy + r} '
            f'Q{cx - k},{cy + k} {cx - r},{cy} Q{cx - k},{cy - k} {cx},{cy - r}Z" fill="{color}"/>')


# ───────────────────────────── hero ─────────────────────────────
def hero():
    W, H = 1200, 470
    s = Svg(W, H, "Tasnim Rahman Tanim — Lead Solutions Architect and ISO/IEC 27001 Lead Auditor")
    s.add(f'<clipPath id="r"><rect width="{W}" height="{H}" rx="20"/></clipPath><g clip-path="url(#r)">')
    s.add(f'<rect width="{W}" height="{H}" fill="{OBSIDIAN}"/>')
    # warm key light, like the portfolio hero
    s.add(f'''<ellipse cx="930" cy="150" rx="520" ry="380" fill="url(#glow)">
      <animate attributeName="opacity" values="0.85;1;0.85" dur="7s" repeatCount="indefinite"/></ellipse>''')
    s.add(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')

    # top bar: logo + location
    s.add(f'<circle cx="68" cy="62" r="18" fill="{ORANGE}"/>')
    s.text("display", "T", 68, 68.5, 17, OBSIDIAN, anchor="middle")
    s.text("display", "TANIM", 98, 68, 17, WHITE, tracking=0.06)
    pin_x = W - 50 - text_width("mono", "DHAKA, BANGLADESH", 14, 0.12)
    s.add(f'<path d="M{pin_x - 20},{57} a5.5,5.5 0 1 1 11,0 c0,4.5 -5.5,10 -5.5,10 s-5.5,-5.5 -5.5,-10z" fill="none" stroke="{ZINC300}" stroke-width="1.6"/>'
          f'<circle cx="{pin_x - 14.5}" cy="57" r="1.8" fill="{ZINC300}"/>')
    s.text("mono", "DHAKA, BANGLADESH", W - 50, 66, 14, ZINC300, anchor="end", tracking=0.12)

    # availability status
    s.add(f'''<circle cx="56" cy="128" r="4" fill="{WHITE}"/>
    <circle cx="56" cy="128" r="4" fill="none" stroke="{WHITE}" stroke-width="1.5">
      <animate attributeName="r" values="4;11" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0" dur="2s" repeatCount="indefinite"/></circle>''')
    s.text("body", "Taking on architecture reviews and ISO 27001 audits", 72, 133.5, 16, WHITE, weight=500)

    # name
    s.text("display", "TASNIM RAHMAN TANIM", 50, 262, 76, WHITE, tracking=-0.01)
    # intro
    s.text("body", "Lead Solutions Architect and ISO/IEC 27001 Lead Auditor, designing and", 52, 316, 21, ZINC300)
    s.text("body", "securing multi-cloud platforms on OCI, AWS and Azure.", 52, 346, 21, ZINC300)

    # skill pills
    x = 52
    for label in ["WAZUH SIEM & XDR", "TERRAFORM IAC", "ODOO 19 ERP SYSTEMS", "DEVSECOPS", "MULTI-CLOUD"]:
        w = text_width("mono", label, 14, 0.1) + 40
        s.add(f'<rect x="{x}" y="388" width="{w:.1f}" height="40" rx="20" fill="{PILL_BG}" stroke="{BORDER}"/>')
        s.text("mono", label, x + w / 2, 413, 14, ZINC300, anchor="middle", tracking=0.1, weight=500)
        x += w + 10
    s.add("</g>")
    s.add(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="{BORDER}"/>')
    defs = f'''<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ff6a1f" stop-opacity="0.75"/>
      <stop offset="0.45" stop-color="{ORANGE}" stop-opacity="0.35"/>
      <stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></radialGradient>
    <linearGradient id="fade" x1="0" x2="0" y1="0" y2="1">
      <stop offset="0.35" stop-color="{OBSIDIAN}" stop-opacity="0"/>
      <stop offset="1" stop-color="{OBSIDIAN}" stop-opacity="0.85"/></linearGradient>'''
    return s.render(defs)


# ───────────────────────────── stats ─────────────────────────────
STATS = [("99.9%", "Uptime", "across client clouds"),
         ("15%", "Win rate", "higher in presales"),
         ("220+", "Engineers", "trained"),
         ("10+", "ERP modules", "shipped")]


def stats():
    W, H, gap = 1200, 150, 16
    cw = (W - gap * 3) / 4
    s = Svg(W, H, "99.9% uptime across client clouds · 15% higher presales win rate · 220+ engineers trained · 10+ ERP modules shipped")
    for i, (num, lab, sub) in enumerate(STATS):
        x = i * (cw + gap)
        s.add(f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{0.12 * i:.2f}s" dur="0.6s" fill="freeze"/>')
        s.add(f'<rect x="{x + 0.5}" y="0.5" width="{cw - 1}" height="{H - 1}" rx="14" fill="{CARD}" stroke="{BORDER}"/>')
        s.text("display", num, x + 26, 72, 46, WHITE)
        s.spans("body", [(lab, ZINC300), (f" · {sub}", ZINC500)], x + 26, 112, 17)
        s.add("</g>")
    return s.render()


# ───────────────────────────── section headers ─────────────────────────────
def header(label, plain, accent, meta, theme):
    W, H = 1200, 132
    fg = WHITE if theme == "dark" else INK
    muted = ZINC400 if theme == "dark" else "#52525c"
    line = "#ffffff26" if theme == "dark" else "#0c0d0e1f"
    s = Svg(W, H, f"{label}: {plain}{accent}".strip())
    s.add(f'<rect x="0" y="1" width="{W}" height="1" fill="{line}"/>')
    s.add(sparkle(9, 38, 8, ORANGE))
    s.text("body", label, 26, 44, 17, fg, weight=500)
    if meta:
        s.text("body", meta, W, 44, 16, muted, anchor="end")
    size = min(50, 50 * (W - 40) / text_width("display", plain + accent, 50))
    s.spans("display", [(plain, fg), (accent, ORANGE)], 0, 112, round(size, 1))
    return s.render()


HEADERS = {
    "about": ("About", "CLOUD PLATFORMS BUILT TO ", "PASS THE AUDIT.", "Dhaka, Bangladesh"),
    "expertise": ("Expertise", "WHAT THE WORK ", "COVERS", "4 disciplines"),
    "work": ("Work", "SELECTED ", "PROJECTS", "4 builds"),
    "career": ("Career", "WHERE IT ", "HAPPENED", "2023 — now"),
    "credentials": ("Credentials", "CERTIFIED TO ", "AUDIT", "ISO/IEC 27001:2022"),
    "contact": ("Contact", "LET'S BUILD SOMETHING ", "SECURE.", "mail.tasnimrahman@gmail.com"),
}


# ───────────────────────────── buttons ─────────────────────────────
def button(label, kind):
    """kind: primary (orange) | ghost (dark outline). Icon: ne arrow / down arrow."""
    size, h = 15, 52
    tw = text_width("mono", label, size, 0.1)
    icon = 26
    W = int(tw + 24 + icon + 14 + 26)
    s = Svg(W, h, label.title())
    if kind == "primary":
        s.add(f'<rect width="{W}" height="{h}" rx="{h / 2}" fill="{ORANGE}"/>')
        s.add(f'<circle cx="{h / 2}" cy="{h / 2}" r="17" fill="{OBSIDIAN}"/>')
        s.add(arrow_ne(h / 2 - 5.5, h / 2 - 5.5, 11, ORANGE, 2.2))
        fg = OBSIDIAN
    else:
        s.add(f'<rect x="0.75" y="0.75" width="{W - 1.5}" height="{h - 1.5}" rx="{h / 2}" fill="{OBSIDIAN}" stroke="#ffffff40" stroke-width="1.5"/>')
        if kind == "download":
            s.add(arrow_down(h / 2 - 6, h / 2 - 7, 12, WHITE, 2))
        else:
            s.add(arrow_ne(h / 2 - 5.5, h / 2 - 5.5, 11, WHITE, 2))
        fg = WHITE
    s.text("mono", label, h / 2 + 24, h / 2 + 5.3, size, fg, weight=600, tracking=0.1)
    return s.render()


BUTTONS = {
    "btn-talk": ("LET'S TALK", "primary"),
    "btn-cv": ("DOWNLOAD CV", "download"),
    "btn-portfolio": ("PORTFOLIO", "ghost"),
    "btn-linkedin": ("LINKEDIN", "ghost"),
}


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    files = {"hero.svg": hero(), "stats.svg": stats()}
    for key, args in HEADERS.items():
        for theme in ("dark", "light"):
            files[f"h-{key}-{theme}.svg"] = header(*args, theme)
    for name, (label, kind) in BUTTONS.items():
        files[f"{name}.svg"] = button(label, kind)
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8")
    print("\n".join(f"{n:28s} {len(v) / 1024:6.1f} KB" for n, v in files.items()))
