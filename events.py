#! /usr/bin/python
import sys
sys.path.append('../../jinja/Jinja2-2.6/')
from jinja2 import Environment, FileSystemLoader
import MySQLdb

if __name__== '__main__':
	env = Environment(loader=FileSystemLoader('templates/'))
	template = env.get_template('events.html')
	print 'Content-type: text/html\n\n'
	print template.render()
