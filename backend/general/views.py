from multiprocessing import context
from django.shortcuts import render
from library.models import Post

# Create your views here.


def home(request):
    return render(request, "index.html")



def about(request):
    return render(request, "about-us.html")
    
def documentation(request):
    return render(request, "documentation.html")

    
def team(request):
    return render(request, "team.html")


def terms(request):
    return render(request, "terms.html")







def search(request):
    
    if request.method == "POST":
        searched = request.POST['searched']
        results = Post.objects.filter(title__icontains=searched)
        context = { 'searched':searched, 'results':results}

        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html', {})   
        