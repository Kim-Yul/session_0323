from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    studentID = models.IntegerField(default=0)
    writer = models.CharField(max_length=10, default="")
    introduce = models.TextField()

    def __str__(self):
        return self.title