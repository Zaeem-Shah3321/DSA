import matplotlib.pyplot as plt

# Function to draw the bars with colors and values on top
def draw_bars(arr, colorArray, pause_time=0.5):
    plt.bar(range(len(arr)), arr, color=colorArray)

    # Annotate each bar with its value
    for i, value in enumerate(arr):
        plt.text(i, value + 0.1, str(value), ha='center', va='bottom', fontsize=10)

    plt.pause(pause_time) # Pause to allow visualization
    plt.clf() # Clear the current plot

# Insertion sort with visualization
def insertion_sort_visual(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Color array for the visualization
        colorArray = ['blue'] * len(arr)
        colorArray[i] = 'red' # Current element being sorted

        # Visualize the current state before sorting
        draw_bars(arr, colorArray)

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

            # Update the color array for visualization
            colorArray = ['blue'] * len(arr)
            colorArray[j + 1] = 'green' # Element being compared
            draw_bars(arr, colorArray)
        arr[j + 1] = key

        # Visualize the array after placing the key
        colorArray = ['blue'] * len(arr)
        draw_bars(arr, colorArray)

    # Final sorted array visualization
    draw_bars(arr, ['green'] * len(arr))
    plt.show()

# Main function
if __name__ == "__main__":
    # Ask user to input numbers separated by space
    user_input = input("Enter numbers separated by space: ")

    # Convert input to a list of integers
    arr = list(map(int, user_input.split()))

    # Setup the figure for plotting
    plt.figure()
    plt.title("Insertion Sort Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")

    # Run insertion sort with visualization
    insertion_sort_visual(arr)