import boto3 
from datetime import datetime
from dateutil.relativedelta import *
import mysql.connector
from mysql.connector import Error 



connection = mysql.connector.connect(host="127.0.0.1", user="ceautomation",database="ceautomation" ,passwd="c27sdfAk99HT6B", port="3307")

db_Info = connection.get_server_info()
#print("Connected to MySql Server Version", db_Info)
cursor = connection.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
#print("You're Connected to database:", record)
project_name_input = input("Enter the Name of the Project:")
sql_select_query = "SELECT * FROM aws_accounts where project_name = %s"
cursor.execute(sql_select_query, (project_name_input, ))
record = cursor.fetchall()
for row in record:
    id = row[0]
    project = row[1]
    key = row[2]
    secret = row[3]
now = datetime.utcnow()
start_date = now.strftime('%Y-%m-%d')
            #print(start_date)

month_1 = now + relativedelta(months=+1)
end_date = month_1.strftime('%Y-%m-%d')
            #print(end_date)
client = boto3.client(
    'ce',
    aws_access_key_id = key,
    aws_secret_access_key = secret
    )
response_forecast = client.get_cost_forecast(
    TimePeriod = {
        'Start': start_date, 
        'End': end_date
        }, 
        Granularity='MONTHLY',
        Metric='AMORTIZED_COST'
        )
forecast= response_forecast['ForecastResultsByTime'][0]['MeanValue']
print(forecast)
