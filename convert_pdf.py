import sys
from xhtml2pdf import pisa

with open('ENTREGABLE.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('ENTREGABLE.pdf', 'wb') as f:
    pisa_status = pisa.CreatePDF(html, dest=f)

if pisa_status.err:
    print('Error creating PDF')
    sys.exit(1)
print('PDF created successfully!')
