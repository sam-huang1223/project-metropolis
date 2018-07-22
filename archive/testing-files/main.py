"""
Before this code can be run, we need to establish a local proxy connection to the Cloud SQL Database
To invoke an instance of the Cloud SQL Proxy, run below command in the command prompt:
<Cloud SQL executable location> -instance=<Instance Connection Name>=tcp:5432 -credential_file <Credential File Location>
For example:
"./auth/cloud_sql_proxy_x64.exe" -instances=test-205022:us-central1:test1223=tcp:5432 -credential_file "./auth/Test-0b54592d1503.json"

Manage the Google Cloud SQL service here:
https://console.cloud.google.com/sql/instances/test1223/overview?project=test-205022&folder&organizationId&duration=PT1H
"""

import psycopg2

conn = psycopg2.connect(user='postgres', password='samuel1205', host='localhost', port='5432')

cur = conn.cursor()

CREATE = False

if CREATE:
    cur.execute(
    """
    create table jsonData (
        id serial primary key,
        data jsonb
    );
    
    insert into jsonData (data) values (
    '{
      "a": 1,
      "b": 2,
      "c": ["dog","cat","mouse"],
      "d": {
        "x": true
      }
     }
    '::jsonb),
    (
    '{
      "a": 20,
      "b": 40,
      "c": ["fish","cat","rat","hamster"],
      "d": {
        "x": false
      }
     }
    '::jsonb);
    """
    )

cur.execute(
"""
SELECT
  jsonb_extract_path_text(data, 'b') as b,
  jsonb_array_length(data->'c') as numAnimals
FROM 
  jsonData
WHERE
  jsonb_extract_path_text(data->'d', 'x') = 'true'
"""
)

print(cur.fetchall())

cur.close()

conn.commit()
conn.close()














"""
# can access pgweb via http://52.40.90.187

import psycopg2
con=psycopg2.connect(dbname= 'labdb', host='lab.cqhelwt9ed5a.us-west-2.redshift.amazonaws.com',
port= '5439', user= 'master', password= 'Redshift123')

cur = con.cursor()

cur.execute("SELECT COUNT(*) FROM users;")
print(cur.fetchall())
cur.execute("SELECT city, COUNT(*) AS count FROM users WHERE likejazz GROUP BY city ORDER BY count DESC LIMIT 10;")
print(cur.fetchall())

cur.close()
con.close()
"""

