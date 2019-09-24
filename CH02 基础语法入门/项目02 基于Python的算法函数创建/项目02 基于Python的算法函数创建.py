'''
【项目02】 基于Python的算法函数创建

作业要求：
根据不同题目，完成代码书写并成功运行
'''
#题目1：有1,2,3,4四个数字，能组成多少个互不相同且不重复数字的两位数？都是多少？
#改题目不用创建函数

n = 0
m = []
for i in range(1,5):
    for j in range(1,5):
        if i != j:
            n += 1
            #print(i*10+j)
            num = '%i%i' %(i,j)
            #print('满足条件的数字为：%s' %num)
            m.append(num)
print('满足条件的数字一共有：%i' %n)
print(m)         

#题目2：输入三个整数x,y,z，请把这三个数由小到大输出，可调用input()，(需要加判断：判断输入数据是是否为数字)
#提示：判断是否为数字:isdigit()
#改题目需要创建函数

def f(n): #n表是输入次数
    lst = []
    for i in range(1,n+1):
        num = input("请输入%i个数字：" % i)
        while num.isdigit() == False:
            num = input('输入的内容不为数字，请重新输入第%i个数字：'% i)
        else:
            lst.append(float(num))
    return(sorted(lst))
f(3)

#题目3：输入一行字符,分别统计出其中英文字母，空格，数字和其他字符的个数
#提示：利用while语句，条件为输入的字符不为'/n'
#该题目不需要创建函数

st = input("请输入一行字符：\n")
letters = 0
space = 0
digit = 0
others = 0
for c in st:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digit += 1
    elif c.isspace():
        space += 1
    else:
        others += 1
print('输入的字符中，有{}个字母，有{}个空格，有{}个数字，及{}其他字符'.format(letters,space,digit,others))

#题目4：猴子吃桃问题
#猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个，
#第二天早上又将剩下的桃子吃掉一半，又多吃了一个
#以后每天早上都吃了前一天剩下的一半零一个，到底10天早上，只剩下一个桃子了，求第一天共摘了多少？
#提示：才去逆向思维的方法，从后往前推断
#该题目不需要创建函数

n = 1 #最后一天剩一个
for day in range(9,0,-1):
    m = (n + 1) * 2
    n = m
    print('第%i天剩下%i个桃子' % (day,n))
print('第一天一共采摘了%i个桃子' % n)

#题目5：猜数字问题，要求如下：
# ① 随机生成1个整数
# ② 猜一个数字并输入
# ③ 判断是大是小，直到猜正确
# ④ 判断时间
#提示：需要time模块，random模块
#该题目不需要创建函数

import random
import time

N = random.randint(0,100)
print(N)
guess = int(input("请输入你猜的数字(小于100)："))
start = time.time()

while guess != N:
    if guess > N:
        print('猜大了')
        guess = int(input("请重新输入你猜的数字(小于100)："))
    elif guess < N:
        print('猜小了')
        guess = int(input("请重新输入你猜的数字(小于100)："))

end = time.time()
time = end - start
print("恭喜你，答对了，正确答案为%i" % N)
print("共花费时间%f秒" % time)