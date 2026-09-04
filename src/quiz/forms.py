from django import forms
from django.core.exceptions import ValidationError
from .models import Exam, Question, Choice


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ["title", "description"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text", "order"]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["text", "is_correct"]


class BaseChoiceFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        if any(self.errors):
            return

        correct_count = 0
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
            is_correct = form.cleaned_data.get("is_correct")
            if is_correct:
                correct_count += 1

        if correct_count != 1:
            raise ValidationError("Exactly one choice must be correct.")


ChoiceFormSet = forms.inlineformset_factory(
    Question,
    Choice,
    form=ChoiceForm,
    formset=BaseChoiceFormSet,
    extra=4,
    can_delete=False,
)
