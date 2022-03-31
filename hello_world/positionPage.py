from flask import Flask
app = Flask(__name__)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

@app.route("/")
def showLocation():
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    return "x " + pos.x + ", y " + pos.y + ", z " + pos.z

app.run()