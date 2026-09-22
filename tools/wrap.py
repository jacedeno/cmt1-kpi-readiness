"""Wrap the artifact-style page (title + link + style + body) into a full HTML document."""
import re
import sys

src = open(sys.argv[1]).read()
title = re.search(r"<title>(.*?)</title>", src).group(1)
body = src.replace(f"<title>{title}</title>\n", "", 1)
link = re.search(r"<link[^>]*>\n", body).group(0)
body = body.replace(link, "", 1)
style = re.search(r"<style>.*?</style>\n", body, re.S).group(0)
body = body.replace(style, "", 1)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
{link}<style>
  html {{ color-scheme: light dark; }}
  body {{ margin: 0; }}
  img {{ max-width: 100%; }}
</style>
{style}</head>
<body>
{body}</body>
</html>
"""
open("index.html", "w").write(html)
print("index.html", len(html), "bytes")
