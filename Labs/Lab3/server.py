import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
receiever = context.socket(zmq.PULL)
receiever.bind("tcp://127.0.0.1:5678")
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:5677")

while True:
    message = receiever.recv()
    publisher.send(message)
    print("[Server]" + message.decode())