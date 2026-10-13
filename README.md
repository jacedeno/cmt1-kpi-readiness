<h1 align="center">CMT1 KPI Data Readiness</h1>
<p align="center"><em>Which SMRP maintenance KPIs SAP ECC can feed at plant CMT1</em></p>

<p align="center">
  <a href="https://jacedeno.github.io/cmt1-kpi-readiness/"><img src="https://img.shields.io/badge/live%20site-GitHub%20Pages-2ea44f?style=flat-square&logo=github&logoColor=white" alt="Live site: GitHub Pages"></a>
  <img src="https://img.shields.io/badge/type-brief-8957e5?style=flat-square" alt="Type: brief">
  <img src="https://img.shields.io/badge/language-EN-6e7781?style=flat-square" alt="Language: EN">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/HTML-static%20site-e34f26?style=flat-square&logo=html5&logoColor=white" alt="HTML static site">
  <img src="https://img.shields.io/github/last-commit/jacedeno/cmt1-kpi-readiness?style=flat-square" alt="Last commit">
</p>

## Overview

Single-page brief published with GitHub Pages: https://jacedeno.github.io/cmt1-kpi-readiness/

It checks, indicator by indicator, which SMRP maintenance KPIs the data SAP ECC already exports
can feed at plant CMT1, what is partial, and what only the planning tool can provide. Written for
the maintenance planning team.

**Read it:** https://jacedeno.github.io/cmt1-kpi-readiness/

## How the pages are built

- `src/kpi-data-readiness.html` is the source of the front page (artifact-style: title, font
  link, style, body). Rebuild with `python3 tools/wrap.py src/kpi-data-readiness.html`, which
  writes `index.html`.
- `src/*-fragment.html` are the mockup fragments (the same content shown in the visual
  companion, public-safe names). Each page is built with
  `python3 tools/mockup.py src/<name>-fragment.html <name>.html "<h1>" "<lede>" "<meta html>"`.
- Commit `index.html` and the page files together with their sources; GitHub Pages serves
  the repo root.
