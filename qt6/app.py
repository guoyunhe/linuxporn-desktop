#!/usr/bin/python3

import signal
import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == "__main__":
    QGuiApplication.setApplicationName("LinuxPorn")
    QGuiApplication.setOrganizationName("GuoYunhe")

    app = QGuiApplication()

    engine = QQmlApplicationEngine("qt6/qml/app.qml")
    rootObjects = engine.rootObjects()

    # quit on view error
    if not rootObjects:
        sys.exit(-1)

    # quit on Ctrl+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # quit on close button
    sys.exit(app.exec())
