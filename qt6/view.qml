import QtCore
import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

ApplicationWindow {
    Rectangle {
        id: main
        width: 200
        height: 200
        color: "green"
    
        Text {
            text: "Hello World"
            anchors.centerIn: main
        }
    }
}