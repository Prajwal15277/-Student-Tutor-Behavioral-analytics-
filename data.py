import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

import pylab

table = pd.read_csv(r"C:\Users\User\OneDrive\Desktop\DA_Project\Data\ba_table.csv") 


#finding which data types we have in dataset
table.dtypes
table.info()


# Exploratory Data Analysis
# Measures of Central Tendency / First moment business decision
#mean
table.video_time.mean()

#median
table.video_time.median()

#mode
table.video_time.mode()


table.mean()
table.mode()
table.median()




# Measures of Dispersion / Second moment business decision
# variance
table.video_time.var()
table.var()

# standard deviation
table.video_time.std()
table.std()

 # range
range = max(table.video_time) - min(table.video_time)
range

# Third moment business decision
table.video_time.skew()
table.skew()

# Fourth moment business decision
table.video_time.kurt()
table.kurt()


#findig dublicates
table[table.duplicated()]
print(table)



#table.student_id= table.student_id.astype['str']

# Drop duplicate rows
table.drop_duplicates()
print(table)

# finding null values 
print(table.isnull().sum())
print(table)

# put 0 there, where null values are present
print(table.fillna(0))


#finding how much rows 
num_rows=table.shape[0]
print(num_rows)


#finding how much unique students 
num_unique_students = table['student_id'].unique()
print("number of unique student:",num_unique_students)


#finding unique course id
num_of_course =table['course_id'].unique()
print('number of course:',num_of_course)


# Assuming 'course_id' is the column name containing course IDs
specific_course_id = 'your_course_id'
specific_course_data = data[data['course_id'] == specific_course_id]

table[course_id] = '103'




#Plot the emotions

sns.countplot(table['emt_sad']).unique()









