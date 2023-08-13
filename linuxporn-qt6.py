#!/usr/bin/python3

import signal
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from core import meta
from qt6.fonts.fontlistmodel import FontListModel

# Thread example
# https://doc.qt.io/qtforpython-6/examples/example_widgets_thread_signals.html
if __name__ == '__main__':
    QGuiApplication.setApplicationName(meta.APP_NAME)
    QGuiApplication.setApplicationDisplayName(meta.APP_DISPLAY_NAME)
    QGuiApplication.setApplicationVersion(meta.APP_VERSION)
    QGuiApplication.setOrganizationName(meta.ORG_NAME)

    app = QGuiApplication()

    engine = QQmlApplicationEngine()
    fontListModel = FontListModel()
    engine.rootContext().setContextProperty('fontListModel', fontListModel)
    engine.load('qt6/app.qml')
    rootObjects = engine.rootObjects()

    # quit on view error
    if not rootObjects:
        sys.exit(-1)

    # quit on Ctrl+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # quit on close button
    sys.exit(app.exec())
