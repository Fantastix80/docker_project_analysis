import logging
from json import loads

from app.enum import EnvironmentVariables as EnvVariables

from kafka import KafkaConsumer


def main():
    try:
        # To consume latest messages and auto-commit offsets
        consumer = KafkaConsumer(
            EnvVariables.get_env("KAFKA_TOPIC_NAME"),
            bootstrap_servers=f'{EnvVariables.get_env("KAFKA_SERVER")}:{EnvVariables.get_env("KAFKA_PORT")}',
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
        )
        for message in consumer:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key, message.value))

    except Exception as e:
        logging.info('Connection successful', e)
