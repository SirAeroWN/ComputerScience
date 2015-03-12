import pygame # for playing music
from CircularQueue import * # for storing the music information
from tkinter import * # for the GUI interface
from tkinter import Toplevel # for the search and add pop ups
from tkinter import messagebox # for the error message

class song: # this is essentially a convenient way to store song info
	def __init__(self, title, artist, album, filename, artwork):
		self.title = title # these are pretty self explainatory
		self.artist = artist
		self.album = album
		self.filename = filename
		self.artfile = artwork
		try:
			self.art = PhotoImage(file = artwork) # avoids doing it elsewhere
		except:
			errorString = 'There\'s something  wrong with the artwork file for ' + self.title + ', you may wish to delete and add this song again to make sure the file path is correct'
			messagebox.showinfo('Error', errorString) # give a neat error message

class circlular(CQueue): # adds an insert method for adding songs
	def __init__(self):
		super().__init__() # base is a circular queue that was imported earlier
		self.currnode = self.head # current node for inserting
		return

	def insert(self, current, data):
		self.currnode = current # sets currnode to the curently displayed song
		node = DoublyLinkedListNode(data, self.currnode.next, self.currnode) # makes the new node
		self.currnode.next.prev = node # set the nodes on either side of the new one to point to it appropriately
		self.currnode.next = node
		return

class MusicPlayer(): # the main GUI class stuffs
	def __init__(self):
		self.root = Tk() # make the first window
		self.root.geometry('600x400') # set window size, it is fixed
		self.info = Frame(self.root) # frame for album art and song info
		self.controls = Frame(self.root) # frame for control buttons
		self.info.pack() # put the frames in the window
		self.controls.pack()
		self.root.title("MyTunes") # name the window 'MyTunes'
		self.music = self.readDatabase() # get all the music and put it in a circular queue
		self.current = self.music.head # the first song is the current one displayed
		pygame.mixer.init() # turn on the music player
		try:
			pygame.mixer.music.load(self.current.data.filename) # load the song so it's ready to play
		except:
			messagebox.showinfo('Error', 'There appears to be something wrong with the file for this song. Make sure it is in the correct directory and not corrupted. You may wish to delete this song and add it again') # give them an error if the file doesn't load right
		self.playing = False # not playing, keeps track of wether a song is currently playing
		self.started = False # not started, keeps track of whether a song has started, that way play just unpauses
		self.Title = StringVar() # these are stringvars for holding add song info
		self.Album = StringVar()
		self.Artist = StringVar()
		self.SFilepath = StringVar()
		self.AFilepath = StringVar()
		self.albumCover = Label(self.info, image = self.current.data.art) # these are labels with the current song's info
		self.titleLbl = Label(self.info, text = self.current.data.title)
		self.artistLbl = Label(self.info, text = self.current.data.artist)
		self.albumLbl = Label(self.info, text = self.current.data.album)
		self.albumCover.grid(rowspan = 4, columnspan = 3) # album artwork gets more space than labels do
		self.titleLbl.grid(row = 1, column = 4)
		self.artistLbl.grid(row = 2, column = 4)
		self.albumLbl.grid(row = 3, column = 4)
		self.nextBtn = Button(self.controls, text = 'Next', command = self.next) # command buttons
		self.previousBtn = Button(self.controls, text = 'Previous', command = self.previous)
		self.playBtn = Button(self.controls, text = 'Play', command = self.play)
		self.pauseBtn = Button(self.controls, text = 'Pause', command = self.pause)
		self.deleteBtn = Button(self.controls, text = 'Delete', command = self.delete)
		self.addBtn = Button(self.controls, text = 'Add', command = self.add)
		self.searchBtn = Button(self.controls, text = 'Search', command = self.search)
		self.nextBtn.grid(row = 1, column = 1) # add command buttons under song info
		self.previousBtn.grid(row = 1, column = 2)
		self.playBtn.grid(row = 1, column = 3)
		self.pauseBtn.grid(row = 1, column = 4)
		self.deleteBtn.grid(row = 1, column = 5)
		self.addBtn.grid(row = 1, column = 6)
		self.searchBtn.grid(row = 1, column = 7)
		self.root.mainloop() #start the window
		return

	# gets all the songs from the database and stores in a circular queue
	def readDatabase(self):
		dataFile = open('songs/Songs.database', 'r') # open the database
		circ = circlular()
		for line in dataFile:
			listOfInfo = line.split(',') # info seperated by commas
			circ.addToTail(song(listOfInfo[0], listOfInfo[1], listOfInfo[2], listOfInfo[3], listOfInfo[4].strip())) # last needs .strip() to remove '\n'
		dataFile.close() # have to close file
		return circ

	# write the current circular queue to the database
	def writeDatabase(self):
		dataFile = open('songs/Songs.database', 'w') # this will remove current contents
		curr = self.music.head
		theinfo = curr.data.title + ',' + curr.data.artist + ',' + curr.data.album + ',' + curr.data.filename + ',' + curr.data.artfile + '\n' # start it off with something
		dataFile.close()
		dataFile = open('songs/Songs.database', 'a') # now we can append to the file with out repeating things
		curr = curr.next
		done = False
		while not done: # go through the whole queue and write info
			theinfo = curr.data.title + ',' + curr.data.artist + ',' + curr.data.album + ',' + curr.data.filename + ',' + curr.data.artfile + '\n'
			dataFile.write(theinfo)
			curr = curr.next
			if curr == self.music.head: # made a whole lap
				done = True
		dataFile.close() # have to close file
		return

	# moves to the next song
	def next(self):
		self.current = self.current.next # move to next song
		self.update() # update the info
		self.started = False # song doesn't auto start (weird, that'a normal for music players to do that...)
		self.playing = False # last song was stopped and new one isn't playing
		return

	# moves to previous song
	def previous(self):
		self.current = self.current.prev # move to previous
		self.update() # update the info
		self.started = False # just the same as next()
		self.playing = False
		return

	# play the loaded song, acts likenormal play buttons
	def play(self):
		if self.playing: # the song is already playing so don't do anything
			do = 'nothing'
		elif not self.started: # the music has not started and therefor isn't playing
			self.started = True # the music is now started
			pygame.mixer.music.play() # this method starts song from begining
		else: # the song has started and resumes where it is
			pygame.mixer.music.unpause() # resumes playback
		self.playing = True # no matter what the music is now playing (not really no matter what, but in any case)
		return

	# just pause it so it can be resumed
	def pause(self):
		pygame.mixer.music.pause() # this method allows for resuming music
		self.playing = False # not playing, but it is started
		return

	# remove the song from the queue ********ALSO REMOVES FROM DATABASE***********
	def delete(self):
		self.current = self.current.next # move to next node
		self.current.prev = self.current.prev.prev # prev now points to deleted node's previous
		self.current.prev.next = self.current # node before deleted node's next now points to deleted node's next
		self.current = self.current.prev # now move back
		self.next() # moves forward and updates info
		self.writeDatabase() # writes to database ***doesn't delete any files***
		return

	# dialof for adding a song
	def add(self):
		self.entrywindow = Toplevel() # aparently making another Tk() instance is bad practice, this is designed for this
		self.entrywindow.title('New Song') # title of window
		Label(self.entrywindow, text = 'Song Title').grid(row = 1, column = 1) # Labels and entry boxes
		thing1 = Entry(self.entrywindow, textvariable = self.Title)
		thing1.grid(row = 1, column = 2)
		Label(self.entrywindow, text = 'Album Title').grid(row = 2, column = 1)
		thing2 = Entry(self.entrywindow, textvariable = self.Album)
		thing2.grid(row = 2, column = 2)
		Label(self.entrywindow, text = 'Artist').grid(row = 3, column = 1)
		thing3 = Entry(self.entrywindow, textvariable = self.Artist)
		thing3.grid(row = 3, column = 2)
		Label(self.entrywindow, text = 'Song Filepath').grid(row = 4, column = 1)
		thing4 = Entry(self.entrywindow, textvariable = self.SFilepath)
		thing4.grid(row = 4, column = 2)
		Label(self.entrywindow, text = 'Artwork Filepath').grid(row = 5,  column = 1)
		thing5 = Entry(self.entrywindow, textvariable = self.AFilepath)
		thing5.grid(row = 5, column = 2)
		Button(self.entrywindow, text = 'Add', command = self.reallyAdd).grid(row = 6, columnspan = 2) # add button, calls the method that actually adds the song
		return

	# actually adds a song to the queue
	def reallyAdd(self):
		self.music.insert(self.current, song(self.Title.get(), self.Artist.get(), self.Album.get(), self.SFilepath.get(), self.AFilepath.get())) # makes a new song instance and inserts it into the queue at the current position
		self.next() # move current to new song and update info
		self.writeDatabase() # write changes to the database
		self.entrywindow.destroy() # kill the add song dialog
		return

	# search dialog for music, they can put info in both feilds but in that case only artist will be searched
	def search(self):
		self.find = Toplevel() # pop up
		self.find.title('Search') # title
		Label(self.find, text = 'Fill in one of the search criteria:').grid(row = 1, columnspan = 2) # labels
		Label(self.find, text = 'Artist:').grid(row = 3, column = 1)
		Label(self.find, text = 'Title:').grid(row = 2, column = 1)
		self.searchArtist = StringVar() # string vars that hold the info
		self.searchTitle = StringVar()
		searchArtistEnt = Entry(self.find, textvariable = self.searchArtist) # entry boxes
		searchTitleEnt = Entry(self.find, textvariable = self.searchTitle)
		searchArtistEnt.grid(row = 3, column = 2)
		searchTitleEnt.grid(row = 2, column = 2)
		Button(self.find, text = 'Search', command = self.findIt).grid(row = 4, columnspan = 2) # button which calls the actual method for searching
		return

	# determine which criteria to use
	def findIt(self):
		if len(self.searchArtist.get()) > 0: # use artist
			self.setCurrent(self.searchByArtist(self.searchArtist.get())) # search for song and set the current song to it
			self.find.destroy() # kill search dialog
		elif len(self.searchTitle.get()) > 0: # use title
			self.setCurrent(self.searchByTitle(self.searchTitle.get())) # search for song and set the current song to it
			self.find.destroy() # kill search dialog
		return

	# do search by artist
	def searchByArtist(self, artistName):
		start = self.current # will hold the currently displayed song node
		curr = self.current # will be changed as search continues
		match = start # default value for return value is the current node, if no results current will not actually change
		notFound = True # haven't found a match yet
		for i in range(0, self.music.size): # go through all the nodes
			if curr.data.artist == artistName:
				match = curr # we found it so set match equal to the node
				i = self.music.size + 10 # breaks for loop
				notFound = False # found it!
			curr = curr.next # move to next node
		if notFound:
			messagebox.showinfo('Not Found', 'It appears that your search criteria doesn\'t match any songs') # didn't find it so display an error
		return match # return match, defaults to current node if there wasn't a match

	# search by title
	def searchByTitle(self, aSongTitle):
		start = self.current # will hold the currently displayed song node
		curr = self.current # will be changed as search continues
		match = start # default value for return value is the current node, if no results current will not actually change
		notFound = True # haven't found a match yet
		for i in range(0, self.music.size): # go through all the nodes
			if curr.data.title == aSongTitle:
				match = curr # we found it so set match equal to the node
				i = self.music.size + 10 # breaks for loop
				notFound = False # found it!
			curr = curr.next # move to next node
		if notFound:
			messagebox.showinfo('Not Found', 'It appears that your search criteria doesn\'t match any songs') # didn't find it so display an error
		return match # return match, defaults to current node if there wasn't a match

	# set the current node
	def setCurrent(self, aNode):
		self.current = aNode # set the current node to the one passed
		self.update() # update the display info
		self.started = False # song not started
		self.playing = False # song not playing

	# update the display info
	def update(self):
		self.albumCover['image'] = self.current.data.art # change image
		self.titleLbl['text'] = self.current.data.title # change labels to current song's
		self.artistLbl['text'] = self.current.data.artist
		self.albumLbl['text'] = self.current.data.album
		try:
			pygame.mixer.music.load(self.current.data.filename) # load the song so it's ready to play
		except:
			messagebox.showinfo('Error', 'There appears to be something wrong with the file for this song. Make sure it is in the correct directory and not corrupted. You may wish to delete this song and add it again') # give them an error if the file doesn't load right
		return

try:
	Appear = MusicPlayer()
except:
	messagebox.showinfo('Oops', 'Something went wrong, you should try starting the program again')