import json
import sys, time
from config import *
from rb import AMQP
from optparse import OptionParser
from urlparse import urlparse
def msg_rcvd(channel, method, header, body):
	print "Received: %(content)s/%(time)d" % json.loads(body)
	channel.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
	opt_parse = OptionParser()
	opt_parse.add_option('-b', '--host', dest = 'hostname', 
		help = "host server")
	opt_parse.add_option('-p', '--port', dest = 'port', 
		help = "port server")
	opt_parse.add_option('-u', '--user', dest = 'username', 
		help = "username")
	opt_parse.add_option('-P', '--pass', dest = 'pasword', 
		help = "pasword")
	params = opt_parse.parse_args()[0]
	if params.hostname == None and len(sys.argv) > 1:
		params = urlparse(sys.argv[1])
	try:
		USERNAME = params.username if params.username != None else USERNAME
		PASSWORD = params.pasword if params.password != None else PASSWORD
	except:
		pass
	AMQP_HOST = params.hostname
	AMQP_PORT = int(params.port)
	while True:
		try:
			amqp = AMQP(USERNAME,PASSWORD,AMQP_HOST,AMQP_PORT,PATH)
			amqp.connect()
			amqp.receive(exchange = EXCHANGE_NAME, queue = QUEUE, _type = TYPE,
				 binding = True, routing_key  = "cluster")
			amqp.basic_consume(callback = msg_rcvd, queue = QUEUE, no_ack = False, consumer_tag = CONSUMER_TAG)
			amqp.startConsumer()
		except Exception, e:
			import traceback; traceback.print_exc();
		time.sleep(5)
		print 'reconnect'