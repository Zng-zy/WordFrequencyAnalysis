# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/15
@ Author: Zng_sh
@ Description： jieba分词统计
"""
import global_variable as glv
import input_json_data as ijd

import jieba

jieba.setLogLevel(jieba.logging.INFO)

# jieba 词库调整
jieba.load_userdict("Jieba_word_frequency_adjustment_dict.txt")

# 排除词语
set_exclude_words = {}


# set_exclude_words = {'什么', '一个', '我们', '你们', '如今', '说道', '知道', '起来', '这里', '奶奶', '姑娘', '出来',
#                      '众人', '那里', '自己', '他们', '一面', '只见', '怎么', '老太太', '两个', '没有', '不是', '不知',
#                      '这个', '听见', '这样', '进来', '咱们', '太太', '告诉', '就是', '东西', '回来', '只是', '大家',
#                      '只得', '丫头', '姐姐', '不用', '过来', '心里', '如此', '今日', '这些', '不敢', '出去', '所以',
#                      '不过', '的话', '不好', '一时', '不能', '银子', '几个', '答应', '二人', '还有', '只管', '这么',
#                      '那些', '听说', '如何', '问道', '看见', '二爷', '小丫头', '人家', '妹妹', '老爷', '说话', '一回',
#                      '那边'}


def from_string_get_jieba_word_segmentation_statistics(string):
    """从一段字符串string中获取jieba分词统计"""
    words = jieba.lcut(string)
    dic_jwss = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            dic_jwss[word] = dic_jwss.get(word, 0) + 1
    for word in set_exclude_words:
        if word in dic_jwss:
            del dic_jwss[word]

    # 字典排序
    dic_jwss = dict(sorted(dic_jwss.items(), key=lambda x: x[1], reverse=True))
    return dic_jwss


def jieba_word_segmentation_statistics__per_n_chapters_as_a_group(json_data_n):
    """jieba分词统计_每n回作为一组"""
    dic_jwss_n = {}  # 记录统计结果
    for key in json_data_n["value"]:
        dic_jwss_temp = from_string_get_jieba_word_segmentation_statistics(json_data_n["value"][key]["content"])
        dic_jwss_n[key] = dic_jwss_temp

    # 将结果保存至全局变量管理器 global_dict
    _value_ = {"description": "jieba分词统计_每{}回".format(json_data_n["description"][1:4]), "value": dic_jwss_n}
    glv.set_value("dic_jwss_{}".format(json_data_n["description"][1:4]), _value_)
    return dic_jwss_n


def jieba_word_segmentation_statistics__first_eighty_and_last_forty_chapters(json_data_80_40):
    """jieba分词统计_前八十回与后四十回各为一组"""
    dic_jwss_80_40 = {}  # 记录统计结果
    for key in json_data_80_40["value"]:
        dic_jwss_temp = from_string_get_jieba_word_segmentation_statistics(json_data_80_40["value"][key]["content"])
        dic_jwss_80_40[key] = dic_jwss_temp

    # 将结果保存至全局变量管理器 global_dict
    _value_ = {"description": "jieba分词统计_前八十回与后四十回", "value": dic_jwss_80_40}
    glv.set_value("dic_jwss_80_40", _value_)
    return dic_jwss_80_40


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
    # jieba分词统计_每一回
    # _dic_jwss_001 = character_appearances_statistics(_json_data_001)
    # jieba分词统计_每五回
    # _dic_jwss_005 = word_number_statistics__per_n_chapters_as_a_group(_json_data_005)
    # jieba分词统计_每十回
    # _dic_jwss_010 = word_number_statistics__per_n_chapters_as_a_group(_json_data_010)
    # jieba分词统计_全文
    _dic_jwss_120 = jieba_word_segmentation_statistics__per_n_chapters_as_a_group(_json_data_120)
    # jieba分词统计_前八十回与后四十回
    _dic_jwss_80_40 = jieba_word_segmentation_statistics__first_eighty_and_last_forty_chapters(_json_data_80_40)

    "=========================分割线=========================分割线========================="
    # lt_del = []
    # for _word in _dic_jwss_120['第一回至一二零']:
    #     if _dic_jwss_120['第一回至一二零'][_word] > 150:
    #         lt_del.append(_word)
    print()
