from django.db import models

# Create your models here.

class TransferModel(models.Model):
	namaPenerima = models.CharField(max_length = 20)
	jumlahTransfer = models.CharField(max_length = 20)
	def __str__(self):
		return "{}. {}".format(self.id, self.judul)