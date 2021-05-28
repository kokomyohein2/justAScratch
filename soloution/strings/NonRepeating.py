# Implement your function below.
def non_repeating(given_string):
    count = {}
    for x in given_string:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    for x in given_string:
        if count[x] == 1:
            return x

    return None


# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab"))  # should return 'c'
print(non_repeating("abab"))  # should return None
print(non_repeating("aabbbc"))  # should return 'c'
print(non_repeating("aabbdbc"))  # should return 'd'
