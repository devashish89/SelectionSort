### Selection Sort #####
# first element(fixed) is always compared against with diff elements
# pass 1
# 9,8,7,6,5,4,3 first compared with second element
# 8,9,7,6,5,4,3 first compared with third element
# 7,9,8,6,5,4,3 first compared with fourth element
# 6,9,8,7,5,4,3 ...
# 5,9,8,7,6,4,3
# 4,9,8,7,6,5,3
# 3,9,8,7,6,5,4
# after whole loop the smallest element has come to the first place
# pass2
# 3,  8,9,7,6,5,4
# 3,   7,9,8,6,5,4
# 3,   6,9,8,7,5,4
# 3,   5,9,8,7,6,4
# 3,4,   9,8,7,6,5

################
def swap_list_elements(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

# selection sort does not return list but sort the same list
def selectionSort(lst):
    first = 0

    while first < len(lst) - 1:
        for i in range(1+first, len(lst), 1):
            if lst[first] > lst[i]:
                swap_list_elements(lst, first, i)

        #print(lst, lst[first], first)
        first += 1

if __name__=='__main__':
    lst = [9, 8, 7, 6, 5, 4, 3]
    selectionSort(lst)
    print(lst)

