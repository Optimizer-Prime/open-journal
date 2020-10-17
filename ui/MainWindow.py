# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 1100)
        MainWindow.setMinimumSize(QtCore.QSize(950, 1100))
        MainWindow.setMaximumSize(QtCore.QSize(950, 1100))
        MainWindow.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(320, 0, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.logo.setFont(font)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/resources/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.journalEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.journalEdit.setGeometry(QtCore.QRect(60, 110, 881, 941))
        self.journalEdit.setStyleSheet("background-color: rgba(191, 64, 64, 0);\n"
"background: 1\n"
"")
        self.journalEdit.setObjectName("journalEdit")
        self.journalName = QtWidgets.QLineEdit(self.centralwidget)
        self.journalName.setGeometry(QtCore.QRect(160, 80, 781, 25))
        self.journalName.setStyleSheet("background: 1")
        self.journalName.setInputMethodHints(QtCore.Qt.ImhNone)
        self.journalName.setDragEnabled(False)
        self.journalName.setReadOnly(True)
        self.journalName.setObjectName("journalName")
        self.journal_path = QtWidgets.QLabel(self.centralwidget)
        self.journal_path.setGeometry(QtCore.QRect(60, 80, 91, 21))
        self.journal_path.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"")
        self.journal_path.setObjectName("journal_path")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(5, 230, 48, 48))
        self.saveBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.saveBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.saveBtn.setStyleSheet("QPushButton {border-image: url(:/resources/save.png)}\n"
"QToolTip {    background-color: rgb(238, 238, 236);\n"
"                           color: black; \n"
"                           border: black solid 1px};")
        self.saveBtn.setText("")
        self.saveBtn.setObjectName("saveBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(5, 470, 48, 48))
        self.deleteBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.deleteBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.deleteBtn.setStyleSheet("QPushButton {border-image: url(:/resources/delete.png)}\n"
"QToolTip {    background-color: rgb(238, 238, 236);\n"
"                           color: black; \n"
"                           border: black solid 1px};")
        self.deleteBtn.setText("")
        self.deleteBtn.setObjectName("deleteBtn")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(5, 170, 48, 48))
        self.openBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.openBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.openBtn.setStyleSheet("QPushButton {border-image: url(:/resources/open.png)}\n"
"QToolTip {    background-color: rgb(238, 238, 236);\n"
"                           color: black; \n"
"                           border: black solid 1px};\n"
"")
        self.openBtn.setText("")
        self.openBtn.setObjectName("openBtn")
        self.encryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encryptBtn.setGeometry(QtCore.QRect(5, 290, 48, 48))
        self.encryptBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.encryptBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.encryptBtn.setStyleSheet("QPushButton {border-image: url(:/resources/encrypt.png)}\n"
"QToolTip {    background-color: rgb(238, 238, 236);\n"
"                           color: black; \n"
"                           border: black solid 1px};")
        self.encryptBtn.setText("")
        self.encryptBtn.setObjectName("encryptBtn")
        self.decryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.decryptBtn.setGeometry(QtCore.QRect(5, 350, 48, 48))
        self.decryptBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.decryptBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.decryptBtn.setStyleSheet("QPushButton {border-image: url(:/resources/decrypt.png)}\n"
"QToolTip {    background-color: rgb(238, 238, 236);\n"
"                           color: black; \n"
"                           border: black solid 1px};")
        self.decryptBtn.setText("")
        self.decryptBtn.setObjectName("decryptBtn")
        self.newBtn = QtWidgets.QPushButton(self.centralwidget)
        self.newBtn.setGeometry(QtCore.QRect(5, 110, 48, 48))
        self.newBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.newBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.newBtn.setStyleSheet("QPushButton {border-image: url(:/resources/new.png)}\n"
"QToolTip {    background-color: rgb(238, 238, 236);\n"
"                           color: black; \n"
"                           border: black solid 1px};\n"
"")
        self.newBtn.setText("")
        self.newBtn.setObjectName("newBtn")
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setGeometry(QtCore.QRect(5, 530, 48, 48))
        self.closeBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.closeBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.closeBtn.setStyleSheet("QPushButton {border-image: url(:/resources/close.png)}\n"
"QToolTip {    background-color: rgb(238, 238, 236);\n"
"                           color: black; \n"
"                           border: black solid 1px};")
        self.closeBtn.setText("")
        self.closeBtn.setObjectName("closeBtn")
        self.export_keyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.export_keyBtn.setGeometry(QtCore.QRect(5, 410, 48, 48))
        self.export_keyBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.export_keyBtn.setMaximumSize(QtCore.QSize(48, 48))
        self.export_keyBtn.setStyleSheet("QPushButton {border-image: url(:/resources/export_key.png)}\n"
"QToolTip {    background-color: rgb(238, 238, 236);\n"
"                           color: black; \n"
"                           border: black solid 1px};")
        self.export_keyBtn.setText("")
        self.export_keyBtn.setObjectName("export_keyBtn")
        self.logo.raise_()
        self.journalName.raise_()
        self.journal_path.raise_()
        self.saveBtn.raise_()
        self.deleteBtn.raise_()
        self.openBtn.raise_()
        self.encryptBtn.raise_()
        self.decryptBtn.raise_()
        self.newBtn.raise_()
        self.journalEdit.raise_()
        self.closeBtn.raise_()
        self.export_keyBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menubar.setPalette(palette)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menuFile.setPalette(palette)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menuHelp.setPalette(palette)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.menuSettings.setPalette(palette)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.statusbar.setPalette(palette)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setObjectName("New")
        self.Open = QtWidgets.QAction(MainWindow)
        self.Open.setObjectName("Open")
        self.Save = QtWidgets.QAction(MainWindow)
        self.Save.setObjectName("Save")
        self.Save_As = QtWidgets.QAction(MainWindow)
        self.Save_As.setObjectName("Save_As")
        self.About_Open_Journal = QtWidgets.QAction(MainWindow)
        self.About_Open_Journal.setObjectName("About_Open_Journal")
        self.Encrypt_Journal = QtWidgets.QAction(MainWindow)
        self.Encrypt_Journal.setObjectName("Encrypt_Journal")
        self.Decrypt_Journal = QtWidgets.QAction(MainWindow)
        self.Decrypt_Journal.setObjectName("Decrypt_Journal")
        self.Preferences = QtWidgets.QAction(MainWindow)
        self.Preferences.setObjectName("Preferences")
        self.Print = QtWidgets.QAction(MainWindow)
        self.Print.setObjectName("Print")
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setShortcut("")
        self.Exit.setObjectName("Exit")
        self.Delete = QtWidgets.QAction(MainWindow)
        self.Delete.setObjectName("Delete")
        self.Close = QtWidgets.QAction(MainWindow)
        self.Close.setObjectName("Close")
        self.Export_key = QtWidgets.QAction(MainWindow)
        self.Export_key.setObjectName("Export_key")
        self.menuFile.addAction(self.New)
        self.menuFile.addAction(self.Open)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Delete)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Encrypt_Journal)
        self.menuFile.addAction(self.Decrypt_Journal)
        self.menuFile.addAction(self.Export_key)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Close)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Exit)
        self.menuHelp.addAction(self.About_Open_Journal)
        self.menuSettings.addAction(self.Preferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Open Journal"))
        self.journalName.setToolTip(_translate("MainWindow", "<html><head/><body><p>Displays the filepath to the currently open journal.</p></body></html>"))
        self.journalName.setPlaceholderText(_translate("MainWindow", "No journal currently open. Create a new journal (plus icon) or open an existing one (folder icon)."))
        self.journal_path.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#eeeeec;\">Journal Path:</span></p></body></html>"))
        self.saveBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save journal (Ctrl + S)</p></body></html>"))
        self.deleteBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Delete journal</p></body></html>"))
        self.openBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open existing journal (Ctrl + O)</p></body></html>"))
        self.encryptBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Encrypt currently open journal</p></body></html>"))
        self.decryptBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Decrypt currently open journal</p></body></html>"))
        self.newBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create new journal (Ctrl + N)</p><p><br/></p></body></html>"))
        self.closeBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save and close journal</p></body></html>"))
        self.export_keyBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Export encryption key</p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.New.setText(_translate("MainWindow", "New"))
        self.New.setToolTip(_translate("MainWindow", "Create new journal"))
        self.New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.Open.setText(_translate("MainWindow", "Open"))
        self.Open.setToolTip(_translate("MainWindow", "Open existing journal"))
        self.Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Save.setToolTip(_translate("MainWindow", "Save journal"))
        self.Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.Save_As.setText(_translate("MainWindow", "Save As..."))
        self.About_Open_Journal.setText(_translate("MainWindow", "About Open Journal"))
        self.Encrypt_Journal.setText(_translate("MainWindow", "Encrypt Journal"))
        self.Encrypt_Journal.setToolTip(_translate("MainWindow", "Encrypt currently open journal"))
        self.Decrypt_Journal.setText(_translate("MainWindow", "Decrypt Journal"))
        self.Decrypt_Journal.setToolTip(_translate("MainWindow", "Decrypt currently open journal"))
        self.Preferences.setText(_translate("MainWindow", "Preferences"))
        self.Print.setText(_translate("MainWindow", "Print"))
        self.Print.setToolTip(_translate("MainWindow", "Print journal"))
        self.Print.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Delete.setText(_translate("MainWindow", "Delete Journal"))
        self.Close.setText(_translate("MainWindow", "Close Journal"))
        self.Export_key.setText(_translate("MainWindow", "Export encryption key"))
import ui.resources_rc
