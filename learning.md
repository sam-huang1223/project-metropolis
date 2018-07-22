# Hosting in the Cloud

GrapheneDB

https://app.graphenedb.com/welcome

OR Google Kubernetes 

https://medium.com/google-cloud/running-neo4j-with-hosted-kubernetes-in-google-cloud-b479e87b74c0

OR Google Compute Engine

Single VM Instance Instructions: https://neo4j.com/developer/neo4j-cloud-google-image/
VM Instances Dashboard: Compute Engine -> VM Instances
Firewall configuration: VPC Network -> Firewall Rules

# Access Web Portal

Go to Graphene portal, click overview tab, then scroll down to Tools, then click Neo4j Browser

To solve issue with WebSocket Error: https://github.com/neo4j/neo4j-browser/issues/509#issuecomment-301628740

# Tableau Connection

See https://github.com/neo4j-contrib/neo4j-tableau

And

https://neo4j-contrib.github.io/neo4j-tableau/website/Neo4jWdc2.html

Connect to Server -> Web Data Connector -> Go to link above -> Define Cypher queries for building table (that will be imported into Tableau)

Someone built an interface that makes it easy to import data from graph-based databases in the form of traditional tables!


# Misc

https://neo4j.com/graphacademy/online-training/getting-started-graph-databases-using-neo4j/part-3/

https://neo4j.com/developer/cypher-query-language/#_find_someone_in_your_network_who_can_help_you_learn_neo4j

https://neo4j.com/blog/dark-side-neo4j-worst-practices/

Alternatives: https://www.tigergraph.com/product/, or TitanDB w/Cassandra