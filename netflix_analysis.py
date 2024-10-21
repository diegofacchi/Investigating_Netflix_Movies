import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("D:/diego/Documents/MyProjects/Investigating_Netflix_Movies/netflix_data.csv")
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
movies_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

plt.hist(movies_1990s["duration"], bins=5, color='lightblue', edgecolor='darkblue')
plt.title('Distribution of Movie durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()
                        
duration = 100

action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

short_movie_count = 0

for key, value in action_movies_1990s.iterrows():
    if value["duration"] < 90:
        short_movie_count += 1

print(f"{short_movie_count}")