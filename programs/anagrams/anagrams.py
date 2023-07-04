"""
anagram program.
"""

def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    if sorted(s1) != sorted(s2):
        return False
    return True



if __name__ == '__main__':
    str1 = "danger"
    str2 = "garden"

    check_exist = check_anagram(str1, str2)
    print(check_exist)
