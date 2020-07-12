from confluent_kafka import Consumer
import logging
import pickle

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

CONSUMER_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'testo',
    'auto.offset.reset': 'earliest',
}


consumer = Consumer(CONSUMER_CONFIG)
consumer.subscribe(['weather'])
logging.info("Subscribed to weather")

while True:
    msg = consumer.poll(2)
    if msg:
        data = pickle.loads(msg.value())
        logging.info(f"Consuming {data['id']}")
        # Do something with data
