
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:/Users/masjk/OneDrive\SAC Projects\American and A10 Comparison.xlsx", sheet_name="A10&AAC (KenPom)")

#scatterplot won't work for just one variable
#adding palette changes dot colors (to get conference's colors for more clarity)
sns.swarmplot(data=data, x="NC AdjEM", y="Conf", palette= ['red','blue'])
plt.title("Non-Conference of Schedule Rating")
plt.xlabel("Adj. SOS Rating")
plt.annotate('Dayton', xy=(6.98, "A10"), xytext=(4.6, "A10"))
plt.annotate('GW', xy=(-10.45, "A10"), xytext=(-10.10, "A10"))
plt.annotate('GMU', xy=(-3.26, "A10"), xytext=(-3.35, "A10"))
plt.annotate('Tulsa', xy=(-10.41, "Amer"), xytext=(-10, "Amer"))
plt.annotate('CLT', xy=(2.62, "Amer"), xytext=(2.825, "Amer"))
plt.show()
