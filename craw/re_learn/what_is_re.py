# coding=utf-8

import re


class ReDemo:

    def __init__(self):
        pass

    @staticmethod
    def rematch(source, pattern_sentence):
        print("--------------")
        print("源字符串: " + source)
        print ("匹配的规则: " + pattern_sentence)
        patten = re.compile(pattern_sentence)
        res = patten.match(source)

        if res is None:
            print("none match")
        else:
            print(res.span())
            print("匹配结果: " + res.group())


if __name__ == '__main__':

    # 配置 单个任意字符
    string_dot_1 = 'http://'
    string_dot_2 = 'htfp://'
    string_dot_3 = 'ftfp://'

    patten_dot = r'ht.p'
    ReDemo.rematch(string_dot_1, patten_dot)
    ReDemo.rematch(string_dot_2, patten_dot)
    ReDemo.rematch(string_dot_3, patten_dot)

    # ^ 以什么开头
    string_www = 'http://www.baidu.com/item/'

    patten_arrow = r'^http'
    ReDemo.rematch(string_dot_1, patten_arrow)
    ReDemo.rematch(string_dot_2, patten_arrow)
    ReDemo.rematch(string_www, patten_arrow)

    # 英文字母 a-z
    string_a_z = 'ajhfhbaojsfhouashfoishfohsjhodbh'
    string_a_0 = '0sfhks'

    patten_a_z = r'[a-zA-Z]'
    ReDemo.rematch(string_a_z, patten_a_z)
    ReDemo.rematch(string_a_0, patten_a_z)

    # [] ,匹配中括号
    string_a_quote = '[s]'
    string_a_quote_more = '[sdd]'

    patten_a_quote = r'\[[a-zA-Z]\]'
    ReDemo.rematch(string_a_quote, patten_a_quote)
    # 中间是多个的话 就匹配不到
    ReDemo.rematch(string_a_quote_more, patten_a_quote)

    #  * 匹配前一个字符0次或者任意次
    string_star = 'adjgdr'
    patern_star = r'A*'
    ReDemo.rematch(string_star, patern_star)

    # + 匹配前一个字符1次或者任意次
    patern_add = r'A+'
    ReDemo.rematch(string_star, patern_add)
    # ? 匹配前一个字符0次或者1次
    string_num = '09'
    pattern_ques = r'[1-9]?[0-9]'
    ReDemo.rematch(string_num, pattern_ques)
    # {m} 或者 {m, n} 匹配前一个字符m次或者n次
    string_m = '1234567'
    pattern_m = r'[a-zA-Z0-9]{3}'
    ReDemo.rematch(string_m, pattern_m)
    # *? 或者 +? 或者 ?? 匹配模式变为非贪婪(尽可能的少匹配字符)

    # $ 以什么结尾

    # \A  \Z

