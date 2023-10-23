import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

# Function to perform Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

# Function to update the plot for each frame of the animation
def update_plot(frame_data, bars, iteration_text):
    for bar, data in zip(bars, frame_data):
        bar.set_height(data)
    iteration_text.set_text(f'Iterations: {len(frame_data)}')

# Generate a random list to sort
arr = [randint(1, 100) for _ in range(20)]

# Create the figure and axis
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, align="edge")
ax.set_xlim(0, len(arr))
ax.set_ylim(0, max(arr) + 10)
iteration_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

# Create an animation
ani = animation.FuncAnimation(
    fig,
    update_plot,
    frames=bubble_sort(arr.copy()),
    fargs=(bars, iteration_text),
    repeat=False,
    blit=False,
    interval=100  # Animation speed (milliseconds)
)

plt.show()
