### Selection Sort #####
# selection sort does not return list but sort the same list
# 10,5,8,20,2,18
# 2|,5,8,20,10,18 # min and 1st element swapped
# 2,5|,8,20,10,18
# 2,5,8,|20,10,18
# 2,5,8,10|,20,18
# 2,5,8,10,18|,20

def selectionSort(lst):
    n = len(lst)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            # find min. element in list
            if lst[i] > lst[j]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]


if __name__ == '__main__':
    lst = [9, 8, 7, 6, 5, 4, 3]
    selectionSort(lst)
    print(lst)
