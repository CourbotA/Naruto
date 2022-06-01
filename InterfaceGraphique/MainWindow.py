from PySide2.QtGui import *
from PySide2.QtWidgets import *


class PagePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Naruto signs")
        self.body = QWidget(self)
        self.setFixedWidth(1200)
        self.setFixedHeight(600)
        self.setStyleSheet("background-image: url(narutoBackground.jpg);"
                           "background-size: cover;"
                           "background-repeat: no-repeat;")
        # self.DefinirStyle()
        self.title()
        self.button()
        self.show()

    def title(self):
        title = QLabel(self)
        title.setText("Naruto signs")
        title.setGeometry(200, 50, 800, 120)
        title.setStyleSheet("letter-spacing: 3px;"
                            "text-decoration: none;"
                            "text-shadow: 2px;"
                            "color:blue;"
                            "font-family: Brush Script MT, Brush Script Std, cursive;"
                            "font-size: 100px;")
        title.setAlignment(Qt.AlignHCenter)
        title.setAttribute(Qt.WA_TranslucentBackground)



    def button(self):
        button_upload = QPushButton("Upload image", self);
        button_upload.setGeometry(500, 400, 200, 75)
        button_upload.setStyleSheet("text-decoration: none;"
                            "background-color: brown;"
                            "selection-color: brown;"
                            "color: white;"
                            "font-size: 25px;")
        button_upload.setToolTip('Upload image please')
        button_upload.clicked.connect(self.on_click)

    # @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.jpg)")
        imagePath = image[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(pixmap)

        self.label.adjustSize()  # <---

        # print(ocr.resimden_yaziya(imagePath))
        print(imagePath)








