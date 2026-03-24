def merge_the_tools(string, k):
    start=0
    end=k
    while end <= len(string):
        temp=string[start:end]
        chunk = "".join(dict.fromkeys(temp))
        print(chunk)
        start += k
        end += k
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
