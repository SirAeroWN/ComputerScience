import pygame
import PIL
from PIL import Image
from CircularQueue import *
from tkinter import *
from tkinter import Toplevel

class song:
	def __init__(self, title, artist, album, filename, artwork):
		self.title = title
		self.artist = artist
		self.album = album
		self.filename = filename
		self.artfile = artwork
		self.art = PhotoImage(file = artwork)

class circlular(CQueue):
	def __init__(self):
		super().__init__()
		self.currnode = self.head
		return

	def insert(self, current, data):
		self.currnode = current
		node = DoublyLinkedListNode(data, self.currnode.next, self.currnode)
		self.currnode.next.prev = node
		self.currnode.next = node
		return

	def delete(self):
		self.currnode = self.currnode.next
		self.currnode.prev = self.currnode.prev.prev
		self.currnode.prev.next = self.currnode
		return

class MusicPlayer():
	def __init__(self):
		self.root = Tk()
		self.root.resizable(width = False, height = False)
		self.root.geometry('600x400')
		self.info = Frame(self.root)
		self.controls = Frame(self.root)
		self.info.pack()
		self.controls.pack()
		self.root.title("MyTunes")
		self.music = self.readDatabase()
		self.current = self.music.head
		pygame.mixer.init()
		pygame.mixer.music.load(self.current.data.filename)
		self.playing = False
		self.started = False
		self.Title = StringVar()
		self.Album = StringVar()
		self.Artist = StringVar()
		self.SFilepath = StringVar()
		self.AFilepath = StringVar()
		self.albumCover = Label(self.info, image = self.current.data.art)
		self.titleLbl = Label(self.info, text = self.current.data.title)
		self.artistLbl = Label(self.info, text = self.current.data.artist)
		self.albumLbl = Label(self.info, text = self.current.data.album)
		self.albumCover.grid(rowspan = 4, columnspan = 3)
		self.titleLbl.grid(row = 1, column = 4)
		self.artistLbl.grid(row = 2, column = 4)
		self.albumLbl.grid(row = 3, column = 4)
		self.nextBtn = Button(self.controls, text = 'Next', command = self.next)
		self.previousBtn = Button(self.controls, text = 'Previous', command = self.previous)
		self.playBtn = Button(self.controls, text = 'Play', command = self.play)
		self.pauseBtn = Button(self.controls, text = 'Pause', command = self.pause)
		self.deleteBtn = Button(self.controls, text = 'Delete', command = self.delete)
		self.addBtn = Button(self.controls, text = 'Add', command = self.add)
		self.searchBtn = Button(self.controls, text = 'Search', command = self.search)
		self.nextBtn.grid(row = 1, column = 1)
		self.previousBtn.grid(row = 1, column = 2)
		self.playBtn.grid(row = 1, column = 3)
		self.pauseBtn.grid(row = 1, column = 4)
		self.deleteBtn.grid(row = 1, column = 5)
		self.addBtn.grid(row = 1, column = 6)
		self.searchBtn.grid(row = 1, column = 7)
		self.root.mainloop()

	def readDatabase(self):
		dataFile = open('songs/Songs.database', 'r')
		circ = circlular()
		for line in dataFile:
			listOfInfo = line.split(',')
			circ.addToTail(song(listOfInfo[0], listOfInfo[1], listOfInfo[2], listOfInfo[3], listOfInfo[4].strip()))
		dataFile.close()
		return circ

	def writeDatabase(self):
		dataFile = open('songs/Songs.database', 'w')
		curr = self.music.head
		theinfo = curr.data.title + ',' + curr.data.artist + ',' + curr.data.album + ',' + curr.data.filename + ',' + curr.data.artfile + '\n'
		dataFile.close()
		dataFile = open('songs/Songs.database', 'a')
		curr = curr.next
		done = False
		while not done:
			theinfo = curr.data.title + ',' + curr.data.artist + ',' + curr.data.album + ',' + curr.data.filename + ',' + curr.data.artfile + '\n'
			dataFile.write(theinfo)
			curr = curr.next
			if curr == self.music.head:
				done = True
		dataFile.close()
		return

	def next(self):
		self.current = self.current.next
		self.albumCover['image'] = self.current.data.art
		self.titleLbl['text'] = self.current.data.title
		self.artistLbl['text'] = self.current.data.artist
		self.albumLbl['text'] = self.current.data.album
		pygame.mixer.music.load(self.current.data.filename)
		self.started = False
		self.playing = False
		return

	def previous(self):
		self.current = self.current.prev
		self.albumCover['image'] = self.current.data.art
		self.titleLbl['text'] = self.current.data.title
		self.artistLbl['text'] = self.current.data.artist
		self.albumLbl['text'] = self.current.data.album
		pygame.mixer.music.load(self.current.data.filename)
		self.started = False
		self.playing = False
		return

	def play(self):
		if self.playing:
			do = 'nothing'
		elif not self.started:
			self.started = True
			pygame.mixer.music.play()
		else:
			pygame.mixer.music.unpause()
		self.playing = True
		return

	def pause(self):
		pygame.mixer.music.pause()
		self.playing = False
		return

	def delete(self):
		self.current = self.current.next
		self.current.prev = self.current.prev.prev
		self.current.prev.next = self.current
		self.current = self.current.prev
		self.next()
		self.writeDatabase()
		return

	def add(self):
		self.entrywindow = Toplevel()
		self.entrywindow.title('New Song')
		Label(self.entrywindow, text = 'Song Title').grid(row = 1, column = 1)
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
		Button(self.entrywindow, text = 'Add', command = self.reallyAdd).grid(row = 6, columnspan = 2)
		# self.entrywindow.mainloop()
		return

	def reallyAdd(self):
		self.music.insert(self.current, song(self.Title.get(), self.Artist.get(), self.Album.get(), self.SFilepath.get(), self.AFilepath.get()))
		self.next()
		self.writeDatabase()
		self.entrywindow.destroy()
		return

	def search(self):
		find = Toplevel()
		find.title('Search')
		
		return

Appear = MusicPlayer()