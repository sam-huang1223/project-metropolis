# Imports the Google Cloud client library
from google.cloud import datastore

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'auth/Project Metropolis-1978d40b3e40.json'

# Instantiates a client
datastore_client = datastore.Client()

# The kind for the new entity
kind = 'Task'
# The name/ID for the new entity
name = 'sampletask1'
# The Cloud Datastore key for the new entity
task_key = datastore_client.key(kind, name)

# Prepares the new entity
task = datastore.Entity(key=task_key)
task['description'] = 'Buy milk'

# Saves the entity
datastore_client.put(task)

print('Saved {}: {}'.format(task.key.name, task['description']))


query = datastore_client.query(kind='Task')
query.add_filter('done', '=', False)
#query.add_filter('name', '=', 'task1')
#query.add_filter('priority', '>=', 4)
#query.order = ['-priority']

results = list(query.fetch())
print(results)