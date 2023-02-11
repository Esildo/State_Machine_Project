import turtle
from FSM import FSM
from tigerFSM import TigerFMS
from PIL import Image
from rabbit import Rabbit
from Meat import  Meat

imgTiger = Image.open("C:\\nikita\Photos_for_labs\\tiger2D.gif")
imgTiger = imgTiger.resize((240,120),Image.ANTIALIAS)
imgTiger.save("tiger_resized.gif")
tiger_image = "tiger_resized.gif"
turtle.register_shape(tiger_image)

imgTigerS = Image.open("C:\\nikita\Photos_for_labs\\sleep2D.gif")
imgTigerS = imgTigerS.resize((240,120),Image.ANTIALIAS)
imgTigerS.save("tigerS_resized.gif")
tigerS_image = "tigerS_resized.gif"
turtle.register_shape(tigerS_image)

imgMeat = Image.open("C:\\nikita\Photos_for_labs\\meat2D.gif")
imgMeat = imgMeat.resize((240,120),Image.ANTIALIAS)
imgMeat.save("meat_resized.gif")
meat_image = "meat_resized.gif"
turtle.register_shape(meat_image)

imgRabbit = Image.open("C:\\nikita\Photos_for_labs\\rabbit2D.gif")
imgRabbit = imgRabbit.resize((180,120),Image.ANTIALIAS)
imgRabbit.save("rabbit_resized.gif")
rabbit_image = "rabbit_resized.gif"
turtle.register_shape(rabbit_image)

img = Image.open("C:\\nikita\Photos_for_labs\\background5.gif")
img = img.resize((1200,1000),Image.ANTIALIAS)
img.save("resized_background.gif")
turtle.screensize(canvwidth=1680, canvheight=1280, bg="white")
window = turtle.Screen()
window.title("Tiger")
window.bgpic("resized_background.gif")


if __name__ == "__main__":
    rab = Rabbit()
    fsm = TigerFMS(rab)




window.mainloop()
