# # print(3, 4, 5, sep = '#', end = '!\n')
# # print('Hello')
#
# def to_float_hours(hours, minutes, seconds):
#     return hours + (minutes / 60) + (seconds / 3600)
#
# print(to_float_hours(0, 15, 0))
# print(to_float_hours(2, 45, 9))
# print(to_float_hours(1, 0, 36))


# num = 6
# while num > 0:
#     num = num - 2
#     print(num)

# C1: Return a substring from parameter s after the function is called
'''s = ''
i = 0
while i < len(s) and not (s[i] in 'aeiouAEIOU'):
    print(s[i])
    i += 1
'''

# C2: Return a substring from parameter s after the function is called
'''
def up_to_vowel(s):
    i = 0
    before_vowel = ''
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
    # print(before_vowel)
        i += 1

        # return before_vowel : nếu return nằm trong while thì chỉ chạy tới i = 1 không ra kết quả rồi ngừng
    return before_vowel # nếu return không nằm trong while loop thì chạy hết chuỗi cho đến khi điều kiện không thỏa
s = 'there'
print(up_to_vowel(s))
'''

'''
def get_answer(prompt):
    answer = input(prompt)
    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)
    return answer

get_answer('are you crazy? enter yes or this will loop 4ever: ' )
'''
def last_vowel(s):
    """(str) -> str
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    """
    i = len(s) - 1
    while i >= 0:
         if s[i] in 'aeiouAEIOU':
             return s[i]
         i = i - 1
   return None
