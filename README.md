#  Real-Time Crypto Price Stream to Azure Event Hub

This Python project fetches real-time cryptocurrency price data from the [CoinGecko API](https://www.coingecko.com/en/api) and streams it to [Azure Event Hub](https://learn.microsoft.com/en-us/azure/event-hubs/) every 10 seconds. This setup is ideal for real-time analytics, dashboards, or big data pipelines.

---

##  Features

- Fetches top 10 cryptocurrencies by market cap.
- Streams live data to Azure Event Hub.
- Easy to configure using environment variables.
- Lightweight and extensible.

---

##  Getting Started

### Prerequisites

- Python 3.8+
- An Azure Event Hub namespace and hub created.
- A `.env` file with your Azure credentials.

### Install Dependencies

```bash
pip install -r requirements.txt
