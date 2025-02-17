from django.db import models
# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name