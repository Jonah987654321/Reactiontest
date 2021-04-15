import time
import random
from guizero import App, Text, PushButton, Waffle


def test():
    button.destroy()
    welcome_message.destroy()
    free.destroy()
    free2.destroy()
    instruction = Text(app, text="Push the red circle as soon as he appears")
    instruction.text_color = "white"
    board = Waffle(app, height=5, width=5, visible=True)
    board.pixel_size = 75
    board.set_all("white")
    app.update()
    waitingTime = (random.randint(0, 10))
    time.sleep(waitingTime)
    starttime = time.perf_counter()

    def ende(x, y):
        if board[x, y].dotty == True:
            board[x, y].dotty = False
            board.set_pixel(x, y, "white")
            end = time.perf_counter()
            timeused = round((end - starttime) * 1000) / 1000
            timedisplay = Text(app, text="Your reaction-time: " + str(timeused) + "s")
            timedisplay.text_color = "white"
            timedisplay.font = "Impact"

    board.update_command(ende)
    x, y = random.randint(0, 4), random.randint(0, 4)
    board[x, y].dotty = True
    board.set_pixel(x, y, "red")


app = App(title="Reaktionstest")
app.bg = "black"
free = Text(app, text="\n\n\n\n\n\n")
welcome_message = Text(app, text="Welcome to the reaction test. \nHere you can test your reaction.")
welcome_message.text_color = "white"
welcome_message.font = "Impact"
free2 = Text(app, text="\n")
button = PushButton(app, test, text="Start")
button.text_color = "white"
app.display()
