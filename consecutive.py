# encoding=utf-8
'''
链接：https://www.nowcoder.com/questionTerminal/c3083cd30d5043e1b95000f139b5b2c9
来源：牛客网

牛牛的好朋友羊羊在纸上写了n+1个整数，羊羊接着抹除掉了一个整数，给牛牛猜他抹除掉的数字是什么。
牛牛知道羊羊写的整数神排序之后是一串连续的正整数，牛牛现在要猜出所有可能是抹除掉的整数。例如：
10 7 12 8 11 那么抹除掉的整数只可能是9
5 6 7 8 那么抹除掉的整数可能是4也可能是9

输入描述:
输入包括2行：
 第一行为整数n(1 <= n <= 50)，即抹除一个数之后剩下的数字个数
 第二行为n个整数num[i] (1 <= num[i] <= 1000000000)


输出描述:
在一行中输出所有可能是抹除掉的数,从小到大输出,用空格分割,行末无空格。如果没有可能的数，则输出mistake
示例1
输入
2 3 6
输出
mistake
'''


def get_result(n,l):
    l.sort()    #先排序
    if n==1 and l[0]==1: #只有一个数字时
        return 2
    if l[-1]>1000000000 or l[0]<1: #超过范围
        return
    if l[-1]-l[0]>n: #不符合规范
        return "mistake"
    for i in range(0,len(l)-1):
        if l[i]+1<l[i+1]:
           return l[i]+1
        elif l[i]+1>l[i+1]: #重复的数字
            return "mistake"
    return "{0} {1}".format(l[0]-1,l[-1]+1) if l[0]-1>0 else l[-1]+1 #防止1起始的字符串


if __name__=="__main__":

    input_size = int(raw_input())
    input_str = raw_input()
    input_int_list = [int(a) for a in input_str.split()]
    # n=4
    # l = [3,7,4,6]
    result = get_result(input_size,input_int_list)
    print result