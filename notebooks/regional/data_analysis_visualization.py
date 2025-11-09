import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_occurrence_map(df):
    """
    Generates a scatter plot visualizing species occurrence data on a map.

    Args:
        df (pd.DataFrame): DataFrame containing 'latitude' and 'longitude' columns
                            representing the geographic coordinates of occurrences.
    """

    # Set seaborn style for better aesthetics
    sns.set_style("whitegrid")

    # Create the scatter plot using matplotlib and seaborn
    plt.figure(figsize=(10, 8))  # Adjust figure size for better visibility
    sns.scatterplot(x='longitude', y='latitude', data=df, s=20, color="blue", alpha=0.7)

    # Set the plot title
    plt.title("Geographic Distribution of Convallaria majalis in Finland")

    # Label the axes
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    # Add a grid for better readability (already handled by sns.set_style)
    # plt.grid(True) # Not needed since sns set style already handles this

    # Show the plot
    plt.show()


if __name__ == '__main__':
    # Create a sample DataFrame for demonstration purposes
    data = {'latitude': [65.0, 64.5, 66.2, 65.8, 67.1],
            'longitude': [25.5, 26.1, 24.9, 25.8, 26.5]}
    df = pd.DataFrame(data)

    # Call the function to generate the plot
    plot_occurrence_map(df)
