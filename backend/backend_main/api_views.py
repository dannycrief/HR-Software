from rest_framework import routers, viewsets, serializers, permissions

from .models import Questions, Answer


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


class AnswerSerializer(serializers.ModelSerializer):
    """Registering Answer Serializer class"""

    class Meta:
        model = Answer
        fields = ["id", "answer", "question_id"]


class AnswerViewSet(viewsets.ModelViewSet):
    """Registering Answer ViewSet class"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    # permission_classes = [permissions.IsAuthenticated]


def get_router_urls():
    """Getting routes from viewsets"""
    router = routers.DefaultRouter()
    router.register('questions', QuestionsViewSet)
    router.register('answers', AnswerViewSet)

    return router.urls
