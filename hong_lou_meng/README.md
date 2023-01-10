# 红楼梦词频分析

> 目标：分析高鹗版前八十回与后四十回的用词习惯差异。用数据说明红楼梦出自不同作者之手

---

&nbsp;

## 01 global_variable.py

**全局变量管理模块：** 将输入数据和输出数据都放置在全局变量global_dict中

> 使用方法：
>1. 引入模块 import global_variable as glv
>2. 使用函数对全局变量global_dict进行操作。如 glv.set_value(key, value)

&nbsp;

## 02 read_to_json_data.py

**文本文件读取模块：** 保存为json格式

> json_data = read_file_to_json("红楼梦.txt") &emsp; &emsp; 读取 红楼梦.txt 并保存在json_data中

&nbsp;

## 03 input_json_data.py

**输入数据管理模块:** 根据模块02得到的json_data数据进行进一步处理，获取不同章回结构的输入数据
> get_input_json_data() &emsp; &emsp; 输入数据管理模块，直接改函数代码获取不同的输入结构数据

---

&nbsp;

## 11 word_number__statistics.py

**字数统计模块：** 统计每章回的字数
> dic_wns_n = word_number_statistics__per_n_chapters_as_a_group(json_data_n)  
> &emsp; &emsp; 每n回字数统计  
> dic_wns_80_40 = word_number_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)  
> &emsp; &emsp; 前八十回与后四十回字数统计

&nbsp;

## 12 single_word_frequency_statistics.py

**单字频率统计模块：** 每章回的单个字的出现次数
> dic_swfs_n = single_word_frequency_statistics__per_n_chapters_as_a_group(json_data_n)  
> &emsp; &emsp; 每n回单字频率统计  
> dic_swfs_80_40 = single_word_frequency_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)    
> &emsp; &emsp; 前八十回与后四十回单字频率统计

&nbsp;

## # todo

- 人物出场统计
- jieba分词统计
