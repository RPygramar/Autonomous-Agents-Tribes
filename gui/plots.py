import matplotlib.pyplot as plt
import matplotlib.animation as animation
from queue import Queue

class Plot:
    def __init__(self):
        # This is the number of data points we'll be initially displaying
        self.data_points = 0
        
        # Initialize lists to store resource values and corresponding x values
        self.total_resources_list = []
        self.blue_tribe_resources_list = []
        self.orange_tribe_resources_list = []
        self.purple_tribe_resources_list = []
        self.red_tribe_resources_list = []
        self.x_values = []  # x values starting from 0
        
        # The next x value to be used when new data comes in
        self.next_x_value = self.data_points
        
        self.fig, self.ax = plt.subplots()  # Create a single subplot
        
        # Set the labels for x and y axes
        self.ax.set_xlabel("Time (seconds)")
        self.ax.set_ylabel("Resource Value")
        
        # Initialize lines for all sets of resource values
        self.total_resources_line, = self.ax.plot(self.x_values, self.total_resources_list, label="Total Resources", color='green')
        self.tribe_blue_resources_line, = self.ax.plot(self.x_values, self.blue_tribe_resources_list, label="Tribe Blue", color='blue')
        self.tribe_orange_resources_line, = self.ax.plot(self.x_values, self.orange_tribe_resources_list, label="Tribe Orange", color='orange')
        self.tribe_purple_resources_line, = self.ax.plot(self.x_values, self.purple_tribe_resources_list, label="Tribe Purple", color='purple')
        self.tribe_red_resources_line, = self.ax.plot(self.x_values, self.red_tribe_resources_list, label="Tribe Red", color='red')

        
        # Add a legend to the plot
        self.ax.legend()

    def animate(self, i, queue1, queue2, queue3, queue4, queue5):
        updated = False  # Track if any data was updated

        if not queue1.empty():
            # Ensure the latest value is used, discarding older values if necessary
            while not queue1.empty():
                resource1 = queue1.get_nowait()
            
            # Append new resource value and corresponding x value
            self.total_resources_list.append(resource1)
            updated = True

        if not queue2.empty():
            # Ensure the latest value is used, discarding older values if necessary
            while not queue2.empty():
                resource2 = queue2.get_nowait()
            
            # Append new resource value
            self.blue_tribe_resources_list.append(resource2)
            updated = True

        if not queue3.empty():
            # Ensure the latest value is used, discarding older values if necessary
            while not queue3.empty():
                resource3 = queue3.get_nowait()
            
            # Append new resource value
            self.orange_tribe_resources_list.append(resource3)
            updated = True

        if not queue4.empty():
            # Ensure the latest value is used, discarding older values if necessary
            while not queue4.empty():
                resource4 = queue4.get_nowait()
            
            # Append new resource value and corresponding x value
            self.purple_tribe_resources_list.append(resource4)
            updated = True
        
        if not queue5.empty():
            # Ensure the latest value is used, discarding older values if necessary
            while not queue5.empty():
                resource5 = queue5.get_nowait()
            
            # Append new resource value and corresponding x value
            self.red_tribe_resources_list.append(resource5)
            updated = True
            

        if updated:
            # Update x values if any resources were updated
            self.x_values.append(self.next_x_value)
            self.next_x_value += 1  # Prepare the next x value
            
            # Update the plot lines with the new data
            self.total_resources_line.set_data(self.x_values, self.total_resources_list)
            self.tribe_blue_resources_line.set_data(self.x_values, self.blue_tribe_resources_list)
            self.tribe_orange_resources_line.set_data(self.x_values, self.orange_tribe_resources_list)
            self.tribe_purple_resources_line.set_data(self.x_values, self.purple_tribe_resources_list)
            self.tribe_red_resources_line.set_data(self.x_values, self.red_tribe_resources_list)
            
            # Adjust xlim to accommodate the next data point
            self.ax.set_xlim(0, self.next_x_value)
            # Adjust ylim based on the maximum resource value
            max_resource_value = max(max(self.total_resources_list, default=0),
                                     max(self.blue_tribe_resources_list, default=0), 
                                     max(self.orange_tribe_resources_list, default=0), 
                                     max(self.purple_tribe_resources_list, default=0), 
                                     max(self.red_tribe_resources_list, default=0))
            self.ax.set_ylim(0, max_resource_value + max_resource_value / 4)

        return self.total_resources_line, self.tribe_blue_resources_line, self.tribe_orange_resources_line, self.tribe_purple_resources_line, self.tribe_red_resources_line

    def main(self, queue1, queue2, queue3, queue4, queue5):
        ani = animation.FuncAnimation(self.fig, self.animate, fargs=(queue1, queue2, queue3, queue4, queue5), blit=False, interval=1000)
        plt.show()