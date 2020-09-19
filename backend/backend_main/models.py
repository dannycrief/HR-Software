from django.db import models


class Tests(models.Model):
    """Main tests model"""
    question_id = models.ForeignKey('Questions', on_delete=models.CASCADE)
    answer_id = models.ForeignKey('Answers', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.question_id)


class Questions(models.Model):
    """Main Questions model"""
    question = models.CharField('Question', max_length=255)
    answer_id = models.ForeignKey('Answers', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.question)


class Answers(models.Model):
    """Main Answer model"""
    answer = models.CharField('Answer', max_length=255)

    def __str__(self):
        return "{}".format(self.answer)


# Demo Tests models
class DemoTests(models.Model):
    """Demo tests model"""
    demo_question_id = models.ForeignKey('DemoQuestions', on_delete=models.CASCADE)
    demo_answer_id = models.ForeignKey('DemoAnswers', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.demo_question_id)


class DemoQuestions(models.Model):
    """Demo Questions model"""
    demo_question = models.CharField('DemoQuestions', max_length=255)
    demo_answer_id = models.ForeignKey('DemoAnswers', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.demo_question)


class DemoAnswers(models.Model):
    """Demo Answer model"""
    demo_answer = models.CharField('DemoAnswers', max_length=255)

    def __str__(self):
        return "{}".format(self.demo_answer)
