# Ask For a list input
user_list:list = eval(input("Enter the list to be sorted: "))

print(f"\nInitial list: {user_list}")

h = len(user_list)
gap_factor = h

while gap_factor != 1:
    gap_factor = int(gap_factor// 1.3)
    no_of_iterations = len(user_list) - gap_factor

    for i in range(no_of_iterations):
        if user_list[i] > user_list[i + gap_factor]:
            user_list[i], user_list[i + gap_factor] = user_list[i + gap_factor], user_list[i]

print(f"\nSorted list by Comb Sort: {user_list}")
