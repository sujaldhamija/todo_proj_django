from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'my_tasks'
