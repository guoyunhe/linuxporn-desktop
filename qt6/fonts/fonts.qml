import QtCore
import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

ScrollView {
    ListView {
        anchors.fill: parent
        model: fontListModel

        delegate: ItemDelegate {
            width: parent.width
            text: fontFamily
        }
    }
}