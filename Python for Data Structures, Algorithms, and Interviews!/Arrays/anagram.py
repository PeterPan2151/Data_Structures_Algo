def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    if len(s1) != len(s2):
        return False
    
    s1_dict = {}
    for i in s1:
        if i.isalpha():
            if i not in s1_dict:
                s1_dict[i] = 1
            else:
                s1_dict[i] += 1

    for i in s2:
        if i.isalpha():
            if i not in s1_dict:
                s1_dict[i] = 1
            else:
                s1_dict[i] -= 1

    for i in s1_dict:
        if s1_dict[i] != 0:
            return False
    return True
    

print(anagram('do g', 'god'))
