import numpy as np
import pandas as pd

data_f= pd.read_csv("student.csv")

#np.where means "if this, then that"

data_f["grade_band"]=np.where(#np.where() is a vectorized if-else for arrays/columns
    data_f["grade"]<= 9,"Low",
    np.where(
            data_f["grade"].between(10,14),"Medium", "high"
    )
)


summary= data_f.groupby("grade_band").agg(#.group helps to split the dataset into separate piles based on grade_band
    students_number=("grade", "count"),#.agg() summarizes statistics you want from each pile.
    average_absences=("absences","mean"),
    internet_percentage=("internet","mean")
)
summary["internet_percentage"]*=100#this converts the internet_percentage into percentages

summary.to_csv("student_bands.csv")#we are putting the table into a new csv file
