with open('ENTREGABLE.md', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('path/to/exam_list_capture.png', './docs/captura_lista_examenes.png')
text = text.replace('path/to/exam_detail_capture.png', './docs/captura_detalle_examen.png')
text = text.replace('path/to/question_form_capture.png', './docs/captura_crear_pregunta.png')
text = text.replace('path/to/db_capture.png', './docs/captura_admin.png')

with open('ENTREGABLE.md', 'w', encoding='utf-8') as f:
    f.write(text)
