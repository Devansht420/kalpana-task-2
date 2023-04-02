import sys
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
 
 
class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        # Set the size of the window and the title
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Live Graph from CSV File")
 
        # Create a QWidget to hold the plot
        self.plot_widget = QWidget(self)
        self.setCentralWidget(self.plot_widget)
 
        # Create a vertical layout for the plot
        self.plot_layout = QVBoxLayout(self.plot_widget)
 
        # Create a Matplotlib figure and axis for the plot
        self.figure = plt.figure()
        self.axis = self.figure.add_subplot(111)
 
        # Create a Matplotlib canvas widget to display the plot
        self.canvas = FigureCanvas(self.figure)
        self.plot_layout.addWidget(self.canvas)
 
        # Set the plot title and labels
        self.axis.set_title("Attitude vs Time")
        self.axis.set_xlabel("Time (s)")
        self.axis.set_ylabel("Attitude")
 
        # Set up the CSV file reader and the data arrays
        self.csv_reader = csv.reader(open("telemetry.csv", "r"))
        self.time_data = []
        self.attitude_data = []
 
        # Set up a QTimer to update the plot at a rate of 1 package/sec
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)
 
    def update_plot(self):
        # Read one row of data from the CSV file
        row = next(self.csv_reader)
        time_value = float(row[0])
        attitude_value = float(row[1])
     
        # Add the new data to the data arrays
        self.time_data.append(time_value)
        self.attitude_data.append(attitude_value)
     
        # Plot the data on the graph
        self.axis.plot(self.time_data, self.attitude_data, 'r-')
     
        # Redraw the canvas
        self.canvas.draw()
 
if __name__ == "__main__":
    # Create the QApplication
    app = QApplication(sys.argv)
 
    # Create the graph window
    window = GraphWindow()
 
    # Show the window and start the event loop
    window.show()
    sys.exit(app.exec_())
 