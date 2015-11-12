import vcs

x = vcs.init()

l = vcs.createline()
l.x = [(.15, .85), (.85, .15), (.15, .85), (.85, .15), (.15, .85)]
l.y = [(0, .2), (.2, .4), (.4, .6), (.6, .8), (.8, 1)]
l.type = ["solid", "dot", "dot", "solid", "dash"]
l.color = range(10, 110, 20)

x.plot(l)
raw_input("Enter")
