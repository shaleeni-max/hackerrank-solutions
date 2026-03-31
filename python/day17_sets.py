def average(array):
    # your code goes here
    unique_heights=set(array)
    avg=sum(unique_heights)/len(unique_heights)
    return avg    
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
