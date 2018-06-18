#!/usr/bin/python

def hello_world(env, response):
	res = env['QUERY_STRING'].split('&')
	res = [bytes(x + '\n', 'ascii') for x in res]
	head = [('Content-Type', 'text/plain')]
	status = bytes('200 OK', 'ascii')
	response(status, head)
	return res
