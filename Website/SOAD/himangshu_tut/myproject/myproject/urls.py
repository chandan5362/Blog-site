"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Chandan036.views import srn_view
from ase.views import (
	registration_view,
	logout_view,
	)

urlpatterns = [
    # path('',firsthead),
    path('admin/', admin.site.urls),
    path('', srn_view, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', registration_view, name="logout")
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',firsthead),
# ]
