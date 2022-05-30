# coding: utf-8
""" 
@author: lipeng
@file: 0090_kafkademo.py 
@time: 2019/11/28
"""
import time

import confluent_kafka

KAFKA_CONF = {
    'bootstrap.servers': "localhost:9092",
    'group.id': '1',
    'auto.offset.reset': 'earliest',
    'fetch.message.max.bytes': '314572800',
    'enable.auto.commit': 'false',

}

# p = confluent_kafka.Producer(KAFKA_CONF)
# n=200000
# while True:
#     p.produce("my-replicated-topic",value=str(n))
#     n+=1


c = confluent_kafka.Consumer(KAFKA_CONF)
c.subscribe(["my-replicated-topic", ])
while True:
    time.sleep(2)
    try:
        msg = c.poll(timeout=5.0)
        if msg is None:
            time.sleep(0.1)
            continue
        elif msg.error():
            print("Kafka consumer error: {}"
                  .format(msg.error()))
            continue

        value = msg.value()
        print(value)

    except Exception as err:
        print('Unexpected kafka consumer: {!r}'.format(err))
        continue

