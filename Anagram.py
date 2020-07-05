####Anagram

# 1

def is_anagram1(str1, str2):
    if len(str1) != len(str2):
        print("Unequal Srings")
    return sorted(str1) == sorted(str2)


# 2

def is_anagram2(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    return list1 == list2


# 3

from collections import Counter


def is_anagram3(str1, str2):
    c1 = Counter(str1)
    c2 = Counter(str2)
    return c1 == c2


print(is_anagram3("silent", "listen"))   