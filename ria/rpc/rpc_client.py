# -*- coding: utf-8 -*-
from rb import AMQP
from config import *
import time
import json
import pika

def reply(channel, method, header, body):
	print 'Receive rpc server replies'
	channel.close()

if __name__ == "__main__":
	amqp = AMQP(USERNAME,PASSWORD,HOST,PORT,PATH)
	amqp.connect()
	result = amqp.connect().queue_declare(exclusive = True, auto_delete = True)
	msg = json.dumps({"client_name": "RPC client", "time": time.time()})
	msg_props = pika.BasicProperties()
	msg_props.reply_to=result.method.queue
	amqp.connect().basic_publish(exchange = EXCHANGE_NAME, 
		body = msg, properties = msg_props, routing_key = "ping")
	print "Sent 'ping' RPC call. Waiting for reply..." + result.method.queue
	amqp.basic_consume(callback = reply, queue = result.method.queue, 
		consumer_tag = result.method.queue)
	amqp.startConsumer()


