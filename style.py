PALETTE = {
    "ink": "#14231A",
    "surface": "#1C2E20",
    "surface_dim": "#233826",
    "paper": "#F4EFDD",
    "paper_dim": "#EAE3CB",
    "leaf": "#6FA37D",
    "amber": "#D98F52",
    "rust": "#C15C5C",
    "line": "#DCD3B8",
    "line_dark": "#33452F",
    "text_on_paper": "#2A2118",
    "text_on_ink": "#EFE9D6",
    "text_muted": "#8FA893",
}


def get_css() -> str:
    p = PALETTE
    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+Tamil:wght@400;500;600&display=swap');

:root {{
    --ink: {p['ink']};
    --surface: {p['surface']};
    --surface-dim: {p['surface_dim']};
    --paper: {p['paper']};
    --paper-dim: {p['paper_dim']};
    --leaf: {p['leaf']};
    --amber: {p['amber']};
    --rust: {p['rust']};
    --line: {p['line']};
    --line-dark: {p['line_dark']};
    --text-paper: {p['text_on_paper']};
    --text-ink: {p['text_on_ink']};
    --text-muted: {p['text_muted']};
}}

/* ---------- base ---------- */
.stApp {{
    background-color: var(--ink);
    background-image: radial-gradient(var(--line-dark) 0.9px, transparent 0.9px);
    background-size: 22px 22px;
    color: var(--text-ink);
}}

html, body, [class*="css"] {{
    font-family: 'Inter', 'Noto Sans Tamil', sans-serif;
}}

h1, h2, h3, .display {{
    font-family: 'Fraunces', 'Noto Sans Tamil', serif;
    font-weight: 500;
    letter-spacing: -0.01em;
    color: var(--text-ink);
}}

.stApp p, .stApp li, .stApp label {{
    font-family: 'Inter', 'Noto Sans Tamil', sans-serif;
    color: var(--text-ink);
}}

::selection {{ background: var(--amber); color: var(--ink); }}

#MainMenu, footer {{ visibility: hidden; }}

/* ---------- eyebrow / kicker ---------- */
.kicker {{
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--amber);
    margin-bottom: 0.6rem;
}}

/* ---------- buttons ---------- */
.stButton > button, .stLinkButton > a, [data-testid="stPageLink"] a {{
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    font-size: 0.9rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    background: var(--amber);
    color: var(--ink) !important;
    border: none;
    border-radius: 2px;
    padding: 0.85rem 1.4rem;
    text-align: center;
    justify-content: center;
    transition: background 0.15s ease, transform 0.15s ease;
}}
.stButton > button:hover, .stLinkButton > a:hover, [data-testid="stPageLink"] a:hover {{
    background: var(--leaf);
    color: var(--paper) !important;
    transform: translateY(-1px);
}}
[data-testid="stPageLink"] p {{
    color: inherit !important;
}}
.quiet-link [data-testid="stPageLink"] a {{
    background: transparent !important;
    color: var(--text-muted) !important;
    text-transform: none;
    font-size: 0.78rem;
    padding: 0.3rem 0;
    border-bottom: 1px dotted var(--text-muted);
    border-radius: 0;
}}
.quiet-link [data-testid="stPageLink"] a:hover {{
    background: transparent !important;
    color: var(--leaf) !important;
    border-bottom-color: var(--leaf);
    transform: none;
}}

.stButton > button[kind="secondary"] {{
    background: var(--surface-dim) !important;
    color: var(--text-muted) !important;
    border: 1px solid var(--line-dark) !important;
    padding: 0.5rem 0.8rem;
    font-size: 0.78rem;
}}
.stButton > button[kind="secondary"]:hover {{
    background: var(--surface-dim) !important;
    color: var(--text-ink) !important;
    transform: none;
}}
.stButton > button[kind="primary"] {{
    padding: 0.5rem 0.8rem;
    font-size: 0.78rem;
}}

/* ---------- file uploader (viewfinder / scanner motif) ---------- */
[data-testid="stFileUploaderDropzone"] {{
    position: relative;
    background: var(--surface);
    border: 1px solid var(--line-dark);
    border-radius: 3px;
}}
[data-testid="stFileUploaderDropzone"]::before,
[data-testid="stFileUploaderDropzone"]::after {{
    content: "";
    position: absolute;
    width: 18px; height: 18px;
    border: 2px solid var(--amber);
    pointer-events: none;
}}
[data-testid="stFileUploaderDropzone"]::before {{
    top: 6px; left: 6px;
    border-right: none; border-bottom: none;
}}
[data-testid="stFileUploaderDropzone"]::after {{
    bottom: 6px; right: 6px;
    border-left: none; border-top: none;
}}
[data-testid="stFileUploaderDropzone"] * {{
    color: var(--text-ink) !important;
    font-family: 'Inter', 'Noto Sans Tamil', sans-serif;
}}
[data-testid="stFileUploaderDropzone"] button {{
    background: var(--amber) !important;
    color: var(--ink) !important;
}}

/* ---------- sidebar ---------- */
[data-testid="stSidebar"] {{
    background: var(--surface);
    border-right: 1px solid var(--line-dark);
}}
[data-testid="stSidebar"] * {{
    color: var(--text-ink) !important;
}}

/* ---------- specimen label card ---------- */
.specimen-card {{
    position: relative;
    background: var(--surface);
    color: var(--text-ink);
    border: 1px solid var(--line-dark);
    border-radius: 2px;
    padding: 1.75rem 1.75rem 1.5rem 1.75rem;
    margin-top: 1.2rem;
    overflow: hidden;
}}
.specimen-card::before {{
    content: "";
    position: absolute;
    top: -1px; left: 0; right: 0;
    height: 8px;
    background-image: linear-gradient(135deg, var(--ink) 50%, transparent 50%),
                       linear-gradient(45deg, var(--ink) 50%, transparent 50%);
    background-size: 14px 16px;
    background-position: top;
    background-repeat: repeat-x;
}}
.specimen-card::after {{
    content: "";
    position: absolute;
    bottom: -20px; right: -20px;
    width: 140px; height: 140px;
    border: 2px solid var(--leaf);
    border-radius: 0 100% 0 100%;
    opacity: 0.18;
}}
.specimen-label {{
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-muted);
}}
.specimen-name {{
    font-family: 'Fraunces', 'Noto Sans Tamil', serif;
    font-style: italic;
    font-weight: 500;
    font-size: 1.6rem;
    color: var(--text-ink);
    margin: 0.15rem 0 0.9rem 0;
}}

/* ---------- confidence gauge ---------- */
.gauge-row {{
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin: 0.35rem 0;
}}
.gauge-track {{
    position: relative;
    flex: 1;
    height: 6px;
    background: var(--surface-dim);
    border: 1px solid var(--line-dark);
    border-radius: 1px;
}}
.gauge-fill {{
    position: absolute;
    top: -1px; left: -1px; bottom: -1px;
    border-radius: 1px;
}}
.gauge-tick {{
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    font-size: 0.78rem;
    color: var(--text-ink);
    min-width: 3.4rem;
    text-align: right;
}}
.gauge-class {{
    font-family: 'Inter', 'Noto Sans Tamil', sans-serif;
    font-size: 0.85rem;
    color: var(--text-ink);
    min-width: 11rem;
}}

/* ---------- radial dial ---------- */
.dial-wrap {{
    display: flex;
    align-items: center;
    gap: 1.4rem;
    margin-bottom: 1.1rem;
}}
.dial {{
    position: relative;
    width: 92px; height: 92px;
    border-radius: 50%;
    flex-shrink: 0;
}}
.dial-inner {{
    position: absolute;
    top: 8px; left: 8px; right: 8px; bottom: 8px;
    background: var(--surface);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1.05rem;
    color: var(--text-ink);
}}
.dial-meta .specimen-label {{ margin-bottom: 0.2rem; }}

/* ---------- other-match ticks ---------- */
.tick-row {{
    display: flex;
    align-items: center;
    gap: 0.7rem;
    padding: 0.3rem 0;
    border-top: 1px solid var(--line-dark);
}}
.tick-row:first-of-type {{ border-top: none; }}
.tick-dot {{
    width: 6px; height: 6px;
    border-radius: 50%;
    flex-shrink: 0;
}}
.tick-name {{
    font-family: 'Inter', 'Noto Sans Tamil', sans-serif;
    font-size: 0.82rem;
    color: var(--text-muted);
    flex: 1;
}}
.tick-value {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: var(--text-muted);
}}

/* ---------- topbar / brand header ---------- */
.topbar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.2rem 0 1.1rem 0;
    border-bottom: 1px solid var(--line-dark);
    margin-bottom: 1.6rem;
}}
.brand {{
    display: flex;
    align-items: center;
    gap: 0.55rem;
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    font-size: 0.82rem;
    color: var(--text-ink);
}}
.brand svg {{ width: 24px; height: 24px; flex-shrink: 0; }}
.topbar-right {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.66rem;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    text-align: right;
}}

/* ---------- species index grid ---------- */
.species-card {{
    background: var(--surface);
    border: 1px solid var(--line-dark);
    border-radius: 2px;
    overflow: hidden;
    margin-bottom: 1rem;
}}
.species-card-label {{
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.04em;
    color: var(--text-ink);
    padding: 0.5rem 0.6rem;
    border-top: 1px solid var(--line-dark);
}}

/* ---------- care guide ---------- */
.care-card {{
    background: var(--surface);
    border: 1px solid var(--line-dark);
    border-radius: 2px;
    padding: 1.4rem 1.6rem;
    margin-top: 1rem;
}}
.care-row {{ margin-bottom: 1rem; }}
.care-row:last-child {{ margin-bottom: 0; }}
.care-heading {{
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}}
.care-text {{
    font-family: 'Inter', 'Noto Sans Tamil', sans-serif;
    font-size: 0.88rem;
    line-height: 1.5;
    color: var(--text-ink);
}}
.care-disclaimer {{
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    font-size: 0.65rem;
    color: var(--text-muted);
    margin-top: 1.1rem;
    padding-top: 0.8rem;
    border-top: 1px solid var(--line-dark);
    line-height: 1.5;
}}

/* ---------- hairline ---------- */
.hairline {{
    border: none;
    border-top: 1px solid var(--line-dark);
    margin: 1.6rem 0;
}}

/* ---------- expander (care timeline) ---------- */
[data-testid="stExpander"] {{
    background: var(--surface);
    border: 1px solid var(--line-dark);
    border-radius: 2px;
    margin-top: 0.6rem;
}}
[data-testid="stExpander"] summary {{
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    font-size: 0.78rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--text-ink) !important;
}}
[data-testid="stExpander"] .care-row {{
    border-top: 1px solid var(--line-dark);
    padding-top: 0.8rem;
}}
[data-testid="stExpander"] .care-row:first-child {{
    border-top: none;
    padding-top: 0;
}}

/* ---------- vertical farm animation (home page signature) ----------
   A full SVG scene: 3 shelves of plants cycling through a growth
   loop, pulsing grow-light bars, an irrigation pipe with falling
   water droplets, and a spinning ventilation fan. All CSS-driven, no
   external video/image file or network dependency — renders
   instantly and works fully offline. */
.farm-scene-wrap {{
    max-width: 360px;
    margin: 0 auto;
    background: var(--surface);
    border: 1px solid var(--line-dark);
    border-radius: 4px;
    padding: 0.8rem;
}}
.farm-plant {{
    animation: farm-grow 4s ease-in-out infinite;
    transform-box: fill-box;
    transform-origin: bottom center;
}}
.farm-light {{
    animation: farm-light-pulse 2.6s ease-in-out infinite;
}}
.farm-droplet {{
    animation: farm-droplet-fall 2.2s ease-in infinite;
}}
.farm-fan-blade {{
    animation: farm-fan-spin 3.5s linear infinite;
    transform-box: fill-box;
    transform-origin: center;
}}
@keyframes farm-grow {{
    0%, 100% {{ transform: scaleY(0.75); opacity: 0.75; }}
    50% {{ transform: scaleY(1); opacity: 1; }}
}}
@keyframes farm-light-pulse {{
    0%, 100% {{ opacity: 0.45; }}
    50% {{ opacity: 0.95; }}
}}
@keyframes farm-droplet-fall {{
    0% {{ transform: translateY(0); opacity: 0; }}
    15% {{ opacity: 1; }}
    85% {{ opacity: 1; }}
    100% {{ transform: translateY(46px); opacity: 0; }}
}}
@keyframes farm-fan-spin {{
    from {{ transform: rotate(0deg); }}
    to {{ transform: rotate(360deg); }}
}}

/* ---------- home tool cards ---------- */
.tool-card {{
    background: var(--surface);
    border: 1px solid var(--line-dark);
    border-radius: 2px;
    padding: 1.2rem 1.3rem;
    height: 100%;
}}
.tool-card-title {{
    font-family: 'Fraunces', 'Noto Sans Tamil', serif;
    font-style: italic;
    font-weight: 500;
    font-size: 1.15rem;
    color: var(--text-ink);
    margin-bottom: 0.4rem;
}}
.tool-card-desc {{
    font-family: 'Inter', 'Noto Sans Tamil', sans-serif;
    font-size: 0.82rem;
    color: var(--text-muted);
    line-height: 1.5;
    min-height: 3.6em;
}}
</style>
"""


def get_topbar_html(right_text="", wordmark="Field Notes"):
    leaf = PALETTE["leaf"]
    right_html = f'<div class="topbar-right">{right_text}</div>' if right_text else ""
    return (
        '<div class="topbar">'
        '<div class="brand">'
        f'<svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">'
        f'<circle cx="16" cy="16" r="14.5" fill="none" stroke="{leaf}" stroke-width="1.3"/>'
        f'<path d="M16 8 C 21 10, 23 15, 21 20 C 19 24, 16 25, 16 25 '
        f'C 16 25, 13 24, 11 20 C 9 15, 11 10, 16 8 Z" '
        f'fill="none" stroke="{leaf}" stroke-width="1.3"/>'
        f'<path d="M16 9 L16 24.5" stroke="{leaf}" stroke-width="0.9" opacity="0.7"/>'
        f'</svg>'
        f'<span>{wordmark}</span>'
        '</div>'
        f'{right_html}'
        '</div>'
    )


def get_farm_rack_html():
    """
    Full SVG vertical-farm scene, built as original vector art (no
    external image/video file, no hotlinked photo — avoids copyright
    risk and works fully offline):
      - 3 shelves, 3 plants each, each plant looping through a gentle
        grow cycle on a staggered delay
      - a grow-light bar above each shelf, pulsing like an active
        fixture
      - a side irrigation pipe with droplets that fall and fade on a
        loop, staggered per shelf
      - a small ventilation fan in the corner, spinning continuously
    Everything is CSS-animated (see .farm-* keyframes in get_css()),
    so it plays immediately with zero network dependency.
    """
    leaf = PALETTE["leaf"]
    amber = PALETTE["amber"]
    line_dark = PALETTE["line_dark"]
    surface_dim = PALETTE["surface_dim"]
    muted = PALETTE["text_muted"]

    def plant(cx, y_base, delay, scale=1.0):
        return (
            f'<g class="farm-plant" style="animation-delay:{delay:.2f}s;" '
            f'transform="translate({cx},{y_base}) scale({scale})">'
            f'<path d="M0 0 L0 -16" stroke="{leaf}" stroke-width="1.6"/>'
            f'<path d="M0 -14 C -7 -15, -9 -22, -6 -27 C -3 -22, -1 -18, 0 -14 Z" fill="{leaf}" opacity="0.9"/>'
            f'<path d="M0 -10 C 8 -11, 10 -18, 7 -23 C 4 -18, 2 -14, 0 -10 Z" fill="{leaf}" opacity="0.7"/>'
            f'</g>'
        )

    def droplet(cx, y, delay):
        return f'<circle class="farm-droplet" cx="{cx}" cy="{y}" r="2.2" fill="#7EB8D9" style="animation-delay:{delay:.2f}s;"/>'

    shelves_y = [70, 140, 210]
    plant_x = [70, 150, 230]

    shelves_svg = ""
    delay = 0.0
    for si, sy in enumerate(shelves_y):
        # grow-light bar above the shelf
        shelves_svg += (
            f'<rect class="farm-light" x="30" y="{sy - 34}" width="290" height="5" rx="2.5" '
            f'fill="{amber}" style="animation-delay:{si * 0.6:.1f}s;"/>'
        )
        # shelf surface
        shelves_svg += f'<rect x="30" y="{sy}" width="290" height="6" rx="2" fill="{surface_dim}" stroke="{line_dark}" stroke-width="1"/>'
        # plants on this shelf
        for px in plant_x:
            shelves_svg += plant(px, sy, delay)
            delay += 0.4
        # irrigation droplet near the pipe for this shelf
        shelves_svg += droplet(24, sy - 30, si * 0.7)

    svg = (
        f'<svg viewBox="0 0 340 260" width="100%" style="max-width:340px; display:block; margin:0 auto;">'
        # frame posts
        f'<line x1="20" y1="20" x2="20" y2="250" stroke="{line_dark}" stroke-width="2"/>'
        f'<line x1="320" y1="20" x2="320" y2="250" stroke="{line_dark}" stroke-width="2"/>'
        # irrigation pipe (left side)
        f'<line x1="24" y1="20" x2="24" y2="250" stroke="{muted}" stroke-width="1.5" opacity="0.5"/>'
        f'{shelves_svg}'
        # small ventilation fan, top right corner
        f'<g transform="translate(300,32)">'
        f'<circle r="12" fill="none" stroke="{line_dark}" stroke-width="1.5"/>'
        f'<g class="farm-fan-blade">'
        f'<path d="M0 0 L0 -9 C 4 -9, 4 -3, 0 0 Z" fill="{leaf}" opacity="0.8"/>'
        f'<path d="M0 0 L8 3 C 8 7, 2 6, 0 0 Z" fill="{leaf}" opacity="0.8"/>'
        f'<path d="M0 0 L-8 3 C -8 7, -2 6, 0 0 Z" fill="{leaf}" opacity="0.8"/>'
        f'</g>'
        f'</g>'
        f'</svg>'
    )

    return f'<div class="farm-scene-wrap">{svg}</div>'