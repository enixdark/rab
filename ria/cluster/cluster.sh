#!/bin/bash
# please stop all rabbitmq node is running
# disable all plugins for each node
# you can use reset node through rabbitmqctl or rabbitmqadmin or rm mnesia db from $HOME_RABBITMQ/var/lib/mnesia

#ensure that no one use port, and use -detached to start nodes without save pid
RABBITMQ_NODE_PORT=5672 RABBITMQ_NODENAME=rabbit rabbitmq-server -detached
RABBITMQ_NODE_PORT=5673 RABBITMQ_NODENAME=rabbit1 rabbitmq-server -detached
RABBITMQ_NODE_PORT=5674 RABBITMQ_NODENAME=rabbit2 rabbitmq-server -detached

rabbitmqctl -n rabbit@HOST_NAME stop_app
rabbitmqctl -n rabbit@HOST_NAME reset
rabbitmqctl -n rabbit@HOST_NAME start_app

rabbitmqctl -n rabbit1@HOST_NAME stop_app
rabbitmqctl -n rabbit1@HOST_NAME reset

rabbitmqctl -n rabbit2@HOST_NAME stop_app
rabbitmqctl -n rabbit1@HOST_NAME reset

#reset node for node that become master
rabbitmqctl -n rabbit1@HOST_NAME join_cluster rabbit@HOST_NAME
rabbitmqctl -n rabbit2@HOST_NAME join_cluster rabbit@HOST_NAME

rabbitmqctl -n rabbit1@HOST_NAME start_app
rabbitmqctl -n rabbit2@HOST_NAME start_app
