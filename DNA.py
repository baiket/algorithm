# encoding=utf-8
'''
链接：https://www.nowcoder.com/questionTerminal/e95337f886f54110b92318f693cd8fad
来源：牛客网

DNA分子是以4种脱氧核苷酸为单位连接而成的长链，这4种脱氧核苷酸分别含有A,T,C,G四种碱基。碱基互补配对原则：A和T是配对的，C和G是配对的。如果两条碱基链长度是相同的并且每个位置的碱基是配对的，那么他们就可以配对合成为DNA的双螺旋结构。现在给出两条碱基链，允许在其中一条上做替换操作：把序列上的某个位置的碱基更换为另外一种碱基。问最少需要多少次让两条碱基链配对成功 
输入描述:
输入包括一行： 包括两个字符串,分别表示两条链,两个字符串长度相同且长度均小于等于50。


输出描述:
输出一个整数，即最少需要多少次让两条碱基链配对成功
示例1
输入
ACGT TGCA
输出
0
'''

def get_result(str_1,str_2):
    count=0
    rule_dict = {"A":"T","T":"A","C":"G","G":"C"}  # 替换的字典规则
    if len(str_1)!=len(str_2) or len(str_1)>50 or len(str_2)>50: #判断是否满足需求
        return
    for i in range(0,len(str_1)):
        if str_1[i] not in rule_dict or str_2[i] not in rule_dict: #判断字符串是否合规
            return
        if rule_dict[str_1[i]] != str_2[i]:
            count += 1
    return count


if __name__=="__main__":
    str_1 = "ATCGGCTTAGCC"
    str_2 = "TCTAATCGGGCG"
    result = get_result(str_1,str_2)
    print result