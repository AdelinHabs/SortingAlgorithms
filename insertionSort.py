# Ask For a list input
user_list:list = eval(input("Enter the list to be sorted: "))
i = 0  #User list counter
j = 0  #Sorted list counter
sorted_list = [0]*len(user_list)

def place_item_in_correct_position(j:int):
    for k in range(len(sorted_list) - 1):
            if sorted_list[j] < sorted_list[k]:
                sorted_list[j], sorted_list[k] = sorted_list[k], sorted_list[j]

for h in range(len(user_list) - 1):
    if user_list[i] < user_list[i + 1]:
        sorted_list[j] = user_list[i]
        place_item_in_correct_position(j)
        
    else:
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
        sorted_list[j] = user_list[i]
        place_item_in_correct_position(j)
        
    i += 1
    j += 1

sorted_list[len(sorted_list) - 1] = user_list[len(user_list) - 1]

print(f"\nInitial list: {user_list}")

print(f"\nSorted list by Insertion Sort: {sorted_list}")
