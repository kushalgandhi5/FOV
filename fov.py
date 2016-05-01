import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

taxRevenue = pd.read_csv("tax revenue/API_GC.TAX.TOTL.GD.ZS_DS2_en_v2.csv", skiprows = 4)
education = pd.read_csv("education expenditure/API_SE.XPD.TOTL.GD.ZS_DS2_en_v2.csv", skiprows=4)
cashSD = pd.read_csv("cash surplus:deficit/API_GC.BAL.CASH.GD.ZS_DS2_en_v2.csv", skiprows=4)
health = pd.read_excel("health/API_SH.XPD.TOTL.ZS_DS2_en_v2-2.xls", skiprows=3)

taxRevenue.drop(taxRevenue.columns[range(4,52)], axis=1, inplace=True)
taxRevenue.drop(taxRevenue.columns[[4, 5, 7, 8, 9, 10, 11, 12]], axis=1, inplace=True)
education.drop(education.columns[range(4,52)], axis=1, inplace=True)
education.drop(education.columns[[4, 5, 7, 8, 9, 10, 11, 12]], axis=1, inplace=True)
cashSD.drop(cashSD.columns[range(4,52)], axis=1, inplace=True)
cashSD.drop(cashSD.columns[[4, 5, 7, 8, 9, 10, 11, 12]], axis=1, inplace=True)
health.drop(health.columns[range(4,52)], axis=1, inplace=True)
health.drop(health.columns[[4, 5, 7, 8, 9, 10, 11]], axis=1, inplace=True)

taxRevenue.rename(columns = {"2010": "taxRevenue"}, inplace = True)
taxRevenue.drop(taxRevenue.columns[range(2,4)], axis=1, inplace=True)

taxRevenue["education"] = education["2010"]
taxRevenue["cashSD"] = cashSD["2010"]
taxRevenue["health"] = health["2010"]
taxRevenue.rename(columns={"Country Code": "CountryCode"}, inplace=True)
taxRevenue.rename(columns={"Country Name": "CountryName"}, inplace=True)
taxRevenue = taxRevenue[["CountryCode", "CountryName", "education", "cashSD", "health", "taxRevenue"]]

engine = create_engine('mysql+mysqlconnector://root@localhost:3306/fov', echo=False)
cnx = engine.raw_connection()
taxRevenue.to_sql(name='masterdata', con=cnx, if_exists = 'append', flavor = "mysql", index=False)



