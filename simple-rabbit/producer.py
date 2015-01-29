import pika
import sys
from configs import CONFIG

EXCHANE_DB = 'hello-exchange'
TYPE = 'direct'
RKEY = 'hola'
credentials = pika.PlainCredentials(CONFIG['username'],CONFIG['password'])
conn_params = pika.ConnectionParameters(CONFIG['host'],credentials = credentials)

conn_broken = pika.BlockingConnection(conn_params)

channel = conn_broken.channel()

channel.exchange_declare(exchange= EXCHANE_DB,type=TYPE,passive=False,
									durable=True,auto_delete=False)

try:
	message = sys.argv[1]
	message_props = pika.BasicProperties()
	message_props.content_type = "text/plain"
	channel.basic_publish(body=message,exchange=EXCHANE_DB,routing_key=RKEY)
	print "start send a message %s from producer to consumer" % message

except:
	print sys.exc_info()
