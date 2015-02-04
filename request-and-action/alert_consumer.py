import pika
import sys
import json
import smtplib
AMQP_SERVER = "localhost"
AMQP_USER = "alert-user"
AMQP_PASS = "alertme"
AMQP_VHOST = "/"
AMQP_EXCHANGE = "alerts"
AMQP_QUEUE_CRITICAL = "critical"
AMQP_QUEUE_RATE = "rate_limit"
PORT = 15672

def send_mail(recipients,subject,message):
	"""Email generator"""

	headers = ("From: %s\r\nTo: \r\nDate: \r\nSubject: %s\r\n\r\n" % ("cqshinn92@gmail.com",subject))
	smtp_server = smtplib.SMTP()
	smtp_server.connect("smtp.gmail.com:587")
	smtp_server.ehlo()
	smtp_server.starttls()
	smtp_server.ehlo()
	smtp_server.login("please fill your email", "please fill your password")
	smtp_server.sendmail("please fill your email",recipients,headers+str(message))
	smtp_server.close()



def critical_notify(channel,method,header,body):
	"""send critical alert via mail"""
	EMAIL_RECIPS = ['please fill email',]
	message = json.loads(body)
	send_mail(EMAIL_RECIPS,"CRIRICAL ALERT",message)
	print ("Sent alert via e-mail! Alert Text: %s " + \
		"Recipients: %s") % (str(message), str(EMAIL_RECIPS))

	channel.basic_ack(delivery_tag=method.delivery_tag)
	channel.basic_ack(delivery_tag=method.delivery_tag)

def rate_limit_notify(channel,method,header,body):
	"""Send message"""
	EMAIL_RECIPS = "please fill email"
	message = json.loads(body)

	send_mail(EMAIL_RECIPS,"RATE LIMIT ALERT",message)
	print ("Sent alert via e-mail! Alert Text: %s " + \
		"Recipients: %s") % (str(message), str(EMAIL_RECIPS))

	channel.basic_ack(delivery_tag=method.delivery_tag)
	channel.basic_ack(delivery_tag=method.delivery_tag)

credentials = pika.PlainCredentials(AMQP_USER,AMQP_PASS)
conn_params = pika.ConnectionParameters(AMQP_SERVER,virtual_host=AMQP_VHOST,credentials=credentials)

conn_broken = pika.BlockingConnection(conn_params)

channel = conn_broken.channel()

exchange = channel.exchange_declare(AMQP_EXCHANGE,type="topic",auto_delete=False)

channel.queue_declare(queue=AMQP_QUEUE_CRITICAL,auto_delete=False)
channel.queue_bind(queue=AMQP_QUEUE_CRITICAL,exchange=AMQP_EXCHANGE,routing_key="critical.*")
channel.queue_declare(queue=AMQP_QUEUE_RATE)
channel.queue_bind(queue=AMQP_QUEUE_RATE,exchange=AMQP_EXCHANGE,routing_key="*.rate_limit")

channel.basic_consume(critical_notify,queue=AMQP_QUEUE_CRITICAL,no_ack=True,consumer_tag=AMQP_QUEUE_CRITICAL)

channel.basic_consume(rate_limit_notify,queue=AMQP_QUEUE_RATE,no_ack=True,consumer_tag=AMQP_QUEUE_RATE)

print "Ready for alert"
channel.start_consuming()
