from datetime import datetime, timedelta, time


pTime = datetime.now()
nytime = datetime.now() + timedelta(hours=3)
lTime = datetime.now() + timedelta(hours=8)


Portland = '{:%H:%M %p}'.format(pTime)
NewYork = '{:%H:%M %p}'.format(nytime)
London = '{:%H:%M %p}'.format(lTime)


print 'Portland Branch Time: ' + Portland
print 'New York Branch Time: ' + NewYork
print 'London Branch Time: ' + London

now = datetime.now()
    
if time(9, 00) <= now.time() <= time(17):
    print "Portland is open"
else:
    print "Portland is closed"

if time(9, 00) <= nytime.time() <= time(17):
    print 'New York is open'
else:
    print "New York is closed"

if time(9, 00) <= lTime.time() <= time(17):
    print 'London is open'
else:
    print "London is closed"
