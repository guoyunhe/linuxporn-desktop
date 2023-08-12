import QtQuick
import QtQuick.Controls

ApplicationWindow {
    title: "LinuxPorn"
    width: 640
    height: 480
    visible: true

    Drawer {
        id: drawer
        modal: false
        interactive: false
        visible: true
        position: 1 // keep open
        width: 200
        height: parent.height

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
                    if (listView.currentIndex !== index) {
                        listView.currentIndex = index
                        stackView.push(moduleView)
                    }
                }
            }
        }
    }

    StackView {
        id: stackView
        anchors.fill: parent
        anchors.leftMargin: drawer.width
        initialItem: "./fonts.qml"
    }
}