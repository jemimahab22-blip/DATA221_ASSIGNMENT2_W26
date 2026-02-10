import pandas as pd

data_frame=pd.read_csv("student.csv")

filtered_students=[
    (data_frame["studytime"]>=3)&
    (data_frame["internet"]==1)&
    (data_frame["absences"]<=5)
]
data_filtered=pd.DataFrame(filtered_students)#I'm saving my filtered dataset into a new csv file
data_filtered.to_csv("high_engagement.csv",index=False)#index=false prevents panda from adding new index columns

number_of_students=len(filtered_students)
average_grade=filtered_students[0].mean()
print(f"Number of students filtered:{number_of_students}")
print(average_grade)