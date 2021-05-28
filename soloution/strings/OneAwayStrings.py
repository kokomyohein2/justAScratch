# Implement your function below.
def is_one_away(s1, s2):
    if len(s1) > len(s2) + 1 or len(s2) > len(s1) + 1:
        return False
    elif len(s1) == len(s2):
        return is_one_away_same_length(s1, s2)
    elif len(s1) > len(s2):
        return is_one_away_diff_length(s1, s2)
    else:
        return is_one_away_diff_length(s2, s1)


def is_one_away_same_length(s1, s2):
    diff_count = 0
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            diff_count += 1
        if (diff_count > 1):
            return False
    return True


def is_one_away_diff_length(s1, s2):
    diff_count = 0
    index = 0
    while (index < len(s2)):
        if s1[index + diff_count] == s2[index]:
            index += 1
        else:
            diff_count += 1

        if diff_count > 1:
            return False

    return True


# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
