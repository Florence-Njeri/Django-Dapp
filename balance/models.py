from django.db import models
from django.urls import reverse

# Create your balance model.
class Balance(models.Model):
    balance = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.balance
