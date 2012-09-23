import curses
import sys
import time
import webbrowser
from random import randint
scr=0;tuples=[];no_of_bombs=1;no_of_defusals=3;level_reached=1
rows=input("Enter no. of rows ")
cols=input("Enter no. of columns ")
lst=[4,7,8,11]
cols+=50
if rows>39:
	rows=39
elif rows<29:
	rows+=10
def maketuples():
	global rows, cols, tuples
	i=1;j=1
	while i<rows-1:
		if i==rows/4-1 or i==rows/2-1 or i==3*rows/4-1:
			i+=1
			continue
		while j<cols-1:
			if j==cols/4-1 or j==cols/2-1 or j==3*cols/4-1:
				j+=1
				continue
			tuples=tuples+[[i,j]]
			j+=1
			if i==rows/2-2 and j==cols/2-2:
				j+=4
		i+=1
		j=1
#maketuples()
#stdscr=curses.initscr()
robot=[[0,0,' '],[0,1,'\\'],[0,2,'/'],[0,3,' '],[1,0,' '],[1,1,'@'],[1,2,'@'],[1,3,' '],[2,0,'<'],[2,1,'('],[2,2,')'],[2,3,'>'],[3,0,' '],[3,1,'/'],[3,2,'\\'],[3,3,' ']]
robo_coord=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
def bombanddef(no_of_bombs, no_of_defusals):
	global tuples,bombs, defusals,rows,cols
	i=0
	while i<no_of_bombs:
		num=randint(1,(rows-2)*(cols-2)-i-17-3*(rows+cols))
		x=tuples.pop(num)
		bombs.append(x)
		i+=1
	i=0
	while i<no_of_defusals:
		num=randint(1,(rows-2)*(cols-2)-i-no_of_bombs-18-3*(rows+cols))
		x=tuples.pop(num)
		defusals.append(x)
		i+=1
bombs=[]; defusals=[]
#bombanddef(no_of_bombs, no_of_defusals)
bullety=[[rows/4-1,2],[rows/2-1,2],[3*rows/4-1, 2]]
bulletx=[[rows-3,cols/4-1],[rows-3, cols/2-1],[rows-3,3*cols/4-1]]
def place_robot():
	global robot
	for items in range(len(robot)):
		stdscr.addch(robot[items][0], robot[items][1],robot[items][2])
class Level2:
	global stdscr
	def __init__(self):
#makescreen()
#stdscr=curses.initscr()
		maketuples()
		place_robot()
		global no_of_bombs,no_of_defusals
		no_of_bombs=1
		no_of_defusals=5
		bombanddef(no_of_bombs,no_of_defusals)
		put_bombs_and_defusals()
	"""global no_of_bombs, no_of_defusals
	def __init__(val1, val2):
		no_of_bombs=val1
		no_of_defusals=val2"""	
	def printing(self):
		global bulletx, bullety, robot, bombs, defusals
		i=0
		while i<3:
			stdscr.addch(bulletx[i][0], bulletx[i][1], curses.ACS_DIAMOND)
			stdscr.addch(bullety[i][0], bullety[i][1], curses.ACS_DIAMOND)
			i+=1
		time.sleep(0.04)
		i=0
		while i<3:
			bulletx[i][0]-=1
			bullety[i][1]+=1
			i+=1
	answer2=0
	def checking(self):
		global robot, bulletx, bullety, bombs, defusals, lst
		i=0
		while i<4:
			if [robot[i][0],robot[i][1]] in bulletx or [robot[i][0],robot[i][1]] in bullety:
				curses.flash()
				return 2
			if [robot[15-i][0],robot[15-i][1]] in bulletx or [robot[15-i][0],robot[15-i][1]] in bullety:
				curses.flash()
				return 2
			i+=1
		i=0
		while i<4:
			if [robot[lst[i]][0],robot[lst[i]][1]] in bulletx or [robot[lst[i]][0], robot[lst[i]][1]] in bullety:
				curses.flash()
				return 2
			i+=1
		return 0
	

for i in range(len(robot)):
	robot[i][0]+=rows/2-2
	robot[i][1]+=cols/2-2

def instructions():	
	curses.initscr()
#	curses.start_color()
	stdscr = curses.newwin(39,150,0,0)
	curses.curs_set(0)
	curses.noecho()
	stdscr.keypad(1)
	#stdscr.border('#','#','#','#','+','+','+','+')
	stdscr.addstr(5,5,"Instructions:\n\n     1) Use the UP, DOWN, LEFT, RIGHT key to move up, down, left, right\n     2) Collect all the defusal kits (D) to earn points and defuse bomb (B) to win\n     3) Do not touch the boundary or you lose\n     4) Do not touch any bomb before collecting all defusal kits or you lose\n     5) Press any key to start game\n")
	stdscr.box()
	stdscr.addstr(30,5,'Loading Game. Please read the instructions in the meanwhile...')
	stdscr.refresh()
	for i in range(70):
		stdscr.addch(32,i+5,curses.ACS_DIAMOND)
		stdscr.refresh()
		time.sleep(.1)
	time.sleep(2)
	curses.endwin()
	curses.initscr()
	stdscr=curses.newwin(39,150,0,0)
	stdscr.refresh()
	curses.endwin()
def makescreen():
	curses.initscr()
	#curses.start_color()
	stdscr = curses.newwin(rows, cols,0,0)
	stdscr.keypad(1)
	stdscr.box()
	i=0
#makescreen()
def put_bombs_and_defusals():
	global no_of_bombs, bombs,defusals, no_of_defusals
	i=0
	while i<no_of_bombs:
		stdscr.addch(bombs[i][0],bombs[i][1],'B',curses.A_BOLD)
		stdscr.refresh()
		i+=1
	i=0
	while i<no_of_defusals:
		stdscr.addch(defusals[i][0],defusals[i][1],'D',curses.A_BOLD)
		stdscr.refresh()
		i+=1
#put_bombs_and_defusals()

#place_robot()
#stdscr.addstr(0,2,' Score: '+str(scr)+' ')
#stdscr.refresh()
tog=0;result=0
class Level1:
	global stdscr
	def __init__(self):
#stdscr=curses.initscr()
#makescreen()
		maketuples()
		place_robot()
		global no_of_bombs,no_of_defusals
		no_of_bombs=1
		no_of_defusals=3
		bombanddef(no_of_bombs,no_of_defusals)
		put_bombs_and_defusals()
	def check(self):
		global tog, robot, bombs, defusals,scr,result
		i=0;
		if robot[0][0]==0 or robot[12][0]==rows-1 or robot[0][1]==0 or robot[3][1]==cols-1:
			tog=2
			curses.flash()
		i=0
		while i<4:
			if [robot[i][0],robot[i][1]] in bombs:
				curses.flash()	
				tog=1
				bombs.remove([robot[i][0],robot[i][1]])
				break
			if [robot[15-i][0], robot[15-i][1]] in bombs:
				curses.flash()	
				tog=1
				bombs.remove([robot[15-i][0], robot[15-i][1]])
				break
			if [robot[i][0],robot[i][1]] in defusals:
				curses.flash()	
				defusals.remove([robot[i][0],robot[i][1]])
				scr+=1
			if [robot[15-i][0],robot[15-i][1]] in defusals:
				curses.flash()	
				defusals.remove([robot[15-i][0],robot[15-i][1]])
				scr+=1
			i+=1
		i=0
		while i<4:
			if [robot[lst[i]][0],robot[lst[i]][1]] in bombs:
				bombs.remove([robot[lst[i]][0],robot[lst[i]][1]])
				curses.flash()
				tog=1
			if [robot[lst[i]][0],robot[lst[i]][1]] in defusals:
				curses.flash()
				scr+=1
				defusals.remove([robot[lst[i]][0], robot[lst[i]][1]])
			i+=1
		if tog==1 and scr!=no_of_defusals:
			result=2
		elif tog==1 and scr==no_of_defusals:
			result=1
		elif tog==2:
			result=2
		return result
score=[0]
while level_reached in [1,2]:
	instructions()
#	print 'now screen will be made'
#	time.sleep(2)
	curses.initscr()
	#curses.start_color()
	stdscr = curses.newwin(rows, cols,0,0)
	stdscr.keypad(1)
	stdscr.box()
	if level_reached==1:
		lev1=Level1()
	elif level_reached==2:
		lev2=Level2()
		lev2.printing()
#	key=curses.KEY_RIGHT
	key=stdscr.getch()
	while key!=27:
		i=0
		if(key==curses.KEY_RIGHT):
			while i<16:
				robot[i][1]+=1
				i+=1
				flag=1
		elif key==ord('p'):
			key=ord('q')
			while key!=ord('p'):
				key=stdscr.getch()
				continue
			key=stdscr.getch()
		elif(key==curses.KEY_LEFT):
			while i<16:
				robot[i][1]-=1
				i+=1
				flag=2
		elif(key==curses.KEY_UP):
			while i<16:
				robot[i][0]-=1
				i+=1
				flag=3
		elif(key==curses.KEY_DOWN):
			while i<16:
				robot[i][0]+=1
				i+=1
				flag=4
		answer=lev1.check()
		if level_reached==2:
			answer2=lev2.checking()
		if level_reached==1:
		 	if answer!=0:
		 		break
		elif level_reached==2:
			if answer!=0 or answer2!=0:
		 		break
		for items in range(len(robot)):
			stdscr.addch(robot[items][0], robot[items][1],robot[items][2])
		if flag==1:
		 	stdscr.addch(robot[8][0], robot[8][1]-1, ' ')
		elif flag==2:
		 	stdscr.addch(robot[11][0], robot[11][1]+1, ' ')
		elif flag==3:
		 	stdscr.addch(robot[13][0]+1, robot[13][1], ' ')
	 		stdscr.addch(robot[14][0]+1, robot[14][1], ' ')
		elif flag==4:
		 	stdscr.addch(robot[1][0]-1, robot[1][1], ' ')
		 	stdscr.addch(robot[2][0]-1, robot[2][1], ' ')
		stdscr.addstr(0,2,' Score: '+str(scr)+' ')
		if level_reached==2:
			lev2.printing()
			i=0
			while i<3:
				stdscr.addch(bulletx[i][0]+2, bulletx[i][1], ' ')
				stdscr.addch(bullety[i][0], bullety[i][1]-2, ' ')
				i+=1
			if bulletx[0][0]==0:
				i=0
				while i<3:
					stdscr.addch(1,bulletx[i][1],' ')
					i+=1
				bulletx=[[rows-2,cols/4-1],[rows-2, cols/2-1],[rows-2,3*cols/4-1]]
			if bullety[0][1]==cols-2:
				i=0
				while i<3:
					stdscr.addch(bullety[i][0],cols-3,' ')
					i+=1
				bullety=[[rows/4-1,2],[rows/2-1,2],[3*rows/4-1, 2]]
		stdscr.refresh()
		stdscr.timeout(45)
		getkey = stdscr.getch()
		key = key if getkey==-1 else getkey
	
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()
	def winning():
		global scr, score, level_reached		
		print 'YOU WON :-D. YOUR TOTAL SCORE IS ' +str(reduce(lambda x,y:x+y,score)+scr)
		level_reached+=1
		score=score+[scr]
#	print "welcome to next level"
#	lev2.printing()
	def losing():
		global level_reached, scr, score
		print 'YOU LOST :-(. YOUR TOTAL SCORE IS ' +str(reduce(lambda x,y:x+y, score)+scr)
		level_reached=-1
		score=score+[scr]
	if level_reached==1:
		if answer!=2:
			winning()
		else:
			losing()
	elif level_reached==2:
		if answer!=2 and answer2!=2:
			winning()
		else:
			losing()
	scr=0;bombs=[];defusals=[];tog=0;tuples=[];result=0;i=0
string=raw_input('TO PLAY MORE EXCITING LEVELS, BUY OUR GAME ONLINE. TO BUY, PLEASE TYPE YES ELSE NO: ')
if string=='yes' or string=='Yes' or string=='YES':
	webbrowser.open_new('./payment.html')
else:
	print 'Thanks for playing'

