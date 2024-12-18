nums = [5, 6, 2, 1, 3, 4]

def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True


# (bubble_sort(nums))
# print(nums)

# ------------------------------------------------------
def selection_sort(lst):
    for i in range(len(lst)):
        lowest = i
        for j in range(i +1, len(lst)):
            if lst[j] < lst[lowest]:
                lowest = j
        lst[i], lst[lowest] = lst[lowest], lst[i]


# selection_sort(nums)
# print(nums)