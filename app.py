from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtGui import QFont


class GUI(QMainWindow):

    def __init__(self) -> None:
        super(GUI, self).__init__()
        uic.loadUi(r'D:\Projects\Text Editor Clone\gui.ui', self)        
        self.setWindowTitle("Notepad Clone")
        self.setStyleSheet("""
            QMainWindow {
                background-color: #333;
                color: #fff;
                border: 1px solid #444;
            }
            QLabel {
                background-color: transparent;
            }
        """)
    
        self.show()
        self.action12px.triggered.connect(lambda : self.change_font_size(12))
        self.action18px.triggered.connect(lambda : self.change_font_size(18))
        self.action24px.triggered.connect(lambda : self.change_font_size(24))

        self.actionOpen.triggered.connect(lambda : self.open_file())
        self.actionSave.triggered.connect(lambda : self.save())
        self.actionExit.triggered.connect(exit)


    def change_font_size(self, size :int) -> None:
        self.plainTextEdit.setFont(QFont('Lucida Console', size))
            

    def save(self) -> None:
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if filename:
            with open(filename, 'w') as f:
                f.write(self.plainTextEdit.toPlainText())


    def open_file(self) -> None:
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if filename:
            with open(filename, 'r') as f:
                self.plainTextEdit.setPlainText(f.read())


    def closeEvent(self, event) -> None:
        dialog = QMessageBox()
        dialog.setText("Do you want to save the file?")
        dialog.addButton(QMessageBox.StandardButton.Yes)
        dialog.addButton(QMessageBox.StandardButton.No)
        dialog.addButton(QMessageBox.StandardButton.Cancel)

        dialog.button(QMessageBox.StandardButton.Yes).clicked.connect(self.save)
        dialog.button(QMessageBox.StandardButton.No).clicked.connect(exit)
        dialog.button(QMessageBox.StandardButton.Cancel).clicked.connect(event.ignore)

        answer = dialog.exec()

        if answer == QMessageBox.StandardButton.Yes:
            self.save()
            event.accept()
        elif answer == QMessageBox.StandardButton.Cancel:
            event.ignore()

def main():
    app = QApplication([])
    window = GUI()
    app.exec()



if __name__ == '__main__':
    main()