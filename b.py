import pandas as pd

#create a simple dataframe
data ={
    'Name': ['Alice','Bob','Charlie','elice','jane'],
    'Age': [25,30,35,31,21],
    'City': ['New York','Paris','London','Banglore','Pune'],
    'College':['SCOET','GCOET','JCOET','JDIET','YCOET']
}
df = pd.DataFrame(data)

#Display the dataframe
print(df)

#Access a column
print(df['Name'])

#basis statistics
print(df['Age'].mean()) #average age

# filter rows
print(df[df['Age'] > 30])