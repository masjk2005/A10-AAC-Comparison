import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#check sheet name!!!!
data = pd.read_excel(r"C:/Users/masjk/OneDrive\SAC Projects\American and A10 Comparison.xlsx", sheet_name="Amer Quad Stats")
sns.barplot(data=data, x="Quad", y="Amt.")
plt.title("American")
plt.ylim(0,120)
plt.show()