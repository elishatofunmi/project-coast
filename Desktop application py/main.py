from PyQt5 import QtWidgets, QtGui, QtCore

from scipy.ndimage import imread
import sys

app = QtWidgets.QApplication(sys.argv)

input_image = imread({'index.jpeg'})
height, width, channels = input_image.shape
bytesPerLine = channels * width
qImg = QtGui.QImage(input_image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
pixmap01 = QtGui.QPixmap.fromImage(qImg)
pixmap_image = QtGui.QPixmap(pixmap01)
label_imageDisplay = QtWidgets.QLabel()
label_imageDisplay.setPixmap(pixmap_image)
label_imageDisplay.setAlignment(QtCore.Qt.AlignCenter)
label_imageDisplay.setScaledContents(True)
label_imageDisplay.setMinimumSize(1,1)
label_imageDisplay.show()