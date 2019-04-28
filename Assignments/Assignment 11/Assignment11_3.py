import sys
import os
import HashingModule as hm

hash_dict=dict()


def addtolog(filep,fd):
    #fd=open("LOG.txt",encoding="utf-8" ,mode="a")
    fd.write(filep+"\n")
    

@hm.time_deco           #execution time calc for the function n logging
def directory(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)
    fd=open("LOG.txt",encoding="utf-8" ,mode="w")
    fd.write("Duplicate files address is presnt here...\n")
    if exists:
        for foldername,subfolder,filename in os.walk(path):
            #print("Current folder is: "+foldername)
            for filen in filename:
                symlnkp=os.path.join(foldername,"SL"+os.path.splitext(filen)[0]+".lnk")
                filen=os.path.join(foldername,filen)
                hash=hm.md5(filen)
                print(filen)
                if hash in hash_dict:
                    addtolog(filen,fd)
                    os.remove(filen) 
                else:
                    hash_dict.update({hash:filen})                   
    else:
        print("Invalid Path")
    fd.close

def main():
    print("---File Extension Finder---")
    print("Application name: {}".format(sys.argv[0]))

    if len(sys.argv)<1 or len(sys.argv)>2:
        print("ERR: Invalid Number of Args")

    if sys.argv[1].lower=="-h":
        print("Script is designed to add address of duplicate file in the LOG.TXT and creates a symbolic link for the deleted file")
        exit()

    if sys.argv[1].lower=="-u":
        print("Usage: Appname  AppName FolderName")
        exit() 

    if len(sys.argv)!=2:
        print("ERR: Invalid no of Args")
        exit()

    try :
        directory(sys.argv[1])

    except Exception as e:
        print("ERR: Invalid Input"+e)
    

if __name__=="__main__":
    main()    
