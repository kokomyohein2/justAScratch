lst = [x for x in range(20)]

def swap(a_lst, front, back):
    a_lst[front], a_lst[back] = a_lst[back], a_lst[front]

def rev_list(a_lst):
    if a_lst is None:
        return []

    front = 0
    back = len(a_lst) - 1
    while front < back:
        swap(a_lst, front, back)
        front += 1
        back -= 1

    return a_lst

# lst.reverse()
# print(lst)

print(rev_list(lst))
