import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Answer(models.Model):
    """Main Answer model"""
    answer = models.CharField('Answer', max_length=255, unique=True)

    def __str__(self):
        return "{}".format(self.answer)


class Question(models.Model):
    """Main Questions model"""
    question = models.CharField('Question', max_length=255)
    answer_id = models.ForeignKey(Answer, to_field='answer', db_column='Answer',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.question)


class DemoAnswer(models.Model):
    """Demo Answer model"""
    demo_answer = models.CharField('DemoAnswer', max_length=255, unique=True)

    def __str__(self):
        return "{}".format(self.demo_answer)


class DemoQuestion(models.Model):
    """Demo Questions model"""
    demo_question = models.CharField('DemoQuestions', max_length=255)
    demo_answer = models.ForeignKey(DemoAnswer, to_field='demo_answer', db_column='DemoAnswer',
                                    on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.demo_question)


class DemoUserTest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    demoUserEmail = models.EmailField(_("Demo User Email"), blank=True, max_length=255)
    dateOfStart = models.DateField(_("Day of Start Demo Test"), auto_now=False, auto_now_add=True)
    timeStart = models.TimeField(_("Start Time of Demo Test"), auto_now=False, auto_now_add=True, null=False)
    timeEnd = models.TimeField(_("End Time of Demo Test"), null=True)

    def __str__(self):
        return "{} - {}".format(self.demoUserEmail, self.dateOfStart)
