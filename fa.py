import vcs, cdms2

x = vcs.init()
fa = vcs.createfillarea()
fa.x = [[.1, .15, .1], [.2, .25, .2], [.3, .35, .3]]
fa.y = [[.2, .15, .1], [.2, .15, .1], [.2, .15, .1]]
fa.style = ["solid", "pattern", "hatch"]
fa.color = [20, 40, 60]
fa.index = [1, 5, 10]
x.plot(fa)

pattern = vcs.createfillarea()
pattern.x = [[.2, .25, .2]]
pattern.y = [[.3, .25, .2]]
pattern.style = "pattern"
pattern.color = [40]
pattern.index = [5]
x.plot(pattern)


hatch = vcs.createfillarea()
hatch.x = [[.3, .35, .3]]
hatch.y = [[.3, .25, .2]]
hatch.style = "hatch"
hatch.color = 60
hatch.index = 10
x.plot(hatch)

raw_input("Enter")
