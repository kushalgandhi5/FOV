import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

Metadata = pd.read_csv("Metadata_Country_API_GC.TAX.TOTL.GD.ZS_DS2_en_v2.csv")

Metadata.rename(columns={"Country Code": "CountryCode"}, inplace=True)


engine = create_engine('mysql+mysqlconnector://root@localhost:3306/fov', echo=False)
cnx = engine.raw_connection()
Metadata.to_sql(name='masterMetadata', con=cnx, if_exists = 'append', flavor = "mysql", index=False)


