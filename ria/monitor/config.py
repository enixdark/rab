# -*- coding: utf-8 -*-
#use rabbitadmin or rabbitctl to create new user alert_user
#rabbitctl add_user rpc_user rpcme
#rabbitctl set_permissions rpc_user ".*" ".*" ".*"
USERNAME = "guest"
PASSWORD = "guest"
HOST = "127.0.0.1"
PORT = 5672
PATH = "/"

EXIT_OK = 0
EXIT_WARNING = 1
EXIT_CRITICAL = 2
EXIT_UNKNOWN = 3

EXCHANGE_NAME = "order_processor"
CONSUMER_TAG = "cluster"
QUEUE_WAREHOUSE = "warehouse_carpinteria"
QUEUE_BACKUP = "backup_orders"
ROUTING = "warehouse"
# QUEUE_RESIZE = "resize-pictures"
TYPE = 'direct'