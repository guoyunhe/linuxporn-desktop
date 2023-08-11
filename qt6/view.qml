import QtQuick
import QtQuick.Controls

ApplicationWindow {
    title: "LinuxPorn"
    width: 640
    height: 480
    visible: true

    menuBar: MenuBar {
        id: menubar
        Menu {
            title: qsTr("&File")
            Action { text: qsTr("&New...") }
            Action { text: qsTr("&Open...") }
            Action { text: qsTr("&Save") }
            Action { text: qsTr("Save &As...") }
            MenuSeparator { }
            Action { text: qsTr("&Quit") }
        }
        Menu {
            title: qsTr("&Edit")
            Action { text: qsTr("Cu&t") }
            Action { text: qsTr("&Copy") }
            Action { text: qsTr("&Paste") }
        }
        Menu {
            title: qsTr("&Help")
            Action { text: qsTr("&About") }
        }
    }

    Drawer {
        modal: false
        interactive: false
        visible: true
        position: 1 // keep open
        width: 300
        height: parent.height - menubar.height
        y: menubar.height

        Label {
            text: "Content goes here!"
            anchors.centerIn: parent
        }
    }

    Button {
        text: "Push Me"
        anchors.centerIn: parent
    }
}