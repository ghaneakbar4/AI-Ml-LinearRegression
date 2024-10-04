import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.linear_model
import sklearn.neighbors

def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]

# load the data 
# خواندن فایل اکسل
oecd_bli=pd.read_csv('oecd_bli_2015.csv',thousands=',')
# خواندن فایل اکسل
dpg_per_capita =pd.read_csv('gdp_per_capita.csv',thousands=',',delimiter='\t',encoding='latin1',na_values="n/a",low_memory=False)

# prepaer the data
# ساخت ابجکت از داده ها
countery_state= prepare_country_stats(oecd_bli,dpg_per_capita) 
# داده های x
X =np.c_[countery_state["GDP per capita"]]
#  yداده های 
y=np.c_[countery_state["Life satisfaction"]]

# # visual the data 
countery_state.plot(kind='scatter',x="GDP per capita", y='Life satisfaction') 
plt.show()
# # select the liner model
model =sklearn.linear_model.LinearRegression()

# # train the model
model.fit(X,y)

# #RESULT
X_new = [[22587]]
print(model.predict(X_new))