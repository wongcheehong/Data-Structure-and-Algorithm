def reverseString(string: str) -> str:
    string = list(string)
    last_index = len(string) - 1
    for start_index in range(len(string)):
        if (start_index < last_index):
            tmp = string[last_index]
            string[last_index] = string[start_index]
            string[start_index] = tmp
        last_index -= 1
    return ''.join(string)


string = "abcdefgh"
print(reverseString(string))
print(''.join(reversed(string)))
