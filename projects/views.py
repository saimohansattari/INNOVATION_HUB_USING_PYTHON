from multiprocessing import context
import re
from unicodedata import category
from django.shortcuts import render

import projects
from .models import Project

# Create your views here.

def dashboard(request):
    mini_projects = Project.objects.all().filter(category='MINI_PROJECT').count()
    final_projects = Project.objects.all().filter(category='FINAL_PROJECT').count()
    total = mini_projects + final_projects

    context = {'mini_projects' : mini_projects, 
                'final_projects':final_projects,
                'total':total
    }
    return render(request, 'dashboard.html',context)
 

def miniProjects(request):
    projects = Project.objects.filter(category="MINI_PROJECT")

    context = {'projects': projects}
    return render(request, 'mini_projects.html', context)    


def finalProjects(request):
    projects = Project.objects.filter(category="FINAL_PROJECT")

    context = {'projects': projects}
    return render(request, 'final_projects.html', context)    
  
  
def hackathon(request):
    projects = Project.objects.filter(category="HACKAHTON_PROJECT")

    context = {'projects': projects}
  
    return render(request, 'hackathon.html', context)

  
def internship(request):
    
    return render(request,'internship.html')