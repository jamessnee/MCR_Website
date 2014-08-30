#! /usr/bin/python
import blog_read
import sys
import os
sys.path.append('../../jinja/Jinja2-2.6/')
from jinja2 import Environment, FileSystemLoader
import cgi, cgitb

if __name__== '__main__':
	env = Environment(loader=FileSystemLoader('templates/'))
	template = env.get_template('index.html')
	print 'Content-type: text/html\n\n'
	posts = blog_read.get_all_posts()
	print template.render(blog_posts=posts)
