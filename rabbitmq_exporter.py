from prometheus_client import start_http_server, Gauge
import requests
import os
import time

# Define environment variables
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')

# Define Prometheus metrics
METRIC_MESSAGES = Gauge('rabbitmq_individual_queue_messages', 'Total count of messages', ['host', 'vhost', 'name'])
METRIC_READY = Gauge('rabbitmq_individual_queue_messages_ready', 'Messages ready to be delivered', ['host', 'vhost', 'name'])
METRIC_UNACK = Gauge('rabbitmq_individual_queue_messages_unacknowledged', 'Unacknowledged messages', ['host', 'vhost', 'name'])

def fetch_rabbitmq_metrics():
    """Fetch metrics from RabbitMQ API and expose them to Prometheus."""
    url = f"http://{RABBITMQ_HOST}:15672/api/queues"
    auth = (RABBITMQ_USER, RABBITMQ_PASSWORD)
    
    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        queues = response.json()
        
        for queue in queues:
            host = RABBITMQ_HOST
            vhost = queue['vhost']
            name = queue['name']
            METRIC_MESSAGES.labels(host, vhost, name).set(queue.get('messages', 0))
            METRIC_READY.labels(host, vhost, name).set(queue.get('messages_ready', 0))
            METRIC_UNACK.labels(host, vhost, name).set(queue.get('messages_unacknowledged', 0))
    except Exception as e:
        print(f"Error fetching RabbitMQ metrics: {e}")

if __name__ == '__main__':
    start_http_server(8000)  # Expose metrics on port 8000
    while True:
        fetch_rabbitmq_metrics()
        time.sleep(30)
