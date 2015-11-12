import vtk, vcs

win = vtk.vtkRenderWindow()
ren = vtk.vtkRenderer()
win.AddRenderer(ren)

pts = vtk.vtkPoints()
polys = vtk.vtkCellArray()
pd = vtk.vtkPolyData()
pd.SetPoints(pts)
pd.SetPolys(polys)

pg = vtk.vtkPolygon()
pid = pg.GetPointIds()

points = ((.25, .25), (.25, .75), (.75, .75), (.75, .25))
pid.SetNumberOfIds(len(points))
for i, p in enumerate(points):
    pid.SetId(i, pts.InsertNextPoint(p[0], p[1], 0.))
cellId = polys.InsertNextCell(pg)

colors = vtk.vtkUnsignedCharArray()
colors.SetNumberOfComponents(4)
colors.SetNumberOfTuples(1)
pd.GetCellData().SetScalars(colors)

color = [20, 100, 220]
colors.SetTupleValue(cellId, color + [255])


m = vtk.vtkPolyDataMapper()
m.SetInputData(pd)
a = vtk.vtkActor()
a.SetMapper(m)

ren.AddActor(a)

"""
a = vcs.vcsvtk.fillareautils.make_patterned_polydata(pd, "pattern", 5, color, 255)
ren.AddActor(a)
"""

win.Render()
