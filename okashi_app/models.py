from django.db import models

# Create your models here.

class Post(models.Model):
    question1_0=models.CharField(max_length=5,null=True)
    question1_1=models.CharField(max_length=5,null=True)
    user_choice1=models.CharField(max_length=1,null=True)


    def __str__(self):
        return self.user_choice1
