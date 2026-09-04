from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from .models import Exam
from .forms import ExamForm, QuestionForm, ChoiceFormSet


def exam_list(request):
    exams = Exam.objects.all()
    return render(request, "quiz/exam_list.html", {"exams": exams})


def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    questions = exam.questions.all().prefetch_related("choices")
    return render(
        request,
        "quiz/exam_detail.html",
        {"exam": exam, "questions": questions},
    )


def exam_create(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            return redirect("quiz:exam_detail", pk=exam.pk)
    else:
        form = ExamForm()
    return render(request, "quiz/exam_form.html", {"form": form})


def question_create(request, exam_pk):
    exam = get_object_or_404(Exam, pk=exam_pk)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        formset = ChoiceFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                question = form.save(commit=False)
                question.exam = exam
                question.save()
                formset.instance = question
                formset.save()
            return redirect("quiz:exam_detail", pk=exam.pk)
    else:
        form = QuestionForm()
        formset = ChoiceFormSet()

    return render(
        request,
        "quiz/question_form.html",
        {"form": form, "formset": formset, "exam": exam},
    )
