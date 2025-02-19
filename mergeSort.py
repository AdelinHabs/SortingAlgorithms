# Function to split the list into smaller possible lists
def split_list(list_to_be_sorted: list[int], left, right):
    if left < right:
        mid = (left + right) // 2  #This divides the sum of left and right and returns the floor value
        split_list(list_to_be_sorted, left, mid)  #Further splitting the first half of the list
        split_list(list_to_be_sorted, (mid + 1), right)  #Further splitting the second half of the list
        merge(list_to_be_sorted, left, mid, right)  #Merging the split lists


# Function to merge the split lists
def merge(list_to_be_merged: list[int], left, mid, right):
    a1 = mid - left + 1  #Getting how many values are in the first half of the list
    a2 = right - mid  #Getting how many values are in the second half of the list
    
    # Temporary lists l & r of length a1 & a2 respectively and having 0s as the default values
    l = [0] * a1
    r = [0] * a2

    # Copying the values in the two halves of the list into my temporary lists
    for i in range(a1):
        l[i] = list_to_be_merged[left + i]

    for j in range(a2):
        r[j] = list_to_be_merged[mid + 1 + j]

    # Checking for the smallest values to come first
    # Initialising constants b1, b2 & k to be used in the check
    b1 = 0  #Initial index of first sub-array
    b2 = 0  #Initial index of second sub-array
    h = left  #Initial index of merged sub-array
    
    while b1 < a1 and b2 < a2:
        if l[b1] <= r[b2]:
            list_to_be_merged[h] = l[b1]
            b1 += 1
        else:
            list_to_be_merged[h] = r[b2]
            b2 += 1
        h += 1

    # Filling in the leftovers from l into the list_to_be_merged if any
    while b1 < a1:
        list_to_be_merged[h] = l[b1]
        b1 += 1
        h += 1

    # Filling in the leftovers from r into the list_to_be_merged if any
    while b2 < a2:
        list_to_be_merged[h] = r[b2]
        b2 += 1
        h += 1


# Ask For a list input
user_list:list = eval(input("Enter the list to be sorted: "))

print(f"\nInitial list: {user_list}")
split_list(user_list, 0, ((len(user_list)) - 1))
print(f"\nSorted list: {user_list}")