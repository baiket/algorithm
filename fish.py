# encoding=utf-8
'''
链接：https://www.nowcoder.com/questionTerminal/e3dd485dd23a42899228305658457927
来源：牛客网

牛牛有一个鱼缸。鱼缸里面已经有n条鱼，每条鱼的大小为fishSize[i] (1 ≤ i ≤ n,均为正整数)，牛牛现在想把新捕捉的鱼放入鱼缸。鱼缸内存在着大鱼吃小鱼的定律。
经过观察，牛牛发现一条鱼A的大小为另外一条鱼B大小的2倍到10倍(包括2倍大小和10倍大小)，鱼A会吃掉鱼B。考虑到这个，牛牛要放入的鱼就需要保证：
1、放进去的鱼是安全的，不会被其他鱼吃掉
2、这条鱼放进去也不能吃掉其他鱼
鱼缸里面已经存在的鱼已经相处了很久，不考虑他们互相捕食。现在知道新放入鱼的大小范围[minSize,maxSize](考虑鱼的大小都是整数表示),
牛牛想知道有多少种大小的鱼可以放入这个鱼缸。 

输入描述:

输入数据包括3行. 
 第一行为新放入鱼的尺寸范围minSize,maxSize(1 ≤ minSize,maxSize ≤ 1000)，以空格分隔。
 第二行为鱼缸里面已经有鱼的数量n(1 ≤ n ≤ 50)
 第三行为已经有的鱼的大小fishSize[i](1 ≤ fishSize[i] ≤ 1000)，以空格分隔。


输出描述:
输出有多少种大小的鱼可以放入这个鱼缸。考虑鱼的大小都是整数表示

示例1

输入
1 12
1
1
输出
3
'''

import math


def danger_fish(fish_size):
    temp_dict = {}
    min_danger = max_danger = set()
    for i in fish_size: # 遍历鱼塘，并集找出所有不安全的鱼
        if i not in temp_dict: # 去除重复
            temp_dict[i] = True
            min_danger = min_danger | set(range(int(math.ceil(i/10.0)),int(math.floor(i/2.0))+1))
            max_danger = max_danger | set(range(i*2 if i*2<=1000 else 1000,i*10+1 if (i*10+1)<=1000 else 1000))
    return min_danger,max_danger


def get_result(min_size,max_size,n,fish_size):

    new_size = set(range(min_size,max_size+1))
    min_danger, max_danger = danger_fish(fish_size)
    result = (new_size-min_danger)&(new_size-max_danger)  # 去除不安全的鱼求交集，找到安全的鱼
    return result

if __name__=="__main__":
    min_size = 1
    max_size = 30
    n = 4
    fish_size = [1,8,127,619]
    result = get_result(min_size,max_size,n,fish_size)
    print len(result),result