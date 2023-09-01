import sqlite3
import pandas as pd
import os

# Replace 'wine_database.db' with the actual database file path
database_file = 'wine_database.db'

# Check if the file exists before deleting
if os.path.exists(database_file):
    os.remove(database_file)
    print(f"{database_file} has been deleted.")
else:
    print(f"{database_file} does not exist.")

# Create a connection to the SQLite database (or connect to your chosen database system)
conn = sqlite3.connect('wine_database.db')
cursor = conn.cursor()

#Create the 'wines' table
cursor.execute('''
    CREATE TABLE red_wine (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT,
        region TEXT,
        winery TEXT,
        price REAL,
        rating REAL,
        year INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE white_wine (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT,
        region TEXT,
        winery TEXT,
        price REAL,
        rating REAL,
        year INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE sparkling_wine (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT,
        region TEXT,
        winery TEXT,
        price REAL,
        rating REAL,
        year INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE rose_wine (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT,
        region TEXT,
        winery TEXT,
        price REAL,
        rating REAL,
        year INTEGER
    )
    
''')

#Read the data from each csv and drop unneeded information
red_df = pd.read_csv('Resources/Red.xls', encoding='iso-8859-1')
red_df = red_df[red_df.Year != "N.V."]
red_df = red_df.drop(columns = "NumberOfRatings")
red_df.columns.values[0] = 'Name'

white_df = pd.read_csv('Resources/White.csv', encoding='iso-8859-1')
white_df = white_df[white_df.Year != "N.V."]
white_df = white_df.drop(columns = "NumberOfRatings")
white_df.columns.values[0] = 'Name'

rose_df = pd.read_csv('Resources/Rose.csv', encoding='iso-8859-1')
rose_df = rose_df[rose_df.Year != "N.V."]
rose_df = rose_df.drop(columns = "NumberOfRatings")
rose_df.columns.values[0] = 'Name'

sparkling_df = pd.read_csv('Resources/Sparkling.csv', encoding='iso-8859-1')
sparkling_df = sparkling_df[sparkling_df.Year != "N.V."]
sparkling_df = sparkling_df.drop(columns = "NumberOfRatings")
sparkling_df.columns.values[0] = 'Name'

#Print the dataframes to confirm integrity
print(red_df)
print(white_df)
print(rose_df)
print(sparkling_df)

#Move each dataframe into the database
red_df.to_sql('red_wine', conn, if_exists='replace', index=False)
white_df.to_sql('white_wine', conn, if_exists='replace', index=False)
rose_df.to_sql('rose_wine', conn, if_exists='replace', index=False)
sparkling_df.to_sql('sparkling_wine', conn, if_exists='replace', index=False)

#Query each table to make sure the data was moved correctly
query = 'SELECT * FROM red_wine'
red_query = pd.read_sql_query(query, conn)
print(red_query)

query = 'SELECT * FROM white_wine'
white_query = pd.read_sql_query(query, conn)
print(white_query)

query = 'SELECT * FROM rose_wine'
rose_query = pd.read_sql_query(query, conn)
print(rose_query)

query = 'SELECT * FROM sparkling_wine'
sparkling_query = pd.read_sql_query(query, conn)
print(sparkling_query)

# Commit changes and close the connection
conn.commit()
conn.close()