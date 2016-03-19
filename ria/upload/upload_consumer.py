from config import *
from rb import AMQP
import json

def callback(channel, method, header, body):
	check = True
	if body == "quit":
		channel.basic_cancel(consumer_tag=CONSUMER_TAG)
		channel.stop_consuming()
		check = False
	data = json.loads(body)
	channel.basic_ack(delivery_tag=method.delivery_tag)
	return (check,data)

def add_points_to_user(channel, method, header, body):
	(check,result) = callback(channel,method,header,body)
	if check:
		print 'send a point to user: %s' % result['user_id']


def resize_picture(channel, method, header, body):
	(check,result) = callback(channel,method,header,body)
	if check:
		print 'resize image %s at %s' % (result['image_id'],result['image_path']) 

if __name__ == "__main__":
	amqp = AMQP(USERNAME,PASSWORD,HOST,PORT,PATH)
	amqp.connect()
	amqp.receive(exchange = EXCHANGE_NAME, queue = QUEUE, _type = TOPIC, binding = True)
	amqp.receive(exchange = EXCHANGE_NAME, queue = QUEUE_RESIZE, _type = TOPIC, binding = True)
	
	amqp.basic_consume(callback = add_points_to_user, queue = QUEUE, consumer_tag = CONSUMER_TAG)
	amqp.basic_consume(callback = resize_picture, queue = QUEUE_RESIZE, consumer_tag = CONSUMER_TAG)
	
	amqp.startConsumer()
	