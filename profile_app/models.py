from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def get_first_rank():
    try:
        return Rank.objects.get(order=1).pk
    except Rank.DoesNotExist:
        return None


class Profile(models.Model):
    """Profile - for user"""
    user = models.OneToOneField(
        User, models.CASCADE, related_name='profile'
    )
    image = models.ImageField(upload_to='profile_pics',default='media/default_pics/user-icon-in-trendy-flat-style-isolated-on-grey-background-user-symbol-700-137463483.jpg')

    # stats
    completed_lesson = models.IntegerField(default=0)
    completed_test = models.IntegerField(default=0)
    number_of_mistake = models.IntegerField(default=0)

    # score
    points = models.IntegerField(default=0)
    coins = models.IntegerField(default=300)
    rank = models.ForeignKey(
        'Rank', models.SET_NULL, 'users',
        null=True, blank=True, default=get_first_rank,
    )

    def __str__(self):
        return f'id:{self.pk} Profile'


class Rank(models.Model):
    """Rank of user"""
    name = models.CharField(max_length=150)
    order = models.PositiveIntegerField(unique=True)  # order for rank
