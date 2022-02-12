#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser

webbrowser.open('https://www.google.com/maps/place/' + "1234 Viola Ave, Glendale, CA")