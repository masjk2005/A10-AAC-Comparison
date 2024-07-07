import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:/Users/masjk/OneDrive\SAC Projects\American and A10 Comparison.xlsx", sheet_name="A10 Quad Stats")

#check sheet name!!!
sns.barplot(data=data, x="Quad", y="Amt.")
plt.title("Atlantic 10")
plt.ylim(0,120)
plt.show()