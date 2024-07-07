import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:/Users/masjk/OneDrive\SAC Projects\American and A10 Comparison.xlsx", sheet_name="Torvik")


#annotating to point out teams that stand out (first tried it on this graph)
#also pointing out GMU and CLT on each graph
sns.swarmplot(data=data, x="CONF", y="BARTHAG", palette= ['red','blue'])
plt.title("Barthag Power Ratings")
plt.ylabel("Power Rating (Chance of beating avg. D1 Team)")
plt.annotate('Dayton', xy=("A10", 0.85), xytext=("A10", 0.82))
plt.annotate('GMU', xy=("A10", 0.7131), xytext=("A10", 0.6935))
plt.annotate("FAU", xy=("Amer",0.819), xytext = ("Amer",0.83))
plt.annotate("UTSA", xy=("Amer", 0.348), xytext = ("Amer",0.36))
plt.annotate("CLT", xy=("Amer", 0.6711), xytext = ("Amer",0.6715))
plt.show()