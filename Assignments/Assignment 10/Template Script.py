import sys

def fun(para):
    #logic
    pass

def main():
    print("---File Extension Finder---")
    print("Application name: {}".format(sys.argv[0]))

    if len(sys.argv)<1 or len(sys.argv[3]>3):
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
        fun(sys.argv[1])

    except Exception as e:
        print("ERR: Invalid Input"+e)
    

if __name__=="__main__":
    main()    

