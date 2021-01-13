import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('seaborn')

fig = plt.figure()
ax = Axes3D(fig)

data = pd.read_csv('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/10-Subplots/data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

'''ax.scatter(ages,dev_salaries,js_salaries,s=100,c='yellow')
plt.show()
ax.bar(ages,dev_salaries,js_salaries)
plt.show()'''
ax.plot3D(ages,dev_salaries,js_salaries,'red')
plt.show()