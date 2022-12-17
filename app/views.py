from django.shortcuts import render, redirect
from .models import Project
from django.core.paginator import Paginator
# Create your views here.
def index(request):
  project_objects = Project.objects.all()
  project_name = request.GET.get('project_name')
  if project_name != '' and project_name is not None:
    project_objects = project_objects.filter(title__icontains = project_name)
    return redirect('projects')
  return render(request,'mysite/index.html',{})


def profilepage(request):
  project_objects = Project.objects.all()
  project_name = request.GET.get('project_name')
  if project_name != '' and project_name is not None:
    project_objects = project_objects.filter(title__icontains = project_name)
    return redirect('projects')
  return render(request,'mysite/profile.html',{})

def detailpage(request,id):
  details = Project.objects.get(id=id)

  return render(request,'mysite/detail.html',{'details':details})



def projects(request):
  project_objects = Project.objects.all()
  project_name = request.GET.get('project_name')
  if project_name != '' and project_name is not None:
    project_objects = project_objects.filter(title__icontains = project_name)
#paginator
  paginator = Paginator(project_objects,4)
  page = request.GET.get('page')
  project_objects = paginator.get_page(page)
  return render(request,'mysite/projects.html',{'project_objects':project_objects})


def contact(request):
  return render(request,'mysite/contact.html',{})