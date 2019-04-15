#a app to copy directory tree as well as files to another folder based on a condition in ignore lambda function.
import sys
import os
import shutil

ignore_func = lambda d, files: [f for f in files if os.path.isfile(os.path.join(d, f)) and not (f.endswith(sys.argv[3]))]

def directory(path):
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    src=os.path.join(os.path.abspath(os.path.curdir),sys.argv[1])
    dst=os.path.join(os.path.abspath(os.path.curdir),sys.argv[2])
    #print(src+dst)
    if exists:
        shutil.copytree(src, dst,ignore=ignore_func)
        print("COPIED")
                    
    else:
        print("Invalid Path")
    

def main():
    print("---File Extension Finder---")
    print("Application name: {}".format(sys.argv[0]))

    if len(sys.argv)<1 or len(sys.argv)>4:
        print("ERR: Invalid Number of Args")

    if sys.argv[1].lower=="-h":
        print("Script is designed for copyping contents of a folder")
        exit()

    if sys.argv[1].lower=="-u":
        print("Usage: Appname  original_folder new_folder")
        exit() 

    if len(sys.argv)!=4:
        print("ERR: Invalid no of Args")
        exit()

    try :
        directory(sys.argv[1])
    except OSError as oe:
        if oe.errno==17:
            print("Folder already exists")
            exit()
    except Exception as e:
        print(e)
    

if __name__=="__main__":
    main()    

