import numpy as np
import pandas as pd

crime_scenes=pd.read_csv("crime.csv")

crime_scenes["risk_based_on_ViolentCrimesPerPop"]=np.where(
    crime_scenes["ViolentCrimesPerPop"]>=0.50,"High-Crime","LowCrime"
)

group_data=crime_scenes.groupby("risk_based_on_ViolentCrimesPerPop").agg(
    average_PctUnemployed=("PctUnemployed","mean")
)

print(f"{group_data}")