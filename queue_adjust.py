# encoding=utf-8
'''
链接：https://www.nowcoder.net/questionTerminal/a4690c9a420b423db91b1c109c133a52
来源：牛客网

在幼儿园有n个小朋友排列为一个队伍，从左到右一个挨着一个编号为(0~n-1)。其中有一些是男生，有一些是女生，男生用'B'表示，女生用'G'表示。小朋友们都很顽皮，当一个男生挨着的是女生的时候就会发生矛盾。作为幼儿园的老师，你需要让男生挨着女生或者女生挨着男生的情况最少。你只能在原队形上进行调整，每次调整只能让相邻的两个小朋友交换位置，现在需要尽快完成队伍调整，你需要计算出最少需要调整多少次可以让上述情况最少。例如：
GGBBG -> GGBGB -> GGGBB
这样就使之前的两处男女相邻变为一处相邻，需要调整队形2次 
输入描述:
输入数据包括一个长度为n且只包含G和B的字符串.n不超过50.


输出描述:
输出一个整数，表示最少需要的调整队伍的次数
示例1
输入
GGBBG
输出
2
'''


def get_result(input_str):
    '''
    分别计算G在前和B在前的移动次数，取最小值。
 
    如果有B个男孩，则移到最左边的index分别为：0,1,2...B-1,所以所有index的和为（B-1）*B/2
    
    一次遍历，计算目前男孩所在的index的和为sumB，则sumB减去上面的和就是所求的结果。
    
    因此只要一次遍历，计算男孩所在的男孩的个数和男孩所在的index的和，求之差就行了。女孩同理。最后求最小值。
    :param input_str: 
    :return: 
    '''
    g_count = input_str.count("G")
    b_count = input_str.count("B")
    g_sum = g_count*(g_count-1)/2
    b_sum = b_count*(b_count-1)/2
    g_index_sum = b_index_sum = 0
    i=0
    for s in input_str:
        g_index_sum += i if s =="G" else 0
        b_index_sum += i if s =="B" else 0
        i+=1
    return min(g_index_sum-g_sum,b_index_sum-b_sum)


if __name__=="__main__":
    input_str = raw_input()
    result = get_result(input_str)
    print result