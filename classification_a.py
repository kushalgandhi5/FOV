import pandas as pd

data = pd.read_csv("masterdata.csv")

#for taxRevenue
taxRevenue = list(data["taxRevenue"])
countryName = list(taxRevenue["CountryName"])
taxRevenue_0to3 = []
taxRevenue_3to5 = []
taxRevenue_5to6 = []
taxRevenue_6above = []

for index in range(len(taxRevenue)):
    if taxRevenue[index] >= 0 and taxRevenue[index] <= 3:
        taxRevenue_0to3.append(countryName[index])
    elif taxRevenue[index] >3 and taxRevenue[index] <= 5:
        taxRevenue_3to5.append(countryName[index])
    elif taxRevenue[index] >5 and taxRevenue[index] <= 6:
        taxRevenue_5to6.append(countryName[index])
    else:
        taxRevenue_6above.append(countryName[index])

#for education
education = list(data["education"])
countryName = list(taxRevenue["CountryName"])
education_0to3 = []
education_3to5 = []
education_5to6 = []
education_6above = []

for index in range(len(education)):
    if education[index] >= 0 and education[index] <= 3:
        education_0to3.append(countryName[index])
    elif education[index] >3 and education[index] <= 5:
        education_3to5.append(countryName[index])
    elif education[index] >5 and education[index] <= 6:
        education_5to6.append(countryName[index])
    else:
        education_6above.append(countryName[index])


#for cashSD
cashSD = list(data["cashSD"])
countryName = list(taxRevenue["CountryName"])
cashSD_0to3 = []
cashSD_3to5 = []
cashSD_5to6 = []
cashSD_6above = []

for index in range(len(cashSD)):
    if cashSD[index] >= 0 and cashSD[index] <= 3:
        cashSD_0to3.append(countryName[index])
    elif cashSD[index] >3 and cashSD[index] <= 5:
        cashSD_3to5.append(countryName[index])
    elif cashSD[index] >5 and cashSD[index] <= 6:
        cashSD_5to6.append(countryName[index])
    else:
        cashSD_6above.append(countryName[index])

#for health
health = list(data["health"])
countryName = list(taxRevenue["CountryName"])
health_0to3 = []
health_3to5 = []
health_5to6 = []
health_6above = []

for index in range(len(health)):
    if health[index] >= 0 and health[index] <= 3:
        health_0to3.append(countryName[index])
    elif health[index] >3 and health[index] <= 5:
        health_3to5.append(countryName[index])
    elif health[index] >5 and health[index] <= 6:
        health_5to6.append(countryName[index])
    else:
        health_6above.append(countryName[index])


