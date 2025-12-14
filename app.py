#!/usr/bin/env python3
import argparse

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.1')
from gi.repository import Gtk, WebKit2


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url",
        type=str,
        default="http://localhost:8888"
    )
    return parser.parse_args()


def initialize_window(host: str):
    win = Gtk.Window()
    win.set_default_size(1024, 768)

    view = WebKit2.WebView()
    view.load_uri(host)

    win.add(view)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()


if __name__ == "__main__":
    namespace = parse_arguments()
    initialize_window(namespace.url)
    Gtk.main()