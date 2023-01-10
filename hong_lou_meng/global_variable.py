# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/09
@ Author: Zng_sh
@ Description： 全局变量管理模块
"""


def init():
    """在主模块初始化"""
    global global_dict
    global_dict = {}


def set_value(key, value):
    """定义一个全局变量 global_dict[key]"""
    global_dict[key] = value


def get_value(key, default_value=None):
    """获得一个全局变量,不存在则返回默认值"""
    try:
        return global_dict[key]
    except KeyError:
        return default_value


def get_global_dict():
    """查看全局变量管理器global_dict"""
    return global_dict


def set_global_dict(f_global_dict):
    """用f_global_dict更新全局变量管理器global_dict"""
    global global_dict
    global_dict = f_global_dict
