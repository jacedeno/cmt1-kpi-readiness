# CMT1 KPI Data Readiness

Single-page brief published with GitHub Pages: https://jacedeno.github.io/cmt1-kpi-readiness/

## How the pages are built

- `src/kpi-data-readiness.html` is the source of the front page (artifact-style: title, font
  link, style, body). Rebuild with `python3 tools/wrap.py src/kpi-data-readiness.html`, which
  writes `index.html`.
- `src/*-fragment.html` are the mockup fragments (the same content shown in the visual
  companion, public-safe names). Each page is built with
  `python3 tools/mockup.py src/<name>-fragment.html <name>.html "<h1>" "<lede>" "<meta html>"`.
- Commit `index.html` and the page files together with their sources; GitHub Pages serves
  the repo root.
