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
    response = connection.get_response((args.ip, args.port), args.message)
    print(response)


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
    password = connection.get_password((args.ip, args.port), cracking.brute_force())
    print(password)


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
    password = connection.get_password((args.ip, args.port), cracking.dictionary_attack("passwords.txt"))
    print(password)


if __name__ == '__main__':
    # stage1()
    # stage2()
    stage3()
