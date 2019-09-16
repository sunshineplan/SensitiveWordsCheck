#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def check(article, filename):
    result = []
    if article == '':
        return ['Please enter something.']
    check_list = file2list(filename)
    if check_list == []:
        return ['Error!\nSensitive Words List is empty.\nPlease check your setting.'], ['empty']
    reg_keywords = [i.replace('@', '.?') for i in check_list if '@' in i]
    string_keywords = [i for i in check_list if '@' not in i]
    for i in reg_keywords:
        p = re.compile(i)
        n = len(p.findall(article))
        if n != 0:
            result.append('[' + i.replace('.?', '@') +
                          '] appears ' + str(n) + ' time(s).')
    for i in string_keywords:
        n = article.upper().count(i.upper())
        if n != 0:
            result.append('[' + i + '] appears ' + str(n) + ' time(s).')
    result = sorted(result)
    if result == []:
        result.append('Congratulations! No sensitive words were found.')
    else:
        result.insert(0, str(len(result)) + ' sensitive word(s) found:\n')
    return result, reg_keywords, string_keywords


def file2list(filename):
    file = open(filename, encoding='utf-8')
    data = file.readlines()
    file.close()
    data = [i.rstrip('\n') for i in data]
    data = [i.strip() for i in data]
    data = [i for i in data if i != '']
    output = list(set(data))
    return output


def str2file(string_data, filename):
    file = open(filename, 'w', encoding='utf-8')
    file.write(string_data)
    file.close()
