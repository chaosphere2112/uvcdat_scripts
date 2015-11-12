import vcs
import EzTemplate
import cdms2

canvas = vcs.init()
canvas.bgX = 600
canvas.bgY = 1000

clt_file = cdms2.open(vcs.prefix + "/sample_data/clt.nc")
clt = clt_file("clt")

template = vcs.createtemplate()
template.blank()
template.data.priority = 1
template.box1.priority = 1
template.xtic1.priority = 1
template.ytic1.priority = 1
template.xtic2.priority = 1
template.ytic2.priority = 1

template.xlabel1.priority = 1
template.xlabel1.y = .2
template.ylabel1.priority = 1
template.ylabel1.x = .03

template.title.priority = 1

graphics_method = vcs.createboxfill()
graphics_method.yticlabels1 = {lat: " " if lat % 45 != 0 else  str(lat) for lat in range(-90, 90, 10)}
graphics_method.xticlabels1 = {lon: " " if lon % 90 != 0 else  str(lon) for lon in range(-180, 180, 10)}

multi = EzTemplate.Multi(template=template.name, columns=2, rows=5, top_margin=.05, bottom_margin=.1, left_margin = .1, right_margin = .1, vertical_spacing=.05)

for row in range(5):
	for col in range(2):
		tmpl_instance = multi.get(row=row, column=col)
		canvas.plot(clt, tmpl_instance, graphics_method, bg=1, ratio="autot")

canvas.png("multi.png")
