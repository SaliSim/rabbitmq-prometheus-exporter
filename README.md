# rabbitmq-prometheus-exporter
A Prometheus exporter written in Python to expose RabbitMQ queue metrics.

## Metrics
- `rabbitmq_individual_queue_messages{host, vhost, name}`
- `rabbitmq_individual_queue_messages_ready{host, vhost, name}`
- `rabbitmq_individual_queue_messages_unacknowledged{host, vhost, name}`

## Prerequisites
- Python 3.x
- RabbitMQ Management Plugin enabled

## Usage
1. Set environment variables:
   ```bash
   export RABBITMQ_HOST=<your_rabbitmq_host>
   export RABBITMQ_USER=<your_rabbitmq_user>
   export RABBITMQ_PASSWORD=<your_rabbitmq_password>
