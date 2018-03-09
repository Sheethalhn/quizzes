import zmq
import sys
from threading import Thread

# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"
sender = context.socket(zmq.PUSH)
sender.connect("tcp://127.0.0.1:5678")

name = sys.argv[1]
print("User [%s] Connected to the chat server." %(name))


def subscribe():
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://127.0.0.1:5677")
    subscriber.setsockopt_string(zmq.SUBSCRIBE, '') 

    while True:
        message = subscriber.recv().decode()
        if(message):
            if ("[{}]:".format(name) not in message):
                print ("\n{}".format(message)+"\n[{}] > ".format(name), end="")
        
def new_thread():
    thread = Thread(target=subscribe)
    thread.start()

new_thread()
while True:
    msg = input("[{}] > ".format(name))
    msg = "[%s]:  %s" % (name, msg)
    sender.send_string(msg)
