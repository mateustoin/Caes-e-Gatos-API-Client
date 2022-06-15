# This Python file uses the following encoding: utf-8
# How to convert from ui to py file: pyside6-uic form.ui > ui_mainwindow.py
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot, Qt
from ui_mainwindow import Ui_Widget
from PySide6.QtGui import QPixmap
from AnimalFetch import AnimalFetch


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.counter = 0
        self.animalSelection = ['Cat', 'Dog1', 'Dog2', 'Fox', 'Duck']
        self.animal_fetch = AnimalFetch()
        self.pix_image = QPixmap()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.photoButton.clicked.connect(self.photo_button_clicked)
        self.ui.saveButton.clicked.connect(self.save_button_clicked)
        self.ui.selectApiButton.addItems(self.animalSelection)

    @Slot()
    def photo_button_clicked(self):
        if self.ui.selectApiButton.currentText() == 'Dog1':
            self.pix_image.loadFromData(self.animal_fetch.get_dog_1_content())
        elif self.ui.selectApiButton.currentText() == 'Dog2':
            self.pix_image.loadFromData(self.animal_fetch.get_dog_2_content())
        # self.pix.loadFromData(test.get_dog_3_content()) # Pode vir com mp4 ou gif
        elif self.ui.selectApiButton.currentText() == 'Duck':
            self.pix_image.loadFromData(self.animal_fetch.get_duck_content())
        elif self.ui.selectApiButton.currentText() == 'Fox':
            self.pix_image.loadFromData(self.animal_fetch.get_fox_content())
        elif self.ui.selectApiButton.currentText() == 'Cat':
            self.pix_image.loadFromData(self.animal_fetch.get_cat_content())
        else:
            print('Colocar alguma Warning Box depois para possíveis erros')

        if self.pix_image.width() > self.pix_image.height():
            self.ui.animalImage.setScaledContents(True)
        else:
            self.ui.animalImage.setScaledContents(False)

        self.pix_image.scaled(self.ui.animalImage.frameSize(),
                              Qt.KeepAspectRatio,
                              Qt.SmoothTransformation)

        self.ui.animalImage.setPixmap(self.pix_image)

    @Slot()
    def save_button_clicked(self):
        # print(self.pix_image.__str__)
        # fileName = QFileDialog.getSaveFileName(self, 'Save File', '', '.jpg')
        # print(fileName)
        name, extension = self.animal_fetch.get_name_and_image_extension()
        self.pix_image.save(name, extension, -1)


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
