# Michelle Oteri
#2252197
   def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        max_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[max_index]:
                max_index = j

        # Swap the found maximum element with the first element
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

        # Print the list after each iteration of the outer loop
        print(" ".join(map(str, numbers)), end=" \n")


if __name__ == "__main__":
    # Read a list of integers
    numbers = [int(x) for x in input().split()]

    # Call the selection_sort_descend_trace function to sort the list
    selection_sort_descend_trace(numbers)

