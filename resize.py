import vcs, cdms2

x = vcs.init()
x.open()
print x.backend.renWin.GetSize()
print x.backend.renWin.GetScreenSize()
x.geometry(1200, 2000)
x.plot([12,3,5])
raw_input("should be big")
x.png("out")
raw_input("should be small")
