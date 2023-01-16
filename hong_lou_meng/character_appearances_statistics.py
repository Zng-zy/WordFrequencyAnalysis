# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/15
@ Author: Zng_sh
@ Description： 人物出场次数统计
"""
import global_variable as glv
import input_json_data as ijd

import jieba

jieba.setLogLevel(jieba.logging.INFO)

# jieba 词库调整
jieba.load_userdict("Jieba_word_frequency_adjustment_dict.txt")

# 人名集
dic_name = {
    "贾宝玉": ["贾宝玉", "宝玉", "宝二爷", "宝兄弟", "爱哥哥", "神瑛侍者"],

    "林黛玉": ["林黛玉", "黛玉", "林姑娘", "林妹妹", "林丫头", "颦颦", "颦儿", "潇湘妃子", "绛珠", "绛珠草", "绛珠仙子"],
    "薛宝钗": ["薛宝钗", "宝钗", "宝姑娘", "宝丫头", "宝姐姐", "蘅芜君"],
    "贾元春": ["贾元春", "元春"],
    "贾探春": ["贾探春", "探春", "三姑娘"],
    "史湘云": ["史湘云", "湘云"],
    "妙玉": ["妙玉"],
    "贾迎春": ["贾迎春", "迎春", "二姑娘"],
    "贾惜春": ["贾惜春", "惜春", "四姑娘"],
    "王熙凤": ["王熙凤", "熙凤", "凤姐", "凤辣子", "凤姐儿", "琏二奶奶", "凤丫头", "凤哥儿"],
    "贾巧姐": ["贾巧姐", "巧姐"],
    "李纨": ["李纨"],
    "秦可卿": ["秦可卿", "可卿", "蓉大奶奶"],

    "贾母": ["贾母", "太君", "老祖宗", '老太太'],
    "贾赦": ["贾赦"],
    "邢夫人": ["邢夫人"],
    "贾政": ["贾政", "存周"],
    "王夫人": ["王夫人"],
    "赵姨娘": ["赵姨娘"],
    "贾琏": ["贾琏", "琏二爷"],

    "贾瑞": ["贾瑞", "瑞大爷"],

    "薛姨妈": ["薛姨妈"],
    "薛蟠": ["薛蟠"],

    "刘姥姥": ["刘姥姥"],

    "平儿": ["平儿"],
    "鸳鸯": ["鸳鸯"],
    "香菱": ["香菱", "秋菱", "英莲"],
    "晴雯": ["晴雯"],
    "袭人": ["袭人", "花珍珠"],
    "紫鹃": ["紫鹃"]
}


def from_string_get_character_appearances_statistics(string):
    """从一段字符串string中获取人物出场次数"""
    words = jieba.lcut(string)
    dic_cas = {}
    for word in words:
        for key in dic_name:
            if word in dic_name[key]:
                re_word = key
                dic_cas[re_word] = dic_cas.get(re_word, 0) + 1
                break
    # 字典排序
    dic_cas = dict(sorted(dic_cas.items(), key=lambda x: x[1], reverse=True))
    return dic_cas


def character_appearances_statistics__per_n_chapters_as_a_group(json_data_n):
    """人物出场次数统计_每n回作为一组"""
    dic_cas_n = {}  # 记录统计结果
    for key in json_data_n["value"]:
        dic_cas_temp = from_string_get_character_appearances_statistics(json_data_n["value"][key]["content"])
        dic_cas_n[key] = dic_cas_temp

    # 将结果保存至全局变量管理器 global_dict
    _value_ = {"description": "人物出场次数统计_每{}回".format(json_data_n["description"][1:4]), "value": dic_cas_n}
    glv.set_value("dic_cas_{}".format(json_data_n["description"][1:4]), _value_)
    return dic_cas_n


def character_appearances_statistics__first_eighty_and_last_forty_chapters(json_data_80_40):
    """人物出场次数统计_前八十回与后四十回各为一组"""
    dic_cas_80_40 = {}  # 记录统计结果
    for key in json_data_80_40["value"]:
        dic_cas_temp = from_string_get_character_appearances_statistics(json_data_80_40["value"][key]["content"])
        dic_cas_80_40[key] = dic_cas_temp

    # 将结果保存至全局变量管理器 global_dict
    _value_ = {"description": "人物出场次数统计_前八十回与后四十回", "value": dic_cas_80_40}
    glv.set_value("dic_cas_80_40", _value_)
    return dic_cas_80_40


if __name__ == '__main__':
    # 初始化全局变量管理器 global_dict
    glv.init()
    # 数据导入
    ijd.get_input_json_data()
    global_dict = glv.get_global_dict()
    # _json_data_001 = global_dict["json_data_001"]
    # _json_data_005 = global_dict["json_data_005"]
    # _json_data_010 = global_dict["json_data_010"]
    _json_data_120 = global_dict["json_data_120"]
    _json_data_80_40 = global_dict["json_data_80_40"]

    "=========================分割线=========================分割线========================="
    # 人物出场次数统计_每一回
    # _dic_cas_001 = character_appearances_statistics(_json_data_001)
    # 人物出场次数统计_每五回
    # _dic_cas_005 = word_number_statistics__per_n_chapters_as_a_group(_json_data_005)
    # 人物出场次数统计_每十回
    # _dic_cas_010 = word_number_statistics__per_n_chapters_as_a_group(_json_data_010)
    # 人物出场次数统计_全文
    _dic_cas_120 = character_appearances_statistics__per_n_chapters_as_a_group(_json_data_120)
    # 人物出场次数统计_前八十回与后四十回
    # _dic_cas_80_40 = character_appearances_statistics__first_eighty_and_last_forty_chapters(_json_data_80_40)

    print()
