import os
import pandas as pd
import matplotlib.pyplot as plt

# Old folder names and new names
folders = [f'v{i}' for i in range(1, 11)]
labels = ['E5F1', 'E1F5', 'E1F3', 'E1F8', 'E1F10', 'E1F20', 'E1F30', 'E1F50', 'E1F100', 'E0F100']

# Function to reset the plot
def reset_plot():
    plt.clf()  # Clear the current figure
    plt.close()  # Close the figure window

# Always reset the data dictionary to ensure we're working with fresh data
#def load_data(folder, skip):
#    csv_path = os.path.join(folder, 'metrics_epoch.csv')
# 
#    if os.path.exists(csv_path):
#       # Read the CSV file
#       df = pd.read_csv(csv_path)
#       
#       data = df[['epoch', 'validation_e/N_mae']].iloc[skip:]   
#       return data

# Plotting the updated data
def plot_data(skip):
    reset_plot()  # Reset the plot before plotting new data
    plt.figure(figsize=(10, 6))
    for i, folder in enumerate(folders):
        label = labels[i]
        csv_path = os.path.join(folder, 'metrics_epoch.csv')
        df = pd.read_csv(csv_path)
        epoch = df['epoch'].iloc[skip:]
        validation_e = df['validation_e/N_mae'].iloc[skip:]
        plt.plot(epoch , validation_e, label=label)

        #data = load_data(folder, 10)
        #data.plot(x='epoch',
        #        y='validation_e/N_mae',label=folder)

    plt.xlabel('Epochs')
    plt.ylabel('Metric Value')
    plt.title('Epoch vs Metric Comparison across Folders (Logarithmic)')
    plt.yscale('log')  # Set the y-axis to logarithmic
    plt.legend()
    plt.grid(True)
    plt.show()
    quit()

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
plot_data(skip=10)

