import time
localtime=time.localtime(time.time())
print "local current time:", localtime
currentformat=time.asctime(localtime)
print "new style format:",currentformat
