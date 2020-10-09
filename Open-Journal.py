#!/usr/bin/env python
import sys
import os
import threading
import schedule
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread
from ui.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # centers window
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        # in app buttons
        self.newBtn.clicked.connect(self.handleNewJournal)
        self.openBtn.clicked.connect(self.handleOpenJournal)
        self.saveBtn.clicked.connect(self.handleSaveJournal)
        self.encryptBtn.clicked.connect(self.handleEncrypt)
        self.decryptBtn.clicked.connect(self.handleDecrypt)
        self.deleteBtn.clicked.connect(self.handleDeleteJournal)
        self.printBtn.clicked.connect(self.handlePrint)

        # menubar buttons
        self.New.triggered.connect(self.handleNewJournal)
        self.Open.triggered.connect(self.handleOpenJournal)
        self.Save.triggered.connect(self.handleSaveJournal)
        self.Delete.triggered.connect(self.handleDeleteJournal)
        self.Encrypt_Journal.triggered.connect(self.handleEncrypt)
        self.Decrypt_Journal.triggered.connect(self.handleDecrypt)
        self.Print.triggered.connect(self.handlePrint)

        # self.saver = SaveThread()
        # self.saver.start()

    def handleNewJournal(self):
        # save current journal, if applicable
        self.handleSaveJournal()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self, "Save New Journal Entry As...",
                                                  "./journals/.txt",
                                                  "All Files (*)",
                                                  options=options)

        try:
            if filename != '':
                self.journalName.setText(filename)
                file = open(filename, 'w')
                text = self.journalEdit.toPlainText()
                file.write(text)
                file.close()
        except FileNotFoundError:
            pass

    def handleOpenJournal(self):
        # save current journal, if applicable
        self.handleSaveJournal()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "Open Journal Entry",
                                                  "./journals",
                                                  "All Files (*)",
                                                  options=options)

        try:
            if filename != '':
                self.journalName.setText(filename)
                with open(filename) as file:
                    data = file.read()
                    self.journalEdit.setText(data)
        except FileNotFoundError:
            pass

    # TODO add autosave feature
    def handleSaveJournal(self):
        try:
            filename = self.journalName.text()
            file = open(filename, 'w')
            text = self.journalEdit.toPlainText()  # TODO use rich text or html
            file.write(text)
            self.statusbar.showMessage("Saving '{filepath}'...".format(filepath=filename), 2000)
            file.close()
        except FileNotFoundError:
            pass

    # def autosaveJournal(self):
    #     schedule.every(5).seconds.do(self.handleSaveJournal)
    #     while True:
    #         schedule.run_pending()
    #         time.sleep(1)

    def handleEncrypt(self):
        pass

    def handleDecrypt(self):
        pass

    def handleDeleteJournal(self):
        try:
            filename = self.journalName.text()
            if filename != '':
                confirm = QMessageBox()
                confirm.setIcon(QMessageBox.Warning)

                confirm.setWindowTitle('Confirm Journal Deletion')
                confirm.setText('You are about to delete the currently opened journal.')
                confirm.setInformativeText('This action cannot be undone. Continue?')
                confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                return_value = confirm.exec_()
                if return_value == QMessageBox.Yes:
                    os.remove(filename)
                    self.journalEdit.clear()
                    self.journalName.clear()
                else:
                    pass
        except FileNotFoundError:
            pass

    def handlePrint(self):
        pass


class SaveThread(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        MainWindow().handleSaveJournal()
        self.sleep(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
