from tkinter import * # Import tkinter
from random import randint

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))
        
# Define a Ball class
class Ball:
    def __init__(self, yspeed):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = 2#1.0 / (1 + yspeed) # Move right by default
        self.dy = 2#yspeed # Move down by default
        self.radius = 6 # The radius is fixed
        self.color = getRandomColor() # Get random color

class BounceBalls:
    def __init__(self):
        self.ballList = [] # Create a list for balls
        
        window = Tk() # Create a window
        window.title("Bouncing Balls") # Set a title
        
        self.width = 350 # Width of the self.canvas
        self.height = 350 / 2 # Width of the self.canvas
        self.canvas = Canvas(window, bg = "white", 
            width = self.width, height = self.height)
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume",
            command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame, text = "-", command = self.remove)
        btRemove.pack(side = LEFT)
        
        self.sleepTime = 100 # Set a sleep time 

        FasterBtn = Button(frame, text = "Faster", command = self.fast)
        FasterBtn.pack(side = LEFT)
        SlowerBtn = Button(frame, text = "Slower", command = self.slow)
        SlowerBtn.pack(side = LEFT)
        self.isStopped = False
        self.animate()
        
        window.mainloop() # Create an event loop
           
    def stop(self): # Stop animation
        self.isStopped = True
        return
    
    def resume(self): # Resume animation
        self.isStopped = False   
        self.animate()
        return

    def fast(self):
        self.sleepTime -= 10
        print(self.sleepTime)
        return

    def slow(self):
        self.sleepTime += 10
        print(self.sleepTime)
        return
    
    def add(self): # Add a new ball
        self.ballList.append(Ball(len(self.ballList)))
        return
    
    def remove(self): # Remove the last ball 
        self.ballList.pop()
        return
                                
    def animate(self): # Move the message
        while not self.isStopped:
            self.canvas.after(self.sleepTime) # Sleep 
            self.canvas.update() # Update self.canvas
            self.canvas.delete("ball") 
            
            for ball in self.ballList:
                self.redisplayBall(ball)
        return
    
    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
            
        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy
    
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, 
            ball.y - ball.radius, ball.x + ball.radius, 
            ball.y + ball.radius, fill = ball.color, tags = "ball")
        return
                                             
BounceBalls() # Create GUI