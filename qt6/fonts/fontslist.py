from PySide6.QtCore import Property, QObject, QThread, Signal, Slot


class FontsController(QObject):
    @Property(int)
    def pp(self):
        return self.ppval

    @pp.setter
    def pp(self, val):
        self.ppval = val

    @pp.notify
    def pp(self, val):
        self.ppval = val

    pp = Property(int, readPP, setPP)
