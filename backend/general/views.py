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

def reference(request):
    return render(request, "reference-overlay.html")    


def faqs(request):
    return render(request, "FAQS.html")       







def search(request):
    
    if request.method == "POST":
        searched = request.POST['searched']
        results = Post.objects.filter(title__icontains=searched)
        context = { 'searched':searched, 'results':results}

        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html', {})   

        

def error_404_view(request, exception):
       
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')

