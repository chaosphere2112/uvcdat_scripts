import vcs, cdms2

f = cdms2.open(vcs.sample_data + "/clt.nc")
s = f("clt")

x = vcs.init()
template = vcs.createtemplate()
template.xtic1.y2 = template.data.y2
template.ytic1.x2 = template.data.x2
template.ytic1.priority = 2
template.ytic2.priority = 0
template.xtic2.priority = 0

line = x.createline()
line.color = 1
line.width = 3
line.type = "dot"
#x.setcontinentsline(line)
x.plot(s, template, continents_line=line)
raw_input("Wait")
x.png("lines")
