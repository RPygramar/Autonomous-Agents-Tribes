import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Plot:
    def __init__(self):
        # This is the number of data points we'll be initially displaying
        self.data_points = 0
       
        # Initialize lists to store resource values and corresponding x values
        self.resources = []
        self.x_values = []  # x values starting from 0

        # The next x value to be used when new data comes in
        self.next_x_value = self.data_points

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(self.x_values, self.resources)

    def animate(self, i, queue):
        if not queue.empty():
            # Ensure the latest value is used, discarding older values if necessary
            while not queue.empty():
                resource = queue.get_nowait()
            
            # Append new resource value and corresponding x value
            self.resources.append(resource)
            self.x_values.append(self.next_x_value)
            self.next_x_value += 1  # Prepare the next x value
            
            # Update the plot line with the new data
            self.line.set_data(self.x_values, self.resources)
            
            # Adjust xlim to accommodate the next data point, and ylim if necessary
            self.ax.set_xlim(0, self.next_x_value)
            self.ax.set_ylim(0, max(self.resources) + max(self.resources)/4)  # Adjust Y-axis based on data range

        return self.line,

    def main(self, queue):
        ani = animation.FuncAnimation(self.fig, self.animate, fargs=(queue,), blit=False, interval=1000)
        plt.show()
        