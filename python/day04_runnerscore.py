if __name__ == '__main__':

    n = int(input())
scores = list(map(int, input().split()))

scores = list(set(scores))
scores.remove(max(scores))

print(max(scores))
