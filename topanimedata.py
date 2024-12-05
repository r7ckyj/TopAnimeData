import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/kaggle/input/top-anime-dataset-2024/Top_Anime_data_cleaned.csv')

# Distribution of Scores
plt.figure(figsize=(10, 6)) #assigning figure size 
sns.histplot(df['Score'], bins=30, kde=True, color='skyblue') # creating histogram
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

# Score vs. Popularity Scatter Plot 
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Score', y='Popularity', data=df, alpha=0.7)
plt.title('Score vs. Popularity')
plt.xlabel('Score')
plt.ylabel('Popularity')
plt.show()



# Top 10 Genres Pie Chart
top_genres = df['Genres'].str.split(',').explode().str.strip().value_counts(dropna=True).head(10)

plt.figure(figsize=(7, 7))
colors = ['pink','purple','hotpink','violet','lightpink','plum','deeppink','indigo','lightyellow','darkorchid']
explode=(0.2,0,0,0,0,0,0,0,0,0)   #to make a distance in selected bar
values=df['Genres'].str.split(',').explode().str.strip().value_counts(dropna=True).head(10)
plt.pie(top_genres,colors=colors,explode=explode,wedgeprops={'edgecolor':'black'},labels= top_genres.index, autopct=lambda x: '{:.0f}'.format(x*values.sum()/100), startangle=50)
plt.title('Top 10 Genres')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# Demographic Pie Chart
demographic = df["Demographic"].value_counts()
plt.figure(figsize=(7,7))
colors = ['pink','purple','hotpink','violet','darkorchid']
explode=(0,0.1,0.1,0.2,0.2)
values=df["Demographic"].value_counts()
plt.pie(demographic,colors=colors,explode=explode,wedgeprops={'edgecolor':'black'},labels=demographic.index,autopct=lambda x: '{:.0f}'.format(x*values.sum()/100))
plt.title("Demographics")
plt.axis('equal')

plt.show()


#Avg Score by Rating

plt.figure(figsize=(10,6))
df.groupby(by = "Rating")["Score"].mean().plot(kind = "bar",ylim=(7.6, 8.4))

plt.title('Average Score by Rating')
plt.xlabel('Rating')
plt.ylabel('Average Score')
plt.tight_layout()
plt.show()

#Avg Score by Genre (split and explode Genres column to make it easier to group)

df["Genres"]=df["Genres"].str.split(', ')
df=df.explode("Genres").replace({np.nan: None})
df.groupby(by = "Genres")["Score"].mean().plot(kind = "bar",ylim=(7.6, 8.4))
plt.title('Average Score by Genre')
plt.xlabel('Genres')
plt.ylabel('Average Score')
plt.tight_layout()
plt.show()
