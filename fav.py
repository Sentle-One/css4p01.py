#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:00:39 2024

@author: hlajoane_the_geologist
"""

import pandas as pd
df = pd.read_csv("/Users/hlajoane_the_geologist/movie_project/movie_dataset.csv",index_col = 0)

column_names = ["Rank", "Title", "Genre", "Description", "Director", "Actors", "Year", "Runtime_minutes", "Rating", "Votes", "Revenue_millions", "Metascore"]
df = pd.read_csv("/Users/hlajoane_the_geologist/movie_project/movie_dataset.csv", header=None, names=column_names, index_col=0, skiprows=1)
#Correcting the spaces between the some column names

x = df["Revenue_millions"].mean()
df["Revenue_millions"].fillna(x, inplace = True) 
y = df["Metascore"].mean()
df["Metascore"].fillna(y, inplace = True) 
#Adding values (nan) in some columns

print(df['Rating'])
print(df['Rating'].min())
print(df['Rating'].max())
print(df['Rating'].mean())
#highest rated movie in the datase: The Dark Knight


filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue = filtered_df['Revenue_millions'].mean()
#Average Revenue for movies between 2015 and 2017: 63.099905660377345 million

movies_2016_count = (df['Year'] == 2016).sum()
#Number of movies released in 2016: 297

nolan_movies_count = (df['Director'] == 'Christopher Nolan').sum()
#The number of movies directed by Nolan:5

high_rated_movies_count = (df['Rating'] >= 8).sum()
#Number of movies with a rating of at least 8: 78

nolan_movies = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan_movies = nolan_movies['Rating'].median()
#Median rating of movies directed by Christopher Nolan: 8.6

average_rating_by_year = df.groupby('Year')['Rating'].mean()
highest_rating_year = average_rating_by_year.idxmax()
highest_rating_value = average_rating_by_year.max()
#Year with the highest average rating: 2007 (Average Rating: 7.133962264150944)

movies_2006 = (df['Year'] == 2006).sum()
movies_2016 = (df['Year'] == 2016).sum()
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
#Percentage increase in the number of movies between 2006 and 2016: 575.00%

unique_genres_count = df['Genre'].nunique()
#Number of unique genres: 207



numerical_features = df[['Year', 'Revenue_millions', 'Rating']]
correlation_matrix = numerical_features.corr()
print(correlation_matrix)
#correlation of the numerical features

























'Graphs in python'

import matplotlib.pyplot as plt

money = (df["Revenue_millions"])
opinion = (df["Rating"])

plt.scatter(money, opinion, color = '#88c999',cmap='viridis')
plt.xlabel('Revenue_millions_dollars')
plt.ylabel('Rating')
plt.title('Movie value and opinions')
plt.show()











