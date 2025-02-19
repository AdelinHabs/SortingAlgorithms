# Ask For a list input
user_list:list = eval(input("Enter the list to be sorted: "))
sorted_list = [0] * len(user_list)

h = len(user_list)  #This value will remain constant during the iterations
k = h  #This value will change during the iterations
n = 0  #This value will change during the iterations

print(f"\nInitial list: {user_list}")

while n < h:
    smallest = user_list[0]  #Initializing the smallest number to be the first item in the user_list
    for i in range(1, k):
        if user_list[i] < smallest:  #Checking if item at index i is smaller that the current smallest number
            smallest = user_list[i]
    sorted_list[n] = smallest  #Adding the smallest number at the time to the sorted list
    user_list.remove(smallest)  #Removing the element that has just been added to the sorted list from the user_list
    k -= 1
    n += 1

print(f"\nSorted list by Selection Sort: {sorted_list}")
