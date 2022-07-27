
import os
from urllib import response
from django.conf import settings
from django.shortcuts import render,redirect
from . models import *
from . forms import CommentForm
from django.http import HttpResponse
# from account import forms

# Create your views here.




def libraries(request):
    all_libraries = Post.objects.all()
    return render(request, 'library_page.html', {'all_libraries' : all_libraries})



def library_detail(request, slug):
    library = Post.objects.get(slug=slug)
    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
          content = request.POST.get('content')
          comment = Comment.objects.create(library = library, user = request.user, content = content)
          comment.save()
          return redirect('library_detail', slug=library.slug)
    else:   
        cf = CommentForm()
    return render(request, 'library_detail.html', {'library' : library, 'comment_form':cf})


def download(request,path):
    file_path =os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            #response = HttpResponse(fh.read(),content_type="application/octet-stream")
            response = HttpResponse(mimetype='application/adminupload')
            response['Content-Disposition']='inline;filename'+os.path.basename(file_path)
            return response
    raise Http404("File not found")