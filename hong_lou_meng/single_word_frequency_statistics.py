# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/09
@ Author: Zng_sh
@ Description： 单字频率统计
"""
import global_variable as glv
import input_json_data as ijd


def from_string_get_single_word_frequency_statistics(string):
    """从一段字符串string中获取单字频率"""
    dic_swfs = {}
    for key in string:
        dic_swfs[key] = dic_swfs.get(key, 0) + 1
    return dic_swfs


def single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_n):
    """单字频率统计_每n回作为一组"""
    dic_swfs_n = {}  # 记录统计结果
    for key in json_data_n["value"]:
        dic_swfs_temp = from_string_get_single_word_frequency_statistics(json_data_n["value"][key]["content"])
        # 字典排序
        dic_swfs_temp = dict(sorted(dic_swfs_temp.items(), key=lambda x: x[1], reverse=True))
        dic_swfs_n[key] = dic_swfs_temp

    # 将结果保存至全局变量管理器 global_dict
    _value_ = {"description": "单字频率统计_每{}回".format(json_data_n["description"][1:4]), "value": dic_swfs_n}
    glv.set_value("dic_swfs_{}".format(json_data_n["description"][1:4]), _value_)
    return dic_swfs_n


def single_word_frequency_statistics__first_eighty_and_last_forty_chapters(json_data_80_40):
    """单字频率统计_前八十回与后四十回各为一组"""
    dic_swfs_80_40 = {}  # 记录统计结果
    for key in json_data_80_40["value"]:
        dic_swfs_temp = from_string_get_single_word_frequency_statistics(json_data_80_40["value"][key]["content"])
        # 字典排序
        dic_swfs_temp = dict(sorted(dic_swfs_temp.items(), key=lambda x: x[1], reverse=True))
        dic_swfs_80_40[key] = dic_swfs_temp

    # 将结果保存至全局变量管理器 global_dict
    _value_ = {"description": "单字频率统计_前八十回与后四十回", "value": dic_swfs_80_40}
    glv.set_value("dic_swfs_80_40", _value_)
    return dic_swfs_80_40


if __name__ == '__main__':
    # 初始化全局变量管理器 global_dict
    glv.init()
    # 数据导入
    ijd.get_input_json_data()
    global_dict = glv.get_global_dict()
    _json_data_001 = global_dict["json_data_001"]
    _json_data_005 = global_dict["json_data_005"]
    _json_data_010 = global_dict["json_data_010"]
    _json_data_120 = global_dict["json_data_120"]
    _json_data_80_40 = global_dict["json_data_80_40"]

    "=========================分割线=========================分割线========================="
    # 单字频率统计_每一回
    _dic_swfs_001 = single_word_frequency_statistics__per_n_chapters_as_a_group(_json_data_001)
    # 单字频率统计_每五回
    _dic_swfs_005 = single_word_frequency_statistics__per_n_chapters_as_a_group(_json_data_005)
    # 单字频率统计_每十回
    _dic_swfs_010 = single_word_frequency_statistics__per_n_chapters_as_a_group(_json_data_010)
    # 单字频率统计_全文
    _dic_swfs_120 = single_word_frequency_statistics__per_n_chapters_as_a_group(_json_data_120)
    # 单字频率统计_前八十回与后四十回
    _dic_swfs_80_40 = single_word_frequency_statistics__first_eighty_and_last_forty_chapters(_json_data_80_40)
    print()
