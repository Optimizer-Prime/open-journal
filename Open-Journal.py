#!/usr/bin/env python
import sys
import os
import subprocess
import threading
import schedule
import time
import shutil
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFileDialog, QMessageBox, QPushButton, QLabel
from PyQt5.QtCore import QThread
from ui.MainWindow import Ui_MainWindow


class AboutWindow(QMainWindow):
    pass


class PreferencesWindow(QMainWindow):
    pass


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
        self.closeBtn.clicked.connect(self.handleCloseJournal)

        # menubar buttons
        self.New.triggered.connect(self.handleNewJournal)
        self.Open.triggered.connect(self.handleOpenJournal)
        self.Save.triggered.connect(self.handleSaveJournal)
        self.Delete.triggered.connect(self.handleDeleteJournal)
        self.Encrypt_Journal.triggered.connect(self.handleEncrypt)
        self.Decrypt_Journal.triggered.connect(self.handleDecrypt)
        self.Close.triggered.connect(self.handleCloseJournal)
        # TODO add exit function

        self.keyStatusWidget()

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
                if self.journalName.text() != '':
                    # clear previous journal
                    self.journalName.clear()
                    self.journalEdit.clear()

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

    def handleCloseJournal(self):
        self.handleSaveJournal()

        try:
            filename = self.journalName.text()
            if filename != '':
                self.journalName.clear()
                self.journalEdit.clear()
            else:
                self.statusbar.showMessage('No journal currently open.', 2000)
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

    def createKey(self):
        """Generates encryption key and saves to file."""
        if os.path.exists('open_journal_key.key'):
            return open('open_journal_key.key', 'rb').read()
        else:
            key = Fernet.generate_key()
            with open('open_journal_key.key', 'wb') as key_file:
                key_file.write(key)
            return open('open_journal_key.key', 'rb').read()

    def loadKey(self):
        """Attempts to load key from root program directory, otherwise prompts user for location."""
        if os.path.exists('open_journal_key.key'):
            return open('open_journal_key.key', 'rb').read()
        else:
            try:
                key_options = QMessageBox()
                key_options.setIcon(QMessageBox.Question)

                key_options.setWindowTitle('Create Or Load Key')
                key_options.setText('No key was found in the program directory.')
                key_options.setInformativeText('Would you like to create a key or load an existing key?\n'
                                               '\nNote: You only need to create a key once.')
                key_options.addButton(QPushButton('Load Key'), QMessageBox.YesRole)
                key_options.addButton(QPushButton('Create Key'), QMessageBox.YesRole)
                key_options.addButton(QPushButton('Cancel'), QMessageBox.RejectRole)
                return_value = key_options.exec_()
                if return_value == 0:  # 0 refers to load key button
                    options = QFileDialog.Options()
                    options |= QFileDialog.DontUseNativeDialog
                    filename, _ = QFileDialog.getOpenFileName(self, "Load Encryption Key",
                                                              "./journals",
                                                              "All Files (*)",
                                                              "Key File (.key)",
                                                              options=options)

                    current_dir = os.getcwd()
                    shutil.copy(filename, current_dir)
                    old_key = os.path.basename(filename)
                    os.rename(old_key, r'open_journal_key.key')  # rename to expected name
                    return open(filename, 'rb').read()
                elif return_value == 1:  # 1 refers to create key button
                    self.createKey()
                elif return_value == 2:
                    pass
            except FileNotFoundError or TypeError:
                pass

    def checkKeyStatus(self):
        return os.path.exists('open_journal_key.key')

    def keyStatusWidget(self):
        key_found = QLabel('Key loaded')
        key_found.setStyleSheet('border :1px solid white;'
                                'background-color: rgb(115, 210, 22);')
        key_not = QLabel('Key not loaded')
        key_not.setStyleSheet('border :1px solid white;'
                              'background-color: rgb(204, 0, 0);')
        if self.checkKeyStatus():
            self.statusbar.addPermanentWidget(key_found)
        else:
            self.statusbar.addPermanentWidget(key_not)

    def handleEncrypt(self):
        try:
            key = self.loadKey()
            self.handleSaveJournal()
            filename = self.journalName.text()
            f = Fernet(key)

            # read journal file
            with open(filename, 'rb') as file:
                journal = file.read()

            # encrypt journal and write to file
            encrypted_journal = f.encrypt(journal)
            with open(filename, 'wb') as file:
                file.write(encrypted_journal)

            # display encrypted contents
            with open(filename) as file:
                data = file.read()
                self.journalEdit.setText(data)
        except FileNotFoundError:
            self.statusbar.showMessage('Encryption failed. No file currently open.', 2000)
        except TypeError:
            pass

    def handleDecrypt(self):
        try:
            key = self.loadKey()
            self.handleSaveJournal()
            filename = self.journalName.text()
            f = Fernet(key)

            # read the journal file
            with open(filename, 'rb') as file:
                encrypted_journal = file.read()

            # decrypt the journal and write to file
            decrypted_journal = f.decrypt(encrypted_journal)
            with open(filename, 'wb') as file:
                file.write(decrypted_journal)

            # display decrypted contents
            with open(filename) as file:
                data = file.read()
                self.journalEdit.setText(data)
        except FileNotFoundError:
            self.statusbar.showMessage('Decryption failed. No file currently open.', 2000)
        except TypeError:
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
            else:
                self.statusbar.showMessage('No journal open, nothing to delete.', 2000)
        except FileNotFoundError:
            pass


class SaveThread(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        MainWindow().handleSaveJournal()
        self.sleep(10)
        # schedule.every(5).seconds.do(MainWindow().handleSaveJournal)
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
