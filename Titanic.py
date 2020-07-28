#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt

#survivor percentage distribution
txtLabels = 'First', 'Second', 'Third', 'Crew' 
fractions = [203, 118, 178,212] 
offsets =(0, 0.05, 0, 0) 
explode=(0,0,0,0.1)
plt.pie(fractions, explode=explode,  labels=txtLabels,
        autopct='%1.1f%%', startangle=90, 
        colors=sns.color_palette('muted') )
plt.axis('equal') 
plt.title("Survival percentage")
plt.show()

#deceased percentage distribution
txtLabels = 'First', 'Second', 'Third', 'Crew' 
fractions = [122, 167, 528,673] 
offsets =(0, 0.05, 0, 0) 
explode=(0,0,0,0.1)
plt.pie(fractions, explode=explode,  labels=txtLabels,
        autopct='%1.1f%%', startangle=90, 
        colors=sns.color_palette('muted') )

plt.axis('equal') 
plt.title("Deceased percentage")
plt.show()

Class=['First','Second','Third','Crew']
Survival=[203,118,178,212]
Deceased=[122,167,528,673]

#assign list variables to DataFrame object
TitanicDataFrame = pd.DataFrame({'Survival': Survival, 'Deceased':  Deceased},index=Class)
TitanicDataFrame
#grouped bar graph
TitanicDataFrame.plot(kind='bar', grid=True) 
plt.show()

#Interpretation: 
#1)The third class people had more number of deceased to survival rate(i.e survival rate 33%).
#2)First class people had more chances of survival to death percentage.
#3)Group bar chat helps us to interpret data more efficiently. As we can see the Survival vs deceased for that particular status we can easily make conclusions.
#4)Just by seeing survival vs dead pie chart percentages individually might be misleading since they do not take into account of the total amount of population for that particular category.
    

