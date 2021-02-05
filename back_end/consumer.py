"""
    We will consume messages from messaging queue
"""
import sys
import os
import pika 

MSG_USER=os.environ.get("MSG_USER")
MSG_PASS=os.environ.get("MSG_PASS")
HOST=os.environ.get("MESSAGING_HOST")


print("Consumer file------------------")

connection = pika.BlockingConnection(pika.ConnectionParameters(HOST,"5672","/",pika.PlainCredentials(MSG_USER,MSG_PASS)))
channel = connection.channel()

channel.queue_declare(queue="hello")

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    print(" [x] Done")

channel.basic_consume(queue="hello",on_message_callback=callback)

print("=> waiting for messages. To exit press CTRL+C")

channel.start_consuming()
connection.close()
