## To get all data:
    MATCH(n) RETURN n

## To delete all data:
    MATCH(n) DETACH DELETE n

## To get students who attended every event:

    MATCH (s:Student)-[r:ATTENDED]->(e:Event) 
    RETURN e, COLLECT(s) AS num
    ORDER BY SIZE(num) DESC LIMIT 10

## To get number of students who attended every event:

    MATCH (s:Student)-[r:ATTENDED]->(e:Event) 
    RETURN e, COUNT(s) AS num
    ORDER BY num DESC LIMIT 10

*https://neo4j.com/developer/kb/understanding-how-merge-works/