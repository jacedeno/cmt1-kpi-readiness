"""Wrap a visual-companion mockup fragment into a standalone page of this site.

usage: python3 tools/mockup.py <fragment.html> <out.html> "<h1>" "<lede>" "<meta html>"
Tokens (colors, dark mode) are copied from the brief's source page so both match.
"""
import re
import sys

FRAGMENT, OUT, H1, LEDE, META = sys.argv[1:6]
BRIEF = "index.html"

brief = open(BRIEF).read()
tokens = re.search(r"(  :root \{.*?\n  \})\n(?=\s*\*, \*::before|\s*body)", brief, re.S).group(1)
frag = open(FRAGMENT).read()
mstyle = re.search(r"<style>(.*?)</style>", frag, re.S).group(1)
body = re.sub(r"<style>.*?</style>\s*", "", frag, flags=re.S)
body = body.replace(' onclick="toggleSelect(this)"', "")
body = re.sub(r"Click the one that matches[^.]*\.", "The layout is chosen with the planning team; the three are shown so the choice can be discussed.", body)
title = re.sub(r"<[^>]+>", "", H1)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap">
<style>
  html {{ color-scheme: light dark; }}
{tokens}
  *, *::before, *::after {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--paper); color: var(--ink); font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', sans-serif; font-size: 15px; line-height: 1.5; }}
  .wrap {{ max-width: 1080px; margin: 0 auto; padding-block: 32px 56px; padding-inline: 16px; }}
  header {{ border-bottom: 3px solid var(--green); padding-bottom: 18px; margin-bottom: 28px; }}
  .eyebrow {{ font-size: 12px; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; color: var(--green); margin-bottom: 8px; }}
  h1 {{ font-size: clamp(26px, 4vw, 36px); line-height: 1.15; margin: 0 0 10px; font-weight: 700; text-wrap: balance; }}
  h2 {{ font-size: 20px; margin: 0 0 6px; font-weight: 700; }}
  .lede {{ max-width: 68ch; color: var(--muted); margin: 0; }}
  .meta {{ display: flex; flex-wrap: wrap; gap: 8px 22px; margin-top: 14px; font-size: 13px; color: var(--muted); }}
  .meta b {{ color: var(--ink); font-weight: 600; }}
  a {{ color: var(--green); }}
  .back {{ display: inline-block; margin-bottom: 18px; font-size: 14px; font-weight: 600; text-decoration: none; }}
  .back:hover {{ text-decoration: underline; }}
  .subtitle {{ color: var(--muted); max-width: 72ch; margin: 0 0 20px; }}
  .options {{ display: flex; flex-direction: column; gap: 16px; }}
  .option {{ background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 16px 18px; display: flex; align-items: flex-start; gap: 14px; }}
  .option .letter {{ background: var(--green-soft); color: var(--green-ink); width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0; }}
  .option .content {{ flex: 1; min-width: 0; }}
  .option .content h3 {{ font-size: 17px; margin: 2px 0 6px; }}
  .option .content > p {{ color: var(--muted); font-size: 14px; margin: 0 0 6px; max-width: 72ch; }}
  .legend {{ display: flex; flex-wrap: wrap; gap: 8px 18px; font-size: 13px; color: var(--muted); margin: 0 0 18px; }}
  .legend i {{ display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 6px; vertical-align: -1px; }}
{mstyle}
  .wire {{ overflow-x: auto; }}
  .steps {{ margin: 6px 0 12px; padding-left: 20px; font-size: 14px; line-height: 1.45; max-width: 72ch; }}
  .steps li {{ margin-bottom: 3px; }}
  .steps b {{ color: var(--green-ink); }}
  .note {{ margin-top: 18px; background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--gold); border-radius: 10px; padding: 14px 18px; font-size: 14.5px; line-height: 1.5; color: var(--ink); }}
  .note b {{ color: var(--green-ink); }}
</style>
</head>
<body>
<div class="wrap">
  <a class="back" href="./">&larr; Back to the KPI data readiness brief</a>
  <header>
    <div class="eyebrow">Capitol Aggregates · Cement plant CMT1 · Maintenance planning · Design proposal</div>
    <h1>{H1}</h1>
    <p class="lede">{LEDE}</p>
    <div class="meta">{META}</div>
  </header>
  <div class="legend"><span><i style="background:#2d6a2e"></i>Corrective order</span><span><i style="background:#d05252"></i>Priority 1</span><span><i style="background:#3b6fd6"></i>Preventive (ZP01)</span><span><i style="background:#e8a817"></i>Planned overtime / break-in</span></div>
{body}
</div>
</body>
</html>
"""
open(OUT, "w").write(html)
print(OUT, len(html), "bytes")
