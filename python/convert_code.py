#!/bin/python
#encoding: utf-8
# Author: zhangbinbin
# Date: 2016-01-11
import sys
import codecs
import re

def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换            
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += unichr(inside_code)
    return rstring
    
def strB2Q(ustring):
    """半角转全角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 32:                                 #半角空格直接转化                  
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:        #半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += unichr(inside_code)
    return rstring

def delete_blank_in_number(string):
    words = string.split()
    assert(len(words) > 0)
    rstring = words[0]
    for i in range(1, len(words)):
        if words[i-1].isdigit() and words[i].isdigit():
            rstring += words[i]
        else:
            rstring += ' ' + words[i]
    return rstring

number_to_chinese = {'1':'一', '2':'二', '3':'三', '4':'四', '5':'五', \
                     '6':'六', '7':'七', '8':'八', '9':'九', '0': '零'}
def convert_number_to_chinese(string):
    rstring = ''
    words = string.split()
    for i in range(0, len(words)):
        word = words[i]
        if word.isdigit():
            # Read as year, like 1994 2001
            if i < len(words) - 1 and words[i+1] == '年' and len(word) == 4: 
                for x in word:
                    assert(x in number_to_chinese)
                    rstring += number_to_chinese[x]
            # Start with 0
            elif word[0] == '0':
                for x in word:
                    rstring += number_to_chinese[x]
            # Read as regular digit
            else:
                if len(words[i]) == 1: rstring += number_to_chinese[word]
                else:
                    cur = len(word) - 1
                    number = ''
                    bit = 0
                    # Ignore 0 in the end
                    while cur >= 0 and word[cur] == '0': 
                        cur -= 1
                        bit += 1
                    assert(cur >= 0)
                    while cur >= 0:
                        bitstr = number_to_chinese[word[cur]] 
                        if bit == 0: pass
                        elif bit % 8 == 0: bitstr += '亿'
                        elif bit % 4 == 0: bitstr += '万'
                        elif bit % 3 == 0: bitstr += '千'
                        elif bit % 2 == 0: bitstr += '百'
                        elif bit % 1 == 0: bitstr += '十'
                        number = bitstr + number
                        cur -= 1
                        bit += 1
                        if cur >= 0 and word[cur] == '0':
                            # Handle 0 in middle, like 3001 3010
                            while cur >= 0 and word[cur] == '0':
                                cur -= 1
                                bit += 1
                            assert(cur >= 0)
                            number = '零' + number
                    if number.startswith('一十'):
                        number = number.decode('utf8')[1:] 
                        number = number.encode('utf8')
                    rstring += number  
        else:
            rstring += word
        rstring += ' '
    return rstring.strip()

def convert_number_to_chinese_test():
    assert(convert_number_to_chinese('1990 年') == '一九九零 年')
    assert(convert_number_to_chinese('2001 年') == '二零零一 年')
    #print convert_number_to_chinese('1990')
    assert(convert_number_to_chinese('1990') == '一千九百九十')
    assert(convert_number_to_chinese('11990') == '一万一千九百九十')
    assert(convert_number_to_chinese('01234') == '零一二三四')
    assert(convert_number_to_chinese('3001') == '三千零一')
    assert(convert_number_to_chinese('3010') == '三千零一十')
    #print convert_number_to_chinese('11')
    assert(convert_number_to_chinese('11') == '十一')
    assert(convert_number_to_chinese('110001') == '十一万零一')

if __name__ == '__main__':
    #convert_number_to_chinese_test()

    if len(sys.argv) != 2:
        print 'Usage: convert_code.py infile'
        sys.exit(1)
    #fid = codecs.open(sys.argv[1], encoding='UTF-8')
    #context = fid.read()
    #new_context = strQ2B(context) 
    #fid.close()
    #print new_context.encode('UTF-8')

    with open(sys.argv[1]) as fid:
        lines = fid.read().decode('utf8')
        for line in lines.split('\n'):
            if line == '': continue
            string = strQ2B(line).encode('utf8')
            string = delete_blank_in_number(string)
            string = convert_number_to_chinese(string)
            print string
