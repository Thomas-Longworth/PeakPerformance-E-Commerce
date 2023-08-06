from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback_view'),
    path('site/', views.site_feedback, name='site_feedback'),
]
