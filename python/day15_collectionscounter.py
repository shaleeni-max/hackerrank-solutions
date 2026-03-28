# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# number of shoes
n = int(input())

# list of shoe sizes
sizes = list(map(int, input().split()))

# count each size
shoe_count = Counter(sizes)

# number of customers
customers = int(input())

total_money = 0

for _ in range(customers):
    size, price = map(int, input().split())
    
    if shoe_count[size] > 0:
        total_money += price
        shoe_count[size] -= 1

print(total_money)
