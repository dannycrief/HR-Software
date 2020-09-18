from django.contrib import admin

from .models import Tests, Questions, Answers, DemoTests, DemoQuestions, DemoAnswers


@admin.register(Tests)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(Questions)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(Answers)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(DemoTests)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(DemoQuestions)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(DemoAnswers)
class AdminTest(admin.ModelAdmin):
    pass
