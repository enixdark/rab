# -*- coding: utf-8 -*-
#use rabbitadmin or rabbitctl to create new user alert_user
#rabbitctl add_user rpc_user rpcme
#rabbitctl set_permissions rpc_user ".*" ".*" ".*"
USERNAME = "rpc_user"
PASSWORD = "rpcme"
HOST = "127.0.0.1"
PORT = 5672
PATH = "/"

EXCHANGE_NAME = "rpc"
CONSUMER_TAG = "ping"
QUEUE = "ping"
# QUEUE_RESIZE = "resize-pictures"
TYPE = 'direct'