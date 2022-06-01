from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

from InterfaceGraphique.MainWindow import PagePrincipale

if __name__ == "__main__":

    application = QApplication(sys.argv)
    main_window = PagePrincipale()

    main_window.show()

    sys.exit(application.exec_())

