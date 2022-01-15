
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont


#initiallize GUI application
widgets = {
      "images" : [],
      "buttons" : []
}
watchApp = QApplication(sys.argv)
grid = QGridLayout()
#window and settings
watchWindow = QWidget()
watchWindow.setWindowTitle("Stay in Theater")
watchWindow.setFixedSize(500,600)
# potatoWindow.move(4000, 200)     #position of the window may vary depending on screen size
watchWindow.setStyleSheet("background: #FFFDD0;")


def openFileNamesDialog():
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames("QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

def saveFileDialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getSaveFileName("","All Files (*);;Text Files (*.txt)", options=options)
    if fileName:
        print(fileName)

def frameOne():
      #display logo
      helloApp = QPixmap("helloApp.png")
      welcomeImg = QLabel()
      welcomeImg.setPixmap(helloApp)
      welcomeImg.setAlignment(QtCore.Qt.AlignCenter)
      welcomeImg.setStyleSheet("margin-bottom: 300px;")
      widgets["images"].append(welcomeImg)

      #add button
      startButton = QPushButton("Try binge watch.")
      startButton.setGeometry(200, 300, 100, 30)
      startButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
      startButton.setStyleSheet(
            "*{border: 2px solid '#E1865F';" +
            "border-radius: 13px;" +
            "background: '#E1865F';" +
            "font-size: 15px;" +
            "color: '#132733';" +
            "padding: 10px 0;" +
            "margin-top: 100px;" +
            "margin: 150px 150px;}" +
            "*:hover{background: '#D35A26';}" 

      )
      widgets["buttons"].append(startButton)

      openFileNamesDialog()
      saveFileDialog()

      #add widgets to the grid
      grid.addWidget(widgets["images"][-1],0,0)
      grid.addWidget(widgets["buttons"][-1], 0,0)

frameOne()

watchWindow.setLayout(grid)
watchWindow.show()
sys.exit(watchApp.exec())

#     msg = input("Enter msg to potato: ")

#     client.sendMsg(msg)
#     response = client.recvMsg()
#     print(response) 