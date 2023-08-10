import os
import sys
import platform

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtCore import QSettings, QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

if __name__ == "__main__":
    QGuiApplication.setApplicationName("Gallery")
    QGuiApplication.setOrganizationName("QtProject")

    app = QGuiApplication()
    QIcon.setThemeName("gallery")

    settings = QSettings()
    if not os.environ.get("QT_QUICK_CONTROLS_STYLE"):
        style_name = settings.value("style")
        if style_name:
            QQuickStyle.setStyle(style_name)

    engine = QQmlApplicationEngine()

    engine.load(QUrl.fromLocalFile("qt6/view.qml"))
    rootObjects = engine.rootObjects()
    if not rootObjects:
        sys.exit(-1)

    sys.exit(app.exec())
