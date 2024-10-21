# Investigating Netflix Movies

This project analyzes Netflix movies from the 1990s using a subset of data. The code focuses on visualizing the distribution of movie durations and analyzing action movies' duration patterns.

## Features:
1. **Data Loading and Filtering**:
   - The dataset is loaded using `pandas` from a CSV file (`netflix_data.csv`).
   - Only movies released between 1990 and 1999 are included in the analysis.
   
2. **Visualization**:
   - A histogram is generated using `matplotlib` to display the distribution of movie durations for the 1990s.
   - The chart shows how many movies fall within specific duration intervals.

3. **Action Movies Analysis**:
   - The code identifies action movies from the filtered 1990s dataset.
   - It counts how many action movies have a duration of less than 90 minutes.

## Technologies:
- Python
- Pandas
- Matplotlib

## Usage:
To run the script, ensure you have the necessary libraries installed. You can install them using:

pip install pandas matplotlib

Then, run the script to see the visualizations and action movie analysis:

python netflix_analysis.py


