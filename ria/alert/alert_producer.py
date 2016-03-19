from rb import AMQP
from config import *

import json
from optparse import OptionParser

if __name__ == '__main__':
	opt_parse = OptionParser()
	opt_parse.add_option('-r', '--routing-key', dest = 'routing_key', 
		help = "Routing key for message (ex: myalert.im)")
	opt_parse.add_option('-m', '--message', dest = 'message', 
		help = "Message text")
	args = opt_parse.parse_args()[0]
	amqp = AMQP(USERNAME,PASSWORD,HOST,PORT,PATH)
	

	amqp.send(exchange = EXCHANGE_NAME, message = json.dumps(args.message),
	 _type = TOPIC, content_type = "application/json", routing_key = json.dumps(args.routing_key))

