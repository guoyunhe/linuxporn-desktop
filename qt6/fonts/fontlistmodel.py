from PySide6.QtCore import QAbstractListModel, QObject, QThread, Signal, Slot


class FontListModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
