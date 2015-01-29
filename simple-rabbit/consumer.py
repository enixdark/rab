import pika
from configs import CONFIG
EXCHANE_DB = 'hello-exchange'
TYPE = 'direct'
RKEY = 'hola'
QUEUE = 'hello-queue'
CTAG = 'hello-consumer'
credentials = pika.PlainCredentials(CONFIG['username'],CONFIG['password'])
conn_params = pika.ConnectionParameters(CONFIG['host'],credentials=credentials)

conn_broken = pika.BlockingConnection(conn_params)

channel = conn_broken.channel()
channel.exchange_declare(exchange = EXCHANE_DB,type = TYPE,
						passive=False,durable=True,auto_delete=False)

channel.queue_declare(queue=QUEUE)
channel.queue_bind(queue=QUEUE,exchange=EXCHANE_DB,routing_key=RKEY)
def message_consumer(channel,method,header,body):
	channel.basic_ack(delivery_tag=method.delivery_tag)
	if body == "quit":
		channel.basic_cancel(consumer_tag= CTAG)
		channel.stop_consuming()
	else:
		print "consumer receve a %s message " % body
	return
channel.basic_consume(message_consumer,queue=QUEUE,consumer_tag=CTAG)
print "start consumer ......."
channel.start_consuming()
