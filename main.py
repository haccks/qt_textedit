import sys
from PySide2.QtWidgets import QMainWindow, QWidget, QApplication, QFileDialog, QMessageBox, QInputDialog, QLineEdit
from PySide2.QtCore import QFile, QIODevice, QTextStream, QFileInfo, QCoreApplication
# from PySide2.QtGui import QTextCursor

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_file = None

    # slots for File
    def new_file(self):
        # self.save_file()
        self.ui.textEdit.clear()
        self.current_file = None
        self.setWindowTitle("Untitled")

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, caption="Open", filter="Text File (*.txt)")
        self.current_file = file_name[0]

        qfile = QFile(self.current_file)
        if not qfile.open(QIODevice.ReadWrite | QIODevice.Text):
            QMessageBox.warning(self, "Warning", qfile.errorString())
            return
        self.setWindowTitle(QFileInfo(self.current_file).fileName())
        qin = QTextStream(qfile)  # Interface for reading and writing text.
        self.ui.textEdit.setText(qin.readAll())
        qfile.close()

    def close_file(self):
        ret = QMessageBox.question(self, '', 'Do you want to save file...', QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.save_file()
        self.ui.textEdit.clear()
        self.current_file = None
        self.setWindowTitle("TextEdit")

    def save_file(self):
        if not self.current_file:
            dialog = QFileDialog(self)
            file_name = dialog.getSaveFileName(self, caption="Save", filter="Text File (*.txt)")
            # print(file_name)
            self.current_file = file_name[0]

        qfile = QFile(self.current_file)  # Interface for reading from and writing to files.
        if not qfile.open(QIODevice.WriteOnly | QIODevice.Text):
            QMessageBox.warning(self, "Warning", qfile.errorString())
            return
        self.setWindowTitle(QFileInfo(self.current_file).fileName())
        out = QTextStream(qfile)  # Interface for reading and writing text.
        out << self.ui.textEdit.toPlainText()
        qfile.close()

    def save_as_file(self):
        dialog = QFileDialog(self)
        file_name = dialog.getSaveFileName(self, caption="Save as...", filter="Text File (*.txt)")

        self.current_file = file_name[0]
        self.save_file()

    def rename_file(self):
        if self.current_file:
            qfile = QFile(self.current_file)
            new_name, ok = QInputDialog.getText(self, "Rename", "Enter a name:", QLineEdit.Normal)
            if not new_name.endswith('.txt'):
                new_name += '.txt'
            if ok and new_name:
                qfile.rename(self.current_file, new_name)
                self.current_file = new_name
                self.setWindowTitle(QFileInfo(self.current_file).fileName())

    # Slots for Edit
    def cut_text(self):
        self.ui.textEdit.cut()

    def copy_text(self):
        self.ui.textEdit.copy()

    def paste_text(self):
        self.ui.textEdit.paste()

    def redo(self):
        self.ui.textEdit.redo()

    def undo(self):
        self.ui.textEdit.undo()

    def select_all(self):
        self.ui.textEdit.selectAll()

    # Slots for TextEdit menu
    def about(self):
        QMessageBox.about(self, '<b>About TextEdit<b>', 'A simple text editor written in Qt (PySide2)')

    @staticmethod
    def quit_app():
        QCoreApplication.quit()

    def help(self):
        QMessageBox.information(self, '', "c'mon!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()


