import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort(data, draw, delay):
    n = len(data)

    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(data, ['green' if x == j or x == j+1 else 'blue' for x in range(len(data))])
                plt.pause(delay)

def generate_data(size):
    return [random.randint(1, 100) for _ in range(size)]

def update_plot(frame, bars, colors):
    for bar, color in zip(bars, colors):
        bar.set_color(color)
    return bars

def main():
    size = 30
    data = generate_data(size)

    fig, ax = plt.subplots()
    bars = ax.bar(range(len(data)), data, color='blue')
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) + 10)

    def draw(data, colors):
        for bar, val, color in zip(bars, data, colors):
            bar.set_height(val)
            bar.set_color(color)

    ani = animation.FuncAnimation(fig, update_plot, fargs=(bars, ['blue'] * len(data)),
                                  frames=bubble_sort(data.copy(), draw, 0.05), repeat=False, save_count=len(data))
    plt.show()

if __name__ == "__main__":
    main()