# @Author  : px

"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

# 定义应用的URL模式
urlpatterns = [
    # 显示管理员界面（Django默认提供界面）
    path('admin/', admin.site.urls),
    # 显示自定义用户认证界面
    path('accounts/', include('accounts.urls')),
    # 显示学习笔记应用的主页
    path('', include('learning_logs.urls'))
]

