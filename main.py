chardefine = ""

def on_on_chat():
    pass
player.on_chat(chardefine, on_on_chat)

def on_forever():
    global chardefine
    chardefine = "b"
loops.forever(on_forever)
