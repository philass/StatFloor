start = '>'
end = "</"
s = 'asdf=5;iwantthis123jasd'
print s[s.find(start)+len(start):s.rfind(end)]
