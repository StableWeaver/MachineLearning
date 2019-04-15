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
                pass
            for filen in filename:
                if str(filen).endswith(str(sys.argv[2])):
                    filen=os.path.join(str(foldername),str(filen))
                    print("FileName: "+filen)
                    os.rename(filen,str(filen).replace(sys.argv[2],sys.argv[3]))
                    print("Renamed........'")
    else:
        print("Invalid Path")
    

def main():
    print("---File Extension Finder---")
    print("Application name: {}".format(sys.argv[0]))

    if len(sys.argv)<1 or len(sys.argv)>4:
        print("ERR: Invalid Number of Args")

    if sys.argv[1].lower=="-h":
        print("Script is designed for changing file extension of many files at once")
        exit()

    if sys.argv[1].lower=="-u":
        print("Usage: Appname  folder_name extension_to_be_replaced extenion_to_which_to_replced")
        exit() 

    if len(sys.argv)!=4:
        print("ERR: Invalid no of Args")
        exit()

    try :
        directory(sys.argv[1])

    except Exception as e:
        print("ERR: Invalid Input"+str(e))
    

if __name__=="__main__":
    main()    

