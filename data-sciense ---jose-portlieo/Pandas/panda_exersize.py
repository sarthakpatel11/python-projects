import pandas as pd

sal = pd.read_csv(
    "D:/Learning Stuff/python/data-sciense ---jose-portlieo/Pandas/Salaries.csv")
# print(sal.head())
# print(sal.info())
# print(sal['BasePay'].mean())
# print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL '])
