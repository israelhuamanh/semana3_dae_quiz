import docx
from docx.shared import Inches

doc = docx.Document()

# Title
title = doc.add_heading('Entregable de Laboratorio 3', 0)

# Section 1
doc.add_heading('1. Nombre del alumno', level=2)
doc.add_paragraph('[Ingresa tu nombre completo aquí]')

# Section 2
doc.add_heading('2. Título del desarrollo', level=2)
doc.add_paragraph('Desarrollo de Aplicación de Cuestionarios (Quiz) con Django')

# Section 3
doc.add_heading('3. Capturas del resultado', level=2)
doc.add_paragraph('Captura 1: Lista de exámenes')
try:
    doc.add_picture(r'..\captura_lista_examenes.png', width=Inches(6.0))
except Exception as e:
    doc.add_paragraph('(No se pudo cargar la imagen)')

doc.add_paragraph('Captura 2: Detalle de un examen')
try:
    doc.add_picture(r'..\captura_detalle_examen.png', width=Inches(6.0))
except Exception as e:
    pass

doc.add_paragraph('Captura 3: Formulario de creación de preguntas y opciones')
try:
    doc.add_picture(r'..\captura_crear_pregunta.png', width=Inches(6.0))
except Exception as e:
    pass

doc.add_paragraph('Captura 4: Base de datos (Panel de Admin)')
try:
    doc.add_picture(r'..\captura_admin.png', width=Inches(6.0))
except Exception as e:
    pass

# Section 4
doc.add_heading('4. Código (Fragmentos principales)', level=2)

doc.add_heading('Modelos (quiz/models.py)', level=3)
doc.add_paragraph('''class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField(verbose_name="Text")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")
    score = models.IntegerField(default=1, verbose_name="Score")
''')

doc.add_heading('Validación de Formulario (quiz/forms.py)', level=3)
doc.add_paragraph('''class BaseChoiceFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        correct_count = sum(1 for form in self.forms if form.cleaned_data.get("is_correct"))
        if correct_count != 1:
            raise ValidationError("Exactly one choice must be correct.")
''')

# Section 5
doc.add_heading('5. Explicación del resultado y casos de prueba', level=2)
doc.add_paragraph('El proyecto implementa un sistema robusto para exámenes. Se programaron 12 casos de prueba (cumpliendo PEP 8) que validan que el sistema no guarde opciones si no existe exactamente 1 respuesta correcta. Además, se probó la adición dinámica del campo "score" mediante migraciones en SQLite.')

# Section 6
doc.add_heading('6. Captura de la estructura del proyecto en el editor', level=2)
doc.add_paragraph('(Por favor, agrega una pequeña captura de las carpetas de tu VS Code aquí)')

# Section 7
doc.add_heading('7. Justificación de Tipos de Campo', level=2)
doc.add_paragraph('1. CharField en Exam.title: Ahorra espacio en la base de datos al limitar la cadena a 200 caracteres, a diferencia de TextField.')
doc.add_paragraph('2. DateTimeField en Exam.created_at: Automatiza el registro de la fecha con auto_now_add=True.')
doc.add_paragraph('3. ForeignKey en Question.exam: Garantiza la relación y evita registros huérfanos gracias a on_delete=CASCADE.')

# Conclusions
doc.add_heading('Conclusiones', level=2)
doc.add_paragraph('1. El uso de inlineformset_factory de Django demostró ser la forma más eficiente de guardar objetos relacionados (preguntas y opciones) en una sola petición HTTP.')
doc.add_paragraph('2. Sobrescribir el método clean() en el FormSet es fundamental para garantizar reglas de negocio estrictas a nivel de backend y evitar datos inconsistentes.')
doc.add_paragraph('3. El sistema de migraciones permitió agregar el atributo "score" de forma rápida y segura, sin corromper los registros previos de la tabla.')
doc.add_paragraph('4. Mantener el SECRET_KEY fuera de settings.py utilizando variables de entorno (.env) es una práctica obligatoria para evitar vulnerabilidades.')
doc.add_paragraph('5. Cumplir con PEP 8 y crear casos de prueba (tests.py) es vital para asegurar que el proyecto pueda ser mantenido sin generar errores a largo plazo.')

# GitHub Link
doc.add_heading('Repositorio', level=2)
doc.add_paragraph('Enlace a GitHub: https://github.com/israelhuamanh/semana3_dae_quiz')

doc.save(r'..\ENTREGABLE_COMPLETO.docx')
