from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_view, name='request_view'),
    path('site/', views.site_refunds, name='site_refunds')

]
