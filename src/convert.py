import markdown
import os

with open(r'..\ENTREGABLE.md', 'r', encoding='utf-8') as f:
    text = f.read()

html_body = markdown.markdown(text, extensions=['fenced_code', 'tables'])

html = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }}
        h1, h2, h3 {{ color: #333; }}
        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
        code {{ background: #f4f4f4; padding: 2px 4px; border-radius: 3px; font-family: monospace; }}
    </style>
</head>
<body>
{{html_body}}
</body>
</html>
'''

with open(r'..\ENTREGABLE.html', 'w', encoding='utf-8') as f:
    f.write(html)
