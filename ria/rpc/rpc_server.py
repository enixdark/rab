# -*- coding: utf-8 -*-
from rb import AMQP
from config import *
import json


def ping(channel, method, header, body):
	channel.basic_ack(delivery_tag = method.delivery_tag)
	msg = json.loads(body)
	print 'received ping ' + header.reply_to
	channel.basic_publish(body="Pong " + str(msg['time']), 
		exchange = "", routing_key = header.reply_to)

if __name__ == "__main__":
	amqp = AMQP(USERNAME,PASSWORD,HOST,PORT,PATH)
	amqp.connect()
	amqp.receive(exchange = EXCHANGE_NAME, queue = QUEUE, _type = TYPE, binding = True,
		routing_key = "ping")
	amqp.basic_consume(callback = ping, queue = QUEUE, 
		consumer_tag = CONSUMER_TAG)
	print "Server has started, waiting for RPC calls..."
	amqp.startConsumer()

