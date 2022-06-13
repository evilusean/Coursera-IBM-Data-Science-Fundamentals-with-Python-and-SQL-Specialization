Scenario/Initial Insctuctions:

https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/Instructions_for_Peer_Graded_Assignment.md.html?origin=www.coursera.org

Instructions
As a hands on Assignment, you will be working on a real world dataset provided by the Chicago Data Portal. Imagine, you have been hired by a non-profit organization that strives to improve educational outcomes for children and youth in the City of Chicago. Your job is to analyze the census, crime, and school data for a given neighborhood or district. You will identify causes that impact the enrollment, safety, health, environment ratings of schools.

You will be asked questions that will help you understand the data just like a data analyst or data scientist would. You will be assessed both on the correctness of your SQL queries and results.

Assignment Topic:
In this assignment, you will download the datasets provided, load them into a database, write and execute SQL queries to answer the problems provided, and upload a screenshot showing the correct SQL query and result for review by your peers. A Jupyter notebook is provided in the preceding lesson to help you with the process.

This assignment involves 3 datasets for the city of Chicago obtained from the Chicago Data Portal:

1. Chicago Socioeconomic Indicators

This dataset contains a selection of six socioeconomic indicators of public health significance and a hardship index, by Chicago community area, for the years 2008 – 2012.

2. Chicago Public Schools

This dataset shows all school level performance data used to create CPS School Report Cards for the 2011-2012 school year.

3. Chicago Crime Data

This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days.

Using a subset of the data given by coursera limited to ~500 rows, original dataset is over 1.55GB in size and contains over 6.5 million rows. 
Data Downloaded as CSV's
Created Tables: CENSUS, CHICAGO_PUBLIC_SCHOOLS, CHICAGO_CRIME_DATA in IBM's Db2 cloud database
Loaded CSV's into newly created tables on IBM's Db2 cloud platform, scripts and CSV's can be found in directory above.

(Deleted db2 credentials, jupyter notebook to protect my private database login information from being publicly available, queries used below)

Problem 1: Find the total number of crimes recorded in the CRIME table.

%sql select count(*)  as TOTAL_NUMBER_OF_CRIME_CASES from CHICAGO_CRIME_DATA

Answer: 533

Problem 2: List community areas with per capita income less than 11000.

%sql select community_area_name from census_data where per_capita_income<11000

Answer:COMMUNITY_AREA_NAME

West Garfield Park

South Lawndale

Fuller Park

Riverdale

Problem 3: List all case numbers for crimes involving minors?

%sql select case_number from chicago_crime_data where lcase(primary_type) = 'offense involving children' or lcase(description) like '%minor'

Result:CASE_NUMBER

HL266884

HK238408

Problem 4: List all kidnapping crimes involving a child?(children are not considered minors for the purposes of crime analysis)

%sql select case_number from chicago_crime_data where primary_type='KIDNAPPING' 

Result:CASE_NUMBER

HN144152

Problem 5: What kind of crimes were recorded at schools?

%sql select primary_type as crime_recorded_atschool from  CHICAGO_CRIME_DATA where location_description like '%SCHOOL%'

Result:CRIME_RECORDED_ATSCHOOL

BATTERY

BATTERY

BATTERY

BATTERY

BATTERY

CRIMINAL DAMAGE

NARCOTICS

NARCOTICS

ASSAULT

CRIMINAL TRESPA

PUBLIC PEACE VI

PUBLIC PEACE VI

Problem 6: List the average safety score for all types of schools.

select avg(safety_score) as average_safety_score from CHICAGO_PUBLIC_SCHOOLS

Result:AVERAGE_SAFETY_SCORE

49

Problem 7: List 5 community areas with highest % of households below poverty line.

%sql select community_area_number, community_area_name from census_data\

order by percent_households_below_poverty desc limit 5;

Result:
COMMUNITY_AREA_NUMBER COMMUNITY_AREA_NAME
54	                  Riverdale
37	                  Fuller Park
68	                  Englewood
29	                  North Lawndale
27	                  East Garfield Park

Problem 8: Which community area(number) is most crime prone?

%sql select community_area_number,count(case_number) as no_of_cases from CHICAGO_CRIME_DATA\

group by community_area_number order by no_of_cases desc limit 1

Result:
COMMUNITY_AREA_NUMBER NO_OF_CASES
    25	                  43

Problem 9: Use a sub-query to find the name of the community area with highest hardship index.

%sql select community_area_name from census_data where hardship_index=(select max(hardship_index) from census_data)

Result:COMMUNITY_AREA_NAME

Riverdale

Problem 10: Use a sub-query to determine the Community Area Name with most number of crimes?

%sql select community_area_name from census_data where\

community_area_number = (select community_area_number from (select * from (select community_area_number, count(community_area_number)\

as crimes_in_community from chicago_crime_data group by community_area_number))where\

crimes_in_community =(select max(crimes_in_community) from (select community_area_number, count(community_area_number) as\

                                                            crimes_in_community from chicago_crime_data group by community_area_number)));

Result:COMMUNITY_AREA_NAME
Austin                                       
                                                           
Fin.   

