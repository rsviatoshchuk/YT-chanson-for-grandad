from PyQt5.QtWidgets import (QWidget, QApplication, QDesktopWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton)
from  PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setFixedSize(800, 600)
        self.center()
        self.create_ui()

    def create_ui(self):
        vbox = QVBoxLayout()

        link_entry_field = QLineEdit()
        link_entry_field.setFixedHeight(50)
        vbox.addWidget(link_entry_field)

        download_button = QPushButton("Завантажити")
        download_button.setFixedHeight(300)
        download_button.setStyleSheet("color:black; font-family: 'Open Sans Condensed'; font-size: 30px")
        vbox.addWidget(download_button)

        help_button = QPushButton("Допомога")
        help_button.setFixedSize(200, 75)
        help_button.setStyleSheet("color:black; font-family: 'Open Sans Condensed'; font-size: 30px")
        vbox.addWidget(help_button, alignment=Qt.AlignRight)

        self.setLayout(vbox)

    def center(self):
        """function, that center window on the screen"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
