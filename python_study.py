# -*- coding:utf-8 -*-
import os





with open('结果.txt','a') as result:
    result = {}
    docs = open('太空旅客.txt')
    path = '词典/'
    names = os.listdir(path)
    for name in names:
        path_file ='词典/' + file + '/'
        s_names = os.listdir(path_file)
        for s_name in s_names:
            path_txt = '词典/' + file + '/' + s_name
            words = open(path_txt)
            for word in words:
                result[name] += 1
                for comment in docs:
                    if word in comment:
                        result.write(name + ':' + result[word] + '\n')
