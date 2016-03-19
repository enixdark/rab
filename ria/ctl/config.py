# -*- coding: utf-8 -*-
USERNAME = "guest"
PASSWORD = "guest"
HOST = "127.0.0.1"
PORT = 5672
PATH = "/"

LOG_EXCHANGE_NAME = "logs-exchange"

LOG_QUEUE_NAME = "log-queue"
MSG_LOG_QUEUE_NAME = "msg-inbox-logs"
ERROR_LOG_QUEUE_NAME = "msg-inbox-error"

CONSUMER_TAG = "hello-consumer"

ROUTING = "fanout"