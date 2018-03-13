#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def check(article,filename):
    result = []
    check_list = file2list(filename)
    reg = [i for i in check_list if '@' in i]
    noreg = [i for i in check_list if '@' not in i]
    for i in reg:
        p = re.compile(i.replace('@', '.?'))
        n = len(p.findall(article))
        if n != 0:
            result.append('[' + i + '] appears ' + str(n) + ' time(s).')
    for i in noreg:
        n = article.count(i)
        if n != 0:
            result.append('[' + i + '] appears ' + str(n) + ' time(s).')
    result = sorted(result)
    if result == []:
        result.append('Congratulations! No sensitive words were found.')
    else:
        if len(result) == 1:
            result.insert(0, str(len(result)) + ' sensitive word was found:')
        else:
            result.insert(0, str(len(result)) + ' sensitive words were found:')
        result.insert(1, '')
    return result


def file2list(filename):
    file = open(filename, encoding='utf-8')
    data = file.readlines()
    file.close()
    data = [i.rstrip('\n') for i in data]
    data = [i.strip() for i in data]
    data = [i for i in data if i!='']
    output = list(set(data))
    return output


def str2file(string_data,filename):
    file=open(filename,'w',encoding='utf-8')
    file.write(string_data)
    file.close()
    return 0