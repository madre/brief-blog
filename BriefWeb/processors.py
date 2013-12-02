#coding=utf-8
"""
__create_time__ = '13-10-14'
__author__ = 'Madre'
"""
from blog.models import Blog


def get_side_panel(request):
    # 存疑，使用全局模板，所有的模板都加载这部分代码，但如果不是所有页面都使用时，怎么破？？
    side_panel = Blog.objects.filter(position="sidepanel")
    return {"sidepanel": side_panel}