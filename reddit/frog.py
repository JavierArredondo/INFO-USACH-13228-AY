from confluent_kafka import Consumer
import pickle

CONSUMER_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'testo',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(CONSUMER_CONFIG)

consumer.subscribe(['reddit'])

while True:
    msg = consumer.poll(1)
    if msg:
        data = pickle.loads(msg.value())
        print(msg, data)
        # Do something with data
