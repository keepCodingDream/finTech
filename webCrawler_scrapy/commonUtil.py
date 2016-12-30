#!/usr/bin/python
# -*- coding: utf-8 -*-

import chardet


class CommonUtil:
    """
       保存一些共方法
    """

    def __init__(self):
        pass

    # 用于去除list中的空格，并组成字符串
    @staticmethod
    def delListEmpty(ori_list):
        result = ''
        for item in ori_list:
            after = item.strip().replace('\\t', '').replace('\\n', '').replace(' ', '').replace('\\r', '')
            if after is not None and len(after) > 5:
                result += after
            return result

    # 抽取list元素下所有的text()
    @staticmethod
    def extractContent(ori_list):
        full_content = []
        for sub_item in ori_list:
            sub_content_list = sub_item.xpath('string(.)').extract()
            for sub_content in sub_content_list:
                full_content.append(sub_content.strip())
        return CommonUtil.delListEmpty(full_content)
