import boto3 
from datetime import datetime
import calendar
from tabulate import tabulate
import mysql.connector
from mysql.connector import Error 

def insert_data(project_name, key_id, secret):
    try: 
        connection = mysql.connector.connect(host="127.0.0.1", user="boto3ce",database="boto3ce" ,passwd="password", port="3307")
        if connection.is_connected():
            db_Info = connection.get_server_info()
            #print("Connected to MySql Server Version", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            #print("You're Connected to database:", record)
            create_table = ("CREATE TABLE if not exists aws_accounts (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, project_name varchar(150) NOT NULL, key_id varchar(150) NOT NULL, secret varchar(150) NOT NULL) ")
            result = cursor.execute(create_table)
            print("aws_account has been sucessfully created")
            insert_query = ("INSERT INTO aws_accounts(project_name, key_id, secret)" "VALUES(%s, %s, %s)")
            insert_data = (project_name, key_id, secret)
            print(insert_data)
            cursor.execute(insert_query, insert_data)
            print("Record inserted successfully into aws_table")
            connection.commit()

    except Error as e:
        print("Error while connecting to MySql", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySql connection is closed")

def input_data():
    project_name = input("Enter the Name of the project:")
    key_id = input("Enter the AWS Access Key ID:")
    secret = input("Enter the AWS Secred Key:")
    return project_name, key_id, secret
    insert_data(project_name, key_id, secret)

def register():
    return_data = input_data()
    project_name = return_data[0] 
    key_id = return_data[1]
    secret = return_data[2]
    insert_data(project_name, key_id, secret)

def view():
        try: 
            connection = mysql.connector.connect(host="127.0.0.1", user="boto3ce",database="boto3ce" ,passwd="password", port="3307")
            if connection.is_connected():
                db_Info = connection.get_server_info()
                #print("Connected to MySql Server Version", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                #print("You're Connected to database:", record)
                print()
                project_name_input = input()
                print()
                sql_select_query = "SELECT * FROM aws_accounts where project_name = %s"
                cursor.execute(sql_select_query, (project_name_input, ))
                record = cursor.fetchall()
                for row in record:
                    id = row[0]
                    project = row[1]
                    key = row[2]
                    secret = row[3]
   
                year = input("Enter the Year:")
                year_int = int(year)
                print()
                print("List of months: JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'")
                print()
                month_name = input("Enter the Month:")
                print()
                datetime_object = datetime.strptime(month_name, "%b")
                month_number = datetime_object.month   
                month_number_int = int(month_number)

                #print (calendar.month(year_int,month_number_int))
                num_days = calendar.monthrange(year_int, month_number_int)
                first_day = datetime(year_int, month_number_int, 1)
                last_day = datetime(year_int, month_number_int, num_days[1])

                start = first_day.strftime('%Y-%m-%d')
                end = last_day.strftime('%Y-%m-%d')
                #print (start)
                #print (end)
                client = boto3.client(
                    'ce',
                    aws_access_key_id = key,
                    aws_secret_access_key = secret
                )
                response = client.get_cost_and_usage(
                TimePeriod = {
                    'Start': start, 
                    'End': end
                }, 
                Granularity='MONTHLY',
                Metrics=['UnblendedCost', 'AmortizedCost' ]
                )
                unblendedcost = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
                #print(unblendedcost)
                print(tabulate([[year,project,month_name.upper(),'Unblended Cost', unblendedcost  ]], headers=['Year','Project','Month','Cost Type','Cost in USD'], tablefmt='orgtbl'))       
        except Error as e:
            print("Error while connecting to MySql", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def main():
    print (f"Please Select the Appropriate Option\n 1. Register A New Project\n 2. View Details of Existing Project")
    option = int(input ())
    if option == 1:
        register()
    if option == 2:
        view()
    else:
        print("Please enter the appropriate options. Thank you.")
if __name__ == '__main__':
    main()
