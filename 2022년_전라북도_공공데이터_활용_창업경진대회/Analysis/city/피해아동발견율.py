import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc

df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-DataAnalysis/Data/피해아동발견율.csv", encoding="euc-kr")
print(df)
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family=font)

# y = df["kid"]
# x = np.arange(len(y))
# xlabel = df["city"]
# plt.title("Bar Chart")
# plt.bar(x, y)
# plt.xticks(x, xlabel)
# plt.yticks(sorted(y))
# plt.xlabel("도시명")
# plt.ylabel("발생율")
# ax=plt.gca()
# ax.get_yaxis().set_visible(False)
# plt.show()

