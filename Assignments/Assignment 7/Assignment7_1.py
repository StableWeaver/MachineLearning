class BookStore:

    NoOfBooks=0

    def __init__(self,x,y):
        self.Name=x
        self.Author=y
        BookStore.NoOfBooks+=1

    def Display(self):
        print("Name : {}\nAuthor : {}\nNo of Books : {}".format(self.Name,self.Author,BookStore.NoOfBooks))


Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()