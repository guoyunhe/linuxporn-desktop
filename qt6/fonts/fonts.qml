import QtCore
import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

ScrollView {
    id: root

    ColumnLayout {
        id: layout
        width: root.width

        ListView {
            id: listView
            model: fontListModel
            Layout.fillWidth: true
            height: contentHeight

            delegate: ItemDelegate {
                width: parent.width
                text: fontFamily
            }
        }

        Button {
            id: loadButton
            text: 'Load more ' + listView.width + ', ' + listView.height

            onClicked: {
                fontListModel.gogoload()
            }
        }
    }
}