# Ask For a list input
user_list:list = eval(input("Enter the list to be sorted: "))

h = len(user_list)

print(f"\nInitial list: {user_list}")

while h > 0:
    for i in range(0, h-1):        
        if user_list[i] > user_list[i+1]:  #Checking if item at index i is bigger than item at index i+1
            user_list[i],user_list[i+1] = user_list[i+1],user_list[i]  #Swap items at index i and i+1
    
    h -= 1  #Reducing the value of h so that the for loop performs operations one less than the previous operations
    
print(f"\nSorted list by Bubble Sort: {user_list}")
