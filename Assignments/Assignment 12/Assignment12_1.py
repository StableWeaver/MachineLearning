#use this as an libray for process display.
import psutil
import sys
def ProcessDisplay():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=["name","pid","username"])

            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
    if len(sys.argv)<1 or len(sys.argv)>1:
        print("ERR: Invalid Number of Args")

    if len(sys.argv)==2:
        if sys.argv[1].lower=="-h":
            print("Script is designed to list running process" )
            exit()

        if sys.argv[1].lower=="-u":
            print("Usage: Appname")
            exit() 

    if len(sys.argv)!=1:
        print("ERR: Invalid no of Args")
        exit()

    try :
        print("#"*80)
        print(" "*35+"Process Monitor")
        print("#"*80)

        listprocess=ProcessDisplay()

        for elem in listprocess:
            print(elem)


    except Exception as e:
        print("ERR: Invalid Input"+e)

if __name__=="__main__":
    main()        

