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
import single_word_frequency_statistics as swfs

# 初始化全局变量管理器 global_dict
glv.init()
# 全局变量管理器 global_dict (查看所有数据结果)
global_dict = glv.get_global_dict()

# 获取输入数据
ijd.get_input_json_data()  # 将json_data保存至global_dict中
json_data_001 = global_dict["json_data_001"]
json_data_005 = global_dict["json_data_005"]
json_data_010 = global_dict["json_data_010"]
json_data_120 = global_dict["json_data_120"]
json_data_80_40 = global_dict["json_data_80_40"]

"============================== word_number_statistics.py 字数统计 =============================="
wns.word_number_statistics__per_n_chapters_as_a_group(json_data_001)  # 字数统计_每一回
wns.word_number_statistics__per_n_chapters_as_a_group(json_data_005)  # 字数统计_每五回
wns.word_number_statistics__per_n_chapters_as_a_group(json_data_010)  # 字数统计_每十回
wns.word_number_statistics__per_n_chapters_as_a_group(json_data_120)  # 字数统计_全文
wns.word_number_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)  # 字数统计_前八十回与后四十回

"=======================  single_word_frequency_statistics.py 单字频率统计  ======================="
swfs.single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_001)  # 单字频率统计_每一回
swfs.single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_005)  # 单字频率统计_每五回
swfs.single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_010)  # 单字频率统计_每十回
swfs.single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_120)  # 单字频率统计_全文
swfs.single_word_frequency_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)  # 单字频率统计_前八十回与后四十回

print()
