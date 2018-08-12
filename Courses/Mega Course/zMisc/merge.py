import datetime

FILELIST = ['file1.txt', 'file2.txt', 'file3.txt']

ALL_READ = open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"),'a')

for ITEM in FILELIST:
    FILE = open(ITEM, 'r')
    ALL_READ.write(FILE.read())
    ALL_READ.write('\n\n')
    FILE.close()

ALL_READ.close()