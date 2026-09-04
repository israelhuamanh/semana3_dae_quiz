from django.db import models


class Exam(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At"
    )

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Question(models.Model):
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name="Exam",
    )
    text = models.TextField(verbose_name="Text")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")
    score = models.IntegerField(default=1, verbose_name="Score")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ["order"]

    def __str__(self):
        return f"{self.exam.title} - {self.text[:50]}"


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name="Question",
    )
    text = models.CharField(max_length=255, verbose_name="Text")
    is_correct = models.BooleanField(default=False, verbose_name="Is Correct")

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
        ordering = ["id"]

    def __str__(self):
        return self.text
