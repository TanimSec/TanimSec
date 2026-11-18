"""Generates the profile's SVG artwork in light and dark variants.

Run: python3 scripts/build_svgs.py   (writes into assets/)
All graphics are self-contained (no external fonts/images) so they render
reliably through GitHub's image proxy.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "dark": dict(bg="#0d1117", panel="#161b22", border="#30363d", text="#e6edf3",
                 muted="#8b949e", grid="#1c2430", accent="#22d3ee", accent2="#3b82f6",
                 glow="#22d3ee"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", border="#d0d7de", text="#1f2328",
                  muted="#59636e", grid="#eaeef2", accent="#0891b2", accent2="#2563eb",
                  glow="#06b6d4"),
}

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"

ROLES = [
    "Lead Solutions Architect",
    "ISO/IEC 27001 Lead Auditor",
    "Cloud & DevSecOps Engineer",
    "SIEM / XDR Builder",
    "Full-Stack & ERP Engineer",
]


def typing_block(t, x, y, size=24, cycle=15.0):
    """Cycling typewriter: each role types in, holds, erases."""
    n = len(ROLES)
    cw = size * 0.6  # monospace advance
    parts = []
    for i, role in enumerate(ROLES):
        w = len(role) * cw + 4
        s, e = i / n, (i + 1) / n
        typed = s + (e - s) * 0.35
        hold = e - (e - s) * 0.12
        kt, vals = [0.0], [0]
        for k, v in ((s, 0), (typed, w), (hold, w), (e, 0)):
            if k > kt[-1] + 1e-9:
                kt.append(round(k, 4)); vals.append(round(v, 1))
            else:
                vals[-1] = round(v, 1)
        if kt[-1] < 1:
            kt.append(1.0); vals.append(0)
        ktstr = ";".join(str(k) for k in kt)
        wv = ";".join(str(v) for v in vals)
        xv = ";".join(str(round(x + v, 1)) for v in vals)
        ckt, cv = [0.0], [0.85 if s == 0 else 0]
        for k, v in ((s - 0.002, 0), (s, 0.85), (e - 0.002, 0.85), (e, 0), (1.0, 0)):
            if k > ckt[-1]:
                ckt.append(round(k, 4)); cv.append(v)
        cursor_kt = ";".join(str(k) for k in ckt)
        cursor_vals = ";".join(str(v) for v in cv)
        # step-like typing: calcMode discrete would be jumpy; linear is smooth
        parts.append(f'''
    <clipPath id="clip{i}"><rect x="{x}" y="{y - size}" height="{size * 1.4}" width="0">
      <animate attributeName="width" values="{wv}" keyTimes="{ktstr}" dur="{cycle}s" repeatCount="indefinite"/>
    </rect></clipPath>
    <text x="{x}" y="{y}" clip-path="url(#clip{i})" font-family="{MONO}" font-size="{size}" font-weight="600" fill="{t['accent']}">{role.replace('&', '&amp;')}</text>
    <rect y="{y - size + 3}" width="{size * 0.5}" height="{size * 1.05}" fill="{t['accent']}" opacity="0">
      <animate attributeName="x" values="{xv}" keyTimes="{ktstr}" dur="{cycle}s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="{cursor_vals}" keyTimes="{cursor_kt}" dur="{cycle}s" repeatCount="indefinite"/>
    </rect>''')
    return "".join(parts)


def hero(t):
    W, H = 1200, 360
    # right-side "secure core" graphic
    cx, cy = 935, 195
    nodes = [("OCI", -170, -95), ("AWS", -195, 20), ("Azure", -150, 120),
             ("SIEM", 170, -95), ("CI/CD", 190, 20), ("IaC", 150, 120)]
    links, chips = [], []
    for i, (label, dx, dy) in enumerate(nodes):
        nx, ny = cx + dx, cy + dy
        links.append(
            f'<line x1="{cx}" y1="{cy}" x2="{nx}" y2="{ny}" stroke="{t["accent"]}" stroke-opacity="0.35" stroke-width="1.5"/>'
            f'<circle r="3.2" fill="{t["accent"]}"><animateMotion dur="{2.4 + i * 0.35:.2f}s" repeatCount="indefinite" '
            f'path="M{nx},{ny} L{cx},{cy}"/></circle>')
        cw = len(label) * 9.6 + 26
        chips.append(
            f'<g><rect x="{nx - cw / 2}" y="{ny - 15}" width="{cw}" height="30" rx="15" fill="{t["panel"]}" stroke="{t["accent"]}" stroke-opacity="0.6"/>'
            f'<text x="{nx}" y="{ny + 5}" text-anchor="middle" font-family="{MONO}" font-size="15" fill="{t["text"]}">{label}</text></g>')
    shield = (f'M{cx},{cy - 62} L{cx + 50},{cy - 42} L{cx + 50},{cy + 4} '
              f'C{cx + 50},{cy + 38} {cx + 26},{cy + 58} {cx},{cy + 70} '
              f'C{cx - 26},{cy + 58} {cx - 50},{cy + 38} {cx - 50},{cy + 4} L{cx - 50},{cy - 42} Z')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
  <title id="title">Tasnim Rahman Tanim</title>
  <desc id="desc">Lead Solutions Architect — Cloud Infrastructure and Cybersecurity. ISO/IEC 27001 Lead Auditor based in Dhaka, Bangladesh.</desc>
  <defs>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="{t['grid']}" stroke-width="1"/>
    </pattern>
    <radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{t['glow']}" stop-opacity="0.28"/>
      <stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="scan" x1="0" x2="0" y1="0" y2="1">
      <stop offset="0" stop-color="{t['accent']}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{t['accent']}" stop-opacity="0.10"/>
      <stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="bar" x1="0" x2="1">
      <stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/>
    </linearGradient>
    <clipPath id="frame"><rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14"/></clipPath>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="{W}" height="{H}" fill="{t['bg']}"/>
    <rect width="{W}" height="{H}" fill="url(#grid)"/>
    <rect x="0" y="-120" width="{W}" height="120" fill="url(#scan)">
      <animate attributeName="y" values="-120;{H}" dur="6s" repeatCount="indefinite"/>
    </rect>

    <!-- terminal title bar -->
    <rect width="{W}" height="40" fill="{t['panel']}"/>
    <line x1="0" y1="40" x2="{W}" y2="40" stroke="{t['border']}"/>
    <circle cx="24" cy="20" r="6" fill="#ff5f57"/><circle cx="44" cy="20" r="6" fill="#febc2e"/><circle cx="64" cy="20" r="6" fill="#28c840"/>
    <text x="{W / 2}" y="25" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{t['muted']}">tanim@sec-ops: ~ — zsh</text>

    <!-- left: identity -->
    <text x="56" y="96" font-family="{MONO}" font-size="17" fill="{t['muted']}"><tspan fill="{t['accent']}">tanim@sec-ops</tspan>:<tspan fill="{t['accent2']}">~</tspan>$ whoami</text>
    <text x="54" y="160" font-family="{SANS}" font-size="52" font-weight="800" fill="{t['text']}" letter-spacing="-1">Tasnim Rahman Tanim</text>
    <rect x="56" y="178" width="120" height="4" rx="2" fill="url(#bar)">
      <animate attributeName="width" values="40;120;40" dur="5s" repeatCount="indefinite"/>
    </rect>
    <text x="56" y="228" font-family="{MONO}" font-size="24" font-weight="600" fill="{t['muted']}">&gt;</text>
    {typing_block(t, 80, 228)}
    <text x="56" y="282" font-family="{SANS}" font-size="17" fill="{t['muted']}">Cybersecurity · Cloud · DevOps · Development</text>
    <text x="56" y="312" font-family="{MONO}" font-size="14" fill="{t['muted']}">📍 Dhaka, Bangladesh   ·   OCI · AWS · Azure   ·   ISO 27001 · NIST · SOC 2</text>

    <!-- right: secure core -->
    <circle cx="{cx}" cy="{cy}" r="150" fill="url(#halo)"/>
    <circle cx="{cx}" cy="{cy}" r="118" fill="none" stroke="{t['accent']}" stroke-opacity="0.25" stroke-dasharray="4 8">
      <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="40s" repeatCount="indefinite"/>
    </circle>
    {''.join(links)}
    <path d="{shield}" fill="{t['panel']}" stroke="{t['accent']}" stroke-width="2.5"/>
    <path d="{shield}" fill="none" stroke="{t['accent']}" stroke-width="2.5" opacity="0.6">
      <animate attributeName="stroke-width" values="2.5;9;2.5" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.5;0;0.5" dur="3s" repeatCount="indefinite"/>
    </path>
    <!-- padlock -->
    <path d="M{cx - 13},{cy - 2} v-11 a13,13 0 0 1 26,0 v11" fill="none" stroke="{t['accent']}" stroke-width="5" stroke-linecap="round"/>
    <rect x="{cx - 21}" y="{cy - 3}" width="42" height="32" rx="6" fill="{t['accent']}"/>
    <circle cx="{cx}" cy="{cy + 11}" r="4.5" fill="{t['panel']}"/>
    {''.join(chips)}
  </g>
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="none" stroke="{t['border']}" stroke-width="1.5"/>
</svg>
'''


STATS = [
    ("99.9%", "uptime on multi-cloud", "architectures delivered"),
    ("10+", "custom Odoo 19", "ERP modules shipped"),
    ("220+", "professionals &amp; students", "trained in SecOps"),
    ("60%", "graduate job", "placement rate"),
    ("+15%", "solution win rate", "from presales demos"),
    ("3", "clouds in production", "OCI · AWS · Azure"),
]


def impact(t):
    W, H = 1200, 150
    cell = W / len(STATS)
    out = []
    for i, (num, l1, l2) in enumerate(STATS):
        x = cell * i + cell / 2
        d = f"{0.15 * i:.2f}s"
        out.append(f'''
    <g opacity="0">
      <animate attributeName="opacity" from="0" to="1" begin="{d}" dur="0.6s" fill="freeze"/>
      <text x="{x}" y="66" text-anchor="middle" font-family="{SANS}" font-size="40" font-weight="800" fill="{t['accent']}">{num}</text>
      <text x="{x}" y="98" text-anchor="middle" font-family="{SANS}" font-size="14" fill="{t['text']}">{l1}</text>
      <text x="{x}" y="118" text-anchor="middle" font-family="{SANS}" font-size="14" fill="{t['muted']}">{l2}</text>
    </g>''')
        if i:
            out.append(f'<line x1="{cell * i}" y1="34" x2="{cell * i}" y2="{H - 30}" stroke="{t["border"]}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">Impact: 99.9% uptime, 10+ ERP modules, 220+ trained, 60% placement, +15% win rate, 3 clouds</title>
  <defs><linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/></linearGradient></defs>
  <clipPath id="c"><rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14"/></clipPath>
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{t['bg']}" stroke="{t['border']}" stroke-width="1.5"/>
  <rect x="1" y="1" width="{W - 2}" height="4" fill="url(#bar)" clip-path="url(#c)"/>
  {''.join(out)}
</svg>
'''


def divider(t):
    W, H = 1200, 24
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="presentation">
  <defs><linearGradient id="g" x1="0" x2="1">
    <stop offset="0" stop-color="{t['accent']}" stop-opacity="0"/>
    <stop offset="0.5" stop-color="{t['accent']}"/>
    <stop offset="1" stop-color="{t['accent2']}" stop-opacity="0"/>
  </linearGradient></defs>
  <rect y="11" width="{W}" height="2" fill="url(#g)"/>
  <circle cy="12" r="4" fill="{t['accent']}"><animate attributeName="cx" values="0;{W};0" dur="8s" repeatCount="indefinite"/></circle>
</svg>
'''


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, t in THEMES.items():
        (OUT / f"hero-{name}.svg").write_text(hero(t), encoding="utf-8")
        (OUT / f"impact-{name}.svg").write_text(impact(t), encoding="utf-8")
        (OUT / f"divider-{name}.svg").write_text(divider(t), encoding="utf-8")
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
