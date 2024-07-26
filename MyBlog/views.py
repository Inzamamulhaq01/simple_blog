from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    posts = [
        {'title':'Post 1','content': 'Content of Post 1'},
        {'title':'Post 2','content': 'Content of Post 2'},
        {'title':'Post 3','content': 'Content of Post 3'},
        {'title':'Post 4','content': 'Content of Post 4'},
        {'title':'Post 5','content': 'Content of Post 5'},
        {'title':'Post 6','content': 'Content of Post 6'},
    ]
    return render(request,'index.html',{'posts':posts})

def detail(request):
    return render(request,'detail.html')

