# TopAnimeData
## Project Summary
I performed Exploratory Data Analysis on a dataset of the top anime of 2024. The goal of this analysis is to uncover key patterns and provide insights that can help optimize recommendation systems and predict future anime success. 

## [SOURCE](https://www.kaggle.com/datasets/bhavyadhingra00020/top-anime-dataset-2024/data)

## Cleaning the Data
- Format date consistently
-	Cleaned genres column, duplicates within cells replaced (e.g. ActionAction replaced with Action)
-	Cleaned demographic column, same way as genres
-	Observation: Since the dataset is ranked by score, the popularity column is incomplete. E.g. the 10th most popular anime is not depicted in the dataset because its score is not in the top 1000. However, the 12,000th most popular anime is. The scores vs popularity scatterplot will show the correlation between these two measures. 
-	Saved cleaned dataset as CSV

