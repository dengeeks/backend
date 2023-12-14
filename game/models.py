from django.db import models


# Create your models here.

class LessonTopic(models.Model):
    """The name of a lesson topic."""
    image = models.ImageField(upload_to='lessontopics_pisc/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """The name of a lesson"""
    lesson_topic = models.ForeignKey(
        'LessonTopic', models.CASCADE, 'lessons'
    )
    image = models.ImageField(upload_to='lesson_pisc/')
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Question(models.Model):
    """Questions for Lesson"""
    lesson = models.ForeignKey(
        'Lesson', models.CASCADE, 'questions'
    )
    image = models.ImageField(upload_to='question_pisc/')
    text = models.CharField(max_length=250)



class Answer(models.Model):
    """Answers on Question"""
    question = models.ForeignKey(
        'Question', models.CASCADE, 'answers'
    )
    text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)
