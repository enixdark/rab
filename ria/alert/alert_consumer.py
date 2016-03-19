#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
from config import *
from rb import AMQP
import json
import smtplib


def send_mail(recipients, subject, message):
	headers = ("From: %s\r\nTo: \r\nDate: \r\n" + \
			   "Subject: %s\r\n\r\n") % (ALERT_EMAIL, subject)
	smtp_server = smtplib.SMTP()
	smtp_server.connect("smtp.gmail.com",587)
	smtp_server.ehlo()
	smtp_server.starttls()
	smtp_server.login(USER_EMAIL,PASSWORD_EMAIL)
	smtp_server.sendmail(EMAIL, recipients, headers + str(message))
	smtp_server.close()

def critical_notify(channel, method, header, body):
	message = json.loads(body)
	sendmail(EMAIL_RECIPS, "CRITICAL ALERT", message)
	print "Sent alert via e-mail! Alert Text: %s " + "Recipients: %s" % (str(message), str(EMAIL_RECIPS))
	channel.basic_ack(delivery_tag=method.delivery_tag)

def rate_limit_notify(channel, method, header, body):
	message = json.loads(body)
	send_mail(EMAIL_RECIPS, "RATE LIMIT ALERT!", message)
	print "Sent alert via e-mail! Alert Text: %s " + "Recipients: %s" % (
		str(message), str(EMAIL_RECIPS))
	channel.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == "__main__":
	amqp = AMQP(USERNAME,PASSWORD,HOST,PORT,PATH)
	# amqp.connect()
	amqp.receive(exchange = EXCHANGE_NAME, queue = QUEUE_CRITICAL, _type = TOPIC, 
		routing_key = ROUTING_CRITICAL, binding = True)
	amqp.receive(exchange = EXCHANGE_NAME, queue = QUEUE_RATE, _type = TOPIC, 
		routing_key = ROUTING_RATE, binding = True)
	amqp.basic_consume(callback = critical_notify, queue = QUEUE_CRITICAL, consumer_tag = "critical")
	amqp.basic_consume(callback = rate_limit_notify, queue = QUEUE_RATE, consumer_tag = "rate_limit")
	amqp.startConsumer()