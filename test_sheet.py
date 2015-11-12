from cdatgui.spreadsheet.window import SpreadsheetWindow
from PySide import QtGui, QtCore

app = QtGui.QApplication([])

window = SpreadsheetWindow()
sheet = window.tabController.currentWidget().sheet

sheet.forceColumnMultiSelect(0)
sheet.forceColumnMultiSelect(0)
sheet.forceRowMultiSelect(0)
sheet.forceRowMultiSelect(0)
sheet.forceSheetSelect()
sheet.forceSheetSelect()
sheet.setFitToWindow(True)
sheet.resizeEvent(None)
sheet.setFitToWindow(False)
sheet.stretchCells()

app.quit()
