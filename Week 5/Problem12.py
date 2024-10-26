def main():
    numbers = [10, -3, 5, 7, -1, 0, 12, -8, 4, 6, -2, 9, -4]

    non_negative_numbers = [num for num in numbers if num >= 0]
    print("List after removing negative numbers:", non_negative_numbers)

    if non_negative_numbers:
        maximum = max(non_negative_numbers)
        minimum = min(non_negative_numbers)
        print("Maximum value:", maximum)
        print("Minimum value:", minimum)
    else:
        print("No non-negative numbers.")

    if non_negative_numbers:
        average = sum(non_negative_numbers) / len(non_negative_numbers)
        print("Average value:", average)
    else:
        print("No non-negative numbers.")

if __name__ == "__main__":
    main()
