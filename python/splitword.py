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



lexicon = ['�л�', '�л�����', '�Ӵ�', 'վ����', '��']
lexicon = [unicode(i, 'gbk') for i in lexicon]
max_len = 0
for x in lexicon:
    if len(x) > max_len:
        max_len = len(x)


sentence = unicode('�л�����Ӵ�վ������', 'gbk')
assert(4 == len(word_segment(lexicon, sentence, max_len)))

sentence = unicode('�л��л��л�����', 'gbk')
assert(3 == len(word_segment(lexicon, sentence, max_len)))


