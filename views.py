from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'home.html')
def res(request):
    options=['Rock','Paper','Scissors']
    computer_choice=random.choice(options)
    user_choice=request.POST.get('choice')
    result=None
    if(user_choice==computer_choice):
        result='Tie'
    elif(user_choice=='Rock' and computer_choice=='Scissors'):
        result='You Win'
    elif(user_choice=='Scissors' and computer_choice=='Paper'):
        result='You Win'
    elif(user_choice=='Paper' and computer_choice=='Rock'):
        result='You Win'
    else:
        result='You Lose' 
    context={
        "result" : result,
        "user_choice" : user_choice,
        "computer_choice" : computer_choice
    }
    return render(request,'result.html',context)
    
    
