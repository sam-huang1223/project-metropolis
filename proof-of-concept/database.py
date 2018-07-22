import pandas as pd
from numpy import nan
from helper import execute_cypher, print_query

xl = pd.ExcelFile("")
df = xl.parse('Sheet2')

data = df.to_dict('list')

for element in data[""]:
    if element is not nan:
        print(element)

#unique_students = pd.unique(df.values.ravel('K'))  # The argument 'K' tells the method to flatten the array in the order the elements are stored in memory

# query to create relationships using MERGE
"""
The MERGE clause ensures that a pattern exists in the graph. 
Either the pattern already exists, or it needs to be created.
"""

#print_query(execute_cypher('MATCH (n) RETURN n'))

