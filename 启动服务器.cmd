@echo off
title Django Server
call ll_env\scripts\activate
python manage.py runserver
