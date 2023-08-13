from PySide6.QtCore import QAbstractItemModel, QObject, QThread, Signal, Slot


class FontModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
