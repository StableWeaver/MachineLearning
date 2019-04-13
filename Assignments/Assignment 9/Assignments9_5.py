filename=input("Enter File name?")
w=str(input("Enter the word to search?")).lower()
count=0
try:
	fd = open(filename)
	for word in fd.read().split():
		if(word.lower()==w):
			#print(word)
			count+=1

	print("\n\nThe word {} occured {} times...\n\n".format(w,count))
		
except FileNotFoundError:
    print("\n\nFile doesn't exist\n\n")

