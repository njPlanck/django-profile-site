from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='index'),
    path('profile/',views.profilepage,name='profilepage'),
    path('projects/',views.projects,name='projects'),
    path('<int:id>/',views.detailpage, name='detailpage'),
    path('contact/',views.contact, name='contact'),
]
