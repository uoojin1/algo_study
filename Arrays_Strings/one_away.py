''' One Away
There are 3 types of edits that can be performed on strings
1. insert a character,
2. remove a character,
3. or replace a character
Q: given 2 strings, check if they are one edit away
'''

def oneEditAway(str1, str2):
    if (str1 == str2):
        return True    
    if(abs(len(str1) - len(str2)) > 1):
        return False

    str1_iter = 0;
    str2_iter = 0;
    difference_count = 0;

    for i in range(min(len(str1), len(str2))):
        print(str1[str1_iter], str2[str2_iter])
        if str1[str1_iter] != str2[str2_iter]:
            if len(str2) > len(str1):
                str2_iter += 1
            elif len(str1) > len(str2):
                str1_iter += 1
            difference_count += 1
        
        str1_iter += 1
        str2_iter += 1

        if difference_count > 1:
            return False
        
    return True

print(oneEditAway("abc", "abbc"))
