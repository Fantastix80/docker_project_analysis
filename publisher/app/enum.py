import os
from enum import Enum


class EnvironmentVariables(str, Enum):
    KAFKA_TOPIC_NAME = 'topic_test'
    KAFKA_SERVER = 'kafka'
    KAFKA_PORT = '29092'

    def get_env(self, variable=None):
        return os.environ.get(self, variable)
