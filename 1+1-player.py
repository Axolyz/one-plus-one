# coding:utf-8
# @Author: Li Baoyan
# @Date:   2019-07-12 10:57:58
# @Last Modified by:   Administrator
# @Last Modified time: 2019-07-25 08:16:14
# 增加了检查用户输入的防作弊机制。增加了最高分机制。
# 对平局的说明。
# 多进制及更强的ai

import random
import re


def chek():
    global q
    global e
    global a
    global d
    if q == 0:
        q = " "
    if e == 0:
        e = " "
    if a == 0:
        a = " "
    if d == 0:
        d = " "


def padd(o):
    global n
    global d
    global a
    for c in o:
        if c == "a":
            a = eval(o) % n
        if c == "d":
            d = eval(o) % n


def input_check(o):
    try:
        m = re.match(r'(\w)\+(\w)', o)

        if m.group(1) in cnum and m.group(2) in pnum:
            return True
        elif m.group(1) in pnum and m.group(2) in cnum:
            return True
        else:
            return False
    except AttributeError:
        return False


def cadd(o):
    global n
    global q
    global e
    for c in o:
        if c == "q":
            q = eval(o) % n
        if c == "e":
            e = eval(o) % n


def tel(a, b, c, d, e):
    global n
    if (c != " " and (a == " " or b == " " or (a + b + b) % n == 0 or (a + b + c) % n == 0)) or (c == " " and (a == " " or b == " " or (a + b + b) % n == 0)):
        opts.remove(d)
        opts2.remove(d)
    if a + b == e:
        opts2.remove(d)


n = 10
draw_num = 20
hel = '''1+1是一个古老的双人策略游戏。规则说明：
1，一方需以自己两手上的任意一个数字与对面的任意一个数字相加，相加后自己的数字变为这两个数字的和，和只取个位。
2，如果和为10的倍数，则这个数字被撤掉，不再参与运算。
3，先把两个数字全部撤掉者胜利。
操作说明：
1，界面上四个数字分别对应键盘的q，e，a，d这四个键的位置。
2，输入指令时应输入含字母的加法语句，如“q+a”或“a+q”，否则可能会导致bug。
'''
cnum = ["q", "e"]
pnum = ["a", "d"]
while True:
    menu = input('输入任意值开始游戏，输入h查看帮助（初次使用请务必查看帮助）。')
    if menu == "h":
        print(hel)
    else:
        break

while True:
    q = 1
    a = 1
    e = 1
    d = 1
    p = 0
    rnd = 0
    while True:
        chek()
        print("轮数：" + str(rnd) + "\n\n" + str(q) + "       " +
              str(e) + "\n\n" + str(a) + "       " + str(d) + "\n\n")
        while True:
            try:
                k = input("输入指令：")
                while input_check(k) is False:
                    print("指令不符合规范！")
                    k = input("输入指令：")
                padd(k)
                break
            except TypeError:
                print("已撤下的字符不能参与运算！")
                continue
        chek()
        if a == " " and d == " ":
            rnd += 1
            print("轮数：" + str(rnd) + "\n\n" + str(q) + "       " +
                  str(e) + "\n\n" + str(a) + "       " + str(d) + "\n\n")
            print("You are winner!\n你的成绩为" + str(rnd) +
                  "轮。")
            break
        chek()
        rnd += 1
        print("轮数：" + str(rnd) + "\n\n" + str(q) + "       " +
              str(e) + "\n\n" + str(a) + "       " + str(d) + "\n\n")
        opts = ['q+a', 'q+d', 'e+a', 'e+d']
        opts1 = opts[:]
        opts2 = opts[:]
        tel(q, a, d, 'q+a', e)
        tel(e, a, d, 'e+a', q)
        tel(q, d, a, 'q+d', e)
        tel(e, d, a, 'e+d', q)
        if opts2 != []:
            opt = random.choice(opts2)
        elif opts != []:
            opt = random.choice(opts)
        else:
            while True:
                try:
                    opt = random.choice(opts1)
                    s = eval(opt) % n
                    break
                except TypeError:
                    continue
        for w in opts:
            if eval(w) % n == 0:
                opt = w
        cadd(opt)
        chek()
        if q == " " and e == " ":
            rnd += 1
            print("轮数：" + str(rnd) + "\n\n" + str(q) + "       " +
                  str(e) + "\n\n" + str(a) + "       " + str(d) + "\n\n")
            print("Computer is winner!")
            break
        if (q == " " or e == " ") and (a == " " or d == " "):
            p += 1
            if p == draw_num:
                print("A draw!")
                break
    wwwwwwttttfffff = input("按回车键退出，输入任意值后回车重新开始。")
    if wwwwwwttttfffff == "":
        break
