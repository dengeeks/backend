from django.db import models


# Create your models here.


class Topic(models.Model):
    """Topic for PDD"""
    name = models.CharField(max_length=200)


class Heading(models.Model):
    topic = models.ForeignKey(
        'Topic', models.CASCADE,'heading',
    )
    text = models.TextField()


