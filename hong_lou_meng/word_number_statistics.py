# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/09
@ Author: Zng_sh
@ Description： 字数统计
"""
import global_variable as glv
import input_json_data as ijd


def word_number_statistics__per_n_chapters_as_a_group(json_data_n):
    """字数统计_每n回作为一组"""
    dic_wns_n = {}  # 记录统计结果
    for key in json_data_n["value"]:
        dic_wns_n[key] = len(json_data_n["value"][key]["content"])

    # 将结果保存至全局变量管理器 global_dict
    _value_ = {"description": "字数统计_每{}回".format(json_data_n["description"][1:4]), "value": dic_wns_n}
    glv.set_value("dic_wns_{}".format(json_data_n["description"][1:4]), _value_)
    return dic_wns_n


def word_number_statistics__first_eighty_and_last_forty_chapters(json_data_80_40):
    """字数统计_前八十回与后四十回各为一组"""
    dic_wns_80_40 = {}  # 记录统计结果
    for key in json_data_80_40["value"]:
        dic_wns_80_40[key] = len(json_data_80_40["value"][key]["content"])

    # 将结果保存至全局变量管理器 global_dict
    _value_ = {"description": "字数统计_前八十回与后四十回", "value": dic_wns_80_40}
    glv.set_value("dic_wns_80_40", _value_)
    return dic_wns_80_40


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
    # 字数统计_每一回
    _dic_wns_001 = word_number_statistics__per_n_chapters_as_a_group(_json_data_001)
    # 字数统计_每五回
    _dic_wns_005 = word_number_statistics__per_n_chapters_as_a_group(_json_data_005)
    # 字数统计_每十回
    _dic_wns_010 = word_number_statistics__per_n_chapters_as_a_group(_json_data_010)
    # 字数统计_全文
    _dic_wns_120 = word_number_statistics__per_n_chapters_as_a_group(_json_data_120)
    # 字数统计_前八十回与后四十回
    _dic_wns_80_40 = word_number_statistics__first_eighty_and_last_forty_chapters(_json_data_80_40)
    print()
