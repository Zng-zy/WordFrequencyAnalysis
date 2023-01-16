# 红楼梦词频分析

> 目标：分析高鹗版前八十回与后四十回的用词习惯差异。用数据说明红楼梦出自不同作者之手

---

&nbsp;

## 00 main.py
**主程序：** 函数入口

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

&nbsp;

## 04 save_result_to_json.py

**数据结果保存模块:** 保存结果为json文件
> save_result_to_json(global_dict) &emsp; &emsp; 将输出数据保存至result__global_dict.json

&nbsp;

## 05 jieba_word_frequency_adjustment_dict.txt
**jieba词库调整字典：** 在模块13<jieba_word_segmentation_statistics.py>和模块14<character_appearances_statistics.py>中调用，使jieba分词更准确
&nbsp;

## 06 result__global_dict.json

**output 程序运行输出结果**

&nbsp;

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

## 13 jieba_word_segmentation_statistics.py

**jieba分词统计模块**
> dic_jwss_n = jieba_word_segmentation_statistics__per_n_chapters_as_a_group(json_data_120)  
> &emsp; &emsp; 每n回jieba分词统计  
> dic_jwss_n = jieba_word_segmentation_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)  
> &emsp; &emsp; 前八十回与后四十回jieba分词统计  

&nbsp;

## 14 character_appearances_statistics.py

**人物出场次数统计模块**
> dic_cas_n = character_appearances_statistics__per_n_chapters_as_a_group(json_data_n)  
> &emsp; &emsp; 每n回人物出场次数统计  
> dic_cas_80_40 = character_appearances_statistics__first_eighty_and_last_forty_chapters(json_data_80_40)  
> &emsp; &emsp; 前八十回与后四十回人物出场次数统计  
> 
&nbsp;

## 14-1 verify_person_name_validity_for_cas.py

**为模块14验证人名集dic_name姓名有效性**
