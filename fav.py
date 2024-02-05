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

x = df["Revenue_millions"].mean()

df["Revenue_millions"].fillna(x, inplace = True) 

y = df["Metascore"].mean()

df["Metascore"].fillna(y, inplace = True) 


print(df['Rating'])
print(df['Rating'].min())
print(df['Rating'].max())
print(df['Rating'].mean())

print(df[df['Rating'] > 8.99])

print(df['Year'])
print(df[df['Year'] > 2014])
print(df[df['Year'] < 2018])

print(df[df['Year'] > 2016])

print(df[df['Rating'] > 7.99])


numerical_features = df[['Year', 'Revenue_millions', 'Rating']]

correlation_matrix = numerical_features.corr()
print(correlation_matrix)
