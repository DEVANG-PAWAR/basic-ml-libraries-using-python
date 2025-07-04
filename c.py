import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({'Branch':['Entc','Mech','Etc','Tesa','Mech','Entc','Etc','Tesa'],
                             'Score': [85,90,78,88,75,67,81,91]})

sns.boxplot(x='Branch',y='Score',data=df)
plt.show()