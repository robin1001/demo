#!/bin/env python
#coding=utf-8


def word_segment(lexicon, sentence, max_len):
    cur = 0
    result = []
    while cur < len(sentence):
        word_len = max_len
        while word_len > 0:
            if sentence[cur:cur+word_len] in lexicon:
                result.append(sentence[cur:cur+word_len])
                cur += word_len
                break
            else:
                word_len -= 1
    return result



lexicon = ['中华', '中华民族', '从此', '站起来', '了']
lexicon = [unicode(i, 'gbk') for i in lexicon]
max_len = 0
for x in lexicon:
    if len(x) > max_len:
        max_len = len(x)


sentence = unicode('中华民族从此站起来了', 'gbk')
assert(4 == len(word_segment(lexicon, sentence, max_len)))

sentence = unicode('中华中华中华民族', 'gbk')
assert(3 == len(word_segment(lexicon, sentence, max_len)))


