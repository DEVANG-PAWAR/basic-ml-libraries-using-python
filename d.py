import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#1. generate random data with numpy
np.random.seed(0)
student_ids = np.arange(1, 21)
entc_scores = np.random.randint(40, 100, size=20)
ece_scores = np.random.randint(25, 100, size=20)
cse_scores = np.random.randint(25, 100, size=20)


#2.create dataframe with pandas
df = pd.DataFrame({
    'StudentID': student_ids,
    'ENTC':entc_scores,
    'ECE': ece_scores,
    'CSE': cse_scores
})


print("First 5 rows of the DataFrame:")
print(df.head())

#3. basic analysis with pandas
print("\nAverage scores:")
print(df[['ENTC', 'ECE', 'CSE']].mean())
print("\nStudent with highest Math score:")



#4.visualization with matplotlib
plt.figure(figsize=(8, 5))
plt.plot(df['StudentID'], df['ENTC'], marker='o', label='ENTC')
plt.plot(df['StudentID'], df['ECE'], marker='s', label='ECE')
plt.plot(df['StudentID'], df['CSE'], marker='^', label='CSE')
plt.xlabel('StudentID')
plt.ylabel('Score')
plt.title('Student Scores by Branch')
plt.legend()
plt.show()

#5.visualization with seaborn
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['ENTC', 'ECE', 'CSE']])
plt.title('Score Distribution by Branch')
plt.ylabel('Score')
plt.show()