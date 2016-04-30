import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

var1 = pd.read_csv("API_GC/API_GC.TAX.TOTL.GD.ZS_DS2_en_v2.csv", skiprows = 4)
var1.drop(var1.columns[range(4,52)], axis=1, inplace=True)
var1.drop(var1.columns[[4, 5, 7, 8, 9, 10, 11, 12]], axis=1, inplace=True)

var2.drop(var2.columns[range(4,52)], axis=1, inplace=True)
var2.drop(var2.columns[[4, 5, 7, 8, 9, 10, 11, 12]], axis=1, inplace=True)

var3.drop(var3.columns[range(4,52)], axis=1, inplace=True)
var3.drop(var3.columns[[4, 5, 7, 8, 9, 10, 11, 12]], axis=1, inplace=True)

var1.rename(columns = {"2010": "taxRevenue"}, inplace = True)
var1["education"] = var2["2010"]
var1["cashSurplusDeficit"] = var3["2010"]

var1.drop(var1.columns[range(2,4)], axis = 1, inplace = True)
var1.rename(columns={"Country Name": "CountryName"}, inplace=True)
var1.rename(columns={"Country Code": "CountryCode"}, inplace=True)

engine = create_engine('mysql+mysqlconnector://root@localhost:3306/fov', echo=False)
cnx = engine.raw_connection()
var1.to_sql(name='masterdata', con=cnx, if_exists = 'append', flavor = "mysql", index=False)