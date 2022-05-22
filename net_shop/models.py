import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.BigIntegerField(blank=True, null=True)


class Customer(models.Model):
    fullname = models.CharField(max_length=1000, blank=True)
    username = models.CharField(max_length=1000, blank=True)
    phone = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    wallet = models.BigIntegerField(blank=True, null=True)


class Computer(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    ip_address = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=1000, blank=True, null=True)


class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    play_time = models.IntegerField(blank=True, null=True)
    total_payment = models.BigIntegerField(blank=True)


class PaidHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.BigIntegerField(blank=True)
    create_time = models.DateTimeField(default=datetime.datetime.now, editable=False)

