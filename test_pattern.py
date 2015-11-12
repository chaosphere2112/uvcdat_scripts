import vcs, cdms2
x = vcs.init()
f = cdms2.open(vcs.sample_data + "/clt.nc")
s = f("clt")

iso = x.createisofill()
iso.levels = range(0, 110, 10)
iso.fillareastyle = "pattern"
iso.fillareaindices = range(1, 11)
iso.fillareacolors = range(20, 220, 20)
iso.fillareaopacity = [100] * 10

x.plot(s, iso)
raw_input("Enter")