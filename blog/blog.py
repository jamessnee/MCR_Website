#! /usr/bin/python

import sys
import time
import os

def parse_date(orig_date):
        comps = orig_date.split('_')
        year = comps[0]
        month = comps[1]
        day = comps[2]
        time = comps[3]
        date = time+' '+day+'/'+month+'/'+year
        return date

def get_all_posts():
        posts = []
        count = 0
        all_files = os.listdir("posts/")
        all_files.reverse()
        for files in all_files:
		fin = open("posts/"+files,'r')
		line = fin.read()
		comps = line.split('|')
		post = {'title': comps[0].decode('utf-8'), 'text': comps[1].decode('utf-8'), 'author': comps[2].decode('utf-8'), 'date': parse_date(files), 'filename': files}
		posts.append(post)
		count = count + 1
        return posts

def delete_post(filename):
        os.remove("posts/"+filename)

def store_post(title,text,author):
        postname = time.strftime("%Y_%m_%d_%T_"+title+".txt")
        postname = postname.replace(' ','_')

        posttext = text.replace('\n','<br />')
        posttext = posttext.replace('\t','<br />')

        fout = open('posts/'+postname,'w')
        fout.write(title+'|'+posttext+'|'+author)
        fout.close()
