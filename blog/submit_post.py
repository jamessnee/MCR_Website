#! /usr/bin/python
import blog
import sys
sys.path.append('../../jinja/Jinja2-2.6/')
from jinja2 import Environment, FileSystemLoader
import cgi, cgitb
from urllib2 import quote

if __name__== '__main__':
	cgitb.enable()
	env = Environment(loader=FileSystemLoader('.'))
	template = env.get_template('templates/submit_post.html')
	print 'Content-type: text/html\n\n'

	form = cgi.FieldStorage()

	title = ""
	if "post_title" in form:
		title = form["post_title"].value
	title = title.encode('ascii', 'xmlcharrefreplace')

	text = ""
	if "post_text" in form:
		text = form["post_text"].value
	text = text.encode('ascii', 'xmlcharrefreplace')
	
	author = ""
	if "post_author" in form:
		author = form["post_author"].value

	# Print the post out so the user can see what they've posted
	print template.render(post_title=title,post_text=text,post_author=author)

	# Store the post
	blog.store_post(title,text,author)
