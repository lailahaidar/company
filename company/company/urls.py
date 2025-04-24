"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('bindxlog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from company.emp.views import employee_record
from emp.views import index_view, show_employees, employee_record, employee_stat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting/', index_view),
    path('show_employees/', show_employees),
    path('employee_record/<int:id>', employee_record),
    path('employee_stat/', employee_stat)
]
