
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Country", "F2010"]

df = pd.read_csv(r'/Users/samyvipin/Downloads/Annual_Greenhouse_Gas_(GHG)_Air_Emissions_Accounts.csv', usecols=columns)
print("Contents in csv file:\n", df)
df.plot
plt.show()

