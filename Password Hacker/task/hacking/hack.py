import argparse

import connection

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


if __name__ == '__main__':
    stage1()
