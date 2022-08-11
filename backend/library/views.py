from multiprocessing import context
from django.urls import reverse_lazy, reverse
import os
from urllib import request, response
from django.conf import settings
from django.shortcuts import render,redirect, get_object_or_404
from . models import *
from . forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.template.loader import render_to_string


# from account import forms

# Create your views here.



def libraries(request):
    all_libraries = Post.objects.all()
    return render(request, 'product-page.html', {'all_libraries' : all_libraries})

def library_preview(request, preview):
    library = Post.objects.get(preview=preview)
    return render(request, 'library_preview.html', {"library" : library})

def library_preview(request, preview):
    library = Post.objects.get(preview=preview)
    return render(request, 'library_preview.html', {"library" : library})



#library_slug(request):


def library_detail(request, slug):
    library = Post.objects.get(slug=slug)
    is_liked = False
    if library.likes.filter(id=request.user.id).exists(): 
        is_liked = True    
        
    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid(): 
          content = request.POST.get('content')
          comment = Comment.objects.create(library = library, user = request.user, content = content)
          comment.save()
          return redirect('library_detail', slug=library.slug)
    else: 

        cf = CommentForm()
    context= {        
        'comment_form':cf, 
        'library' : library,
        'is_liked':is_liked, 
        'total_likes': library.total_likes(),
 
    }    
    return render(request, 'library_detail.html', context)


def download(request,path):
    file_path =os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            #response = HttpResponse(fh.read(),content_type="application/octet-stream")
            response = HttpResponse(mimetype='application/adminupload')
            response['Content-Disposition']='inline;filename'+os.path.basename(file_path)
            return response
    raise HttpResponse("File not found")
    


def like_library(request):
    library = get_object_or_404(Post, id=request.POST.get('library_id'))
    is_liked = False
    if library.likes.filter(id = request.user.id).exists():
        library.likes.remove(request.user)
        is_liked = False
    else:
        library.likes.add(request.user)
        is_liked = True

    context= {
        'is_liked':is_liked, 
        'total_likes': library.total_likes(),
        'library' : library,
    }  
    
    if request.is_ajax():
        html = render_to_string('like_section.html', context, request=request) 
        context = {'form': html}  
        return JsonResponse(context)



