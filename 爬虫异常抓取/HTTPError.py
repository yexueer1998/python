import urllib2

req = urllib2.Request('http://blog.csdn.net')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
