#coding=utf-8
"""
本文件用于删除目录下所有 *.pyc的文件
__create_time__ = '13-10-18'
__author__ = 'Madre'
"""
import os
import fnmatch

MAX_DEPTH = 4  # 遍历4层目录


def delete_pyc(path, depth):
    if MAX_DEPTH == depth:
        print depth
        return
    for it in os.listdir(path):
        if os.path.isdir(path+'/'+it):
            delete_pyc(path+'/'+it, depth+1)
        else:
            if fnmatch.fnmatch(' '*depth + it, '*.pyc'):
                os.remove(path+'/'+it)


if __name__ == "__main__":
    file_path = os.path.split(os.path.realpath(__file__))[0]
    try:
        delete_pyc(file_path, 1)
    except:
        import traceback
        print traceback.fromat_exc()
