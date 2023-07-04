from django.shortcuts import render , redirect
from .models import Question , Answer
from .forms import QuestionForm
# Create your views here.


def questions_list(request):
    data = Question.objects.all()
    return render(request,'Fourm/list.html',{'steven':data})







def question_detail(request,id):
    data = Question.objects.get(id=id)
    answer = Answer.objects.filter(question=data)
    return render(request,'Fourm/detail.html',{'data':data , 'answers':answer})




def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/questions/')



    else:
        form = QuestionForm()
    return render(request,'Fourm/add.html',{'form':form})





    







def edit_question(request):
     data = Question.objects.get(id=id)
     if request.method == 'POST':
        form = QuestionForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/questions/')

     else:
        form = QuestionForm(instance=data)
     return render(request,'Fourm/save.html',{'form':form})
     



  