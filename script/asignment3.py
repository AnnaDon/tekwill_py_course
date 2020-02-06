myBook = open('/home/adrian/QA/tekwill_py_course/03/The Hunger Games.txt')
myBook.seek(0)
listOfPaleindroms = list()

def reverse(s):
	return s[::-1]
def isPalindrome(s): 
    	# Calling reverse function 
	rev = reverse(s) 
  
   	 # Checking if both string are equal or not 
	if (s == rev and len(s) > 1):
		return True
	return False

for i in myBook.read().translate({ord(c): " " for c in "!@#$%^\"&*()[]{};:,./<>?\|`~-=_+"}).split():
	ans = isPalindrome(i)
	len(i)
	if ans == 1:
		listOfPaleindroms.append(i) 
list_set = set(listOfPaleindroms) 
# convert the set to the list 
unique_list = (list(list_set)) 

#create dictionary
dictionaryOfPaleindroms = {}
for i in unique_list:
	numOfRepetitions = listOfPaleindroms.count(i)
	dictionaryOfPaleindroms[i] = numOfRepetitions

print (dictionaryOfPaleindroms)
	
	
