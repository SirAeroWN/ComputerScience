import pygame
import PIL
from PIL import Image
from CircularQueue import *
from tkinter import *

class song:
	def __init__(self, title, artist, album, filename, artwork):
		self.title = title
		self.artist = artist
		self.album = album
		self.filename = filename
		self.art = PhotoImage(file = artwork)

class circlular(CQueue):
	def __init__(self):
		super().__init__()
		self.currnode = self.head
		return

	def insert(self, data):
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
		self.root.title = "MyTunes"
		self.music = self.readDatabase()
		self.current = self.music.head
		pygame.mixer.init()
		pygame.mixer.music.load(self.current.data.filename)
		self.playing = False
		self.started = False
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
		return circ

	def next(self):
		self.current = self.current.next
		self.albumCover['image'] = self.current.data.art
		self.titleLbl['text'] = self.current.data.title
		self.artistLbl['text'] = self.current.data.artist
		self.albumLbl['text'] = self.current.data.album
		pygame.mixer.music.load(self.current.data.filename)
		return

	def previous(self):
		self.current = self.current.prev
		self.albumCover['image'] = self.current.data.art
		self.titleLbl['text'] = self.current.data.title
		self.artistLbl['text'] = self.current.data.artist
		self.albumLbl['text'] = self.current.data.album
		pygame.mixer.music.load(self.current.data.filename)
		return

	def play(self):
		if self.playing:
			do = 'nothing'
		elif not self.started:
			pygame.mixer.music.unpause()
		else:
			pygame.mixer.music.play()
		self.playing = True
		return

	def pause(self):
		pygame.mixer.music.pause()
		return

	def delete(self):
		return

	def add(self):
		return

	def search(self):
		return

makeTheDamnThingAppear = MusicPlayer()