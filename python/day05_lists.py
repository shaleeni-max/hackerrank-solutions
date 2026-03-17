if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "insert":
            i = int(cmd[1])
            e = int(cmd[2])
            lst.insert(i, e)

        elif cmd[0] == "print":
            print(lst)

        elif cmd[0] == "remove":
            lst.remove(int(cmd[1]))

        elif cmd[0] == "append":
            lst.append(int(cmd[1]))

        elif cmd[0] == "sort":
            lst.sort()

        elif cmd[0] == "pop":
            lst.pop()

        elif cmd[0] == "reverse":
            lst.reverse()
