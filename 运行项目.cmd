@echo off
chcp 936

cls
title Django��Ŀ��ʼ��
echo (1/5) ���ڽ���Python���⻷��...
python -m venv ll_env
call ll_env\scripts\activate

cls
echo (2/5) ���ڸ���pip...
pip install --upgrade pip

cls
echo (3/5) ���ڰ�װDjango...
pip install django

cls
echo (4/5) ���ڰ�װdjango-bootstrap5...
pip install django-bootstrap5

cls
echo (5/5) ���ڰ�װplatformshconfig...
pip install platformshconfig

cls
title Django���ط�����
echo ��������Django���ط�����...
python manage.py runserver