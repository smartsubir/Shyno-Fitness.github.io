from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('sfadmin/', admin.site.urls),
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("feedback", views.feedback, name='feedback'),
    path("healthcal", views.healthcal, name='healthcal'),


]