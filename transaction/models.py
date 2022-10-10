from django.db import models
from django.utils import timezone
from wallet.models import Wallet

class Transaction(models.Model):
  wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
  date = models.DateField(default=timezone.now)
  amount = models.IntegerField()
  note = models.TextField()