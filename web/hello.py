#!/usr/bin/python

def hello_world(env, response):
	head = [('Content-Type', 'text/plain')]
	status = '200 OK'
	response(status, head)
	return env
