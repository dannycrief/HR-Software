from rest_framework import routers, viewsets, serializers, permissions

from .models import Questions, Answers, Tests, DemoTests, DemoAnswers, DemoQuestions


# Tests Serializer
class TestsSerializer(serializers.ModelSerializer):
    """Registering Answer Serializer class"""

    class Meta:
        model = Tests
        fields = ["id", "question_id", "answer_id"]


class TestsViewSet(viewsets.ModelViewSet):
    """Registering Answer ViewSet class"""
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer

    # permission_classes = [permissions.IsAuthenticated]


# Question Serializer
class QuestionSerializer(serializers.ModelSerializer):
    """Registering Question Serializer class"""

    class Meta:
        model = Questions
        fields = ["id", "question", "answer_id"]


class QuestionsViewSet(viewsets.ModelViewSet):
    """Registering Questions ViewSet class"""
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    # permission_classes = [permissions.IsAuthenticated]


# Answers Serializer
class AnswersSerializer(serializers.ModelSerializer):
    """Registering Answer Serializer class"""

    class Meta:
        model = Answers
        fields = ["id", "answer"]


class AnswersViewSet(viewsets.ModelViewSet):
    """Registering Answer ViewSet class"""
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

    # permission_classes = [permissions.IsAuthenticated]


# Demo Tests Serializer
class DemoTestsSerializer(serializers.ModelSerializer):
    """Registering Demo Tests Serializer class"""

    class Meta:
        model = DemoTests
        fields = ["id", "demo_question_id", "demo_answer_id"]


class DemoTestsViewSet(viewsets.ModelViewSet):
    """Registering Demo Tests ViewSet class"""
    queryset = DemoTests.objects.all()
    serializer_class = DemoTestsSerializer

    # permission_classes = [permissions.IsAuthenticated]


# Question Serializer
class DemoQuestionSerializer(serializers.ModelSerializer):
    """Registering Question Serializer class"""

    class Meta:
        model = DemoQuestions
        fields = ["id", "demo_question", "demo_answer_id"]


class DemoQuestionsViewSet(viewsets.ModelViewSet):
    """Registering Questions ViewSet class"""
    queryset = DemoQuestions.objects.all()
    serializer_class = DemoQuestionSerializer

    # permission_classes = [permissions.IsAuthenticated]


# Demo Answers Serializer
class DemoAnswersSerializer(serializers.ModelSerializer):
    """Registering Demo Answer Serializer class"""

    class Meta:
        model = DemoAnswers
        fields = ["id", "demo_answer"]


class DemoAnswersViewSet(viewsets.ModelViewSet):
    """Registering Demo Answer ViewSet class"""
    queryset = DemoAnswers.objects.all()
    serializer_class = DemoAnswersSerializer

    # permission_classes = [permissions.IsAuthenticated]


def get_router_urls():
    """Getting routes from viewsets"""
    router = routers.DefaultRouter()
    router.register('tests', TestsViewSet)
    router.register('questions', QuestionsViewSet)
    router.register('answers', AnswersViewSet)

    router.register('demo_tests', DemoTestsViewSet)
    router.register('demo_questions', DemoQuestionsViewSet)
    router.register('demo_answers', DemoAnswersViewSet)

    return router.urls
