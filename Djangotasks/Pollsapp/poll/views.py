from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Question,Choice

# Create your views here.
# def home_view(request):
# 	question_list=Question.objects.order_by('-pub_date')[:3]
# 	context={'question_list' : question_list}
# 	return render(request,'poll/home.html',context)
def index_view(request):
	question_list=Question.objects.all()
	context={
		'question_list': question_list
	}
	return render(request,'poll/index.html',context)

def details_view(request,qid):
	question=get_object_or_404(Question,pk=qid)
	return render(request,'poll/details.html',{'question':question})


def vote_view(request,qid):
	question=get_object_or_404(Question,pk=qid)
	try:
		selected_choice =question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'poll/vote.html',{
			'question':question ,
			'error_message':"Select a choice "
			})
		
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('poll:results',
			args=(question.id,)))

def results_view(request,qid):
	question=get_object_or_404(Question,pk=qid)
	return render(request,'poll/results.html',{'question':question})

