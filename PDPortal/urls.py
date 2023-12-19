"""
URL configuration for PDPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.shortcuts import render

from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "HomePage"),
    path('institute-team/', views.instTeam, name = "InstituteTeamCont"),
    path('saveContact/', views.saveContact, name = "saveContact"),
    path('saveContact2/', views.saveContact2, name = "saveContact2"),
    path('saveContact3/', views.saveContact3, name = "saveContact3"),
    path('cross-open/', views.CrossOpen, name = "CrossOpen"),
    path('indAdjudicator/', views.indAdjudicator, name = "IndAdjudicator")
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
