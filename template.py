from string import Template
s=Template('$who likes to $what')
p=s.substitute(who="chanan",what="eat chicken")
print p
d=dict(who='tim',what='banana')
k=Template('$who likes to $what').substitute(d)
print k
l=Template('$who likes to $what').safe_substitute(d)
print l
