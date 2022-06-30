from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    data = models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name}_{self.number}"