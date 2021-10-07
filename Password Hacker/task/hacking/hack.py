import argparse

import connection
import cracking

# Stage 1/5: Establishing a connection
# Input [command line]:
#   1. IP address
#   2. port
#   3. message for sending
# Requirements:
#   1. Create a new socket.
#   2. Connect to a host and a port using the socket.
#   3. Send a message from the third command line argument to the host using the socket.
#   4. Receive the server’s response.
#   5. Print the server’s response.
#   6. Close the socket.


def stage1():
    parser = argparse.ArgumentParser("This program connects to an IP address and prints the response")
    parser.add_argument("ip", help="IP address for connection")
    parser.add_argument("port", help="Port for connection", type=int)
    parser.add_argument("message", help="Message for sending")
    args = parser.parse_args()
    print(connection.get_response((args.ip, args.port), args.message))


# Stage 2/5: Simple brute force
# Input [command line]:
#   1. IP address
#   2. port
# Requirements:
#   1. Parses the command line and gets two arguments that are IP address and port.
#   2. Tries different passwords until it finds the correct one.
#   3. Prints the password it found.


def stage2():
    parser = argparse.ArgumentParser("This program connects to an IP address and prints the response")
    parser.add_argument("ip", help="IP address for connection")
    parser.add_argument("port", help="Port for connection", type=int)
    args = parser.parse_args()
    print(connection.get_password((args.ip, args.port), cracking.brute_force()))


# Stage 3/5: Smarter, dictionary-based brute force
# Input [command line]:
#   1. IP address
#   2. port
# Requirements:
#   1. Parses the command line and gets two arguments that are IP address and port.
#   2. Finds the correct password using the list of typical passwords.
#   3. Prints the password it found.


def stage3():
    parser = argparse.ArgumentParser("This program connects to an IP address and prints the response")
    parser.add_argument("ip", help="IP address for connection")
    parser.add_argument("port", help="Port for connection", type=int)
    args = parser.parse_args()
    print(connection.get_password((args.ip, args.port), cracking.dictionary_attack("passwords.txt")))


# Stage 4/5:  Catching exception
# Input [command line]:
#   1. IP address
#   2. port
# Requirements:
#   1. Parses the command line and gets two arguments that are IP address and port.
#   2. Try all logins with an empty password.
#   3. When you find the login, try out every possible password of length 1.
#   4. When an exception occurs, you know that you found the first letter of the password.
#   5. Use the found login and the found letter to find the second letter of the password.
#   6. Repeat until you receive the ‘success’ message.
#   7. Print the combination of login and password in JSON format.

def stage4():
    parser = argparse.ArgumentParser("This program connects to an IP address and prints the response")
    parser.add_argument("ip", help="IP address for connection")
    parser.add_argument("port", help="Port for connection", type=int)
    args = parser.parse_args()
    print(connection.get_password_json((args.ip, args.port)))


if __name__ == '__main__':
    # stage1()
    # stage2()
    # stage3()
    stage4()
