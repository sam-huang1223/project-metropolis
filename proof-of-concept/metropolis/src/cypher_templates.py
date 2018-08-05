# TODO write this for adding relationships then update database.py code

def add_relationship(node1_var, node1, node1_properties):
    return "MERGE ({node1_var}:{node1}{name:'Sam Huang'})\n" + \
    "MERGE ({node2_var}:Event{name:'B tingz'})\n" + \
    "MERGE (student)-[:ATTENDED]->(event)".format(
        node1_var=node1_var,
        node1=node1,

        node2_var=node2_var,
        # Find a way to add dynamic number of properties
    )

