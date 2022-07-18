#install specific version of libraries used in lab
#! mamba install pandas==1.3.3
#! mamba install numpy=1.21.2
#! mamba install scipy=1.7.1-y
#!  mamba install seaborn=0.9.0-y
#!  mamba install matplotlib=3.4.3-y

#Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

#Read in the csv file from the url using the request library
ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
ratings_df = pd.read_csv(ratings_url)

#Identify all duplicate cases using prof variable - find the unique values of the prof variables
ratings_df.prof.unique()
#Print out the number of unique values in the prof variable
ratings_df.prof.nunique()
#Using all observations, Find the average and standard deviation for age
ratings_df['age'].mean()
ratings_df['age'].std()
#first we drop duplicates using prof as a subset and assign it a new dataframe name called no_duplicates_ratings_df
no_duplicates_ratings_df = ratings_df.drop_duplicates(subset =['prof'])
no_duplicates_ratings_df.head()
#Use the new dataset to get the mean of age
no_duplicates_ratings_df['age'].mean()
no_duplicates_ratings_df['age'].std()
#Using a bar chart, demonstrate if instructors teaching lower-division courses receive higher average teaching evaluations.
ratings_df.head()
#Find the average teaching evaluation in both groups of upper and lower-division
division_eval = ratings_df.groupby('division')[['eval']].mean().reset_index()
#Plot the barplot using the seaborn library
sns.set(style="whitegrid")
ax = sns.barplot(x="division", y="eval", data=division_eval)
#Create a scatterplot with the scatterplot function in the seaborn library
ax = sns.scatterplot(x='age', y='eval', data=ratings_df)
#Using gender-differentiated scatter plots, plot the relationship between age and teaching evaluation scores.
#Create a scatterplot with the scatterplot function in the seaborn library this time add the hue argument
ax = sns.scatterplot(x='age', y='eval', hue='gender',
                     data=ratings_df)
#Create a box plot for beauty scores differentiated by credits.
#We use the boxplot() function from the seaborn library
ax = sns.boxplot(x='credits', y='beauty', data=ratings_df)
#What is the number of courses taught by gender?
#We use the catplot() function from the seaborn library
sns.catplot(x='gender', kind='count', data=ratings_df)
#Create a group histogram of taught by gender and tenure
#We will add the hue = Tenure argument
sns.catplot(x='gender', hue = 'tenure', kind='count', data=ratings_df)
#Add division as another factor to the above histogram
#We add another argument named row and use the division variable as the row
sns.catplot(x='gender', hue = 'tenure', row = 'division',
            kind='count', data=ratings_df,
            height = 3, aspect = 2)
#Create a scatterplot of age and evaluation scores, differentiated by gender and tenure
#Use the relplot() function for complex scatter plots
sns.relplot(x="age", y="eval", hue="gender",
            row="tenure",
            data=ratings_df, height = 3, aspect = 2)
#Create a distribution plot of teaching evaluation scores
#We use the distplot() function from the seaborn library, set kde = false because we don'e need the curve
ax = sns.distplot(ratings_df['eval'], kde = False)
#Create a distribution plot of teaching evaluation score with gender as a factor
### use the distplot function from the seaborn library
sns.distplot(ratings_df[ratings_df['gender'] == 'female']['eval'], color='green', kde=False) 
sns.distplot(ratings_df[ratings_df['gender'] == 'male']['eval'], color="orange", kde=False) 
plt.show()
#Create a box plot - age of the instructor by gender
ax = sns.boxplot(x="gender", y="age", data=ratings_df)
#Compare age along with tenure and gender
ax = sns.boxplot(x="tenure", y="age", hue="gender",
                 data=ratings_df)




#Question 1: Create a distribution plot of beauty scores with Native English speaker as a factor
sns.distplot(ratings_df[ratings_df['native'] == 'yes']['beauty'], color="orange", kde=False) 
sns.distplot(ratings_df[ratings_df['native'] == 'no']['beauty'], color="blue", kde=False) 
plt.show()
#Question 2: Create a Horizontal box plot of the age of the instructors by visible minority
ax = sns.boxplot(x="age", y="minority", data=ratings_df)
#Question 3: Create a group histogram of tenure by minority and add the gender factor
sns.catplot(x='tenure', hue = 'minority', row = 'gender',
            kind='count', data=ratings_df,
            height = 3, aspect = 2)
#Question 4: Create a boxplot of the age variable
ax = sns.boxplot(y="age", data=ratings_df)

