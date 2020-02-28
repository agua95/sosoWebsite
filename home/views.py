from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
#def index(request):
 #   latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #  context = { 'latest_question_list': latest_question_list }
   # return render(request,'polls/index.html',context)
from .models import Tutorial
from django.shortcuts import render, get_object_or_404


# Create your views here.
def homepage(request):
    return render(request=request, template_name="home/home.html", context={"tutorials":Tutorial.objects.all})

def details(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    return render(request=request, template_name="home/detail.html", context={"tutorial":tutorial})
