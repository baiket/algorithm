# encoding=utf-8
'''
链接：https://www.nowcoder.com/questionTerminal/276712b113c6456c8cf31c5073a4f9d7
来源：牛客网

牛牛有两个字符串（可能包含空格）,牛牛想找出其中最长的公共连续子串,希望你能帮助他,并输出其长度。 
输入描述:
输入为两行字符串（可能包含空格），长度均小于等于50.


输出描述:
输出为一个整数，表示最长公共连续子串的长度。
示例1
输入
abcde
abgde
输出
2
'''


def get_result(s1,s2):
    '''
    动态规划实现
    状态转移方程：s[i][j] = s[i-1][j-1]+1
    :param s1: 
    :param s2: 
    :return: 
    '''
    matrix = [[0 for i in range(len(s2))] for j in range(len(s1))] #初始化二维数据,先列后行
    max = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            temp = matrix[i-1][j-1] if i>0 and j>0 else 0
            if s1[i]==s2[j]:
                matrix[i][j]=temp+1
            else:
                matrix[i][j]=0
            max = matrix[i][j] if matrix[i][j]>max else max
    return max


if __name__=="__main__":
    input_str_1 = raw_input()
    input_str_2 = raw_input()
    # input_str_1 = "ABCDE"
    # input_str_2 = "ABCGR"
    result = get_result(input_str_1,input_str_2)
    print result