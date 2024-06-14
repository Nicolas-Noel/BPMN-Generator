from django.urls import path

from . import views

app_name = "bpmn_generator"

urlpatterns = [
    path("about", views.about, name="about"),
    path("", views.dashboard, name="dashboard"),
    path("documentation", views.documentation, name="documentation"),
    path("generate", views.generate, name="generate"),
]