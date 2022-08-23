

# --------------trick -1 ------------------------------------

# with open("./whether - Sheet1.csv") as whether_file:
#     whether = whether_file.readlines()
#     print(whether)


# --------------trick -2 with csv import--------------------

# import csv
# with open("./whether - Sheet1.csv") as whether_file:
#     data = csv.reader(whether_file)
#     tempratures = []
#     for row in data:
#         if row[1] != "Temp":
#             tempratures.append(row[1])
#     print(tempratures)


# --------------trick -2 with panda import--------------------


# c:\users\zxc\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip

# import pandas
# data = pandas.read_csv("./whether - Sheet1.csv")
# print(data)
# print(data["Temp"])
# data.info()
# print(data.to_dict())
# print(data["Temp"].to_list())
# print(data["Temp"].mean())
# print(data["Temp"].median())
# print(data["Temp"].mode())
