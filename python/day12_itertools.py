# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = product(A, B)

for i in result:
    print(i, end=' ')
