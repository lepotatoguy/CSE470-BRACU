from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# https://www.youtube.com/watch?v=kRJpQxi2jIo #add custom fields in user model


# class User(AbstractUser):
#     # True for male and False for female
#     # gender = models.BooleanField(default=True)
#     cash = models.FloatField(default=0.0)
#     card = models.FloatField(default=0.0)
#     card_due = models.BooleanField(default=False)
# you can add more fields here.


# class User(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

from django.contrib.auth.models import User


class Finance(models.Model):
    # need to change to one to one if needed
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True, primary_key=True)
    phone_number = models.CharField(max_length=11)
    cash = models.CharField(max_length=250, default='0')
    card_limit = models.CharField(max_length=250, default='-1')
    loan = models.CharField(max_length=250, default='-1')
    due = models.CharField(max_length=250, default='-1')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']


class Transaction(models.Model):
    finance = models.ForeignKey(
        Finance, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, blank=True)
    remarks = models.TextField(null=True, blank=True)
    cash_transaction = models.FloatField(default="0.0")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            finance_user = Finance.objects.get(
                user=self.User
            )
            if self.id is None:
                finance_user.cash = finance_user.cash - self.cash_transaction
                # self.type = voucher_type
                finance_user.save()
        except Exception:
            print("Error")
        super(Transaction, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']
