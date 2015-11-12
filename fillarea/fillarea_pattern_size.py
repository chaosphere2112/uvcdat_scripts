import vcs
fa = vcs.createfillarea()
fa.x = [0, 0, 1, 1]
fa.y = [0, 1, 1, 0]
fa.style = "hatch"
fa.color = 242
fa.index = 5
canvas = vcs.init()
canvas.bgX = int(raw_input("Width:"))
canvas.bgY = int(raw_input("Height:"))
canvas.plot(fa, bg=1)
canvas.png("fa_%dx%d.png" % (canvas.bgX, canvas.bgY), width=canvas.bgX, height=canvas.bgY)
