import vcs,cdms2

x = vcs.init()
f = cdms2.open(vcs.sample_data + "/clt.nc")
s = f("clt")

iso = x.createisofill()

iso.levels = range(0, 100, 10)
iso.fillareastyle = "pattern"
iso.fillareaindices = range(1, 11)
iso.fillareacolors = range(20, 220, 20)
iso.fillareaopacity = [100] * 10
iso.ext_2 = True

t = x.createtemplate("top")
t.scale(.5, "y")
t.move(.4, "y")
t.blank()
t.legend.priority = 1
t.data.priority = 1


iso.list()
x.plot(s, t, iso)

t = x.createtemplate("bot")
t.scale(.5, "y")
t.move(-.1, "y")
t.blank()
t.legend.priority = 1
t.data.priority = 1

iso = x.createisofill("hatch", iso.name)
iso.fillareastyle = "hatch"

x.plot(s, t, iso)

fname = raw_input("File Name: ")
if fname:
    x.png(fname)
