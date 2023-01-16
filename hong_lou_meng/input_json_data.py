# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/09
@ Author: Zng_sh
@ Description： 输入数据管理模块
"""
import read_to_json_data as read
import global_variable as glv


def per_n_chapters_as_a_group(n, json_data):
    """每n回作为一组"""
    json_data_temp = {}  # 储存以n回为一组json_data数据
    lt_key = list(json_data.keys())
    lt2_key = [lt_key[i:i + n] for i in range(0, len(lt_key), n)]
    for lt_i in lt2_key:
        json_data_temp[lt_i[0] + "至" + lt_i[-1]] = {
            "title": "\n".join([json_data[key]["title"] for key in lt_i]),
            "content": "".join([json_data[key]["content"] for key in lt_i])
        }
    _value_ = {
        "description": "每{:0>3}回作为一组".format(n),
        "value": json_data_temp
    }
    # 将处理后输入数据保存至全局变量管理器 global_dict
    glv.set_value("json_data_{:0>3}".format(n), _value_)


def first_eighty_and_last_forty_chapters(json_data):
    """前八十回与后四十回各为一组"""
    _value_ = {
        "description": "前八十回与后四十回各为一组",
        "value": {
            "前八十回": {
                "title": "\n".join([json_data[key]["title"] for key in list(json_data.keys())[:80]]),
                "content": "".join([json_data[key]["content"] for key in list(json_data.keys())[:80]])
            },
            "后四十回": {
                "title": "\n".join([json_data[key]["title"] for key in list(json_data.keys())[80:]]),
                "content": "".join([json_data[key]["content"] for key in list(json_data.keys())[80:]])
            }
        }
    }
    # 将处理后输入数据保存至全局变量管理器 global_dict
    glv.set_value("json_data_80_40", _value_)


def get_input_json_data():
    """获取输入数据json_data_n"""
    # 导入数据
    json_data = read.read_file_to_json("红楼梦.txt")

    # 输入数据01 ———— 每一回作为一组
    per_n_chapters_as_a_group(1, json_data)

    # # 输入数据02 ———— 每五回作为一组
    # per_n_chapters_as_a_group(5, json_data)
    #
    # # 输入数据03 ———— 每十回作为一组
    # per_n_chapters_as_a_group(10, json_data)

    # 输入数据04 ———— 全文作为一组
    per_n_chapters_as_a_group(120, json_data)

    # 输入数据05 ———— 前八十回与后四十回各为一组
    first_eighty_and_last_forty_chapters(json_data)


if __name__ == '__main__':
    get_input_json_data()
    global_dict = glv.get_global_dict()
    print()
