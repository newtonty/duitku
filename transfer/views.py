from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import TransferForm
from .models import TransferModel

def index(request):
	transfer = TransferModel.objects.all()

	context = {
		'page_title':'List Post',
		'posts':transfer,
	}

	return render(request,'blog/index.html',context)

def create(request):
	transfer_form = TransferForm()

	if request.method == 'TRANSFER':
		TransferModel.objects.create(
				namaPenerima = request.TRANSFER.get('judul'),
				jumlahTransfer = request.TRANSFER.get('category'),
			)

		return HttpResponseRedirect("/blog/")


	context = {
		'page_title':'create post',
		'post_form': transfer_form
	}

	return render(request,'blog/create.html',context)














