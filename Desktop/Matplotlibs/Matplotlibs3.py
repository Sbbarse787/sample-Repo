import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df=pd.read_csv('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/05-Fill_Betweens/data.csv')
print(df.head())
age=df['Age']
all_dev=df['All_Devs']
python=df['Python']
JavaScript=df['JavaScript']

plt.plot(age,all_dev,label='All developers',linestyle='--')
plt.plot(age,python,label='Python developers')
overall_median=57287

plt.fill_between(age,python,all_dev,where=(python>all_dev),
	             interpolate=True,alpha=0.25,label='Above average')

plt.fill_between(age,python,all_dev,where=(python<=all_dev),
	             interpolate=True,alpha=0.25,label='below average')

plt.plot(age,JavaScript,label='JavaScript developers')
plt.title('Salary of individual developers Vs Age of developers')
plt.xlabel('Age of developers')
plt.ylabel('Salary of individual developers')
plt.legend()
plt.show()
plt.scatter(python,all_dev,s=200,c='red',marker='o',cmap='flag',alpha=0.75,label='all dev')
plt.scatter(python,JavaScript,s=200,c='blue',linestyle='dashed',cmap='summer',alpha=1,label='JavaScript')

cbar=plt.colorbar()
cbar.set_label('JavaScript dev')

plt.xscale('log')
plt.yscale('log')

plt.title('Python Dev salary Vs All dev Salary')
plt.xlabel('Python dev')
plt.ylabel('All dev')
plt.legend()
plt.tight_layout()
plt.show()