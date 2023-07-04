from django.shortcuts import render
from .models import Question , Answer
# Create your views here.


def questions_list(request):
    data = Question.objects.all()
    return render(request,'Fourm/list.html',{'steven':data})







def question_detail(request,id):
    data = Question.objects.get(id=id)
    answer = Answer.objects.filter(question=data)
    return render(request,'Fourm/detail.html',{'data':data , 'answers':answer})