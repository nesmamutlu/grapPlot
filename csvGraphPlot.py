import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
file_path = '/home/esma/workspace/test.csv'  
print(f"Reading file from: {file_path}")  

try:
    data = pd.read_csv(file_path, header=None)  # Use header=None if there are no column names
    print(data.head())  # Check the data structure

    # If the data has only one column, plot it using sequential numbers for the x-axis
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data[0], marker='o')

    # Customize the graph
    plt.title('Data Plot')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.grid(True)

    # Show the plot
    plt.show()

except FileNotFoundError:
    print("Error: The specified file was not found. Please check the file path.")

