#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
from config import *

credentials = pika.PlainCredentials(USERNAME,PASSWORD)
conn_params = pika.ConnectionParameters(HOST,PORT,PATH,credentials=credentials)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

channel.exchange_declare(exchange = LOG_EXCHANGE_NAME, exchange_type="direct",
				durable = True, passive = False, auto_delete = False)
# channel.exchange_declare(exchange = MSG_LOG_EXCHANGE_NAME, exchange_type="direct",
# 				durable = True, passive = False, auto_delete = False)
# channel.exchange_declare(exchange = ERROR_LOG_EXCHANGE_NAME, exchange_type="direct",
# 				durable = True, passive = False, auto_delete = False)

channel.queue_declare(queue = LOG_QUEUE_NAME, False, True, False, False)
channel.queue_declare(queue = MSG_LOG_QUEUE_NAME, False, True, False, False)
channel.queue_declare(queue = ERROR_LOG_QUEUE_NAME, False, True, False, False)

channel.queue_bind(exchange = LOG_QUEUE_NAME, queue = ERROR_LOG_QUEUE_NAME, 
	routing_key = "error.msg-inbox")
channel.queue_bind(exchange = LOG_QUEUE_NAME, queue = MSG_LOG_EXCHANGE_NAME, 
	routing_key = "*.msg-inbox")