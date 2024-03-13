
# 外层表示循环次数，没循环一次产生一个结果，最后一个没有需要比较的，所以只需要 n -1 次
# 内层循环表示冒泡过程，由于需要和后一位比较，所以最后一位需要忽略
def sort(arr):
    for a in range(1,len(arr)):
        for b in range(0,len(arr) - a -1):
            if(arr[b] > arr[b+1]):
                arr[b],arr[b+1] = arr[b+1],arr[b]


arr = [3,2,5,9,6,7,2]
sort(arr)
print(arr)