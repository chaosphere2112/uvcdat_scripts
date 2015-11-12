import vcs, cdms2

x = vcs.init()
try:
    f = cdms2.open(vcs.sample_data + '/clt.nc')
except AttributeError:
    f = cdms2.open(vcs.prefix + "/sample_data/clt.nc")
s = f('clt')

x.bgX = 1536
x.bgY = 1186
x.plot(s)

actors = []
rens = []
for ren in vcs.vcs2vtk.vtkIterate(x.backend.renWin.GetRenderers()):
    for act in vcs.vcs2vtk.vtkIterate(ren.GetActors()):
        actors.append(act)
    rens.append(ren)

print "# Actors:", len(actors)
print "# Renderers:", len(rens)