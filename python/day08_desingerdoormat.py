# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

# Top part
for i in range(1, n, 2):
    pattern = (".|." * i).center(m, "-")
    print(pattern)

# Middle
print("WELCOME".center(m, "-"))

# Bottom part
for i in range(n-2, -1, -2):
    pattern = (".|." * i).center(m, "-")
    print(pattern)
