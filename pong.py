# Basic pong game 

import turtle as tl

window = tl.Screen()
window.title("Pong")
window.bgcolor("Black")
window.setup(height = 800, width = 800)
window.tracer(0)

class PaddleLeft:
    def __innit__(self, x):
        self.x = x

#Main loop

active = True

while(active):
    window.update()

#Classes for the game elements



