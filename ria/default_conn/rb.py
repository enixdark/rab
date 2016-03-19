import pika

DEFAULT_USERNAME = "guest"
DEFAULT_PASSWORD = "lalertme"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5672
DEFAULT_PATH = "/"

class AMQP(object):
	def __init__(self, user = DEFAULT_USERNAME, password = DEFAULT_PASSWORD, 
					   host = DEFAULT_PORT, port = DEFAULT_PORT, vhost = DEFAULT_PATH):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.vhost = vhost

	def connect(self):
		if not self.channel:
			credentials = pika.PlainCredentials(self.user,self.password)
			broker = pika.BlockingConnection(pika.ConnectionParameters(
				self.host,self.port,self.vhost, credentials = credentials))
			self.channel = broker.channel()
		return self.channel

	def receive(self,exchange,queue,tyoe = "direct",passive = False, durable = True
		auto_delete = False, binding = False, routing_key = "*"):
		self.connect().exchange_declare(exchange, passive = passive, durable = durable, 
			auto_delete = auto_delete)
		self.connect().queue_declare(queue, auto_delete = auto_delete)
		if binding:
			self.connect().queue_binding(queue = queue, exchange = exchange, routing_key = routing_key)

	def send(self, exchange, message, passive = False, durable = True
		auto_delete = False, callback = lambda x: pass):
		self.connect().exchange_declare(exchange, passive = passive, durable = durable, 
			auto_delete = auto_delete)
		msg_props = pika.BasicProperties()
		msg_props.content_type = "text/plain"
		self.connect().basic_publish(body = message, exchange=exchange, properties = msg_props,
		routing_key=ROUTING)

	def startConsumer(self,queue = queue, msg_consumer = msg_consumer, callback = lamda m: pass):
		self.connect().basic_consume(callback = callback, 
			queue=queue, consumer_tag = consumer_tag)
		print 'server has started at %s:%d' % (HOST,PORT)
		self.connect().start_consuming()