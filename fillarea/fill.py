import vcs

x = vcs.init()
fa = x.createfillarea()
fa.x = [[0, 0, .25, .25], [0, 0, .5, .5], [0, 0, .1, .1]]
fa.y = [[0, .25, .25, 0], [.25, .5, .5, .25], [.5, 1, 1, .5]]
fa.style = ["pattern"]
fa.opacity = 100
fa.color = 50
fa.index = 1

x.plot(fa)
raw_input("Enter")

"""
import cdms2

c = cdms2.open(vcs.sample_data + "/clt.nc")('clt')
t = x.gettemplate()
t.blank()
t.legend.priority = 1
t.data.priority = 1
iso = x.createisofill()
iso.fillareastyle = "solid"
iso.fillareaopacity = [100] * 10
iso.fillareaindices = range(1, 10)
iso.levels = range(0, 101, 10)
iso.fillareacolors = vcs.getcolors(iso.levels)
x.plot(c, t, iso)
"""
#x.interact()
