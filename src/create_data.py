import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User
from quiz.models import Exam, Question, Choice

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

exam, created = Exam.objects.get_or_create(title='Python Basics', defaults={'description':'Test your Python knowledge'})
if created:
    q1 = Question.objects.create(exam=exam, text='What is PEP 8?', order=1, score=5)
    Choice.objects.create(question=q1, text='A style guide', is_correct=True)
    Choice.objects.create(question=q1, text='A web framework', is_correct=False)
    Choice.objects.create(question=q1, text='An ORM', is_correct=False)
    Choice.objects.create(question=q1, text='A testing tool', is_correct=False)

    q2 = Question.objects.create(exam=exam, text='What does Django use for DB?', order=2, score=5)
    Choice.objects.create(question=q2, text='SQLAlchemy', is_correct=False)
    Choice.objects.create(question=q2, text='Django ORM', is_correct=True)
    Choice.objects.create(question=q2, text='Peewee', is_correct=False)
    Choice.objects.create(question=q2, text='Pony', is_correct=False)

print('Data created successfully!')
