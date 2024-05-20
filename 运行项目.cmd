@echo off
chcp 936

cls
title Django项目初始化
echo (1/5) 正在建立Python虚拟环境...
python -m venv ll_env
call ll_env\scripts\activate

cls
echo (2/5) 正在更新pip...
pip install --upgrade pip

cls
echo (3/5) 正在安装Django...
pip install django

cls
echo (4/5) 正在安装django-bootstrap5...
pip install django-bootstrap5

cls
echo (5/5) 正在安装platformshconfig...
pip install platformshconfig

cls
title Django本地服务器
echo 正在启动Django本地服务器...
python manage.py runserver