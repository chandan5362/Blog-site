from django.shortcuts import render
from .models import Abhisarga
from ase.models import Account
# Create your views here.


def srn_view(request):
	asetrack = {}
	event = Account.objects.all()
	event2 = Abhisarga.objects.all()
	asetrack['event'] = event
	# asetrack['event2'] = event2
	return render(request,"a.html",asetrack)
    # asetrack = {}
    # event = Account.objects.all()
	# # event2 = Abhisarga.objects.all()
    # asetrack['event'] = event
	# # asetrack['event2'] = event2
	# event2 = Abhisarga.objects.all()
    # return render(request, "a.html", asetrack)