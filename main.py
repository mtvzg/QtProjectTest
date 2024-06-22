import os
import sys
from PyQt5.QtWidgets import QFileSystemModel, QMainWindow, QApplication

from test_window import Ui_MainWindow


class FileExplorer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = QFileSystemModel()
        self.model.setRootPath('')

        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(''))

        self.treeView.doubleClicked.connect(self.open_item)
        self.pushButton.clicked.connect(self.go_back)

    def open_item(self, index):
        path = self.model.filePath(index)
        if os.path.isdir(path):
            self.treeView.setRootIndex(self.model.index(path))
        else:
            os.startfile(path)

    def go_back(self):
        current_path = self.model.filePath(self.treeView.rootIndex())
        parent_path = os.path.dirname(current_path)

        self.treeView.setRootIndex(self.model.index(parent_path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec_())
