import QtCore
import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Item {
    id: root

    ColumnLayout {
        anchors.centerIn: parent
        
        Button {
            Layout.alignment: Qt.AlignCenter
            icon.name: 'linuxporn'
            icon.width: 64
            icon.height: 64
            flat: true
        }

        Label {
            Layout.alignment: Qt.AlignCenter
            text: `${Application.displayName} (${Application.version})`
        }

        Label {
            Layout.alignment: Qt.AlignCenter
            text: `By Guo Yunhe`
        }

        Label {
            Layout.alignment: Qt.AlignCenter
            text: 'GNU General Public License version 3'
        }

        Button {
            Layout.alignment: Qt.AlignCenter
            icon.name: 'internet-web-browser'
            text: 'linuxporn.guoyunhe.me'
            flat: true

            onClicked: {
                Qt.openUrlExternally('https://linuxporn.guoyunhe.me/')
            }
        }
    }
}