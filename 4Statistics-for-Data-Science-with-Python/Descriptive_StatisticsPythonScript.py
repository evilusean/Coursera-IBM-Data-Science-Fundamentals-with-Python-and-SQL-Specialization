
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot

#read csv from url
ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
ratings_df=pd.read_csv(ratings_url)

#data checks
ratings_df.describe()
ratings_df.head()
ratings_df.info()
ratings_df.shape
ratings_df.head(10)
#check ratings mean median min max
ratings_df['students'].mean()
ratings_df['students'].median()
ratings_df['students'].min()
ratings_df['students'].max()
#plot basic histogram
pyplot.hist(ratings_df['beauty'])
#Use a group by gender to view the mean scores of the beauty we can say that beauty scores differ by gender as the mean beauty score for women is higher than men
ratings_df.groupby('gender').agg({'beauty':['mean', 'std', 'var']}).reset_index()
#Calculate the percentage of males and females that are tenured professors. Will you say that tenure status differ by gender?
tenure_count = ratings_df[ratings_df.tenure == 'yes'].groupby('gender').agg({'tenure': 'count'}).reset_index()
#Find the percentage
tenure_count['percentage'] = 100 * tenure_count.tenure/tenure_count.tenure.sum()
tenure_count
#
#Question 1: Calculate the percentage of visible minorities are tenure professors. Will you say that tenure status differed if teacher was a visible minority?
tenure_count = ratings_df.groupby('minority').agg({'tenure': 'count'}).reset_index()
tenure_count['percentage'] = 100 * tenure_count.tenure/tenure_count.tenure.sum()
tenure_count
#Question 2: Does average age differ by tenure? Produce the means and standard deviations for both tenured and untenured professors.
ratings_df.groupby('tenure').agg({'age':['mean', 'std']}).reset_index()
Question 3: Create a histogram for the age variable.
pyplot.hist(ratings_df['age'])
#Question 4: Create a bar plot for the gender variable.
pyplot.bar(ratings_df.gender.unique(),ratings_df.gender.value_counts(),color=['pink','blue'])
pyplot.xlabel('Gender')
pyplot.ylabel('Count')
pyplot.title('Gender distribution bar plot')
Question 5: What is the Median evaluation score for tenured Professors?
ratings_df[ratings_df['tenure'] == 'yes']['eval'].median()