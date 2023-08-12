import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    QGuiApplication.setApplicationName("Gallery")
    QGuiApplication.setOrganizationName("QtProject")

    app = QGuiApplication()
    QIcon.setThemeName("gallery")

    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile("qt6/qml/app.qml"))
    rootObjects = engine.rootObjects()

    if not rootObjects:
        sys.exit(-1)  # quit on view error

    window = rootObjects[0]
    window.setIcon(QIcon.fromTheme('linuxporn'))

    sys.exit(app.exec())
