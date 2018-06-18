#!/usr/bin/python

def hello_world(env, response):
	res = env['QUERY_STRING'].split('&')
	res = [bytes(x + '\n', 'ascii') for x in res]
	head = [('Content-Type', 'text/plain')]
	status = '200 OK'
	response(status, head)
	return res
