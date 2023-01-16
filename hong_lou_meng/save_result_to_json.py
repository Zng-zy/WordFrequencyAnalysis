# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/15
@ Author: Zng_sh
@ Description：保存结果为json文件
"""
import json


def save_result_to_json(global_dict):
    # 去除global_dict中输入数据
    dic_result = {}
    for key in global_dict:
        if "json_data" not in key:
            dic_result[key] = global_dict[key]
    # 数据写入
    with open("result__global_dict.json", "w", encoding="utf-8") as f:
        json.dump(dic_result, f, ensure_ascii=False)
    print("Successfully saved data to result__global_dict.json!")
    return
