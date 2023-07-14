#!/usr/bin/python3
import os
from fabric.api import hosts, put, run, env

env.hosts = ['18.233.62.144', '35.153.255.28']

def do_deploy(archive_path):
	try:
		if not os.path.isfile(archive_path):
			return False
	
		# uploading archive to remote server
		put(archive_path, '/tmp/')

		#extracting filename only
		name = archive_path.split('/')[-1].split('.')[0]
	
		#creating directory
		path = "/data/web_static/releases/{}".format(name)
		run('mkdir {}'.format(path))

		#uncompressing the archive
		run("tar -xzf /tmp/{archive_path.split('/')[-1]} -C {}".format(path))
		
		#deleting the archive
		run("rm /tmp/{}".format(archive_path.split('/')[-1]))

		#deleting the symbolic link
		run("rm /data/web_static/current")

		#create a new symbolic link
		run("ln -s /{} /data/web_static/current".format(path))
	

		return True
	except:
		return False
