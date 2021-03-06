# see learning.md for notes
# see setup.py for required packages

# virtual env is metropolis

from py2neo import Graph
from config import CREDENTIALS, DATABASE

def execute_cypher(cypher_query):
    graph = Graph(DATABASE['HTTPS'], user=CREDENTIALS['user'], password=CREDENTIALS['password'])
    return graph.run(cypher_query)

def print_query(query):
    for result in query:
        print(result)