Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> line = "Cats are smarter than dogs"
>>> line
'Cats are smarter than dogs'
>>> import re
>>> re.match(r'dogs', line, re.M|re.I)
>>> re.match(r'Cats', line, re.M|re.I)
<_sre.SRE_Match object at 0x016AA988>
>>> matchObje = re.match(r'Cats', line, re.M|re.I)
>>> matchObje.group()
'Cats'
>>> matchObj = re.rearch(r'dogs', line, re.M|re.I)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    matchObj = re.rearch(r'dogs', line, re.M|re.I)
AttributeError: 'module' object has no attribute 'rearch'
>>> matchObje = re.rearch(r'dogs', line, re.M|re.I)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    matchObje = re.rearch(r'dogs', line, re.M|re.I)
AttributeError: 'module' object has no attribute 'rearch'
>>> matchObj = re.search(r'dogs', line, re.M|re.I)
>>> print matchObj.group()
dogs
>>> matchObje
<_sre.SRE_Match object at 0x01FEB4F0>
>>> matchObje = re.search(r'dogs',line)
>>> matchObje
<_sre.SRE_Match object at 0x016AA988>
>>> matchObje = re.search(r'dogs$',line)
>>> matchObje
<_sre.SRE_Match object at 0x01FEB4F0>
>>> matchObje.group()
'dogs'
>>> line = "Cats are dogs smarter than dogs"
>>> matchObje = re.search(r'dogs$',line)
>>> matchObje.group()
'dogs'
>>> matchObje
<_sre.SRE_Match object at 0x02142288>
>>> 
