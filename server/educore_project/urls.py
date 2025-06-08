"""
URL configuration for educore_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('modules.accounts.urls')),
    path('api/announcement/', include('modules.announcement.urls')),
    path('api/staff/', include('modules.staff.urls')),
    path('api/students/', include('modules.students.urls')),
    path('api/curriculum',include('modules.curriculum.urls')),
    path('api/classroom',include('modules.classroom.urls')),
    path('api/attendance',include('modules.attendance.urls')),
    path('api/examination',include('modules.examination.urls')),
    path('api/task',include('modules.task.urls'))

]
