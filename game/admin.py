from django.contrib import admin

from game import models


# Register your models here.

@admin.register(models.LessonTopic)
class LessonTopicAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
