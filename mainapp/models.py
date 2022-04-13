from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class User(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


class Finance(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=255)
    remarks = models.TextField(null=True, blank=True)
    cash_remaining = models.FloatField(default=0.0)
    card_cash_remaining = models.FloatField(default=0.0)
    card_due = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['status']
