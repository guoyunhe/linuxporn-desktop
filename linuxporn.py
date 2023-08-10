#!/usr/bin/python3

import gi
gi.require_version('Gtk', '4.0')

from gi.repository import Gtk


def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title('LinuxPorn')
    btn = Gtk.Button(label="Hello, World!")
    btn.connect('clicked', lambda x: win.close())
    win.set_child(btn)
    win.present()


app = Gtk.Application(application_id='me.guoyunhe.LinuxPorn')
app.connect('activate', on_activate)
app.run(None)
