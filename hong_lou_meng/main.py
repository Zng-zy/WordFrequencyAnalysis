# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/09
@ Author: Zng_sh
@ Description： 配置全局变量
"""
import global_variable as glv
import input_json_data as ijd
import word_number_statistics as wns  # 字数统计
import single_word_frequency_statistics as swfs  # 单字频率统计
import jieba_word_segmentation_statistics as jwss  # jieba分词统计
import character_appearances_statistics as cas  # 人物出场次数统计
import save_result_to_json as srj

# 初始化全局变量管理器 global_dict
glv.init()
# 全局变量管理器 global_dict (查看所有数据结果)
global_dict = glv.get_global_dict()

# 获取输入数据 --> 要获取不同输入数据时须进入函数get_input_json_data()内修改
ijd.get_input_json_data()  # 将json_data保存至global_dict中
json_data_001 = global_dict["json_data_001"]
# json_data_005 = global_dict["json_data_005"]
# json_data_010 = global_dict["json_data_010"]
json_data_120 = global_dict["json_data_120"]
json_data_80_40 = global_dict["json_data_80_40"]

"============================== word_number_statistics.py 字数统计 =============================="
print("Loading word_number_statistics...")
wns.word_number_statistics__per_n_chapters_as_a_group(json_data_001)  # 字数统计_每一回
# wns.word_number_statistics__per_n_chapters_as_a_group(json_data_005)  # 字数统计_每五回
# wns.word_number_statistics__per_n_chapters_as_a_group(json_data_010)  # 字数统计_每十回
wns.word_number_statistics__per_n_chapters_as_a_group(json_data_120)  # 字数统计_全文
wns.word_number_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)  # 字数统计_前八十回与后四十回

"=======================  single_word_frequency_statistics.py 单字频率统计  ======================="
print("Loading single_word_frequency_statistics...")
# swfs.single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_001)  # 单字频率统计_每一回
# swfs.single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_005)  # 单字频率统计_每五回
# swfs.single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_010)  # 单字频率统计_每十回
# swfs.single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_120)  # 单字频率统计_全文
# swfs.single_word_frequency_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)  # 单字频率统计_前八十回与后四十回

"======================  jieba_word_segmentation_statistics.py jieba分词统计  ======================"
print("Loading jieba_word_segmentation_statistics...")
# jwss.jieba_word_segmentation_statistics__per_n_chapters_as_a_group(json_data_001)  # jieba分词统计_每一回
# jwss.jieba_word_segmentation_statistics__per_n_chapters_as_a_group(json_data_005)  # jieba分词统计_每五回
# jwss.jieba_word_segmentation_statistics__per_n_chapters_as_a_group(json_data_010)  # jieba分词统计_每十回
# jwss.jieba_word_segmentation_statistics__per_n_chapters_as_a_group(json_data_120)  # jieba分词统计_全文
# jwss.jieba_word_segmentation_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)  # jieba分词统计_前八十回与后四十回

"======================  character_appearances_statistics.py 人物出场次数统计  ======================"
print("Loading character_appearances_statistics...")
cas.character_appearances_statistics__per_n_chapters_as_a_group(json_data_001)  # 人物出场次数统计_每一回
# cas.character_appearances_statistics__per_n_chapters_as_a_group(json_data_005)  # 人物出场次数统计_每五回
# cas.character_appearances_statistics__per_n_chapters_as_a_group(json_data_010)  # 人物出场次数统计_每十回
cas.character_appearances_statistics__per_n_chapters_as_a_group(json_data_120)  # 人物出场次数统计_全文
cas.character_appearances_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)  # 人物出场次数统计_前八十回与后四十回

"================================================================================================"

# 保存结果为json文件<result__global_dict.json>
srj.save_result_to_json(global_dict)

print("-"*50 + "\nFinish!")
