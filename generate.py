#!/usr/bin/env python3
"""Generate index.html from data.json using template.html."""

import json
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Load data
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

# Render template
env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape(["html"]))
template = env.get_template("template.jinja")
html = template.render(managers=data['managers'])

# Write output
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated index.html with {len(data['managers'])} managers")
