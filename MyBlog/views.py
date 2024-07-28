from sre_constants import SUCCESS
from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Post,about
from MyBlog.forms import Contactform
from django.core.paginator import Paginator
import logging
# Create your views here.

def index(request):
    posts = Post.objects.all()
    # Paginator used to Show no of posts/page
    paginator = Paginator(posts,6)
    # recieve the current page number from url using get 
    page_no = request.GET.get('page')
    # based on the page recieved (ex 1) we get the page posts to the index html
    page = paginator.get_page(page_no)
    
    
    
    return render(request,'index.html',{'page':page})




def detail(request,slug):
    # getting post by post id using model class
    try:
        post = Post.objects.get(slug=slug)
        other_posts = Post.objects.filter().exclude(pk=post.id)
    
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")
        
    
    return render(request,'detail.html',{'post':post , 'other_posts':other_posts})



def contact(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        
        # values that are filled in the contact form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        
        
        if form.is_valid():    
            
            SUCCESS = 'Your Email Has Sent!'
            
            return render(request,'contact.html',{'form':form,'SUCCESS':SUCCESS})
           
            
        else:
            return render(request,'contact.html',{'form':form,'name':name,'email':email,'message':message})
        
    return render(request,'contact.html')

def aboutus(request):
    # about content is object 
    about_content = about.objects.first().content
    # logger = logging.getLogger("test")
    # logger.debug(about_content)
    return render(request,'about.html',{'about_content':about_content})
