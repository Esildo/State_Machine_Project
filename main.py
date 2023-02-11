import turtle
from FSM import FSM
from tigerFSM import TigerFMS
from PIL import Image

img = Image.open("C:\\nikita\Photos_for_labs\\background5.gif")
img = img.resize((1200,1000),Image.ANTIALIAS)
img.save("resized_background.gif")
turtle.screensize(canvwidth=1680,canvheight=1280,bg="white")
window = turtle.Screen()
window.title("Tiger")
window.bgpic("resized_background.gif")


if __name__ == "__main__":
    fsm = TigerFMS()

window.mainloop()
