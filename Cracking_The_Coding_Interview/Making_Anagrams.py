import collections

def number_needed(a, b):
    concat = a+b
    a_dict = collections.Counter(a)
    b_dict = collections.Counter(b)
    summ = 0
    chk = ""
    
    for letter in concat:        
        if((letter in a_dict) and (letter in b_dict) and a_dict[letter] == b_dict[letter]):
            summ += 0
        else:
            if(letter not in chk):
                summ += abs(a_dict[letter]-b_dict[letter])
        chk += letter        
    return summ    

a = input().strip()
b = input().strip()

print(number_needed(a, b))