def minion_game(string):
    # your code goes here
    VOWELS = 'AEIOU'
    kevin_scores = stuart_scores = 0
    length = len(string)
    
    string = string.upper()
    
    for i in range(length):
        if string[i] in VOWELS:
            kevin_scores += length - i
        else:
            stuart_scores += length - i

    if kevin_scores > stuart_scores:
        print(f"Kevin {kevin_scores}")
    elif stuart_scores > kevin_scores:
        print(f"Stuart {stuart_scores}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
