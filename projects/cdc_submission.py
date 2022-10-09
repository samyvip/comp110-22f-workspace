"""Plots of Global Greenhouse Emissions."""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


x: list = [2017, 2018, 2019, 2020, 2021]
# Africa CO2
y: list = [8.532, 8.594, 8.964, 9.368, 11.350]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Carbon Dioxide Emissions in Africa')
plt.xticks(np.linspace(2017, 2021, 5))


plt.show()

# Africa greenhouse
y: list = [804.550, 820.242, 824.164, 746.013, 765.998]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Greenhouse Emissions in Africa')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# Africa methane
y: list = [528.406, 540.723, 543.184, 490.432, 519.403]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Methane Emissions in Africa')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# Africa Nitrous Oxide
y: list = [267.613, 270.926, 272.016, 246.213, 235.245]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Nitrous Oxide Emissions in Africa')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# Asia CO2
y: list = [107.852, 106.771, 106.823, 106.510, 109.570]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Carbon Dioxide Emissions in Asia')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# Asia greenhouse
y: list = [2935.803, 2941.458, 3075.612,2998.238, 3186.667]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Greenhouse Emissions in Asia')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# Asia methane
y: list = [1969.123, 1974.377, 2071.890, 2017.755, 2118.340]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Methane Emissions in Asia')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# Asia nitrous oxide
y: list = [858.827, 860.310, 896.899, 873.973, 958.757]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Nitrous Oxide Emissions in Asia')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# World CO2
y: list = [372.097, 373.052, 372.570, 365.372, 389.377]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Carbon Dioxide Emissions in the World')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# world greenhouse
y: list = [6441.159, 6474.044, 6596.958, 6255.609, 6660.610]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Greenhouse Emissions in the World')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# world methane
y: list = [3894.472, 3914.004, 4000.040, 3790.607, 4035.877]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Methane Emissions in the World')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()

# world nitrous oxide
y: list = [2174.591, 2186.988, 2224.347, 2099.630, 2235.356]
plt.plot(x,y)
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r')
plt.xlabel('Years')
plt.ylabel('Million Metric Tons of CO2 Equivalent')
plt.title('Nitrous Oxide Emissions in the World')
plt.xticks(np.linspace(2017, 2021, 5))
plt.show()