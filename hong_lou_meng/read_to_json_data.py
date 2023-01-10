# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@ Time  : 2023/01/09
@ Author: Zng_sh
@ Description： 读取红楼梦文本文件，处理段落标点等转化为json格式
"""
import re


def read_file_to_json(filename):
    """初始化dic_flag<flag管理容器>和json_data<数据储存容器>"""
    # 读取章回号，作为键
    lt_key = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line[0] == "第":
                lt_key.append(line[13:16])
    # 初始化 dic_flag<flag管理容器>
    dic_flag = dict.fromkeys(lt_key, 0)
    # 初始化 json_data<数据储存容器>
    json_data = dict(zip(lt_key, [{"title": "", "content": ""} for _ in range(len(lt_key))]))

    """提取数据放入json_data<数据储存容器>中"""
    with open(filename, 'r', encoding='utf-8') as f:
        counter = 0
        for line in f:
            counter += 1
            line = line.replace("\n", "")

            # flag管理容器
            if True:
                # flag 清零
                if line == "":
                    dic_flag = dict.fromkeys(dic_flag, 0)
                    continue
                # flag 竖起
                elif line[0] == "第":
                    dic_flag[line[13:16]] = 1
                    json_data[line[13:16]]["title"] = line[17:33]
                    next(f)
                    continue

            # main 提取数据放入json_data<数据储存容器>中
            lt_temp = [key for key in dic_flag if dic_flag[key] == 1]
            if len(lt_temp) == 1:
                # 去除空格和回车
                line = line.replace(" ", "").replace(u'\u3000', u'').replace('\n', '').replace('\r', '')
                # 去除标点符号
                del_character = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､　、〃〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏﹑﹔·！？｡。'
                line = re.sub(r"[%s]+" % del_character, "", line)
                json_data[lt_temp[0]]["content"] += line
    return json_data


if __name__ == '__main__':
    _json_data = read_file_to_json("红楼梦.txt")
    pass
