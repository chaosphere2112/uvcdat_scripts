import vtk


w = vtk.vtkRenderWindow()
w.SetSize(600, 600)
r = vtk.vtkRenderer()
w.AddRenderer(r)

polydata = vtk.vtkPolyData()
points = vtk.vtkPoints()
polygons = vtk.vtkCellArray()
color_arr = vtk.vtkUnsignedCharArray()
color_arr.SetNumberOfComponents(4)
color_arr.SetNumberOfTuples(1)
polydata.SetPoints(points)
polydata.SetPolys(polygons)
polydata.GetCellData().SetScalars(color_arr)

coords = [(.25, .25), (.5, .5), (.25, .5)]
color = (200, 120, 170, 255)

poly = vtk.vtkPolygon()
point_ids = poly.GetPointIds()
point_ids.SetNumberOfIds(len(coords))
for ind, coord in enumerate(coords):
    point = points.InsertNextPoint(coord[0], coord[1], 0.)
    point_ids.SetId(ind, point)

cellId = polygons.InsertNextCell(poly)

color_arr.SetTupleValue(cellId, color)

from vcs.vcsvtk.fillareautils import create_pattern
img = create_pattern(16, 16, "hatch", 1, (0, 93, 171), 255)
texture = vtk.vtkTexture()
texture.RepeatOn()
texture.SetInputData(img)

texture_coordinator = vtk.vtkProjectedTexture()
texture_coordinator.SetPosition(0, 0, 2)
texture_coordinator.SetFocalPoint(0, 0, 0)
texture_coordinator.SetUp(0, 1, 0)
texture_coordinator.SetSRange(0, 1)
texture_coordinator.SetTRange(0, 1)
texture_coordinator.SetInputData(polydata)
texture_coordinator.Update()
polydata.GetPointData().SetTCoords(texture_coordinator.GetOutput().GetPointData().GetTCoords())

actor = vtk.vtkActor()
actor.SetTexture(texture)
m = vtk.vtkPolyDataMapper()
m.SetInputData(polydata)
actor.SetMapper(m)

pngwriter = vtk.vtkPNGWriter()
pngwriter.SetInputData(img)
pngwriter.SetFileName("texture.png")
pngwriter.Update()
pngwriter.Write()

r.AddActor(actor)
w.Render()
raw_input("enter")
