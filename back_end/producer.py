import pika 
import os

MSG_USER=os.environ.get("MSG_USER")
MSG_PASS=os.environ.get("MSG_PASS")
NAME=os.environ.get("TEST")
HOST=os.environ.get("MESSAGING_HOST")

print("pika install")
print("hello, my name is {name}. {user} -> {password}".format(name=NAME,user=MSG_USER,password=MSG_PASS))
print("---------------------------------------")


#connection = pika.BlockingConnection(pika.ConnectionParameters(HOST,5672,'/',pika.PlainCredentials(
#MSG_USER,MSG_PASS)))

connection = pika.BlockingConnection(pika.ConnectionParameters(HOST,"5672","/",pika.PlainCredentials("example","example")))

channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="",routing_key="hello",body="new message")

connection.close()
