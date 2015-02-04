import pika
import json
from optparse import OptionParser

EXCHANGE = 'alerts'

opt_parser = OptionParser()
opt_parser.add_option("-r","--routing-key",dest="routing_key",
						help="Routing key for message (e.g. myalert.im")
opt_parser.add_option("-m","--message",dest="message",
						help="message text for alert")

args = opt_parser.parse_args()[0]

creads_broker = pika.PlainCredentials("alert-user","alertme")

conn_params = pika.ConnectionParameters("localhost",virtual_host="/",credentials=creads_broker)

conn_broken = pika.BlockingConnection(conn_params)

channel = conn_broken.channel()

message = json.dumps(args.message)

message_props = pika.BasicProperties()

message_props.content_type = "application/json"

message_props.durable = False

channel.basic_publish(body=message,exchange=EXCHANGE,properties=message_props,
						routing_key=args.routing_key)

print ("Sent message %s tagged with routing key '%s' to " + \
"exchange '/'.") % (json.dumps(args.message),
args.routing_key)
