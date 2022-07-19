#install specific version of libraries used in lab
#! mamba install pandas==1.3.3
#! mamba install numpy=1.21.2
#! mamba install scipy=1.7.1-y
#!  mamba install seaborn=0.9.0-y
#!  mamba install matplotlib=3.4.3-y
#!  mamba install statsmodels=0.12.0-y

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
#Read in the csv file from the URL using the request library
ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
ratings_df = pd.read_csv(ratings_url)
"""
T-Test: Using the teachers' rating data set, does gender affect teaching evaluation rates?
We will be using the t-test for independent samples. For the independent t-test, the following assumptions must be met.

One independent, categorical variable with two levels or group
One dependent continuous variable
Independence of the observations. Each subject should belong to only one group. There is no relationship between the observations in each group.
The dependent variable must follow a normal distribution
Assumption of homogeneity of variance
State the hypothesis

µµ ("there is no difference in evaluation scores between male and females")
µµ ("there is a difference in evaluation scores between male and females")
"""

#We can plot the dependent variable with a histogram
ax = sns.distplot(ratings_df['eval'],
                  bins=20,
                  kde=True,
                  color='red',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
## we can assume it is Normal

#We can use the Levene's Test in Python to check test significance
scipy.stats.levene(ratings_df[ratings_df['gender'] == 'female']['eval'],
                   ratings_df[ratings_df['gender'] == 'male']['eval'], center='mean')
# since the p-value is greater than 0.05 we can assume equality of variance

#Use the ttest_ind from the scipy_stats library
scipy.stats.ttest_ind(ratings_df[ratings_df['gender'] == 'female']['eval'],
                   ratings_df[ratings_df['gender'] == 'male']['eval'], equal_var = True)
#Conclusion: Since the p-value is less than alpha value 0.05, we reject the null hypothesis as there is enough proof that there is a statistical difference in teaching evaluations based on gender
"""
ANOVA: Using the teachers' rating data set, does beauty score for instructors differ by age?
First, we group the data into cateries as the one-way ANOVA can't work with continuous variable - using the example from the video, we will create a new column for this newly assigned group our categories will be teachers that are:

40 years and younger
between 40 and 57 years
57 years and older
"""
ratings_df.loc[(ratings_df['age'] <= 40), 'age_group'] = '40 years and younger'
ratings_df.loc[(ratings_df['age'] > 40)&(ratings_df['age'] < 57), 'age_group'] = 'between 40 and 57 years'
ratings_df.loc[(ratings_df['age'] >= 57), 'age_group'] = '57 years and older'
"""
State the hypothesis

µµµ (the three population means are equal)
 At least one of the means differ
Test for equality of variance
"""
scipy.stats.levene(ratings_df[ratings_df['age_group'] == '40 years and younger']['beauty'],
                   ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['beauty'], 
                   ratings_df[ratings_df['age_group'] == '57 years and older']['beauty'], 
                   center='mean')
# since the p-value is less than 0.05, the variance are not equal, for the purposes of this exercise, we will move along

#First, separate the three samples (one for each job category) into a variable each.
forty_lower = ratings_df[ratings_df['age_group'] == '40 years and younger']['beauty']
forty_fiftyseven = ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['beauty']
fiftyseven_older = ratings_df[ratings_df['age_group'] == '57 years and older']['beauty']

#Now, run a one-way ANOVA.
f_statistic, p_value = scipy.stats.f_oneway(forty_lower, forty_fiftyseven, fiftyseven_older)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))
#Conclusion: Since the p-value is less than 0.05, we will reject the null hypothesis as there is significant evidence that at least one of the means differ.

#ANOVA: Using the teachers' rating data set, does teaching evaluation score for instructors differ by age?
#Test for equality of variance
scipy.stats.levene(ratings_df[ratings_df['age_group'] == '40 years and younger']['eval'],
                   ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['eval'], 
                   ratings_df[ratings_df['age_group'] == '57 years and older']['eval'], 
                   center='mean')

forty_lower_eval = ratings_df[ratings_df['age_group'] == '40 years and younger']['eval']
forty_fiftyseven_eval = ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['eval']
fiftyseven_older_eval = ratings_df[ratings_df['age_group'] == '57 years and older']['eval']

f_statistic, p_value = scipy.stats.f_oneway(forty_lower_eval, forty_fiftyseven_eval, fiftyseven_older_eval)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))
#Conclusion: Since the p-value is greater than 0.05, we will fail to reject the null hypothesis as there is no significant evidence that at least one of the means differ.

"""
Chi-square: Using the teachers' rating data set, is there an association between tenure and gender?
State the hypothesis:

 The proportion of teachers who are tenured is independent of gender
 The proportion of teachers who are tenured is associated with gender
Create a Cross-tab table
"""
cont_table  = pd.crosstab(ratings_df['tenure'], ratings_df['gender'])
cont_table
#Use the scipy.stats library and set correction equals False as that will be the same answer when done by hand, it returns: 𝜒2 value, p-value, degree of freedom, and expected values.
scipy.stats.chi2_contingency(cont_table, correction = True)
#Conclusion: Since the p-value is greater than 0.05, we fail to reject the null hypothesis. As there is no sufficient evidence that teachers are tenured as a result of gender.

"""
Correlation: Using the teachers rating dataset, Is teaching evaluation score correlated with beauty score?
State the hypothesis:

 Teaching evaluation score is not correlated with beauty score
 Teaching evaluation score is correlated with beauty score
Since they are both continuous variables we can use a pearson correlation test and draw a scatter plot
"""
#create plot
ax = sns.scatterplot(x="beauty", y="eval", data=ratings_df)
scipy.stats.pearsonr(ratings_df['beauty'], ratings_df['eval'])
#Conclusion: Since the p-value (Sig. (2-tailed) < 0.05, we reject the Null hypothesis and conclude that there exists a relationship between beauty and teaching evaluation score.

#Question 1: Using the teachers rating data set, does tenure affect teaching evaluation scores?¶
#Use α = 0.05
scipy.stats.ttest_ind(ratings_df[ratings_df['tenure'] == 'yes']['eval'],
                   ratings_df[ratings_df['tenure'] == 'no']['eval'], equal_var = True)
#The p-value is less than 0.05 that means that - we will reject the null hypothesis as there evidence that being tenured affects teaching evaluation scores
"""
Question 2: Using the teachers rating data set, is there an association between age and tenure?¶
Discretize the age into three groups 40 years and youngers, between 40 and 57 years, 57 years and older (This has already been done for you above.)
What is your conclusion at α = 0.01 and α = 0.05?"""
## use the chi-square function
scipy.stats.chi2_contingency(cont_table, correction = True)
#At the α = 0.01, p-value is greater, we fail to reject null hypothesis as there is no evidence of an association between age and tenure
#At the α = 0.05, p-value is less, we reject null hypoothesis as there is evidence of an association between age and tenure
#Question 3: Test for equality of variance for beauty scores between tenured and non-tenured instructors
#Use α = 0.05
### use the levene function to find the p-value and conclusion
scipy.stats.levene(ratings_df[ratings_df['tenure'] == 'yes']['beauty'],
                   ratings_df[ratings_df['tenure'] == 'no']['beauty'], 
                   center='mean')
#Since the p-value is greater than 0.05, we will assume equality of variance of both groups

#Question 4: Using the teachers rating data set, is there an association between visible minorities and tenure?¶
#Use α = 0.05
## run the chi2_contingency() on the contigency table
scipy.stats.chi2_contingency(cont_table, correction = True)
#Since the p-value is greater than 0.05, we fail to reject null hypoothesis as there is evidence of an association between visible minorities and tenure










