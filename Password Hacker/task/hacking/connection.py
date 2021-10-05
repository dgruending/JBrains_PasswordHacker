import socket


def get_response(address, message, response_length=4096):
    """
    Send a message to a server socket and return the response.

    Sends a specified message to a server socket and return the response
    with a maximum length of response_length [default 4096 Bytes]

    :param address: Server address, Tuple (IP, port)
    :param message: Message to be send. Needs to be a String.
    :param response_length: Maximum number of bytes to be received.
    :return: Server response as string.
    """
    with socket.socket() as client:
        client.connect(address)
        client.send(message.encode())
        response = client.recv(response_length)
        return response.decode()
