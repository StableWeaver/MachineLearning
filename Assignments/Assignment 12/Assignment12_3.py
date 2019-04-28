import psutil
import os
from Assignment12_1 import ProcessDisplay
import sys
from datetime import datetime

def logprocesslist(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)
    if exists:
        filep=os.path.join(path,"ProcessMonitor"+str(datetime.now()))
        fd=open(filep,encoding="utf-8" ,mode="w")
        proclist=ProcessDisplay()
        for i in proclist:
            fd.write(str(i)+"\n")

        fd.close()    
    else:
        print("Folder doesn't exists.")
def main():
    if len(sys.argv)!=2:
        print("ERR: Invalid no of Args")
        exit()

    if sys.argv[1].lower=="-h":
            print("Script is designed to create a log file in desired folder" )
            exit()

    if sys.argv[1].lower=="-u":
            print("Usage: Appname")
            exit() 

    try :
        print("#"*80)
        print(" "*35+"Process Monitor")
        print("#"*80)

        logprocesslist(sys.argv[1])


    except Exception as e:
        print("ERR: Invalid Input"+e)

if __name__=="__main__":
    main()        


