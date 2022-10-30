from django import forms


class TransferForm(forms.Form):
	namaPenerima = forms.CharField(max_length = 20)
	jumlahTransfer = forms.CharField(max_length = 20)