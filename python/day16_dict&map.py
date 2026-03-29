# Enter your code here. Read input from STDIN. Print output to STDOUT
phone_book = {}

N = int(input())

for i in range(N):
    name, number = input().split()
    phone_book[name] = number

while True:
    try:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except:
        break
