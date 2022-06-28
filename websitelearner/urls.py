"""websitelearner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name='home'),
    # path('homepage/', view.homepage),
    # path('blog/<int:courseid>', view.blog), #int
    # path('blog/<str:courseid>', view.blog), #string
    # path('blog/<slug:courseid>', view.blog), #slug
    path('blog/<courseid>', view.blog), #slug #dynamic route
    path('about', view.aboutus, name='about'), #ABOUT US
    # path('index', view.index), #ABOUT US

    path('contact', view.contact, name='contact'), #contact
    path('feature', view.feature, name='feature'), #feature
    path('project', view.project, name='project'), #project
    path('quote', view.quote, name='quote'), #quote
    path('service', view.service, name='service'), #service
    path('team', view.team, name='team'), #team
    path('testimonial', view.testimonial, name='testimonial'), #testimonial
    path('404', view.fourzerofour, name='fourzerofour'), #fourzerofour
    path('userform', view.userform, name='userform'), #userform
    path('thank-you/', view.thankyou, name='thankyou'), #thank-you
    path('calculator/', view.calculator, name='calculator'), #calculator

]
