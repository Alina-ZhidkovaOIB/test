
n1 = int(input())
numbers1 = set(map(int, input().split()))
n2 = int(input())
numbers2 = set(map(int, input().split()))

common_numbers = numbers1.intersection(numbers2)
print(len(common_numbers))
