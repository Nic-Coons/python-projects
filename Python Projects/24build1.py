from datetime import datetime, timedelta, time
import glob, os
import shutil
now = datetime.utcnow()

os.chdir('C:\\Users\\Nic\\Desktop\\folderA')
for file in glob.glob("*.*"):    
    print file
    dateone = os.path.getctime(file)
    datetwo = datetime.fromtimestamp(dateone)
    nudate = str(now - datetwo)
    print nudate
    if 'day' in nudate:
        print 'yes'
        shutil.move(file, 'C:\\Users\\Nic\\Desktop\\folderB')
    else:
        print 'no'
      
        

