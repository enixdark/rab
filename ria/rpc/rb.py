import pika

DEFAULT_USERNAME = "guest"
DEFAULT_PASSWORD = "guest"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5672
DEFAULT_PATH = "/"

default_callback = lambda x: None

class AMQP(object):
	def __init__(self, user = DEFAULT_USERNAME, password = DEFAULT_PASSWORD, 
					   host = DEFAULT_PORT, port = DEFAULT_PORT, vhost = DEFAULT_PATH):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.vhost = vhost
		self.channel = None

	def connect(self):
		if self.channel is None:
			credentials = pika.PlainCredentials(self.user,self.password)
			broker = pika.BlockingConnection(pika.ConnectionParameters(
				self.host,self.port,self.vhost, credentials = credentials))
			self.channel = broker.channel()
		return self.channel

	def receive(self,exchange, queue, _type = "direct",passive = False, durable = True,
		auto_delete = False, binding = False, routing_key = "*"):
		self.connect().exchange_declare(exchange, passive = passive, durable = durable, 
			auto_delete = auto_delete, type = _type)
		self.connect().queue_declare(queue, auto_delete = auto_delete)
		print exchange,queue,_type
		if binding:
			self.connect().queue_bind(queue = queue, exchange = exchange, routing_key = routing_key)

	def send(self, exchange, message, _type = "direct", passive = False, durable = True,
		auto_delete = False, content_type = "text/plain",routing_key = "",delivery_mode = 0):
		self.connect().exchange_declare(exchange, passive = passive, durable = durable, 
			auto_delete = auto_delete, type = _type)
		msg_props = pika.BasicProperties()
		msg_props.content_type = content_type
		msg_props.delivery_mode = delivery_mode
		# msg_props.durable = False
		print routing_key
		self.connect().basic_publish(body = message, exchange=exchange, properties = msg_props,
			routing_key = routing_key)
		print "send a message with content : %s" % message


	def basic_consume(self, queue = "", consumer_tag = "",
						callback = default_callback):
		print callback, queue
		self.connect().basic_consume(callback, 
			queue = queue, consumer_tag = consumer_tag)

	def startConsumer(self):
		print 'server has started at %s:%d' % (self.host,self.port)
		self.connect().start_consuming()


	def close(self):
		if self.channel:
			self.channel.close()