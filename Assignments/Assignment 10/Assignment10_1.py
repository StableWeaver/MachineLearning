import sys
import os

def directory(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    if exists:
        for foldername,subfolder,filename in os.walk(path):
            #print("Current folder is: "+foldername)
            for sub in subfolder:
                print("")
            for filen in filename:
                if str(filen).endswith(str(sys.argv[2])):
                    print("File : {}".format(os.path.abspath(filen)))
    else:
        print("Invalid Path")
    

def main():
    print("---File Extension Finder---")
    print("Application name: {}".format(sys.argv[0]))

    if len(sys.argv)<1 or len(sys.argv)>3:
        print("ERR: Invalid Number of Args")

    if sys.argv[1].lower=="-h":
        print("Script is designed for")
        exit()

    if sys.argv[1].lower=="-u":
        print("Usage: Appname  _______________")
        exit() 

    if len(sys.argv)!=3:
        print("ERR: Invalid no of Args")
        exit()

    try :
        directory(sys.argv[1])

    except Exception as e:
        print("ERR: Invalid Input"+e)
    

if __name__=="__main__":
    main()    

