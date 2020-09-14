from django.db import models


class Tests(models.Model):
    pass


class Questions(models.Model):
    question = models.CharField('Question', max_length=255)
    answer_id = models.ForeignKey('Answer', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.question)


class Answer(models.Model):
    answer = models.CharField('Answer', max_length=255)
    question_id = models.ForeignKey('Questions', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.answer)
