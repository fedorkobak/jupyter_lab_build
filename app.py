#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.1')
from gi.repository import Gtk, WebKit2

win = Gtk.Window()
win.set_default_size(1024, 768)

view = WebKit2.WebView()
view.load_uri("http://localhost:8888")

win.add(view)
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()

