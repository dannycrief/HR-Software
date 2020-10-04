from django.contrib import admin

from .models import Question, Answer, DemoQuestion, DemoAnswer, DemoUserTest


@admin.register(Question)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(DemoQuestion)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(DemoAnswer)
class AdminTest(admin.ModelAdmin):
    pass


@admin.register(DemoUserTest)
class AdminDemoUserTest(admin.ModelAdmin):
    pass
