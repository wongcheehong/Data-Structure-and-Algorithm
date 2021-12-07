def containsCommonItem(list1, list2):
    dict = {item: True for item in list1}
    return any(dict.get(item, False) for item in list2)


a = ['a', 'b', 'c', 'd', 'e', 'f']
b = ['z', 'y', 'a']

# O(a+b+b)
print(containsCommonItem(a, b))
