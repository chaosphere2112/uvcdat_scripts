#!/usr/bin/env python

import sys
from PySide import QtCore, QtGui
import vtk
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class VTKWidget(QtGui.QFrame):
    becameDrawable = QtCore.Signal()

    def __init__(self, parent=None, f=0):
        super(VTKWidget, self).__init__(parent=parent, f=f)

        self.inter = QVTKRenderWindowInteractor(parent=self)
        

        self.ren_win = self.inter.GetRenderWindow()
        self.ren_win.DebugOn()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.inter)
        self.setLayout(layout)

        self.events = (self.ren_win.AddObserver("ModifiedEvent",
                                                self.modified),
                       self.inter.AddObserver("ConfigureEvent",
                                              self.modified)
                       )

    def is_drawable(self):
        print "Before IsDrawable"
        # Need to redirect stderr to quash the Invalid Drawable errors?
        val = self.ren_win.IsDrawable()
        print "After IsDrawable"
        return val

    def modified(self, obj, ev):
        if self.ren_win.IsDrawable():
            self.ren_win.RemoveObserver(self.events[0])
            self.inter.RemoveObserver(self.events[1])
            self.becameDrawable.emit()


def build():
    # create a rendering window and renderer
    ren = vtk.vtkRenderer()

    # create source
    source = vtk.vtkSphereSource()
    source.SetCenter(0, 0, 0)
    source.SetRadius(5.0)

    # mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    # actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # assign actor to the renderer
    ren.AddActor(actor)
    return ren


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.show()
        w = VTKWidget(self)

        self.setCentralWidget(w)
        renderer = vtk.vtkRenderer()
        renderer.SetBackground(0, 0, 0)
        w.ren_win.AddRenderer(renderer)

        def r():
            print "Render time"
            w.ren_win.Render()
        w.becameDrawable.connect(r)


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())
