import pandas as pd
from numpy import nan

from .helper import execute_cypher, print_query

def creation_script():
    xl = pd.ExcelFile("../raw-data/QAA-Events-Sign-Ups-2017-2018.xlsx")
    df = xl.parse('Sheet2')

    data = df.to_dict('list')

    for event in data.keys():
        for student in data[event]:
            if student is not nan:
                query = ('MERGE ({node1_var}:{node1}{{name:"{node1_name}"}})\n'
                    'MERGE ({node2_var}:{node2}{{name:"{node2_name}"}})\n'
                    'MERGE ({node1_var})-[r:{relation}]->({node2_var})').format(
                        node1_var = 'student',
                        node1 = 'Student',
                        node1_name = student,
                        node2_var = 'event',
                        node2 = 'Event',
                        node2_name = event,
                        relation = 'ATTENDED'
                    )
                execute_cypher(query)

#The MERGE clause ensures that a pattern exists in the graph.
#Either the pattern already exists, or it needs to be created.

#unique_students = pd.unique(df.values.ravel('K'))  # The argument 'K' tells the method to flatten the array in the order the elements are stored in memory
# 233 unique students + 8 events = 241 nodes

# query to create relationships using MERGE
# Integrate date as property in ATTENDED relationship

def test():
    print_query(execute_cypher('MATCH (n) RETURN n'))

