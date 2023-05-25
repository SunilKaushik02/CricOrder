import pandas as pd
import streamlit as st
import sqlite3

st.title('Batting order for Cricket')

names=['Ayush',
      'Aman',
      'Amar',
      'Ajitesh',
      'Adithya',
      'Souvik',
      'Sai',
      'Sailaja',
      'Abhiroop',
      'Santhosh',
      'Satthish',
       'Sunil',
       'Sudheer',
       'Ritesh',
       'Anil',
       'Armaan',
      ]

# names=list(map(lambda x: x.lower(), names))

# names.sort()

# print(names,len(names))

name=st.selectbox('Please select your name',
                      options=['Ayush',
      'Aman',
      'Amar',
      'Ajitesh',
      'Adithya',
      'Souvik',
      'Sai',
      'Sailaja',
      'Abhiroop',
      'Santhosh',
      'Satthish',
       'Sunil',
       'Sudheer',
       'Ritesh',
       'Anil',
       'Armaan',
      ])

st.write('You selected:',name)

# name=input('Please enter your first name only:')

# Create a connection to the database
conn = sqlite3.connect('test.db')

# Create a cursor object
cursor = conn.cursor()

# Read the name column
# cursor.execute('DROP TABLE users')

# cursor.execute('CREATE TABLE users (name TEXT)')
cursor.execute('SELECT name FROM users')

results = cursor.fetchall()

if name in names:
    if name in results:
        st.write('You have been assigned a number already!')

    else:
        cursor.execute('INSERT INTO users (name) VALUES (?)',[name])


# Get the results
# Insert some data
# cursor.execute('INSERT INTO users (name, age) VALUES ("Jane Doe", 25)')
conn.commit()

conn.close()

# Create a connection to the database
conn = sqlite3.connect('test.db')

# Create a cursor object
cursor = conn.cursor()

cursor.execute('SELECT name FROM users')

results = cursor.fetchall()
# st.write(results)


# Commit the changes
conn.commit()

# Close the connection
conn.close()

res=pd.DataFrame(results,columns=['Name'])
# print(res)

res['Name']=res['Name'].str.title()

# print(res)

res=res.drop_duplicates('Name').reset_index(drop=True)

res['Order']=[x for x in range(1,res.shape[0]+1)]

st.write(res)

