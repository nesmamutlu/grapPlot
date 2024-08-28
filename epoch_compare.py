import os
import pandas as pd
import matplotlib.pyplot as plt

# Old folder names and new names
folders_old = [f'v{i}' for i in range(1, 11)]
folders_new = ['E5F1', 'E1F5', 'E1F3', 'E1F8', 'E1F10', 'E1F20', 'E1F30', 'E1F50', 'E1F100', 'E0F100']

# Function to reset the plot
def reset_plot():
    plt.clf()  # Clear the current figure
    plt.close()  # Close the figure window

# Always reset the data dictionary to ensure we're working with fresh data
def load_data():
    data = {}
    for old_folder, new_folder in zip(folders_old, folders_new):
        csv_path = os.path.join(old_folder, 'metrics_epoch.csv')
        
        if os.path.exists(csv_path):
            # Read the CSV file
            df = pd.read_csv(csv_path)
            
            # Get the epoch column and the last column, remove the first 10 rows
            epoch_column = df.columns[0]  # First column where the epoch numbers are stored
            last_column = df.columns[-1]  # Last column (metrics)
            
            # Remove the first 10 rows
            df_trimmed = df.iloc[10:]
            
            # Store the epoch and last column data
            data[new_folder] = (df_trimmed[epoch_column], df_trimmed[last_column])
    return data

# Plotting the updated data
def plot_data(data):
    reset_plot()  # Reset the plot before plotting new data
    plt.figure(figsize=(10, 6))
    for folder, (epochs, metrics) in data.items():
        plt.plot(epochs, metrics, label=folder)

    plt.xlabel('Epochs')
    plt.ylabel('Metric Value')
    plt.title('Epoch vs Metric Comparison across Folders (Logarithmic)')
    plt.yscale('log')  # Set the y-axis to logarithmic
    plt.legend()
    plt.grid(True)

    # Save the plot to a file with a unique name
    base_filename = 'epoch_metric_comparison'
    file_extension = '.png'
    filename = base_filename + file_extension
    counter = 1

    # Check if the file exists and if so, append a number to the filename
    while os.path.exists(filename):
        filename = f"{base_filename}_{counter}{file_extension}"
        counter += 1

    # Save the plot with the unique filename
    plt.savefig(filename)

    # Show the plot
    plt.show()

# Load data, update it, and plot it
data = load_data()
plot_data(data)

