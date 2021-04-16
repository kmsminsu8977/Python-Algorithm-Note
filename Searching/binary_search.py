import sys

def binary_search(data, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid + 1
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1

target = int(input("target : "))
input = sys.stdin.readline
data = list(map(int,input().split())) # 5 10 15 20 25
print(data)
n =  len(data)

data.sort()
print(binary_search(data, 10, 0, n-1))
