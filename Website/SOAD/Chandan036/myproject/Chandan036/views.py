from django.shortcuts import render
from .models import Abhisarga
# from ase.models import Account
# Create your views here.
def firsthead(request):
	asetrack = {}
	
	asetrack['val'] = Abhisarga.objects.all()
	# asetrack['event'] = Account.objects.all()


	return render(request,"a.html",asetrack)