#use this as an libray for process display.
import psutil
import sys

def ProcessDisplay():
    some=[p.info for p in psutil.process_iter(attrs=['pid', 'name']) if sys.argv[1] in p.info['name']]
    for i in some:
        print(i)

def main():
    if len(sys.argv)!=2:
        print("ERR: Invalid no of Args")
        exit()

    if sys.argv[1].lower=="-h":
            print("Script is designed to find a running process" )
            exit()

    if sys.argv[1].lower=="-u":
            print("Usage: Appname process_name")
            exit() 

    try :
        print("#"*80)
        print(" "*35+"Process Finder")
        print("#"*80)

        ProcessDisplay()

    except Exception as e:
        print("ERR: Invalid Input"+e)

if __name__=="__main__":
    main()        

