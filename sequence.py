# encoding=utf-8
#
'''
链接：https://www.nowcoder.com/questionTerminal/46eb436eb6564a62b9f972160e1699c9
来源：牛客网

给出一个正整数N和长度L，找出一段长度大于等于L的连续非负整数，他们的和恰好为N。答案可能有多个，我我们需要找出长度最小的那个。
例如 N = 18 L = 2：
5 + 6 + 7 = 18 
3 + 4 + 5 + 6 = 18
都是满足要求的，但是我们输出更短的 5 6 7

输入描述:
输入数据包括一行： 两个正整数N(1 ≤ N ≤ 1000000000),L(2 ≤ L ≤ 100)


输出描述:
从小到大输出这段连续非负整数，以空格分隔，行末无空格。如果没有这样的序列或者找出的序列长度大于100，则输出No
示例1
输入
18 2
输出
5 6 7

'''

def get_result(n,l):
    result_list = []
    if n<1 or n>1000000000:
        return
    if l<2 or l>100:
        return
    for i in range(l,101): #根据等差数列求和公式的变形，判断a1是否存在
        f1 = 2*n - i*i +i
        if f1%(2*i) == 0 and f1>=0:
            a1 = f1/(2*i)
            for j in range(0,i):
                result_list.append(str(a1+j))
            return " ".join(result_list)
    return "No"


if __name__=="__main__":
    input_str = raw_input()
    input_int_list = [int(a) for a in input_str.split()]
    n,l = input_int_list[0],input_int_list[1]
    result = get_result(n,l)
    print result