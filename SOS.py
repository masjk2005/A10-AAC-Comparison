import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:/Users/masjk/OneDrive\SAC Projects\American and A10 Comparison.xlsx", sheet_name="A10&AAC (KenPom)")


sns.swarmplot(data=data, x="SoSAdjEM", y="Conf", palette= ['red','blue'])
plt.title("Overall Strength of Schedule Rating")
plt.xlabel("Adj. SOS Rating")
plt.annotate('Dayton', xy=(6.89, "A10"), xytext=(5.94, "A10"))
plt.annotate('Tulsa', xy=(-1.11, "Amer"), xytext=(-0.95, "Amer"))
plt.annotate('GMU', xy=(2.27, "A10"), xytext=(1.8, "A10"))
plt.annotate('NT', xy=(5.85, "Amer"), xytext=(5.95, "Amer"))
plt.annotate('CLT', xy=(2.62, "Amer"), xytext=(2.71, "Amer"))
plt.show()