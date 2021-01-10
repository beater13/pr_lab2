import library as protocol

if __name__ == "__main__":
    n = 22
    g = 42

    proto_handler = protocol.socket()
    protocol.connect_to(proto_handler, 'localhost', 50)
    value = protocol.receive(proto_handler)

    print(value)

    value = 'second message'
    protocol.send(proto_handler, value)
    val_new = protocol.receive(proto_handler)
    protocol.send(proto_handler, val_new + ' final message')
    print(val_new)
