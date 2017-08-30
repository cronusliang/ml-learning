import os
from os import listdir
from os.path import isfile, join

def rename_file(path):

    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print onlyfiles
    os.chdir(r'C:\Users\Administrator\Desktop\prank')
    for file in onlyfiles:
        print ("old name - "+file)
        print ("new name - "+file.translate(None,'0123456789'))
        os.rename(file,file.translate(None,'0123456789'))

rename_file('C:\Users\Administrator\Desktop\prank')