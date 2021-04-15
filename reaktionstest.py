import time
import random
from guizero import App, Text, PushButton, Waffle


def test():
    button.destroy()
    welcome_message.destroy()
    free.destroy()
    free2.destroy()
    instruction = Text(app, text="Drücke auf den roten Kreis sobald er erscheint.")
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
            zeit = Text(app, text="Deine Zeit: " + str(timeused) + "s")
            zeit.text_color = "white"
            zeit.font = "Impact"
            # restart = PushButton(app, restart, text="Neustart")
            # restart.bg = "#a3a3a3"
            # restart.text_color = "white"

    board.update_command(ende)
    x, y = random.randint(0, 4), random.randint(0, 4)
    board[x, y].dotty = True
    board.set_pixel(x, y, "red")


app = App(title="Reaktionstest")
app.bg = "black"
free = Text(app, text="\n\n\n\n\n\n")
welcome_message = Text(app, text="Wilkommen beim Reaktionstest.\n Hier kannst du deine Reaktion testen.")
welcome_message.text_color = "white"
welcome_message.font = "Impact"
free2 = Text(app, text="\n")
button = PushButton(app, test, text="Start")
button.text_color = "white"
app.display()