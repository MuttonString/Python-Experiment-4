@echo off
chcp 65001
cls
title Django Project initialization
echo (1/3) 正在建立Python虚拟环境
python -m venv ll_env
call ll_env\scripts\activate
cls
echo (2/3) 正在更新pip
pip install --upgrade pip
cls
echo (3/3) 正在安装Django
pip install django
cls
echo 完成
pause