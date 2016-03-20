import sys, json
import time, traceback
from config import *
from rb import AMQP

def msg_rcvd(channel, method, header, body):
	message = json.loads(body)
	print "Received order %(ordernum)d for %(type)s." % message
	channel.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == "__main__":
	amqp = AMQP(USERNAME,PASSWORD,"Erlang",5676,PATH)
	amqp.connect()
	amqp.receive(exchange = EXCHANGE_NAME, queue = QUEUE_WAREHOUSE, _type = TYPE,
				 binding = True, routing_key  = ROUTING)
	amqp.basic_consume(callback = msg_rcvd, queue = QUEUE_WAREHOUSE, 
		no_ack = False, consumer_tag = CONSUMER_TAG)
	amqp.startConsumer()