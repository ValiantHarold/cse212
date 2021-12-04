def find_chars(string):

    string = string.replace(" ", "").lower()

    new_set = set()

    for char in string:
        new_set.add(char)
    return new_set


print(find_chars("add each character of string to a set to find the unique characters"))
# Solution {'o', 'a', 'f', 'c', 'g', 'd', 't', 'i', 'h', 'q', 'n', 'e', 'r', 's', 'u'}

print(find_chars("now try to remove spaces from the set"))
# Solution {'o', 'a', 'f', 'c', 't', 'h', 'n', 'y', 'm', 'e', 'p', 'r', 's', 'w', 'v'}

print(find_chars("HOW ABOUT CAPITAL LETTERS"))
# Solution {'o', 'a', 'c', 't', 'i', 'h', 'l', 'b', 'e', 'p', 'r', 's', 'w', 'u'}

print(find_chars("the quick brown fox jumps over the lazy dog"))
# Solution {'q', 'd', 'p', 't', 'u', 'f', 'k', 'e', 'v', 'w', 'o', 'n', 'l', 'j', 'g', 'x', 'z', 'm', 'i', 'c', 'h', 'a', 'b', 's', 'y', 'r'}
