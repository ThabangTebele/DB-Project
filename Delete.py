import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from .env file
load_dotenv()

# Your Cosmos DB credentials
url = os.getenv('COSMOS_DB_URL')
key = os.getenv('COSMOS_DB_KEY')
database_name = os.getenv('COSMOS_DB_DATABASE_NAME')
container_name = os.getenv('COSMOS_DB_CONTAINER_NAME')

client = CosmosClient(url, credential=key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Loop through and delete all documents
for item in container.read_all_items():
    container.delete_item(item, partition_key=item['coin'])

print("All documents deleted.")
