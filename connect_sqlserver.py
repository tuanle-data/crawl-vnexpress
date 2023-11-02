import pyodbc
from vnexpress import get_news, get_sports_news

def connect_to_sql_server(server, database, username):
    try:
        # Define the connection string for Windows Authentication
        connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;UID={username}"

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Return the connection and cursor
        return connection, cursor
    except Exception as e:
        print(f"Error: {e}")
        return None, None
    
def insert_data_into_sql_server(server, database, username, table_name, data):
    try:
        # Define the connection string
        connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;UID={username}"

        # Establish a connection to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Construct the SQL INSERT statement
        # insert_sql = f"INSERT INTO {table_name} (Title, Link) VALUES (?, ?)"

        # Construct the SQL MERGE statement
        merge_sql = f"""
        MERGE INTO {table_name} AS Target
        USING (VALUES (?, ?)) AS Source (title, link)
        ON Target.title = Source.title
        WHEN MATCHED THEN
            UPDATE SET Target.link = Source.link  
        WHEN NOT MATCHED THEN
            INSERT (title, link) VALUES (Source.title, Source.link);
        """

        # Iterate through the data and execute the INSERT statement for each tuple
        for item in data:
            # cursor.execute(insert_sql, (item[0], item[1]))
            cursor.execute(merge_sql, (item[0], item[1]))
        
        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Data successfully inserted into the SQL Server table.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
server_name = 'TPP-LAPTOP-080\SQLEXPRESS'
user = 'TPP-LAPTOP-080\Installer'
database_name = 'AdventureWorks2022'
table_name = "[dbo].[VnExpress]"


connection, cursor = connect_to_sql_server(server_name, database_name, user)

result = get_sports_news()

insert_data_into_sql_server(server=server_name, database=database_name, username=user, table_name=table_name, data=result)
