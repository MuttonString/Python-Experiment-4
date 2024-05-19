from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    '''学到的有关某个主题的具体知识'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''返回一个表示条目的简单字符串'''
        # return f'{self.text[:50]}...'
        # 练习 18.2：简短的条目　当前，当 Django 在管理网站或 shell 中显示Entry 实例时，模型 Entry__str__() 方法都在其末尾加上省略号。请在 __str__() 方法中添加一条 if 语句，仅在条目长度超过 50 个字符时才添加省略号。使用管理网站添加一个不超过 50 个字符的条目，并核实在显示它时不带省略号。
        limit = 50
        if len(self.text) > limit:
            return f'{self.text[:limit]}...'
        else:
            return self.text
