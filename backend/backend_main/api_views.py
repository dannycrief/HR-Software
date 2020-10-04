from rest_framework import routers, viewsets, serializers, permissions

from .models import Question, Answer, DemoAnswer, DemoQuestion, DemoUserTest


# Question Serializer
class QuestionSerializer(serializers.ModelSerializer):
    """Registering Question Serializer class"""

    class Meta:
        model = Question
        fields = ["id", "question", "answer_id"]


class QuestionsViewSet(viewsets.ModelViewSet):
    """Registering Questions ViewSet class"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # permission_classes = [permissions.IsAuthenticated]


# Answers Serializer
class AnswersSerializer(serializers.ModelSerializer):
    """Registering Answer Serializer class"""

    class Meta:
        model = Answer
        fields = ["id", "answer"]


class AnswersViewSet(viewsets.ModelViewSet):
    """Registering Answer ViewSet class"""
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

    # permission_classes = [permissions.IsAuthenticated]


# Question Serializer
class DemoQuestionSerializer(serializers.ModelSerializer):
    """Registering Question Serializer class"""

    class Meta:
        model = DemoQuestion
        fields = ["id", "demo_question", "demo_answer_id"]


class DemoQuestionsViewSet(viewsets.ModelViewSet):
    """Registering Questions ViewSet class"""
    queryset = DemoQuestion.objects.all()
    serializer_class = DemoQuestionSerializer


# Demo Answers Serializer
class DemoAnswersSerializer(serializers.ModelSerializer):
    """Registering Demo Answer Serializer class"""

    class Meta:
        model = DemoAnswer
        fields = ["id", "demo_answer"]


class DemoAnswersViewSet(viewsets.ModelViewSet):
    """Registering Demo Answer ViewSet class"""
    queryset = DemoAnswer.objects.all()
    serializer_class = DemoAnswersSerializer


class DemoUserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoUserTest
        fields = ['id', 'demoUserEmail', 'dateOfStart', 'timeStart', 'timeEnd', 'demoGrade']


class DemoUserTestViewSet(viewsets.ModelViewSet):
    queryset = DemoUserTest.objects.all()
    serializer_class = DemoUserTestSerializer


def get_router_urls():
    """Getting routes from viewsets"""
    router = routers.DefaultRouter()
    router.register('questions', QuestionsViewSet)
    router.register('answers', AnswersViewSet)

    router.register('demo_questions', DemoQuestionsViewSet)
    router.register('demo_answers', DemoAnswersViewSet)
    router.register('demo_user_test', DemoUserTestViewSet)

    return router.urls
