from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todonote(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=1000)
    notetime=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}-{self.title}"