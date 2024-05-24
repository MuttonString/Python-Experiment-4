# @Author  : px

"""定义learning_logs的URL模式"""
from django.urls import path
from . import views

# 定义应用的名称，名为'learning_logs'
app_name = 'learning_logs'
# 定义应用的URL模式
urlpatterns = [
    # 重定向到应用的主页
    path('', views.index, name='index'),
    # 重定向到应用的主题页
    path('topics/', views.topics, name='topics'),
    # 重定向到应用的主题页，主题ID为topic_id
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 重定向到应用的新主题页，创建新主题
    path('new_topic', views.new_topic, name='new_topic'),
    # 重定向到应用的新条目页，为主题ID为topic_id的主题创建新条目
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 重定向到应用的编辑条目页，编辑条目ID为entry_id的条目
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry')
]

