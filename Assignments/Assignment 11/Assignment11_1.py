import sys
import os
import HashingModule as hm
Hash=list()
Add=list()


@hm.time_deco           #execution time calc for the function n logging
def directory(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    if exists:
        for foldername,subfolder,filename in os.walk(path):
            #print("Current folder is: "+foldername)
            for filen in filename:
                filen=os.path.join(foldername,filen)
                Add.append(filen)
                Hash.append(hm.md5(filen))       
        for i in range(len(Add)):
            print("FilePath :{}".format(Add[i]))
            print("Hash :{}".format(Hash[i]))
    else:
        print("Invalid Path")
    

def main():
    print("---File Extension Finder---")
    print("Application name: {}".format(sys.argv[0]))

    if len(sys.argv)<1 or len(sys.argv)>2:
        print("ERR: Invalid Number of Args")

    if sys.argv[1].lower=="-h":
        print("Script is designed to display hashes of all the files in given folder")
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
