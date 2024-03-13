import math
# py的切片是左闭右开
# 全部使用索引
# 防止越界
def search(p,arr,low,high)->int:
    m = (high + low)//2
    v = arr[m]
    if v == p:
        return  m
    elif p < v:
        return search(p,arr,low,m-1) if low < m else -1
    elif p > v:
        return search(p,arr,m+1,high) if high > m else -1
    
def search(p,arr,low,high)->int:
    if low > high:
        return -1
    m = (high + low)//2
    v = arr[m]
    if v == p:
        return  m
    elif p < v:
        return search(p,arr,low,m-1)
    elif p > v:
        return search(p,arr,m+1,high)
arr = [1,2,3,4,5,100,200]
i = search(101,arr,0,len(arr)-1)
print(i)