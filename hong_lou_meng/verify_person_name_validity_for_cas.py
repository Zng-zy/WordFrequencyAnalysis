# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/15
@ Author: Zng_sh
@ Description： 为模块character_appearances_statistics.py 验证人名集姓名有效性
"""
import global_variable as glv
import input_json_data as ijd
import jieba

jieba.setLogLevel(jieba.logging.INFO)

# jieba 词库调整
jieba.load_userdict("Jieba_word_frequency_adjustment_dict.txt")


def from_string_get_jieba_word_segmentation_statistics(string):
    """从一段字符串string中获取jieba分词统计"""
    words = jieba.lcut(string)
    dic_word_frequency = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            dic_word_frequency[word] = dic_word_frequency.get(word, 0) + 1

    # 字典排序
    dic_word_frequency = dict(sorted(dic_word_frequency.items(), key=lambda x: x[1], reverse=True))
    jieba_str = "/".join(words)
    return dic_word_frequency, jieba_str


def verify_person_name_validity_for_cas(dic_word_frequency):
    """为模块character_appearances_statistics.py 验证人名集姓名有效性。 输入数据为jieba分词统计_全文dic_jwss_120"""
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
    lt_name = [dic_name[key] for key in dic_name]
    lt_name = [j for i in lt_name for j in i]
    dic_name_number = {}
    for key in lt_name:
        dic_name_number[key] = dic_name_number.get(key, 0) + dic_word_frequency.get(key, 0)
    return dic_name_number


if __name__ == '__main__':
    # 初始化全局变量管理器 global_dict
    glv.init()
    # 数据导入
    ijd.get_input_json_data()
    global_dict = glv.get_global_dict()
    _json_data_120 = global_dict["json_data_120"]

    "=========================分割线=========================分割线========================="

    _dic_word_frequency, _jieba_str = from_string_get_jieba_word_segmentation_statistics(
        _json_data_120["value"]["第一回至一二零"]["content"])
    _dic_name_number = verify_person_name_validity_for_cas(_dic_word_frequency)
    print(_jieba_str)
