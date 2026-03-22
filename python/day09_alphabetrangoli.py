def print_rangoli(size):
    alphabet=[chr(i) for i in range(97,123)]
    alphabet=alphabet[:size]
    indices=list(range(size))
    indices=indices[:-1]+indices[::-1]

    for i in indices:
        start_index=i+1
        original=alphabet[-start_index:]
        row=original[::-1]+original[1:]
        row='-'.join(row)
        width=size*4-3
        row=row.center(width,'-')
        print(row)




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
