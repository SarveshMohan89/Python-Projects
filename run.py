import urllib

file = urllib.urlopen("http://www.python.org")
s = file.read()
f.close()

#I'm guessing this would output the html source code?
print(s)
