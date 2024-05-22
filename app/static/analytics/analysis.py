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
        df = pd.read_csv(filename)
        data = data.append(df, ignore_index=True)

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
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 2, 1)
    source_languages.plot(kind='bar', title='Source Languages')
    plt.subplot(2, 2, 2)
    target_languages.plot(kind='bar', title='Target Languages')
    plt.subplot(2, 2, 3)
    translation_lengths.plot(kind='hist', title='Translation Lengths')
    plt.subplot(2, 2, 4)
    translation_times.plot(kind='hist', title='Translation Times')
    plt.tight_layout()
    plt.savefig('app/static/analytics/translation_analysis.png')

# Get the absolute path of the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Use the absolute path to access the data directory
data_dir = os.path.join(script_dir, '../data')

# Call the function with the path to your data directory
analyze_translations(data_dir)
