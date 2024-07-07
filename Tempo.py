import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:/Users/masjk/OneDrive\SAC Projects\American and A10 Comparison.xlsx", sheet_name="Tempo and Luck (KnPm)")
print(data)

#flipping x and y variable to show vertically (tempo should be read vertically)
sns.swarmplot(data=data, x="Conf", y="AdjT", palette= ['red','blue'])
plt.title("Tempo Ratings")
plt.ylabel("Adj. Tempo (Poss. per 40 min.)")
plt.annotate('Tulane', xy=("Amer", 72.7), xytext=("Amer", 72.20))
plt.annotate('CLT', xy=("Amer",62.8), xytext=("Amer", 62.80))
plt.annotate('NT', xy=("Amer",61.8), xytext=("Amer", 61.98))
plt.annotate('GMU', xy=("A10",63.8), xytext=("A10", 63.26))
plt.annotate('GW', xy=("A10",69.8), xytext=("A10", 70.1))
plt.show()

