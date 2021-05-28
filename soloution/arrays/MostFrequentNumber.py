list1 = [3,3,1,3,2,1]

def most_frequent(given_list):
    maxCount = -1
    maxItem = None
    count = {}
    for i in given_list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if  count[i] > maxCount:
            maxItem=i
            maxCount = count[i]

    return maxItem

print(most_frequent(list1))
