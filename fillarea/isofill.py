import vcs, cdms2
x = vcs.init()
f = cdms2.open(vcs.sample_data + "/clt.nc")

base_iso = vcs.createisofill("base")
base_iso.levels = range(0, 101, 10)

t = vcs.createtemplate("base")

x.plot(f("clt"), t, base_iso)

pattern_iso = vcs.createisofill("patterned", base_iso)
pattern_iso.fillareastyle = "pattern"
pattern_iso.fillareaindices = range(1, 11)

# Just draw the legend and the data
t2 = vcs.createtemplate("just_data", t.name)
t2.blank()
t2.data.priority = 1
t2.legend.priority = 1
x.plot(f("clt"), t2, pattern_iso)
fname = raw_input("Save?")
if fname:
    x.png(fname)