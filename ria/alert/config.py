# -*- coding: utf-8 -*-
#use rabbitadmin or rabbitctl to create new user alert_user
#rabbitctl add_user alert_user alertme
#rabbitctl set_permissions alert_user ".*" ".*" ".*"
USERNAME = "alert_user"
PASSWORD = "alertme"
HOST = "127.0.0.1"
PORT = 5672
PATH = "/"

EXCHANGE_NAME = "alerts"

QUEUE_CRITICAL = "critical"
ROUTING_CRITICAL = "*critiacal.*"

QUEUE_RATE = "rate_limit"
ROUTING_RATE = "*.rate_limit"

CONSUMER_TAG = "hello-consumer"

TOPIC = "topic"

EMAIL_RECIPS = ["cqshinn92@gmail.com"]
ALERT_EMAIL = "cqshinn92@gmail.com"
EMAIL = "cqshinn92@gmail"

USER_EMAIL = ""
PASSWORD_EMAIL = ""