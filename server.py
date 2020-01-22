# Python Simple Server
# Student: Carlos Mendez
# Class: CNT4713 U01
# Professor: Ruben Balmaceda
# Spring 2020 - January 21, 2020

import http.server
import socketserver

# TCP/IP Transmission Control Protocol/Internet Protocol.
# TCP address consists of IP address and PORT.
PORT = 8080

# Simple HTTP request handler that serves files from
# current directory and any of its subdirectories.
Handler = http.server.SimpleHTTPRequestHandler

# An instance of TCPServer describes a server that
# uses the TCP protocol to send and receive messages
# (http is an application layer protocol on top of TCP).
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# To instantiate a TCP Server, we need two things:
# 1: The TCP address (IP address and a port number)
# 2: The handler
# TCP address is passed as a tuple of (ip address, port number).

# Passing an empty string as the ip address means that the server
# will be listening on any network interface (all available IP addresses).

# And since PORT stores the value of 8080, then the server will be
# listening on incoming requests on that port.

# serve_forever is a method on the TCPServer instance that starts the
# server and begins listening and responding to incoming requests.

# Reference: https://www.afternerd.com/blog/python-http-server/