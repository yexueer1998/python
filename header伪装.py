Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib2
>>> import urllib
>>> url = 'www.zhihu.com'
>>> user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
>>> headers = { 'User-Agent' : user_agent }
>>> request = urllib2.Request(url, headers)
>>> request = urllib2.Request('http://www.baidu.com',headers={'User-Agent':user_agent})
>>> response = urllib2.urlopen(request)
>>> request = urllib2.Request('http://www.zhihu.com',headers={'User-Agent':user_agent})
>>> response = urllib2.urlopen(request)
>>> page = response.read()
>>> 
