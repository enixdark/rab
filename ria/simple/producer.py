#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
from pika import spec
import os, sys
from config import *

credentials = pika.PlainCredentials(USERNAME,PASSWORD)
conn_params = pika.ConnectionParameters(HOST, PORT, PATH, credentials = credentials)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

# only use for version under 2.0.0, version above 2.0.0  
# the method confirm_delivery dont accept callback
# def confirm_handler(frame):
# 	if type(frame.method) == spec.Confirm.SelectOk:
# 		print "channel in 'confirm' mode"
# 	elif type(frame.method) == spec.Basic.Nack:
# 		if frame.method.delivery_tag in msg_ids:
# 			print "message lost"
# 	elif type(frame.method) == spec.Basic.Ack:
# 		if frame.method.delivery_tag in msg_ids:
# 			print 'Confir received'
# 			msg_ids.remove(frame.method.delivery_tag)

channel.exchange_declare(exchange = EXCHANGE_NAME, type = "direct",
						passive = False, durable = True, auto_delete = False)

# channel.confirm_delivery(callback = confirm_handler)
# msg_ids = []

channel.confirm_delivery()
msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"
print 'sent message %s to %s' % (msg, EXCHANGE_NAME)
# msg_ids.append(len(msg_ids) + 1)
channel.basic_publish(body = msg, exchange=EXCHANGE_NAME, properties = msg_props,
	routing_key=ROUTING)
channel.close()