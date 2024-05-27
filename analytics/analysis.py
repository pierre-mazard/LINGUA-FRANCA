# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

def analyze_translations(directory):
    # Get a list of all CSV files in the directory
    filenames = glob.glob(directory + '/*.csv')

    # Initialize an empty DataFrame to hold all the data
    data = pd.DataFrame()

    # Loop over the filenames and append each file's data to the DataFrame
    for filename in filenames:
        df = pd.read_csv(filename, encoding='utf-8')
        data = data._append(df, ignore_index=True)

    # Filter out rows where 'Original Text' or 'Translated Text' are 'empty text field'
    data = data[(data['Original Text'] != 'empty text field') & (data['Translated Text'] != 'empty text field')]

    if data.empty:
        with open(os.path.join(directory, 'translation_stats.txt'), 'w') as f:
            f.write("No data available for analysis.")
        return

    # Convert the 'Time' column to datetime
    data['Time'] = pd.to_datetime(data['Time'])

    # Analyze the most translated languages
    source_languages = data['Source Language'].value_counts()
    target_languages = data['Target Language'].value_counts()

    # Analyze the length of translations
    translation_lengths = data['Translated Text'].str.len()

    # Analyze the time of translations
    translation_times = data['Time'].dt.hour

    # Plot the results
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    source_languages.plot(kind='bar', color='skyblue')
    plt.title('Source Languages')
    plt.xlabel('Language')
    plt.ylabel('Number of Translations')

    plt.subplot(2, 2, 2)
    target_languages.plot(kind='bar', color='lightgreen')
    plt.title('Target Languages')
    plt.xlabel('Language')
    plt.ylabel('Number of Translations')

    plt.subplot(2, 2, 3)
    plt.hist(translation_lengths, bins=20, color='salmon', alpha=0.7)
    plt.title('Distribution of Translation Lengths')
    plt.xlabel('Length of Translation')
    plt.ylabel('Frequency')

    plt.subplot(2, 2, 4)
    plt.hist(translation_times, bins=24, color='lightcoral', alpha=0.7)
    plt.title('Distribution of Translation Times')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Frequency')

    plt.tight_layout()

    # Save the plot
    plot_path = os.path.join(directory, 'translation_analysis.png')
    plt.savefig(plot_path)

    # Save statistics to a text file
    stats_path = os.path.join(directory, 'translation_stats.txt')
    with open(stats_path, 'w') as f:
        f.write("Most common source languages:\n")
        f.write(str(source_languages) + '\n\n')
        f.write("Most common target languages:\n")
        f.write(str(target_languages) + '\n\n')
        f.write("Summary statistics for translation lengths:\n")
        f.write(str(translation_lengths.describe()) + '\n\n')
        f.write("Summary statistics for translation times:\n")
        f.write(str(translation_times.describe()))

    print("Analysis completed.")

# Get the absolute path of the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Use the absolute path to access the data directory
data_dir = os.path.join(script_dir, '../data')

# Call the function with the path to your data directory
analyze_translations(data_dir)
