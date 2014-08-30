#! /usr/bin/python
import blog
import sys
import os
sys.path.append('../../jinja/Jinja2-2.6/')
from jinja2 import Environment, FileSystemLoader
import cgi, cgitb

if __name__== '__main__':
	env = Environment(loader=FileSystemLoader('.'))
	template = env.get_template('templates/admin.html')
	print 'Content-type: text/html\n\n'

	posts = blog.get_all_posts()
	print template.render(blog_posts=posts)
