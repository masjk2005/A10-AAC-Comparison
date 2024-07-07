import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#had to add r before entering file name AND flipped the back-slashes where the colors were different#
data = pd.read_excel(r"C:/Users/masjk/OneDrive\SAC Projects\American and A10 Comparison.xlsx", sheet_name="A10&AAC (KenPom)")
print(data)

#possible advanced sns graphs: 'dot plot with several variables,'Scatterplot with varying point sizes and hues,' 
#...'Scatterplot with categoircal variables,'

sns.scatterplot(data=data,x="AdjO",y="AdjD",hue="Conf")
plt.xlim(95,120)
plt.ylim(95,120)


#ci=None takes away the 'shadow'-looking thing on the main line (the confidence interval)
sns.regplot(data=data,x="AdjO",y="AdjD", ci=None)
plt.xlim(95,120)
plt.ylim(95,120)


#couldn't use 'hue' for ^regplot^ but lmplot could
#use x/ylims to scale graphs (has to be before plt.show() for each graph)
#added title too but its at the very top 
sns.lmplot(data=data,x="AdjO",y="AdjD",hue="Conf", palette= ['red','blue'], ci=None)
plt.xlim(95,120)
plt.ylim(95,120)
plt.title("OAdj vs. DAdj by Conference")
plt.annotate('St. Louis', xy=(111.5, 114.37), xytext=(111.55, 112.95))
plt.annotate('GMU', xy=(109.5, 101.5), xytext=(108.64, 100.32))
plt.annotate('UTSA', xy=(106.91, 113.7), xytext=(105.05, 114.5))
plt.annotate('Dayton', xy=(117.8, 102.1), xytext=(117.7, 99.4))
plt.annotate('FAU', xy=(117.8, 102.1), xytext=(118.2, 102.2))
plt.annotate('CLT', xy=(108.7, 104), xytext=(107.5, 104.3))
plt.show()

