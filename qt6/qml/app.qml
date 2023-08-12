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
        id: drawer
        modal: false
        interactive: false
        visible: true
        position: 1 // keep open
        width: 200
        height: parent.height - menubar.height
        y: menubar.height

        ListModel {
            id: listModel
            ListElement {
                moduleName: "Fonts"
                moduleIcon: "preferences-desktop-font"
                moduleView: "./fonts.qml"
            }
            ListElement {
                moduleName: "Colors"
                moduleIcon: "preferences-desktop-color"
                moduleView: "./colors.qml"
            }
            ListElement {
                moduleName: "Wallpaper"
                moduleIcon: "preferences-desktop-wallpaper"
                moduleView: "./wallpaper.qml"
            }
            ListElement {
                moduleName: "Settings"
                moduleIcon: "preferences"
                moduleView: "./settings.qml"
            }
        }

        ListView {
            id: listView
            anchors.fill: parent
            model: listModel
            delegate: ItemDelegate {
                width: ListView.view.width
                highlighted: ListView.isCurrentItem
                text: moduleName
                icon.name: moduleIcon

                onClicked: {
                    listView.currentIndex = index
                    stackView.push(moduleView)
                }
            }
        }
    }

    StackView {
        id: stackView
        anchors.fill: parent
        anchors.leftMargin: drawer.width
    }
}