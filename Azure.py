import requests
import time
import json
import os
from azure.eventhub import EventHubProducerClient, EventData
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from .env file
load_dotenv()

# Connecting to Azure Event Hub
connection_str = os.getenv('AZURE_EVENT_HUB_CONNECTION_STRING')
eventhub_name = os.getenv('AZURE_EVENT_HUB_NAME')

# Sends data to Azure Event Hub
producer = EventHubProducerClient.from_connection_string(
    conn_str=connection_str,
    eventhub_name=eventhub_name
)

# Fetching cryptocurrency prices from CoinGecko API
def get_top_crypto():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,  # Top 10 coins
        'page': 1
    }
    response = requests.get(url, params=params)
    return response.json()

# Main loop to fetch data and send to Azure Event Hub
while True:
    try:
        data = get_top_crypto()
        events = []
        for coin in data:
            payload = {
                "coin": coin["id"],
                "symbol": coin["symbol"],
                "name": coin["name"],
                "price_usd": coin["current_price"],
                "market_cap": coin["market_cap"],
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
            print("Sending:", payload)
            events.append(EventData(json.dumps(payload)))
        
        with producer:
            producer.send_batch(events)
        
        time.sleep(10)  # fetch every 10 seconds
    except Exception as e:
        print("Error:", e)
        time.sleep(5)