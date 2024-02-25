from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
<<<<<<< HEAD

    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<str:pk>/', views.updateProject, name="update-project"),
=======
    path('create-project/', views.createProject, name="create-project")
>>>>>>> 3703a2740cee4613db21fcb4019b64394c29f9ff
]