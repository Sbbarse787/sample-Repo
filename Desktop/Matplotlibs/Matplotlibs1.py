import pandas as pd
import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
#df=pd.read_csv('Use the URL')
'''with open('Language_Worked_with.csv') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	language_counter=Counter()
	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages=[]
popularity=[]

for item in language_counter.most_common(15):
		languages.append(item[0])
		popularity.append(item[1])

print(languages)
print(popularity)
'''

df=pd.read_csv('Language_Worked_with.csv')
#print(df.head())

ids=df['Responder_id']
lang_responses=df['LanguagesWorkedWith']

language_counter=Counter()
for response in lang_responses:
	language_counter.update(response.split(';'))


print(language_counter)
languages=[]
popularity=[]

for item in language_counter.most_common(15):
		languages.append(item[0])
		popularity.append(item[1])




plt.style.use('fivethirtyeight')

languages.reverse()
popularity.reverse()
print(languages)

explode=[0,0,0,0,0,0,0,0,0,0,0,0.2,0,0,0]
plt.pie(popularity,labels=languages,wedgeprops={'edgecolor':'black'},explode=explode,shadow=True,autopct='%1.1f%%')

plt.title('Languages Vs popularity')
#plt.ylabel('Languages')
#plt.xlabel('Number of people uses')

#plt.legend()
#plt.grid(True)
plt.tight_layout()

plt.show()

#If values are greater than 5 than than use bar char or line chart instead of PIE chart