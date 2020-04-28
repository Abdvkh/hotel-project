from django.urls import path
from .views import home, about_us

urlpatterns = [
               path('', home, name='home'),
               path('about-us/', about_us, name='about-us'),
]
