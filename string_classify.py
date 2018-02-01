# encoding=utf-8
'''
链接：https://www.nowcoder.com/questionTerminal/9fbb4d95e6164cd9ab52e859fbe8f4ec
来源：牛客网

牛牛有N个字符串，他想将这些字符串分类，他认为两个字符串A和B属于同一类需要满足以下条件：
A中交换任意位置的两个字符，最终可以得到B，交换的次数不限。比如：abc与bca就是同一类字符串。
现在牛牛想知道这N个字符串可以分成几类。 
输入描述:
首先输入一个正整数N（1 <= N <= 50），接下来输入N个字符串，每个字符串长度不超过50。


输出描述:
输出一个整数表示分类的个数。
示例1
输入
4
abcd
abdc
dabc
bacd
输出
1
'''

def get_result(l):
    '''
    通过字典收集每个字符出现的次数，然后利用set的唯一性，统计分类的个数
    :param l: 
    :return: 
    '''
    rs=set()
    for s in l:
        s_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 0
            s_dict[i]+=1
        rs.add(tuple(s_dict.items()))
    return len(rs)


if __name__=="__main__":
    N = int(raw_input())
    l = []
    for i in range(N):
        l.append(raw_input())
    result = get_result(l)
    print result