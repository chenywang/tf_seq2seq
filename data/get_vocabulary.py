# -*- coding:utf-8 -*-
# @Author : Michael-Wang
import json


def get_vocabulary(text_path, dict_path):
    f = open(text_path)
    vocabulary = dict()
    for line in f.readlines():
        for word in line.split(' '):
            vocabulary.setdefault(word, 0)
            vocabulary[word] += 1

    with open(dict_path, "w") as f:
        json.dump(vocabulary, f)


if __name__ == '__main__':
    get_vocabulary('../data/english.txt', '../data/english_dict.json')
    get_vocabulary('../data/chinese.txt', '../data/chinese_dict.json')
