from django.shortcuts import render
from activeClass.models import ect_project_repository
from .forms import ect_project_repositoryForm

# Create your views here.

def index(request):
    context={
        'all_students' : ect_project_repository.objects.all()
    }
    return render(request,'activeClass/active.html', context)

def about(request):
    return render(request, 'activeClass/aboutUs.html')

def contact(request):
    form = ect_project_repositoryForm(request.POST or None, )
    context= {
        'form': form,
    }
    if form.is_valid():
        form.save()
    return render(request, 'activeClass/contact.html', context)

def faq(request):
    return render(request, 'activeClass/FAQ.html')