# -*- coding: utf-8 -*-
#use rabbitadmin or rabbitctl to create new user alert_user
#rabbitctl add_user alert_user alertme
#rabbitctl set_permissions alert_user ".*" ".*" ".*"
USERNAME = "alert_user"
PASSWORD = "alertme"
HOST = "127.0.0.1"
PORT = 5672
PATH = "/"

EXCHANGE_NAME = "upload-pictures"
CONSUMER_TAG = ""
QUEUE = "add-points"
QUEUE_RESIZE = "resize-pictures"
TOPIC = 'fanout'