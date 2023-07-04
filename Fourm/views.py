from django.shortcuts import render , redirect
from .models import Question , Answer
from .forms import QuestionForm , AnswerForm 
# Create your views here.


def questions_list(request):
    data = Question.objects.all()
    return render(request,'Fourm/list.html',{'steven':data})







def question_detail(request,id):
    data = Question.objects.get(id=id)
    answer = Answer.objects.filter(question=data)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.question = data
            myform.save()
        


    else:
        form = AnswerForm()    
    return render(request,'Fourm/detail.html',{'data':data , 'answers':answer, 'form':form})




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
     




def delete_question(request,id):
    data = Question.objects.get(id=id)
    data.delete()
    return redirect('/questions/')



  