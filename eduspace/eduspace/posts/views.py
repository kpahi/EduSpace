from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


from .models import Subjects,Explain
# Create your views here.
def home(request):
	subjects = Subjects.objects.all()
	#return HttpResponse("Hi there");
	return render(request,'index.html',{'subjects': subjects})

def physics(request, sub_id):
	#details = get_object_or_404(Explain, sub_id = 5)
	details = Explain.objects.filter(sub_id = 5)
	#model = Subjects
	#template_name = 'physics.html'
	return render(request, 'physics.html', {'details':details})

def chemistry(request, sub_id):
	details = Explain.objects.filter(sub_id = 6)
	return render(request,'chemistry.html', {'details':details})

def indv_expl(request, explain_id):
	description = get_object_or_404(Explain, pk = explain_id)
	return render(request, 'indv_expl.html', {'descriptions': description})