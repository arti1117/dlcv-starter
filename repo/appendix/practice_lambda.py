from functools import reduce

# true is 1, false is 0

# lambda 인자 : 표현식
# map(함수, 리스트)
# reduce(함수, 순서형 자료)
# filter(함수, 리스트)

a = range(10)
b = 'abcde'

print(list(map(lambda x: x**2, a)))

print(reduce(lambda x, y: y + x, b))

print(list(filter(lambda x: x % 2, a)))

