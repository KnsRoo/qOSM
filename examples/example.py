from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.uic import loadUi
import qOSM
import sys 
from qOSM.common import QOSM

def onMarkerMoved(key, latitude, longitude):
	print("Moved!!", key, latitude, longitude)
	coordsEdit.setText("{}, {}".format(latitude, longitude))

def onMarkerRClick(key):
	print("RClick on ", key)

def onMarkerLClick(key):
    print("Marker LClick on ", key)

def onMarkerDClick(key):
	print("DClick on ", key)

def onMapRClick(latitude, longitude):
	print("RClick on ", latitude, longitude)

def onMapDClick(latitude, longitude):
	print("DClick on ", latitude, longitude)

def onMapMoved(latitude, longitude):
	print("Moved to ", latitude, longitude)

class Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.count = 0
		self.setMinimumSize(QSize(800, 500))    
		loadUi('ui.ui', self) 
		self.view = QOSM(self)
		self.view.resize(781, 391);
		self.view.mapMoved.connect(onMapMoved)
		self.view.mapClicked.connect(self.onMapLClick)
		self.view.mapRightClicked.connect(onMapRClick)
		self.view.markerRightClicked.connect(self.onMarkerRClick)

	def onMarkerRClick(self, key, lat, lng):
		if self.checkBox.isChecked():
			self.view.removeMarker(key)


	def onMapLClick(self, latitude, longitude):
		if self.checkBox.isChecked():
			self.count+=1
			self.view.addMarker("My mark "+str(self.count), latitude, longitude, **dict(
        icon="http://maps.gstatic.com/mapfiles/ridefinder-images/mm_20_gray.png",
        draggable = True,
        title="mark n "+str(self.count)))

	@pyqtSlot()
	def on_go_clicked(self):
		self.view.addCircle(48.864716, 2.349014, 1000)
		self.panMap(48.864716, 2.349014)

	def panMap(self, lat, lng,):
		frame = self.view.page()
		frame.runJavaScript('mymap.panTo(L.latLng({}, {}));'.format(lat, lng))

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())