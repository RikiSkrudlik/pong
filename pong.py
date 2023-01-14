# Basic pong game 

import turtle as tl

window = tl.Screen()
window.title("Pong")
window.bgcolor("Black")
window.setup(height = 800, width = 800)
window.tracer(0)

class PaddleLeft:
    def __innit__(self, x, y):
        self.x = x
        self.y = y

#Main loop

activeThing = true

while(activeThing):
    window.update()

#Classes for the game elements



