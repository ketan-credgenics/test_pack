#importing libraries
import pandas as pd
from sqlalchemy import create_engine
import sys
import time

#Understand Variables:
#engine: connection to teh database
#table_nm: mention the table name 
#company_id: For which company you need the data
#comm_mode: What kind of communication you want, eg. IVR, whatsapp, etc
#filtercond: Filtering a json key, format >>> comm_dict->>'vendor' = 'yellow_messenger'

engine = create_engine(
    'postgresql://piyush_read:fvhjdffegjd2wcddc@prod-recovery-read.cnzlch7wyuxy.ap-south-1.rds.amazonaws.com:5432/recovery_service_db'
)
table_nm = 'communication'
comapny_id = 'f30dcf9d-d0b9-422a-ae30-f426165a65ab'
comm_mode = 'whatsapp'
filtercond = "comm_dict->>'vendor' = 'yellow_messenger'"


def readData(engine, table_nm, company_id, comm_mode, filtercond = ""):
    query = "SELECT * FROM " + table_nm + " WHERE company_id = '" + company_id + "' and lower(type_of_comm) = '" + comm_mode.lower() + "'"
    if filtercond != "": #if we want to filter the JSON
         query = query + " and " + filtercond
            
    df = pd.read_sql_query(query, con = engine)
    time.wait(10)
    df_norm = pd.concat([df[['company_id', 'type_of_comm']], pd.json_normalize(df['comm_dict'])], axis = 1)
    
    return df_norm
