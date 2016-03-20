import json
import sys, random
from config import *
from rb import AMQP
from optparse import OptionParser

if __name__ == "__main__":
	opt_parse = OptionParser()
	opt_parse.add_option('-m', '--message', dest = 'message', help = "message to send to rabbit server")
	opt_parse.add_option('-b', '--host', dest = 'hostname', help = "message to send to rabbit server")
	opt_parse.add_option('-p', '--port', dest = 'port', help = "port server")
	opt_parse.add_option('-u', '--user', dest = 'username', help = "username")
	opt_parse.add_option('-P', '--pass', dest = 'pasword', help = "pasword")
	opt_parse.add_option('-t', "--type", dest = "type", help = "type")
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
	msg = json.dumps({"ordernum": random.randrange(0, 100, 1), "type" : params.type})
	amqp = AMQP(USERNAME,PASSWORD,AMQP_HOST,AMQP_PORT,PATH)
	amqp.connect()
	amqp.send(message = msg, exchange = EXCHANGE_NAME, content_type = "application/json", routing_key = ROUTING)
