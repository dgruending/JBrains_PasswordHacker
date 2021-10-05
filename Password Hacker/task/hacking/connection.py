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


def get_password(address, method, response_length=4096, success_message="Connection success!",
                 fail_message="Wrong password!"):
    """
    Connect to the server and attempt to crack the password.

    Attempt to find the server password with the specified method and return it.
    :param address: Server address, Tuple (IP, port)
    :param method: Cracking method, generator function for password strings
    :param response_length: Maximum number of bytes to be received.
    :param success_message: server response for correct password
    :param fail_message: server response for incorrect password
    :return: Found password
    """
    with socket.socket() as client:
        client.connect(address)
        for password in method:
            client.send(password.encode())
            response = client.recv(response_length).decode()
            if response == success_message:
                return password
            elif response == fail_message:
                continue
            else:
                # something went wrong
                return response
