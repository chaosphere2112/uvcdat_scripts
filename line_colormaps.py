import vcs, cdms2

f = cdms2.open(vcs.sample_data + '/clt.nc')
s = f("clt", squeeze=1, time="1979-1")
zeroed = cdms2.createVariable([[0 for _ in range(s.shape[1])] for _ in range(s.shape[0])], axes=s.getAxisList(), grid=s.getGrid())

x = vcs.init()

box = vcs.createboxfill()
box.boxfill_type = "custom"
box.levels = [1, 100]
box.fillareacolors = [242]

light = vcs.createline()
colormap = vcs.createcolormap()
colormap.index[1] = [10, 10, 10]
light.colormap = colormap
light.type = "dash-dot"

dark = vcs.createline()
dark.width = 2

justdata = vcs.createtemplate()
justdata.blank()
justdata.data.priority = 1

x.plot(s, continents=4, continents_line=light, bg=1)
x.plot(zeroed, justdata, box, continents=1, continents_line=dark, bg=1)
x.png("nice_continents")
