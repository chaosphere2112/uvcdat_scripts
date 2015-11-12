import vcs, cdms2

x = vcs.init()
try:
    f = cdms2.open(vcs.sample_data + '/clt.nc')
except AttributeError:
    # vcs.sample_data is new in 2.4
    f = cdms2.open(vcs.prefix + "/sample_data/clt.nc")
s = f('clt')

import cProfile
x.bgX = 1536
x.bgY = 1186
x.plot(s)
x.configure()
s = x.backend.renWin.GetSize()

p = cProfile.Profile()
p.enable()
for i in range(s[0]):
    x1, y1 = i, i % s[1]
    x.configurator.actor_at_point(x1, y1)
p.disable()
p.print_stats(sort="tottime")
