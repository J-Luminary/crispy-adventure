_break=('				')
def variablePractice():
	if 5>2:
		print("five is greater than 2")

	#second test
	x = 5
	y = "hello world"
	print (y)

	"""
	this is a comment written in
	more than just one line
	"""

	x=55+26
	z="jordan is amazing"
	print(x)
	print(z)

	g=float(72)
	h=62
	j="i am text"
	print(type(g),type(h),type(j))
	#^you can add , between actions to complete multuple per line

	x='jordan'
	print(x)
	#syntax can also be done with '' instead of ""

	my_name='jordan'
	print(my_name)

	my_favorite_fruits=('banana','blackberries',"watermellon")
	x,y,z = my_favorite_fruits
	print(x,y,z)
	x=y=z='the one and only Jordan'
	print(x), print(y), print(z)
	x,y,z='the final countdown','2..','1..'
	print(x,y,z)
	print(x+y+z)

	number_stack='2','3','4'
	x,y,z=number_stack
	print(x+y+z)
	g='jordan'
	h='is amazing'
	print(x+y+z,g,h)

	globalvariable1='a global variable outside the function'

	#def myfunction(): creates the function you do not need to close it
	#closing it is using the indentation #	Practicing variables

def myfunction():
	y='- this is a local varable inside of a function and cannot be used outside of it'
	print(y)
	print('my first function using',globalvariable1)
	global g
	g = 'lol jk this is now the new global takeover'
	#this \/ will now call the previous function to excecute
	#myfunction()
	myfunction()
	print(g) #		My first function

x='this is global variable x'
def myfunction2(): #	Global variable testing
	global x
	x = "used to be global variable x now its taken over MWAHAHAH!"

def variaablePractice2():
	carname='volvo'
	print(carname)

	number_stack2=(1,2.8,1j)
	x,y,z=number_stack2
	print(x,type(x),y,type(y),z,type(z),'this is the number_stack')
	a=float(x)
	b=int(y)
	c=complex(x)
	print(a,type(a),b,type(b),c,type(c),'- this is the number_stack after conversion')

	import random
	print(random.randrange(1,10))

	#All about strings now
	a='my name is Jordan'
	print(a,'- we will now break this down')
	print(a[11])
	print(len(a))
	for x in 'Jord':
		print(x)
	print('Jordan' in a)
	#^this will check if the string listed is present in the variable listed
	if 'Jordan' in a:
		print("yes, 'Jordan' is present")
	if 'Jordan' not in a:
		print("'Jordan' is not present")
	print(a[11:17])
	print(a[:10])
	print(a[0:7])
	print(a[-6:-2]) #this is negative indexing it starts from the back of the string
	y='jordant'
	print(y[0:5]) #you havet to think about moving on strings as a cursor
	#ex: print(y[0:5]) will print |Jorda|nt it takes the first cursor space 0 to
	#the 5th cursor space print(y[1:4]) will print J|ord|ant
	print(a.lower())
	print(a.upper())
	b=' my name is jordan '
	print(b)
	print(b.strip())
	print(a.replace('J','H'))
	print(a.split("s"))
	a='hello'
	b='jordan'
	c=a+' '+b
	print(c)

	age=25
	tx='my name is jordan, and i am {} years old'
	print(tx.format(age))

def firstHomework():
	"""
	first homework
	create 3 varables printage printname printcoolstatus
	coolstatus should be true or false if you are cool or not
	print them each in their own function
	then if cool then print "yes i am cool"
	if not cool then print 'totally not cool'
	"""
	"""
	_age=1000
	_name='Jordan the GOD'
	_coolstatus="cool"
	def printAge():
		print('age:',_age)

	def printName():
		print('Name:',_name)

	def printCoolStatus():
		coolhelper='Cool Status:'
		if _coolstatus == 'cool':
			print(coolhelper,'Totally Cool! <3')
		if _coolstatus != 'cool':
			print(coolhelper,'Totally Not Cool! x.x')
	printName(), printAge(), printCoolStatus()
	"""
	def coolMachine1():
		_age=1000
		_name='Jordan the GOD'
		_coolstatus='cool'
		def printAge():
			print('age:',_age)

		def printName():
			print('Name:',_name)

		def printCoolStatus():
			coolhelper='Cool Status:'
			if _coolstatus == 'cool':
				print(coolhelper,'Totally Cool! <3')
			if _coolstatus != 'cool':
				print(coolhelper,'Totally Not Cool! x.x')
		print('Welcome to the COOL MACHINE!!!'), printName(), printAge(), printCoolStatus()#	Function practice #	Function homework
	
def coolMachine(): #	Function homework practice using Boolean 
	_age=1000
	_name='Jordan the GOD'
	_coolstatus= True
	_welcome='Welcome to the COOL MACHINE!!!'
	_who='Who are you?'
	_letsCheck='Lets check your cool status!!! :D'
	def printAge():
		print('age:',_age)

	def printName():
		print('Name:',_name)

	def printCoolStatus():
		coolhelper='Cool Status:'
		if _coolstatus == True:
			print(coolhelper,'Totally Cool! <3')
		else:
			print(coolhelper,'Totally Not Cool! x.x')
	print(_welcome,),print(_who), printName(), printAge(),print(_letsCheck), printCoolStatus()

def listPratice(): #	Practicing lists
	#[1:3] is changing the list from INDEX 1 to INDEX 3 @-@
	#_listTest=['jordan',(@1)'devika','selena'(@3),'serena']
	_listTest=['jordan','devika','selena','serena']
	_listTest[1:4]=['devi','sel','serAna']
	print(_listTest)
	_listTest.insert(1,'Julia')
	print(_listTest)
	_listTest.append('michelle')
	print(_listTest)
	#	.extend can append any iterable object (tuples,sets,dictionaries,ect.)
	#	this adds a tuple to the previous list
	_listTest2=('girls','women')
	_listTest.extend(_listTest2)
	print(_listTest)
	_listTest.remove('jordan')
	print(_listTest)
	#	.pop() will remove the last item .pop(5) will remove the index listed
	_listTest.pop(5)
	print(_listTest)
	_listTest.pop()
	print(_listTest)
	#	del _listTest[1] deletes the selected index
	del _listTest[1]
	print(_listTest)
	#	this will delete the list variable and return: nboundLocalError: 
	#	local variable '_listTest' referenced before assignment
	#	del _listTest print(_listTest)
	_listTest.clear()
	print(_listTest)

def listPratice2(): # 	Practicing loops in lists
	#	the value after for ex(x or internetMaster) is used to call that for loop
	#	later in the code
	_listTest=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
	for x in _listTest:
		print(x)
	print(_break)
	#	using modifiers range and len let the for loop create an iterable 
	#	with a range of length of index for the designated list this next example
	#	creates the iterable index of [0,1,2,3,4,5,6,7] 
	for internetMaster in range(len(_listTest)):
		print(_listTest[internetMaster])
	print(_break)
	
	i=0
	while i < len(_listTest):
		print(_listTest[i])
		i=i+1
	print(_break)
	[print(x)for x in _listTest]

	_newList=[]
	for _letters in _listTest:
		if 'm' in _letters:
			_newList.append(_letters)
	print(_newList)

def ifElsePractice(): #		Practicing if and else
	