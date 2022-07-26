let chardefine = ""
player.onChat(chardefine, function () {
    mobs.spawn(PIG, player.position())
})
loops.forever(function () {
    chardefine = "b"
})
