myBook = open('/home/gherman/qa/tekwill_py_course/03/The Hunger Games.txt')
myBook.seek(0)

#create paleindrom list
listOfPaleindroms = list()
for i in myBook.read().translate({ord(c): "" for c in "!@#$%^\"&*()[]{};:,./<>?\|`~-=_+"}).split():
        if (i == i[::-1] and len(i)>1):
            listOfPaleindroms.append(i) 

#create dictionary
dictionaryOfPaleindroms = {}
for i in list(set(listOfPaleindroms)):
	numOfRepetitions = listOfPaleindroms.count(i)
	dictionaryOfPaleindroms[i] = numOfRepetitions

print (dictionaryOfPaleindroms)

dir(myBook)
