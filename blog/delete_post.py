#! /usr/bin/python
import blog
import sys
import os
sys.path.append('../../jinja/Jinja2-2.6/')
from jinja2 import Environment, FileSystemLoader
import cgi, cgitb

if __name__== '__main__':
	env = Environment(loader=FileSystemLoader('.'))
	template = env.get_template('templates/delete_post.html')
	print 'Content-type: text/html\n\n'

	form = cgi.FieldStorage()

	filename = ""
	if "filename" in form:
		filename = form['filename'].value

	print template.render(post_title=filename)

	blog.delete_post(filename)
