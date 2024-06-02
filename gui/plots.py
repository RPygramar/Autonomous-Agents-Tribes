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
        
        self.blue_tribe_barplot = []
        self.orange_tribe_barplot = []
        self.purple_tribe_barplot = []
        self.red_tribe_barplot = []

        self.blue_tribe_houses_list = []
        self.orange_tribe_houses_list = []
        self.purple_tribe_houses_list = []
        self.red_tribe_houses_list = []

        self.x_values = []  # x values starting from 0
        
        # The next x value to be used when new data comes in
        self.next_x_value = self.data_points
        
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, figsize=(6,9))  # Create three subplots
        
        # Set the labels for x and y axes of the line plot
        self.ax1.set_xlabel("Time (seconds)")
        self.ax1.set_ylabel("Resource Value")
        
        # Initialize lines for all sets of resource values
        self.total_resources_line, = self.ax1.plot(self.x_values, self.total_resources_list, label="Total Resources", color='green')
        self.tribe_blue_resources_line, = self.ax1.plot(self.x_values, self.blue_tribe_resources_list, label="Tribe Blue", color='blue')
        self.tribe_orange_resources_line, = self.ax1.plot(self.x_values, self.orange_tribe_resources_list, label="Tribe Orange", color='orange')
        self.tribe_purple_resources_line, = self.ax1.plot(self.x_values, self.purple_tribe_resources_list, label="Tribe Purple", color='purple')
        self.tribe_red_resources_line, = self.ax1.plot(self.x_values, self.red_tribe_resources_list, label="Tribe Red", color='red')
        
        # Add a legend to the line plot
        self.ax1.legend()
        self.ax1.set_title("Total Resources per Tribe")

        # Initialize the bar plot for the confidence values
        self.ax2.set_xlabel("Tribes")
        self.ax2.set_ylabel("Confidence Values")
        self.ax2.set_title("Average Total Confidence Values of Tribes")

        # Set the labels for x and y axes of the house plot
        self.ax3.set_xlabel("Time (seconds)")
        self.ax3.set_ylabel("House Values")
        self.ax3.set_title("Nº of houses per Tribe")

        
        # Initialize lines for all sets of house values
        self.tribe_blue_houses_line, = self.ax3.plot(self.x_values, self.blue_tribe_houses_list, label="Tribe Blue", color='blue')
        self.tribe_orange_houses_line, = self.ax3.plot(self.x_values, self.orange_tribe_houses_list, label="Tribe Orange", color='orange')
        self.tribe_purple_houses_line, = self.ax3.plot(self.x_values, self.purple_tribe_houses_list, label="Tribe Purple", color='purple')
        self.tribe_red_houses_line, = self.ax3.plot(self.x_values, self.red_tribe_houses_list, label="Tribe Red", color='red')

        # Add a legend to the house plot
        self.ax3.legend()

    def animate(self, i, queue1, queue2, queue3, queue4, queue5, queue6, queue7, queue8, queue9, queue10, queue11, queue12, queue13):
        updated = False  # Track if any data was updated

        if not queue1.empty():
            while not queue1.empty():
                resource1 = queue1.get_nowait()
            self.total_resources_list.append(resource1)
            updated = True

        if not queue2.empty():
            while not queue2.empty():
                resource2 = queue2.get_nowait()
            self.blue_tribe_resources_list.append(resource2)
            updated = True

        if not queue3.empty():
            while not queue3.empty():
                resource3 = queue3.get_nowait()
            self.orange_tribe_resources_list.append(resource3)
            updated = True

        if not queue4.empty():
            while not queue4.empty():
                resource4 = queue4.get_nowait()
            self.purple_tribe_resources_list.append(resource4)
            updated = True
        
        if not queue5.empty():
            while not queue5.empty():
                resource5 = queue5.get_nowait()
            self.red_tribe_resources_list.append(resource5)
            updated = True
        
        if not queue6.empty():
            while not queue6.empty():
                resource6 = queue6.get_nowait()
            self.blue_tribe_barplot.append(resource6)
            updated = True

        if not queue7.empty():
            while not queue7.empty():
                resource7 = queue7.get_nowait()
            self.orange_tribe_barplot.append(resource7)
            updated = True

        if not queue8.empty():
            while not queue8.empty():
                resource8 = queue8.get_nowait()
            self.purple_tribe_barplot.append(resource8)
            updated = True

        if not queue9.empty():
            while not queue9.empty():
                resource9 = queue9.get_nowait()
            self.red_tribe_barplot.append(resource9)
            updated = True

        if not queue10.empty():
            while not queue10.empty():
                house1 = queue10.get_nowait()
            self.blue_tribe_houses_list.append(house1)
            updated = True

        if not queue11.empty():
            while not queue11.empty():
                house2 = queue11.get_nowait()
            self.orange_tribe_houses_list.append(house2)
            updated = True

        if not queue12.empty():
            while not queue12.empty():
                house3 = queue12.get_nowait()
            self.purple_tribe_houses_list.append(house3)
            updated = True

        if not queue13.empty():
            while not queue13.empty():
                house4 = queue13.get_nowait()
            self.red_tribe_houses_list.append(house4)
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

            self.tribe_blue_houses_line.set_data(self.x_values, self.blue_tribe_houses_list)
            self.tribe_orange_houses_line.set_data(self.x_values, self.orange_tribe_houses_list)
            self.tribe_purple_houses_line.set_data(self.x_values, self.purple_tribe_houses_list)
            self.tribe_red_houses_line.set_data(self.x_values, self.red_tribe_houses_list)
            
            # Adjust xlim to accommodate the next data point
            self.ax1.set_xlim(0, self.next_x_value)
            self.ax3.set_xlim(0, self.next_x_value)
            
            # Adjust ylim based on the maximum resource value
            max_resource_value = max(max(self.total_resources_list, default=0),
                                     max(self.blue_tribe_resources_list, default=0), 
                                     max(self.orange_tribe_resources_list, default=0), 
                                     max(self.purple_tribe_resources_list, default=0), 
                                     max(self.red_tribe_resources_list, default=0))
            self.ax1.set_ylim(0, max_resource_value + max_resource_value / 4)

            max_house_value = max(max(self.blue_tribe_houses_list, default=0),
                                  max(self.orange_tribe_houses_list, default=0),
                                  max(self.purple_tribe_houses_list, default=0),
                                  max(self.red_tribe_houses_list, default=0))
            self.ax3.set_ylim(0, max_house_value + max_house_value / 4)
            
            # Update the bar plot
            self.update_bar_plot()

        return (self.total_resources_line, self.tribe_blue_resources_line, self.tribe_orange_resources_line, 
                self.tribe_purple_resources_line, self.tribe_red_resources_line,
                self.tribe_blue_houses_line, self.tribe_orange_houses_line, self.tribe_purple_houses_line, 
                self.tribe_red_houses_line)

    def update_bar_plot(self):
        # Clear the previous bar plot
        self.ax2.clear()
        
        # Prepare the bar plot data
        tribes = ['Blue', 'Orange', 'Purple', 'Red']
        resources = [
            self.blue_tribe_barplot[-1] if self.blue_tribe_barplot else 0,
            self.orange_tribe_barplot[-1] if self.orange_tribe_barplot else 0,
            self.purple_tribe_barplot[-1] if self.purple_tribe_barplot else 0,
            self.red_tribe_barplot[-1] if self.red_tribe_barplot else 0
        ]
        
        # Create the bar plot
        self.ax2.bar(tribes, resources, color=['blue', 'orange', 'purple', 'red'])

    def update_second_line_plot(self):
        pass

    def main(self, queue1, queue2, queue3, queue4, queue5, queue6, queue7, queue8, queue9, queue10, queue11, queue12, queue13):
        ani = animation.FuncAnimation(self.fig, self.animate, fargs=(queue1, queue2, queue3, queue4, queue5, queue6, queue7, queue8, queue9, queue10, queue11, queue12, queue13), blit=False, interval=1000)
        plt.tight_layout()
        plt.show()