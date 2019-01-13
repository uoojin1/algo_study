''' reverse a given string

given a string 'abcde', reverse it
result = 'edcba
'''

input_string = 'abcdefg'
number_array = [1,2,3,4,5,6,7,8,9,10]

def reverseString(input_string):
    result = ''
    for char in input_string:
        result = char + result # keep adding it to the front
    return result

def reverseVowels(input_string):
    result = ''
    input_list = list(input_string)
    left_index = 0
    right_index = len(input_list)-1
    def isVowel(letter):
        if not letter or letter == '':
            return False
        if letter in 'aeiou':
            return True
        else:
            return False
    while left_index < right_index:
        print left_index, right_index
        while not isVowel(input_list[left_index]):
            left_index += 1
        while not isVowel(input_list[right_index]):
            right_index -= 1
        # swap
        if left_index < right_index:
            print 'swap!', input_list[left_index], input_list[right_index]
            temp = input_list[left_index]
            input_list[left_index] = input_list[right_index]
            input_list[right_index] = temp
        left_index += 1
        right_index -= 1
    return input_list

print reverseVowels(input_string)

def reverseArray(input_array):
    left_index = 0
    right_index = len(input_array)-1
    while left_index >= right_index:
        temp = input_array[left_index]
        input_array[left_index] = input_array[right_index]
        input_array[right_index] = temp
        left_index += 1
        right_index -= 1
    return input_array

# print reverseString(input_string)
# print reverseArray(number_array)