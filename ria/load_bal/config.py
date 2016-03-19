# -*- coding: utf-8 -*-
#use rabbitadmin or rabbitctl to create new user alert_user
#rabbitctl add_user rpc_user rpcme
#rabbitctl set_permissions rpc_user ".*" ".*" ".*"
USERNAME = "guest"
PASSWORD = "guest"
HOST = "127.0.0.1"
PORT = 5672
PATH = "/"

EXCHANGE_NAME = "cluster"
CONSUMER_TAG = "cluster"
QUEUE = "cluster"
# QUEUE_RESIZE = "resize-pictures"
TYPE = 'direct'