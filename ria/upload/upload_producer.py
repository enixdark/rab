from config import *
from rb import AMQP
import json
from optparse import OptionParser

if __name__ == "__main__":
	opt_parse = OptionParser()
	# opt_parse.add_option('-r', '--routing-key', dest = 'routing_key', 
	# 	help = "Routing key for message (ex: myalert.im)")
	# opt_parse.add_option('-m', '--message', dest = 'message', 
	# 	help = "Message text")
	opt_parse.add_option('-i', '--image-id', dest = 'image_id', 
		help = "Image id")
	opt_parse.add_option('-u', '--user-id', dest = 'user_id', 
		help = "User id")
	opt_parse.add_option('-p', '--image-path', dest = 'image_path', 
		help = "Image path")
	args = opt_parse.parse_args()[0]
	message = json.dumps({
		'image_id': args.image_id,
		'user_id': args.user_id,
		'image_path': args.image_path
	})
	amqp = AMQP(USERNAME,PASSWORD,HOST,PORT,PATH)
	amqp.connect()
	amqp.send(exchange = EXCHANGE_NAME, _type = TOPIC, 
		content_type = "application/json", message = message, delivery_mode = 2)
	amqp.close()
