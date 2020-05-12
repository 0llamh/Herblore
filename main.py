#       main.py
#       handles main function and GUI

import PySimpleGUI as ui
import xlsxwriter

import Catalog
import Herb

ui.theme('Dark Green 3')
layout = [[ui.Text('Generate an herb!')],
          [ui.Button('Create Herb'), ui.Button('Export')],
          [ui.Text(size=(30, 1), key="name", font=('Helvetica', 15, 'bold')), ui.Text(size=(15, 1), key="rarity")],
          [ui.Text(size=(50, 1), key="description")]]
window = ui.Window('Herblore', layout)


def main():
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in 'Create Herb':
            # print('herb created')
            h = Herb.Herb()
            window["name"].update(h.name)
            window["rarity"].update("Herb Rarity: %i" % h.rarity)
            # todo: attribute specific descriptions based on texture and origins
            window["description"].update("A " + h.color + " herb from the " + h.origin.lower())
        elif event in 'Export':
            # todo: catch duplicate herb exports.
            # todo: send error reports to a dialog, so generated herb isnt lost
            try:
                Catalog.write(h)
            except(UnboundLocalError):
                window["name"].update("ERROR")
                window["rarity"].update("")
                window["description"].update("Generate an herb before exporting.")
            except(xlsxwriter.exceptions.FileCreateError):
                window["name"].update("ERROR")
                window["rarity"].update("")
                window["description"].update("Spreadsheet currently open in another process.")

    window.close()


if __name__ == "__main__":
    main()
