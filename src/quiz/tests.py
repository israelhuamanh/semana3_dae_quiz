from django.test import TestCase, Client
from django.urls import reverse
from .models import Exam, Question, Choice
from .forms import ChoiceFormSet


class ExamModelTest(TestCase):
    def test_exam_str(self):
        exam = Exam.objects.create(title="Math Test", description="Basic Math")
        self.assertEqual(str(exam), "Math Test")


class QuestionModelTest(TestCase):
    def test_question_str(self):
        exam = Exam.objects.create(title="Math Test")
        question = Question.objects.create(exam=exam, text="What is 2+2?")
        self.assertEqual(str(question), "Math Test - What is 2+2?")


class ChoiceModelTest(TestCase):
    def test_choice_str(self):
        exam = Exam.objects.create(title="Math Test")
        question = Question.objects.create(exam=exam, text="What is 2+2?")
        choice = Choice.objects.create(question=question, text="4", is_correct=True)
        self.assertEqual(str(choice), "4")


class BusinessRuleTest(TestCase):
    def setUp(self):
        self.exam = Exam.objects.create(title="Math Test")
        self.question = Question.objects.create(exam=self.exam, text="What is 2+2?")

    def test_exactly_one_correct_choice_valid(self):
        data = {
            'choices-TOTAL_FORMS': '4',
            'choices-INITIAL_FORMS': '0',
            'choices-MIN_NUM_FORMS': '0',
            'choices-MAX_NUM_FORMS': '1000',
            'choices-0-text': '3', 'choices-0-is_correct': '',
            'choices-1-text': '4', 'choices-1-is_correct': 'on',
            'choices-2-text': '5', 'choices-2-is_correct': '',
            'choices-3-text': '6', 'choices-3-is_correct': '',
        }
        formset = ChoiceFormSet(data=data, instance=self.question)
        self.assertTrue(formset.is_valid())

    def test_zero_correct_choices_invalid(self):
        data = {
            'choices-TOTAL_FORMS': '4',
            'choices-INITIAL_FORMS': '0',
            'choices-MIN_NUM_FORMS': '0',
            'choices-MAX_NUM_FORMS': '1000',
            'choices-0-text': '3', 'choices-0-is_correct': '',
            'choices-1-text': '4', 'choices-1-is_correct': '',
            'choices-2-text': '5', 'choices-2-is_correct': '',
            'choices-3-text': '6', 'choices-3-is_correct': '',
        }
        formset = ChoiceFormSet(data=data, instance=self.question)
        self.assertFalse(formset.is_valid())
        self.assertIn("Exactly one choice must be correct.", formset.non_form_errors())

    def test_multiple_correct_choices_invalid(self):
        data = {
            'choices-TOTAL_FORMS': '4',
            'choices-INITIAL_FORMS': '0',
            'choices-MIN_NUM_FORMS': '0',
            'choices-MAX_NUM_FORMS': '1000',
            'choices-0-text': '3', 'choices-0-is_correct': 'on',
            'choices-1-text': '4', 'choices-1-is_correct': 'on',
            'choices-2-text': '5', 'choices-2-is_correct': '',
            'choices-3-text': '6', 'choices-3-is_correct': '',
        }
        formset = ChoiceFormSet(data=data, instance=self.question)
        self.assertFalse(formset.is_valid())
        self.assertIn("Exactly one choice must be correct.", formset.non_form_errors())


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.exam = Exam.objects.create(title="Science Test")

    def test_exam_list_view(self):
        url = reverse('quiz:exam_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Science Test")

    def test_exam_detail_view(self):
        url = reverse('quiz:exam_detail', args=[self.exam.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Science Test")

    def test_exam_create_view_get(self):
        url = reverse('quiz:exam_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_exam_create_view_post(self):
        url = reverse('quiz:exam_create')
        response = self.client.post(url, {'title': 'History Test', 'description': 'History description'})
        self.assertEqual(response.status_code, 302)  # Redirects after successful creation
        self.assertTrue(Exam.objects.filter(title="History Test").exists())

    def test_question_create_view_get(self):
        url = reverse('quiz:question_create', args=[self.exam.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_question_create_view_post(self):
        url = reverse('quiz:question_create', args=[self.exam.pk])
        data = {
            'text': 'What is H2O?',
            'order': 1,
            'choices-TOTAL_FORMS': '4',
            'choices-INITIAL_FORMS': '0',
            'choices-MIN_NUM_FORMS': '0',
            'choices-MAX_NUM_FORMS': '1000',
            'choices-0-text': 'Water', 'choices-0-is_correct': 'on',
            'choices-1-text': 'Air', 'choices-1-is_correct': '',
            'choices-2-text': 'Fire', 'choices-2-is_correct': '',
            'choices-3-text': 'Earth', 'choices-3-is_correct': '',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Question.objects.filter(text="What is H2O?").exists())
        self.assertTrue(Choice.objects.filter(text="Water", is_correct=True).exists())
