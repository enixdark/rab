#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
from config import *


credentials = pika.PlainCredentials(USERNAME,PASSWORD)
conn_params = pika.ConnectionParameters(HOST,PORT,PATH, credentials = credentials)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

channel.exchange_declare(exchange = EXCHANGE_NAME, type ="direct",
	passive=False, durable = True, auto_delete = False)

channel.queue_declare(queue = QUEUE_NAME)
channel.queue_bind(queue = QUEUE_NAME, exchange=EXCHANGE_NAME, routing_key=ROUTING)

def msg_consumer(channel, method, header, body):
	channel.basic_ack(delivery_tag=method.delivery_tag),
	if body == "quit":
		channel.basic_cancel(consumer_tag=CONSUMER_TAG)
		channel.stop_consuming()
	else:
		print body

channel.basic_consume(msg_consumer, queue=QUEUE_NAME, consumer_tag=CONSUMER_TAG)
print 'server has started at %s:%d' % (HOST,PORT)
channel.start_consuming()