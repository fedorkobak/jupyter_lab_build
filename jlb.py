#!/usr/bin/env python3
import logging
import argparse
import jupyterlab.labapp


import multiprocessing
import multiprocessing.managers

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.1')
from gi.repository import Gtk, WebKit2


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Logger initialized")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url",
        type=str,
        default=None
    )
    parser.add_argument(
        "--zoom",
        type=float,
        default=0.9,
        help="WebKit zoom level (1.0 = 100%)."
    )
    return parser.parse_args()


def initialize_window(host: str, zoom: float):
    win = Gtk.Window()
    win.set_default_size(1024, 768)

    view = WebKit2.WebView()
    view.set_zoom_level(zoom)
    view.load_uri(host)

    win.add(view)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()


def server_process(shared: multiprocessing.managers.Namespace):
    server = jupyterlab.labapp.LabApp.initialize_server()
    shared.url = server.server_info()["url"]
    server.start()


def main():
    cli_args = parse_arguments()

    url = cli_args.url
    jupyter_process = None

    if url is None:
        # if url is not passed starting jupyter lab server
        with multiprocessing.Manager() as m:
            shared = m.Namespace()
            jupyter_process = multiprocessing.Process(
                # target=jupyterlab.labapp.main()
                target=server_process,
                args=(shared,)
            )
            jupyter_process.start()

            # waiting for juptyerlab-server to initialize the url
            while not hasattr(shared, "url"):
                pass
            url = shared.url

    logger.info(f"Using url {url}")
    initialize_window(url, cli_args.zoom)
    Gtk.main()
    logger.debug("Leaving application")

    if jupyter_process is not None:
        logger.debug("Stopping juptyer server")
        jupyter_process.terminate()
        logger.debug("Server stopped")


if __name__ == "__main__":
    main()

