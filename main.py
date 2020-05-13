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
          [ui.Text(size=(60, 4), key="description")]]
window = ui.Window('Herblore', layout)


def main():
    lastevent = ''          # define error checker variable pre-loop
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in 'Create Herb':
            h = Herb.Herb()
            window["name"].update(h.name)
            window["rarity"].update("Herb Rarity: %i" % h.rarity)
            # todo: attribute specific descriptions based on texture and origins
            window["description"].update("A " + h.color + " herb from " + h.origin.lower() + " that is prepared "
                                         + h.preparation + " as " + h.use + " " + h.expiration + ".")
        elif event in 'Export':
            try:
                if lastevent == event:      # if both last and current events were exports
                    ui.popup_error('Herb already exported. Please generate another.', title='Export Error')
                else:               # otherwise just export like normal
                    Catalog.write(h)
            except(UnboundLocalError):
                ui.popup_error('Generate an herb before exporting', title='Export Error')
            except(xlsxwriter.exceptions.FileCreateError):
                ui.popup_error("Spreadsheet currently open in another process. Please close it.", title='Export Error')
        lastevent = event           # save what happened this event loop for the next (duplicate export checking)

    window.close()


if __name__ == "__main__":
    main()
